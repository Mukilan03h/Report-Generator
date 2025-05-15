"""
Unit tests for the Daily Report Generator application.
"""
import pytest
from pathlib import Path
import json
from datetime import datetime

from src.report_generator.report_utils import ReportManager
from src.report_generator.file_utils import FileProcessor

# Test data
SAMPLE_REPORT = {
    "id": "report_123",
    "title": "Test Report",
    "content": "This is a test report.",
    "template": "default",
    "date": "2023-01-01",
    "priority": "Medium",
    "created_at": "2023-01-01T12:00:00"
}

@pytest.fixture
def temp_storage(tmp_path):
    """Create a temporary storage file for testing."""
    storage_file = tmp_path / "test_reports.json"
    # Initialize with empty list
    with open(storage_file, 'w') as f:
        json.dump([], f)
    return storage_file

def test_save_and_retrieve_report(temp_storage):
    """Test saving and retrieving a report."""
    manager = ReportManager(temp_storage)
    
    # Save a report
    report_id = manager.save_report(SAMPLE_REPORT)
    assert report_id is not None
    
    # Retrieve the report
    report = manager.get_report(report_id)
    assert report is not None
    assert report['id'] == report_id
    assert report['title'] == SAMPLE_REPORT['title']

def test_list_reports(temp_storage):
    """Test listing reports with sorting and pagination."""
    manager = ReportManager(temp_storage)
    
    # Add multiple reports with different dates
    reports = [
        {"id": f"report_{i}", "title": f"Report {i}", "created_at": f"2023-01-{i:02d}T12:00:00"}
        for i in range(1, 6)
    ]
    
    for report in reports:
        manager.save_report(report)
    
    # Test default sorting (descending by created_at)
    listed = manager.list_reports(limit=3)
    assert len(listed) == 3
    assert listed[0]['id'] == 'report_5'  # Most recent first
    
    # Test ascending order
    listed = manager.list_reports(limit=3, descending=False)
    assert listed[0]['id'] == 'report_1'  # Oldest first

def test_file_processor_save_and_extract(tmp_path):
    """Test file saving and text extraction."""
    processor = FileProcessor()
    test_content = "This is a test file."
    test_file = tmp_path / "test.txt"
    
    # Create a test file
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    # Test text extraction
    extracted = processor.extract_text(test_file)
    assert extracted.strip() == test_content

# Add more tests as needed
