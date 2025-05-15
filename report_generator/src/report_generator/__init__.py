"""
Daily Report Generator

A Streamlit web application that generates structured daily reports from various inputs
using Google's Gemini API.
"""

__version__ = '0.1.0'
__author__ = 'Your Name <your.email@example.com>'
__all__ = ['app', 'config', 'gemini_utils', 'report_utils', 'file_utils']

# Import main components
from .config import *
from .gemini_utils import GeminiReportGenerator
from .report_utils import ReportManager
from .file_utils import FileProcessor
