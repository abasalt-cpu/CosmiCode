from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


class ReportType(Enum):
    BASIC = "basic"
    ADVANCED = "advanced"
    PREMIUM = "premium"