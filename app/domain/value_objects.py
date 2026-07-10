from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class BirthDate:
    value: date


@dataclass(frozen=True)
class FullName:
    value: str