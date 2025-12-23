"""
Data loading utilities for the Adaptive Taxonomy Mapper.

Responsibilities:
- Safely load JSON data
- Validate structure
- Support scalability and future extensions
"""

import json
from typing import Any


def load_json(path: str) -> Any:
    """
    Loads a JSON file safely.

    Designed to:
    - Fail clearly if input is invalid
    - Handle large datasets cleanly
    - Support production-style debugging

    Parameters:
        path (str): Path to the JSON file

    Returns:
        Parsed JSON content
    """

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise RuntimeError(f"[Loader Error] File not found: {path}")

    except json.JSONDecodeError as err:
        raise RuntimeError(
            f"[Loader Error] Invalid JSON format in {path}: {err}"
        )


def load_json_stream(path: str):
    """
    Generator for loading very large JSON arrays incrementally.

    Use this when:
    - JSON contains millions of objects
    - You want low memory usage

    Expected JSON format:
    [
      {...},
      {...},
      ...
    ]
    """

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise RuntimeError("Stream loader expects a JSON array")

            for item in data:
                yield item

    except FileNotFoundError:
        raise RuntimeError(f"[Loader Error] File not found: {path}")

    except json.JSONDecodeError as err:
        raise RuntimeError(
            f"[Loader Error] Invalid JSON format in {path}: {err}"
        )
