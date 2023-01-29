"""REST client handling, including StrasbourgDataStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class StrasbourgDataStream(RESTStream):
    """StrasbourgData stream class."""

    url_base = "https://data.strasbourg.eu/api/records/1.0/search/?dataset="

    records_jsonpath = "$.records[*]"
