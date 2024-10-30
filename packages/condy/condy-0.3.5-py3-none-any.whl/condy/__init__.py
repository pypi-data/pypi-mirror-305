from .client import CondyClient
from .exceptions import (
    CondyException,
    NetworkError,
    TimeoutError,
    ProcessingError,
    APIError
)
from .models import (
    DocumentOutput,
    MultiPageInput,
    MultiDocumentQuery,
    MultiDocumentResponse,
    RAGQuery,
    RAGResponse,
    ChunksResponse,
    StatusResponse,
    ProcessingSummaryStats,
    CostStats,
    TotalStats,
    ProcessingProgress  # Added new model
)

__version__ = "0.3.5"  # Bumped version for new feature
__all__ = [
    "CondyClient",
    "CondyException",
    "NetworkError",
    "TimeoutError",
    "ProcessingError",
    "APIError",
    "DocumentOutput",
    "MultiPageInput",
    "MultiDocumentQuery",
    "MultiDocumentResponse",
    "RAGQuery",
    "RAGResponse",
    "ChunksResponse",
    "StatusResponse",
    "ProcessingSummaryStats",
    "CostStats",
    "TotalStats",
    "ProcessingProgress"  # Added to __all__
]