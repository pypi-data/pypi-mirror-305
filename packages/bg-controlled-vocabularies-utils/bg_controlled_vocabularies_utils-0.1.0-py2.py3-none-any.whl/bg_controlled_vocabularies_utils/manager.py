import logging
import os
import pathlib
import yaml

from singleton_decorator import singleton
from typing import List


from . import constants


@singleton
class Manager:
    """Class for managing the controlled vocabularies."""

    def __init__(self, **kwargs):
        """Constructor for class Manager"""
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", None)
        self.logfile = kwargs.get("logfile", None)

        if self.config is None:
            if self.config_file is None or not os.path.exists(self.config_file):
                self.config_file = constants.DEFAULT_CONFIG_FILE
                logging.info(f"Configuration file not provided. Using default configuration file: {self.config_file}")

            logging.info(f"Will load contents of config file '{self.config_file}'")
            self.config = yaml.safe_load(pathlib.Path(self.config_file).read_text())

        self.inverse_lookup = {}

        self._create_inverse_lookup()

        logging.info(f"Instantiated Manager in {os.path.abspath(__file__)}")

    def _create_inverse_lookup(self):
        """Create an inverse lookup for the configuration file."""
        for section in self.config:

            if section not in self.inverse_lookup:
                self.inverse_lookup[section] = {}

            for standard_name in self.config[section]:
                alt_names = self.config[section][standard_name].get("alt_names", [])
                for alt_name in alt_names:
                    self.inverse_lookup[section][alt_name] = standard_name

    def get_standard_name(
        self,
        section: str,
        name: str
    ) -> str:
        """Return the standard name for the given section and name.

        Args:
            section (str): The section in the configuration file.
            name (str): The name in the configuration file.

        Returns:
            str: The standard name for the given section and name.
        """
        if section not in self.inverse_lookup:
            logging.warning(f"Did not find section '{section}' in configuration file '{self.config_file}'")
            return None

        if name not in self.inverse_lookup[section]:
            logging.warning(f"Did not find name '{name}' in section '{section}' in configuration file '{self.config_file}'")
            return None

        return self.inverse_lookup.get(section, {}).get(name, None)

    def get_alternative_names(
        self,
        section: str,
        name: str
    ) -> List[str]:
        """Return the alternative names for the given section and name.

        Args:
            section (str): The section in the configuration file.
            name (str): The name in the configuration file.

        Returns:
            List[str]: The alternative names for the given section and name.
        """
        if section not in self.config:
            logging.warning(f"Did not find section '{section}' in configuration file '{self.config_file}'")
            return None

        if name not in self.config[section]:
            logging.warning(f"Did not find name '{name}' in section '{section}' in configuration file '{self.config_file}'")
            return None

        return self.config.get(section, {}).get(name, {}).get("alt_names", None)
