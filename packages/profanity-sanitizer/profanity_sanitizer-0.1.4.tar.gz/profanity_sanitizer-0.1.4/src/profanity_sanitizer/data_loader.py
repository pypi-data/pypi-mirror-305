import json
from typing import Any, Dict, List, Union


class DataLoader:
    """Class responsible for loading data from JSON files."""

    @staticmethod
    def load_json(json_file: str) -> Union[Dict[str, Any], List[Any]]:
        """
        Load a JSON file.

        Args:
            json_file (str): The path to the JSON file.

        Returns:
            Union[Dict[str, Any], List[Any]]: The loaded JSON data.

        Raises:
            FileNotFoundError: If the JSON file is not found.
            ValueError: If the JSON file is not valid.
        """
        try:
            with open(json_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The JSON file '{json_file}' was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The JSON file '{json_file}' is not valid JSON.")
