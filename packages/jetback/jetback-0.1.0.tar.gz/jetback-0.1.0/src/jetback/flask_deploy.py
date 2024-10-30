from functions_framework import http as functions_framework_http

def jetback_deploy_flask(app):

    """
    Wrap a Flask application for deployment.

    Args:
        app (flask.Flask): The Flask application to deploy.

    Returns:
        function: The entry point function for the backend.

    Raises:
        ImportError: If Flask is not installed.
        TypeError: If the provided app is not a Flask application.
    """

    try:
        import flask
    except ImportError:
        raise ImportError("Flask is not installed. Install it with 'pip install jetback[flask]'")

    if not isinstance(app, flask.Flask):
        raise TypeError("The 'app' argument must be a Flask application.")
    
    @functions_framework_http
    def jetback_entrypoint(request):
        with app.request_context(request.environ):
            return app.full_dispatch_request()
    
    return jetback_entrypoint
