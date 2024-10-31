# Condy: Python Client for Condensation.ai

A modern, async Python client library for interacting with the Condensation.ai API, providing seamless access to document processing and RAG (Retrieval-Augmented Generation) capabilities.

## Features

- 🚀 Fully async implementation using `httpx`
- 📄 Document processing and chunking
- 🔍 RAG (Retrieval-Augmented Generation) querying
- 💪 Type hints and modern Python practices
- ⚡ Efficient markdown processing and page management
- 🛡️ Comprehensive error handling
- 📝 Rich document metadata support

## Installation

```bash
pip install condy
```

## Quick Start

```python
import asyncio
from condy import CondyClient

async def main():
    # Initialize the client
    client = CondyClient(api_key="your-api-key")
    
    # Process a document from URL with metadata
    doc_output = await client.process_document(
        url="https://example.com/document.md",
        filename="document.md",
        file_key="custom-key",
        public_url="https://example.com/document.md"
    )
    
    # Query the document using RAG
    response = await client.query_rag(
        question="What are the key points?",
        document_id=doc_output.document_id
    )
    
    print(response.answer)

asyncio.run(main())
```

## Core Features

### Document Processing

```python
# Upload pages directly with metadata
pages = {
    1: "Page 1 content",
    2: "Page 2 content"
}
doc_output = await client.upload_pages(
    pages=pages,
    filename="document.txt",
    file_key="unique-identifier",
    public_url="https://example.com/document.txt"
)

# Or process markdown from URL with metadata
doc_output = await client.process_document(
    url="https://example.com/document.md",
    filename="document.md",
    file_key="doc-123",
    public_url="https://example.com/document.md"
)
```

### RAG Queries

```python
# Query a document
response = await client.query_rag(
    question="What does the document say about X?",
    document_id="doc-id",
    max_chunks=5
)

# Access the response
print(response.answer)
print(response.source_pages)  # List of source pages used
```

### Chunk Management

```python
# Fetch document chunks
chunks = await client.fetch_chunks(
    document_id="doc-id",
    include_embeddings=False  # Set to True to include vector embeddings
)
```

## Configuration

The client can be configured with custom settings:

```python
client = CondyClient(
    api_key="your-api-key",
    base_url="https://custom-url.example.com",  # Optional
    timeout=60.0  # Custom timeout in seconds
)
```

## Document Metadata

The library supports rich document metadata:

```python
# Process document with full metadata
doc_output = await client.process_document(
    url="https://example.com/doc.pdf",
    content_type="pdf",
    filename="important-doc.pdf",  # Optional: Custom filename
    file_key="doc-2023-01",       # Optional: Unique identifier
    public_url="https://example.com/doc.pdf"  # Optional: Public access URL
)
```

## Error Handling

The library provides specific exceptions for different error cases:

- `NetworkError`: For connection and network-related issues
- `TimeoutError`: For request timeout issues
- `APIError`: For API-specific errors with status codes and details

```python
from condy import NetworkError, TimeoutError, APIError

try:
    response = await client.query_rag(question="...", document_id="...")
except TimeoutError:
    print("Request timed out")
except NetworkError:
    print("Network error occurred")
except APIError as e:
    print(f"API error: {e.status_code} - {e.detail}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

The usage of the library is subject to the [Condensation.ai Terms of Service](https://condensation.ai/terms-and-conditions).

## Support

For support, please contact support@condensation.ai.