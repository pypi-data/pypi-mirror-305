from typing import NamedTuple


class SigningKey(NamedTuple):
    keytype: str
    base64: str
