from typing import Any, List, Optional, Dict
from pydantic import BaseModel, Field
from uuid import UUID

class ProcessingSummary(BaseModel):
    """Processing status and progress information"""
    pages_processed: int = Field(default=0, alias="processed_pages")
    total_pages: int
    current_status: str
    cost: Optional[float] = 0.0
    additional_cost: Optional[float] = 0.0
    error_message: Optional[str] = None

class DocumentOutput(BaseModel):
    """Response from document upload/processing"""
    message: str
    document_id: str
    processing_summary: ProcessingSummary

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "message": "Document processing started",
                "document_id": "123e4567-e89b-12d3-a456-426614174000",
                "processing_summary": {
                    "processed_pages": 0,
                    "total_pages": 5,
                    "current_status": "processing",
                    "cost": 0.0,
                    "additional_cost": 0.0
                }
            }
        }
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

class StatusResponse(BaseModel):
    """Document processing status"""
    processing_summary: ProcessingSummary
    queue_position: Optional[int] = None