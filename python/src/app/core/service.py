from __future__ import annotations
from typing import Tuple


class Service:
    def __init__(self):
        self.version = 1

    def query(self) -> str:
        return 'string response'

    def get_version(self) -> int:
        return self.version

    def health(self) -> Tuple:
        return "Healthy", 200
