from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from site_home import app as app_home
from site_about import app as app_about


application = DispatcherMiddleware(
    app = app_home.server, 
    mounts = {
        '/about': app_about.server     
    }
)


if __name__ == "__main__":
    run_simple(hostname='0.0.0.0', port=8080, application=application)
    # run_simple(hostname='127.0.0.1', port=8080, application=application)