server = """

import os

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from app_init.app_factory import create_app


if os.environ["settings"]:
    settings_name = os.environ["settings"]
else:
    raise Exception("'settings' environment " "variable is not defined")
flask_app = create_app(settings_name)
app = DispatcherMiddleware(flask_app)


if __name__ == "__main__":
    run_simple("127.0.0.1", 8000, app, use_debugger=True, threaded=True)


"""
