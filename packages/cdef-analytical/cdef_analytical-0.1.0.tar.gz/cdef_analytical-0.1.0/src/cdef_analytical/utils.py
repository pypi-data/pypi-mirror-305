import json
from pathlib import Path
from typing import Any

import chardet

from cdef_analytical.logging_config import logger


def detect_and_load_json(file_path: Path) -> dict[str, Any]:
    """
    Detect the encoding of a JSON file and load it as UTF-8.

    Args:
        file_path: Path to the JSON file

    Returns:
        Decoded JSON content as a dictionary

    Raises:
        ValueError: If the file cannot be read or parsed
    """
    try:
        # Read the raw bytes first
        raw_data = file_path.read_bytes()

        # Detect the encoding
        result = chardet.detect(raw_data)
        detected_encoding = (
            result["encoding"] if result and result["encoding"] else "utf-8"
        )

        logger.debug(f"Detected encoding {detected_encoding} for {file_path}")

        # List of encodings to try, starting with the detected one
        encodings = [detected_encoding, "utf-8", "latin1", "iso-8859-1", "cp1252"]

        # Try each encoding until one works
        for encoding in encodings:
            try:
                decoded_content = raw_data.decode(encoding)
                logger.debug(f"Successfully decoded using encoding: {encoding}")
                break
            except UnicodeDecodeError:
                continue
        else:
            raise ValueError(f"Could not decode {file_path} with any known encoding")

        # Parse the JSON
        try:
            data = json.loads(decoded_content)
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {file_path}: {str(e)}")

    except Exception as e:
        logger.error(f"Error loading {file_path}: {str(e)}")
        raise
