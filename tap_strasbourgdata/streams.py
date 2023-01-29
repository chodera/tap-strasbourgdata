"""Stream type classes for tap-strasbourgdata."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_strasbourgdata.client import StrasbourgDataStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class PiscinesStream(StrasbourgDataStream):
    """Stream representing frequentation of swimming pools in Strasbourg."""
    name = "piscines"
    path = "frequentation-en-temps-reel-des-piscines"
    primary_keys = ["recordid"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "piscines.json"
