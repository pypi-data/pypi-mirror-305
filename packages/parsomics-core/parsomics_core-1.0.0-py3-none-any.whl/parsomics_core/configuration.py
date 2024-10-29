import tomllib
from pathlib import Path
from typing import Any

from parsomics_core.globals.environment import Environment
from parsomics_core.globals.logger import setup_logging

DEFAULT_CONFIG_FILE_NAME = "config.toml"
DEFAULT_CONFIG_FILE_PATH = Path.home() / Path(
    f".config/parsomics/{DEFAULT_CONFIG_FILE_NAME}"
)


class ConfigurationReader:
    config_file_path: Path
    config: dict[str, Any]

    def _read_config_file(self):
        with open(self.config_file_path, "rb") as f:
            self.config = tomllib.load(f)

        # Environment setup
        environment: Environment = Environment(self.config["environment"])
        setup_logging(environment)

    def __init__(self, config_file_path: Path | None = None):
        self.config_file_path = (
            config_file_path
            if config_file_path is not None
            else DEFAULT_CONFIG_FILE_PATH
        )
        self.config_file_path = self.config_file_path.resolve()
        self._read_config_file()
