import httpx
import logging
from typing import Dict, List, Optional, Union, Any
from .exceptions import NetworkError, TimeoutError, APIError
from .utils import process_markdown, process_text
from .models import (
    DocumentOutput,
    MultiDocumentQuery,
    MultiDocumentResponse,
    MultiPageInput,
    RAGQuery,
    RAGResponse,
    ChunksResponse,
    StatusResponse
)

logger = logging.getLogger(__name__)

class CondyClient:
    """Client for interacting with the Condensation.ai API
    
    Examples:
        >>> client = CondyClient(api_key="your-api-key")  # Production
        >>> client = CondyClient(api_key="your-api-key", environment="dev")  # Development
    """
    
    ENVIRONMENTS = {
        "prod": "https://api.condensation.ai/rag",
        "dev": "http://localhost:8010",
        "staging": "https://api.staging.condensation.ai/ra"
    }
    
    def __init__(
        self, 
        api_key: str,
        environment: str = "prod",
        base_url: Optional[str] = None,
        timeout: float = 60.0,
        verbose: bool = False
    ):
        self.api_key = api_key
        self.base_url = base_url or self.ENVIRONMENTS.get(environment, self.ENVIRONMENTS["prod"])
        self.base_url = self.base_url.rstrip('/')
        self.timeout = timeout
        self.verbose = verbose
        self.headers = {
            "x-api-key": self.api_key
        }

    def _log(self, level: str, message: str) -> None:
        if self.verbose:
            getattr(logger, level)(message)

    async def fetch_content(self, url: str) -> str:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                return response.text
            except httpx.TimeoutException as e:
                self._log("error", f"Content fetch timed out: {str(e)}")
                raise TimeoutError("Timeout while fetching content") from e
            except httpx.RequestError as e:
                self._log("error", f"Network error during content fetch: {str(e)}")
                raise NetworkError("Network error while fetching content") from e
    async def process_document(
        self,
        url: Optional[str] = None,
        content: Optional[str] = None,
        content_type: str = "markdown",
        filename: Optional[str] = None,
        file_key: Optional[str] = None,
        public_url: Optional[str] = None
    ) -> DocumentOutput:
        """Process and upload a document
        
        Args:
            url: Optional URL to fetch content from
            content: Optional direct content input
            content_type: Type of content ("markdown" or "text")
            filename: Optional name of the file
            file_key: Optional key identifier for the file
            public_url: Optional public URL where the file is accessible
            
        Returns:
            DocumentOutput containing document ID and processing status
        """
        try:
            # Get content either from URL or direct input
            if url:
                self._log("info", "Fetching content from URL...")
                document_content = await self.fetch_content(url)
            elif content:
                document_content = content
            else:
                raise ValueError("Either url or content must be provided")

            # Process content based on type
            self._log("info", f"Processing content as {content_type}...")
            if content_type == "markdown":
                pages_dict = process_markdown(document_content)
            else:
                pages_dict = process_text(document_content)

            # Upload to API
            self._log("info", f"Uploading {len(pages_dict)} pages...")
            return await self.upload_pages(
                pages_dict,
                filename=filename,
                file_key=file_key,
                public_url=public_url
            )

        except Exception as e:
            self._log("error", f"Error processing document: {str(e)}")
            raise
    async def upload_pages(
        self, 
        pages: Dict[int, str],
        filename: Optional[str] = None,
        file_key: Optional[str] = None,
        public_url: Optional[str] = None
    ) -> DocumentOutput:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                input_data = MultiPageInput(
                    pages=pages,
                    filename=filename,
                    file_key=file_key,
                    public_url=public_url
                )
                
                response = await client.post(
                    f"{self.base_url}/raginmultipage",
                    json=input_data.model_dump(exclude_none=True),
                    headers=self.headers
                )
                
                if not response.is_success:
                    self._log("error", f"Error response: {response.status_code}")
                    self._log("error", f"Response body: {response.json()}")
                    raise APIError(
                        response.status_code,
                        response.json().get('detail', 'Unknown error')
                    )
                    
                return DocumentOutput(**response.json())
                
            except httpx.TimeoutException as e:
                self._log("error", f"Upload request timed out: {str(e)}")
                raise TimeoutError("Request timed out") from e
            except httpx.RequestError as e:
                self._log("error", f"Network error during upload: {str(e)}")
                raise NetworkError("Network error occurred") from e

    async def check_status(self, document_id: str) -> StatusResponse:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.get(
                    f"{self.base_url}/raginmultipage/{document_id}/status",
                    headers=self.headers
                )
                
                if not response.is_success:
                    self._log("error", f"Error response: {response.status_code}")
                    self._log("error", f"Response body: {response.json()}")
                    raise APIError(
                        response.status_code,
                        response.json().get('detail', 'Unknown error')
                    )
                
                return StatusResponse(**response.json())
                
            except httpx.TimeoutException as e:
                self._log("error", f"Status check timed out: {str(e)}")
                raise TimeoutError("Request timed out") from e
            except httpx.RequestError as e:
                self._log("error", f"Network error during status check: {str(e)}")
                raise NetworkError("Network error occurred") from e

    async def query_rag(
        self, 
        question: str, 
        document_id: str, 
        max_chunks: int = 5
    ) -> RAGResponse:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                query = RAGQuery(
                    question=question,
                    document_id=document_id,
                    max_chunks=max_chunks
                )
                
                response = await client.post(
                    f"{self.base_url}/ragout",
                    json=query.model_dump(),
                    headers=self.headers
                )
                
                if not response.is_success:
                    self._log("error", f"Error response: {response.status_code}")
                    self._log("error", f"Response body: {response.json()}")
                    raise APIError(
                        response.status_code,
                        response.json().get('detail', 'Unknown error')
                    )
                
                return RAGResponse(**response.json())
                
            except httpx.TimeoutException as e:
                self._log("error", f"Query request timed out: {str(e)}")
                raise TimeoutError("Request timed out") from e
            except httpx.RequestError as e:
                self._log("error", f"Network error during query: {str(e)}")
                raise NetworkError("Network error occurred") from e

    async def fetch_chunks(
        self, 
        document_id: str, 
        include_embeddings: bool = False
    ) -> ChunksResponse:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                params = {"include_embeddings": "true"} if include_embeddings else {}
                
                response = await client.get(
                    f"{self.base_url}/chunks/{document_id}",
                    params=params,
                    headers=self.headers
                )
                
                if not response.is_success:
                    self._log("error", f"Error response: {response.status_code}")
                    self._log("error", f"Response body: {response.json()}")
                    raise APIError(
                        response.status_code,
                        response.json().get('detail', 'Unknown error')
                    )
                
                return ChunksResponse(**response.json())
                
            except httpx.TimeoutException as e:
                self._log("error", f"Chunks request timed out: {str(e)}")
                raise TimeoutError("Request timed out") from e
            except httpx.RequestError as e:
                self._log("error", f"Network error fetching chunks: {str(e)}")
                raise NetworkError("Network error occurred") from e

    async def query_multiple_documents(
        self,
        query: str,
        document_ids: List[str],
    ) -> MultiDocumentResponse:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                query_data = MultiDocumentQuery(
                    query=query,
                    document_ids=document_ids
                )
                
                response = await client.post(
                    f"{self.base_url}/ragmulti",
                    json=query_data.model_dump(),
                    headers=self.headers
                )
                
                if not response.is_success:
                    self._log("error", f"Error response: {response.status_code}")
                    self._log("error", f"Response body: {response.json()}")
                    raise APIError(
                        response.status_code,
                        response.json().get('detail', 'Unknown error')
                    )
                
                return MultiDocumentResponse(**response.json())
                
            except httpx.TimeoutException as e:
                self._log("error", f"Multi-query request timed out: {str(e)}")
                raise TimeoutError("Request timed out") from e
            except httpx.RequestError as e:
                self._log("error", f"Network error during multi-query: {str(e)}")
                raise NetworkError("Network error occurred") from e