"""StrasbourgData tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_strasbourgdata.streams import (
    StrasbourgDataStream,
    PiscinesStream,
    PiscinesFrequentationStream
)
STREAM_TYPES = [
    #PiscinesStream,
    PiscinesFrequentationStream
]


class TapStrasbourgData(Tap):
    """strasbourgdata tap class."""
    name = "tap-strasbourgdata"

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapStrasbourgData.cli()
