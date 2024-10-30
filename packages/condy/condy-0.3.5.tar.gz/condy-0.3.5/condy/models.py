from typing import Any, List, Optional, Dict
from pydantic import BaseModel, Field
from uuid import UUID

class CostStats(BaseModel):
    """Cost statistics for processing"""
    total_tokens: int
    total_cost: float

class TotalStats(BaseModel):
    """Total processing statistics"""
    tokens: int
    cost: float
    initial_estimate: float
    additional_cost: float

class ProcessingSummaryStats(BaseModel):
    """Detailed processing summary statistics"""
    pages_processed: int
    condensation_rag_stats: CostStats
    embedding_stats: CostStats
    total: TotalStats
class ProcessingProgress(BaseModel):
    """Progress information for document processing"""
    elapsed_time: float
    status: str
    processed_pages: int
    total_pages: int
    progress_percentage: float
    processing_summary: Optional[ProcessingSummaryStats] = None
class MultiPageInput(BaseModel):
    """Input for uploading multi-page documents"""
    pages: Dict[int, str]
    filename: Optional[str] = None
    file_key: Optional[str] = None
    public_url: Optional[str] = None

class MultiDocumentQuery(BaseModel):
    """Query across multiple documents"""
    document_ids: List[str]
    query: str

class MultiDocumentResponse(BaseModel):
    """Response from multi-document query"""
    relevant_content: List[Dict[str, Any]]
    source_pages: Dict[str, List[int]]

class RAGQuery(BaseModel):
    """Single document RAG query"""
    question: str
    document_id: str
    max_chunks: Optional[int] = Field(default=5, ge=1, le=20)

class RAGResponse(BaseModel):
    """Response from RAG query"""
    answer: str
    source_pages: List[int]

class ChunkData(BaseModel):
    """Individual chunk information"""
    content: str
    page_number: int
    embedding: Optional[List[float]] = None

class ChunksResponse(BaseModel):
    """Response containing document chunks"""
    document_id: UUID
    chunks: List[ChunkData]

class DocumentOutput(BaseModel):
    """Response from document upload/processing"""
    document_id: str
    message: str = "Document processing started"
    total_pages: int
    processed_pages: int = 0
    status: str = "processing"
    processing_summary: Optional[ProcessingSummaryStats] = None
    error_message: Optional[str] = None

class StatusResponse(BaseModel):
    """Document processing status response"""
    total_pages: int
    processed_pages: int
    status: str
    processing_summary: ProcessingSummaryStats
    error_message: Optional[str] = None

    class Config:
        from_attributes = True