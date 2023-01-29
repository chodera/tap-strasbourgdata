"""Stream type classes for tap-strasbourgdata."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_strasbourgdata.client import StrasbourgDataStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class PiscinesStream(StrasbourgDataStream):
    """Stream containing general information on swimming pools in Strasbourg."""
    name = "piscines"
    path = "lieux_piscines"
    primary_keys = ["recordid"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "piscines.json"
class PiscinesFrequentationStream(StrasbourgDataStream):
    """Stream representing frequentation of swimming pools in Strasbourg."""
    name = "piscines_frequentation"
    path = "frequentation-en-temps-reel-des-piscines"
    primary_keys = ["recordid"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "piscines_frequentation.json"
