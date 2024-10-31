import re
import logging
from typing import Dict
from .exceptions import ProcessingError

logger = logging.getLogger(__name__)

def process_markdown(content: str) -> Dict[int, str]:
    """Process markdown content into pages using page markers"""
    logger.info("Starting markdown processing")
    if not content:
        raise ProcessingError("Empty markdown content")

    try:
        # Split the content into pages
        pages = re.split(r'<!-- PAGE \d+ -->', content)
        pages = [page.strip() for page in pages if page.strip()]

        # Create a dictionary with integer keys
        page_dict = {i: content for i, content in enumerate(pages, start=1)}

        if not page_dict:
            raise ProcessingError("No extractable text found in the markdown")

        logger.info(f"Markdown processing completed. Extracted {len(page_dict)} pages.")
        return page_dict
    except Exception as e:
        logger.error(f"Error processing markdown: {str(e)}")
        raise ProcessingError(f"Failed to process markdown: {str(e)}")

def process_text(
    content: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> Dict[int, str]:
    """
    Process raw text into overlapping chunks.
    
    Args:
        content: Raw text content
        chunk_size: Size of each chunk in characters
        overlap: Number of characters to overlap between chunks
        
    Returns:
        Dict[int, str]: Dictionary of chunk number to chunk content
    """
    logger.info("Starting text processing")
    if not content:
        raise ProcessingError("Empty text content")

    try:
        # Split content into sentences (rough approximation)
        sentences = re.split(r'(?<=[.!?])\s+', content)
        
        chunks = []
        current_chunk = []
        current_length = 0
        
        for sentence in sentences:
            sentence_length = len(sentence)
            
            if current_length + sentence_length > chunk_size:
                # Store current chunk
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                
                # Start new chunk with overlap
                if chunks:
                    # Get last few sentences from previous chunk
                    overlap_text = ' '.join(current_chunk[-3:])  # Adjust as needed
                    current_chunk = [overlap_text, sentence]
                    current_length = len(overlap_text) + sentence_length
                else:
                    current_chunk = [sentence]
                    current_length = sentence_length
            else:
                current_chunk.append(sentence)
                current_length += sentence_length
        
        # Add final chunk
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        # Create page dictionary
        page_dict = {i: chunk for i, chunk in enumerate(chunks, start=1)}
        
        if not page_dict:
            raise ProcessingError("No extractable text found in the content")

        logger.info(f"Text processing completed. Created {len(page_dict)} chunks.")
        return page_dict
        
    except Exception as e:
        logger.error(f"Error processing text: {str(e)}")
        raise ProcessingError(f"Failed to process text: {str(e)}")