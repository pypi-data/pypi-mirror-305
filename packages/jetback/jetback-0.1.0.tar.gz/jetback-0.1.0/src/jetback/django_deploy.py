from functions_framework import http as functions_framework_http

class WSGIAdapter:
    def __init__(self, app):
        self.app = app

    def __call__(self, request):
        environ = {
            'REQUEST_METHOD': request.method,
            'SCRIPT_NAME': '',
            'PATH_INFO': request.path,
            'QUERY_STRING': request.query_string.decode('utf-8'),
            'SERVER_NAME': request.host.split(':')[0],
            'SERVER_PORT': request.host.split(':')[1] if ':' in request.host else '80',
            'HTTP_HOST': request.host,
            'HTTP_USER_AGENT': request.headers.get('User-Agent', ''),
            'HTTP_ACCEPT': request.headers.get('Accept', ''),
            'CONTENT_TYPE': request.headers.get('Content-Type', ''),
            'CONTENT_LENGTH': request.headers.get('Content-Length', ''),
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': request.scheme,
            'wsgi.input': request.stream,
            'wsgi.errors': lambda: None,
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
        }

        for key, value in request.headers.items():
            key = 'HTTP_' + key.upper().replace('-', '_')
            if key not in ('HTTP_CONTENT_TYPE', 'HTTP_CONTENT_LENGTH'):
                environ[key] = value

        response_headers = []

        def start_response(status, headers, exc_info=None):
            response_headers[:] = [status, headers]

        response_body = b''.join(self.app(environ, start_response))

        status_code = int(response_headers[0].split()[0])
        headers = dict(response_headers[1])
        body = response_body.decode('utf-8')

        return (body, status_code, headers)

def jetback_deploy_django(app):
    """
    Wrap a Django WSGI application for deployment.

    Args:
        app: The Django WSGI application to deploy.

    Returns:
        function: The entry point function for the backend.

    Raises:
        ImportError: If Django is not installed.
        TypeError: If the provided app is not a Django WSGI application.
    """
    try:
        import django
        from django.core.handlers.wsgi import WSGIHandler
    except ImportError:
        raise ImportError("Django is not installed. Install it with 'pip install jetback[django]'")
    
    if not isinstance(app, WSGIHandler):
        raise TypeError("The 'app' argument must be a Django WSGI application (WSGIHandler instance).")

    adapter = WSGIAdapter(app)

    @functions_framework_http
    def jetback_entrypoint(request):
        return adapter(request)

    return jetback_entrypoint