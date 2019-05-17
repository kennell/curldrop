from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems


class StandaloneServer(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneServer, self).__init__()

    def load_config(self):
        config = dict(
            [
                (key, value)
                for key, value in iteritems(self.options)
                if key in self.cfg.settings and value is not None
            ]
        )
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
