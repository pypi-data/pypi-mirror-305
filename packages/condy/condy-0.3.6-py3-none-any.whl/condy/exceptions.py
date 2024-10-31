class CondyException(Exception):
    """Base exception for all condy-related errors"""
    pass

class NetworkError(CondyException):
    """Raised when network-related errors occur"""
    pass

class TimeoutError(CondyException):
    """Raised when requests timeout"""
    pass

class ProcessingError(CondyException):
    """Raised when processing markdown content fails"""
    pass

class APIError(CondyException):
    """Raised when API returns an error response"""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"API Error ({status_code}): {detail}")