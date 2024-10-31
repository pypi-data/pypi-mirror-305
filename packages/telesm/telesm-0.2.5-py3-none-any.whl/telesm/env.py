import dotenv
import os


class Env:
    PATHS = ['./.env', '~/.telesm.conf']

    def load_env(self):
        for path in self.PATHS:
            if os.path.exists(os.path.expanduser(path)):
                dotenv.load_dotenv(os.path.expanduser(path))
