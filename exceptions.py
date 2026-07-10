class CosmiCodeError(Exception):
    """Base exception for CosmiCode."""


class InvalidBirthDate(CosmiCodeError):
    """Raised when birth date is invalid."""


class CalculationError(CosmiCodeError):
    """Raised when CCI calculation fails."""