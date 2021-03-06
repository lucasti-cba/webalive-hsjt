from typing import Dict, Mapping, Sequence, Tuple, Union

_Cap = Dict[str, Union[str, int]]

def findmatch(
    caps: Mapping[str, list[_Cap]], MIMEtype: str, key: str = ..., filename: str = ..., plist: Sequence[str] = ...
) -> Tuple[str | None, _Cap | None]: ...
def getcaps() -> dict[str, list[_Cap]]: ...
