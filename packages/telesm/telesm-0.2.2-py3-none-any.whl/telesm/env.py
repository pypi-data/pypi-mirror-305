import dotenv
import os


class Env:
    PATHS = ['./.env', '~/.telesm.conf']

    def load_env(self):
        for path in self.PATHS:
            if os.path.exists(path):
                dotenv.load_dotenv(os.path.expanduser(path))
