import asyncio
from typing import Any, Callable
from dataclasses import dataclass, field
from io import BytesIO
from functions_framework import http as functions_framework_http

@dataclass
class ASGICycle:
    scope: dict
    body: BytesIO = field(default_factory=BytesIO)
    state: str = "REQUEST"
    response: dict = field(default_factory=dict)

    def __call__(self, app: Any, body: bytes) -> dict:
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.app_queue = asyncio.Queue()
        self.put_message({"type": "http.request", "body": body, "more_body": False})
        asgi_instance = app(self.scope, self.receive, self.send)
        self.loop.run_until_complete(asgi_instance)
        return self.response

    def put_message(self, message: dict) -> None:
        self.app_queue.put_nowait(message)

    async def receive(self) -> dict:
        return await self.app_queue.get()

    async def send(self, message: dict) -> None:
        if message["type"] == "http.response.start":
            self.response["status_code"] = message["status"]
            self.response["headers"] = {k.decode(): v.decode() for k, v in message.get("headers", [])}
        elif message["type"] == "http.response.body":
            self.body.write(message.get("body", b""))
            if not message.get("more_body", False):
                self.response["body"] = self.body.getvalue()
                self.put_message({"type": "http.disconnect"})

@dataclass
class FastAPIAdapter:
    app: Any

    def __call__(self, request: Any) -> dict:
        return self.handle_request(request)

    def handle_request(self, request: Any) -> dict:
        scope = self.build_scope(request)
        cycle = ASGICycle(scope)
        response = cycle(self.app, request.data)
        
        return {
            "statusCode": response["status_code"],
            "headers": response["headers"],
            "body": response["body"].decode() if isinstance(response["body"], bytes) else response["body"]
        }

    def build_scope(self, request: Any) -> dict:
        return {
            "type": "http",
            "method": request.method,
            "http_version": "1.1",
            "headers": [[k.lower().encode(), v.encode()] for k, v in request.headers.items()],
            "path": request.path,
            "raw_path": request.path.encode(),
            "query_string": request.query_string,
            "scheme": request.scheme,
            "server": (request.host.split(':')[0], int(request.host.split(':')[1]) if ':' in request.host else 80),
            "client": (request.remote_addr, 0),
            "asgi": {"version": "3.0", "spec_version": "2.1"},
        }

def jetback_deploy_fastapi(app):
    """
    Wrap a FastAPI application for deployment.

    Args:
        app (fastapi.FastAPI): The FastAPI application to deploy.

    Returns:
        function: The entry point function for the backend.

    Raises:
        ImportError: If FastAPI is not installed.
        TypeError: If the provided app is not a FastAPI application.
    """
    try:
        from fastapi import FastAPI
    except ImportError:
        raise ImportError("FastAPI is not installed. Install it with 'pip install jetback[fastapi]'")

    if not isinstance(app, FastAPI):
        raise TypeError("The 'app' argument must be a FastAPI application.")

    adapter = FastAPIAdapter(app)

    @functions_framework_http
    def jetback_entrypoint(request: Any) -> Callable:
        return adapter(request)

    return jetback_entrypoint