import os
import tempfile
from pathlib import Path
from typing import Union, Dict, Any, Optional
import logging
import docx
import pandas as pd

logger = logging.getLogger(__name__)

class FileProcessor:
    """Handles file uploads and processing"""
    
    SUPPORTED_EXTENSIONS = [
        '.txt', '.md', '.markdown',  # Text files
        '.docx',  # Word documents
        '.csv', '.xlsx', '.xls',  # Spreadsheets
        '.pdf'  # PDF files (requires additional dependencies)
    ]
    
    @staticmethod
    def save_uploaded_file(uploaded_file, directory: Union[str, Path]) -> Path:
        """
        Save an uploaded file to the specified directory
        
        Args:
            uploaded_file: File object from Streamlit's file_uploader
            directory: Directory to save the file to
            
        Returns:
            Path to the saved file
        """
        try:
            directory = Path(directory)
            directory.mkdir(parents=True, exist_ok=True)
            
            # Create a temporary file with the same extension
            file_ext = Path(uploaded_file.name).suffix.lower()
            temp_file = tempfile.NamedTemporaryFile(
                delete=False, 
                suffix=file_ext,
                dir=directory
            )
            
            # Write the uploaded file to the temporary file
            temp_file.write(uploaded_file.getvalue())
            temp_file.close()
            
            return Path(temp_file.name)
            
        except Exception as e:
            logger.error(f"Failed to save uploaded file: {str(e)}")
            raise
    
    @staticmethod
    def extract_text(file_path: Union[str, Path]) -> str:
        """
        Extract text from various file formats
        
        Args:
            file_path: Path to the file to extract text from
            
        Returns:
            Extracted text as a string
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            # Handle different file types
            if file_path.suffix.lower() == '.docx':
                return FileProcessor._extract_from_docx(file_path)
            elif file_path.suffix.lower() in ['.xlsx', '.xls']:
                return FileProcessor._extract_from_excel(file_path)
            elif file_path.suffix.lower() == '.csv':
                return FileProcessor._extract_from_csv(file_path)
            elif file_path.suffix.lower() == '.pdf':
                return FileProcessor._extract_from_pdf(file_path)
            else:
                # Default to reading as text
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
                    
        except Exception as e:
            logger.error(f"Failed to extract text from {file_path}: {str(e)}")
            raise
    
    @staticmethod
    def _extract_from_docx(file_path: Path) -> str:
        """Extract text from a Word document"""
        doc = docx.Document(file_path)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    
    @staticmethod
    def _extract_from_excel(file_path: Path) -> str:
        """Extract text from Excel files"""
        df = pd.read_excel(file_path)
        return df.to_string()
    
    @staticmethod
    def _extract_from_csv(file_path: Path) -> str:
        """Extract text from CSV files"""
        df = pd.read_csv(file_path)
        return df.to_string()
    
    @staticmethod
    def _extract_from_pdf(file_path: Path) -> str:
        """Extract text from PDF files"""
        try:
            import PyPDF2
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = []
                for page in reader.pages:
                    text.append(page.extract_text())
                return '\n'.join(text)
        except ImportError:
            logger.warning("PyPDF2 is required for PDF processing. Install with: pip install PyPDF2")
            return ""
    
    @staticmethod
    def get_file_metadata(file_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Get metadata about a file
        
        Args:
            file_path: Path to the file
            
        Returns:
            Dictionary containing file metadata
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        stat = file_path.stat()
        
        return {
            'name': file_path.name,
            'size': stat.st_size,
            'created': stat.st_ctime,
            'modified': stat.st_mtime,
            'extension': file_path.suffix.lower(),
            'is_supported': file_path.suffix.lower() in FileProcessor.SUPPORTED_EXTENSIONS
        }
