import yaml
import os
from utils import get_repo_path


class ConfigFileLoader:

    def __init__(self, filepath: str = None) -> None:
        if filepath is None:
            filepath = os.path.join(get_repo_path(), "config.yaml")
        if os.path.exists(filepath):
            self.filepath = filepath
            with open(self.filepath, "r") as f:
                self.config = yaml.safe_load(f)
        else:
            raise FileNotFoundError(f"Config file not found: {filepath}")

    def get_seed(self) -> int:
        return self.config["general_config"]["seed"]

    def get_params(self) -> dict:
        return self.config["general_config"]["params"]
