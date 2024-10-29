"""Return a config object from a toml file for the application."""
import tomli
import tomli_w

from .config import Config
import psiconfig.text as text


class TomlConfig(Config):
    """
        A class to handle config files in toml format
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _read_config(self) -> dict[str, object]:
        """Open the config file and return the contents as a dict."""
        self.status = self.OK
        try:
            with open(self.path, 'rb') as f_config:
                try:
                    config = tomli.load(f_config)
                    return self.check_defaults(config)
                except tomli.TOMLDecodeError:
                    if self.defaults:
                        return self.defaults
                    else:
                        self.error = f'{text.INVALID_TOML} {self.path}'
        except FileNotFoundError:
            if self.defaults:
                return self.defaults
            else:
                self.error = text.DEFAULTS_ERR
        self.status = self.STATUS_ERROR
        return {}

    def save(self):
        if not self.path.parent.is_dir():
            self.create_directories()
        try:
            with open(self.path, mode='wb') as f_config:
                tomli_w.dump(self.__dict__['config'], f_config)
                return self.STATUS_OK
        except Exception as err:
            self.status = self.STATUS_ERROR
            self.error = err
