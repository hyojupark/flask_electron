import os

from flask import request, url_for

from app import app
from app.controller import base_controller


class Server:
    def __init__(self, host, port, debug, use_reloader, threaded):
        self.host = host
        self.port = int(os.environ.get("PORT", port))
        self.debug = debug
        self.use_reloader = use_reloader
        self.threaded = threaded

    def register_views(self):
        base_controller.BaseView.register(app, route_base='/')

    @staticmethod
    def url_for_other_page(page):
        args = request.view_args.copy()
        args['page'] = page
        return url_for(request.endpoint, **args)

    def run(self) -> bool:
        self.register_views()
        app.jinja_env.globals['url_for_other_page'] = self.url_for_other_page
        app.run(host=self.host,
                port=self.port,
                debug=self.debug,
                use_reloader=self.use_reloader,
                threaded=self.threaded)

        return True

if __name__ == '__main__':
    server = Server(host='127.0.0.1', port=5000, debug=True, use_reloader=False, threaded=True)
    server.run()
