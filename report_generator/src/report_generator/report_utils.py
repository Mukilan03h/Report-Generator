import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ReportManager:
    """Manages report storage and retrieval"""
    
    def __init__(self, storage_path: Path):
        """
        Initialize the ReportManager
        
        Args:
            storage_path: Path to the JSON file where reports will be stored
        """
        self.storage_path = storage_path
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """Ensure the storage file and parent directory exist"""
        try:
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            if not self.storage_path.exists():
                with open(self.storage_path, 'w') as f:
                    json.dump([], f)
        except Exception as e:
            logger.error(f"Failed to initialize report storage: {str(e)}")
            raise
    
    def save_report(self, report_data: Dict[str, Any]) -> str:
        """
        Save a report to the storage
        
        Args:
            report_data: Dictionary containing report data
            
        Returns:
            The ID of the saved report
        """
        try:
            # Load existing reports
            reports = self._load_reports()
            
            # Generate a unique ID for the report
            report_id = f"report_{len(reports) + 1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            # Add metadata
            report_data.update({
                'id': report_id,
                'created_at': datetime.now().isoformat(),
            })
            
            # Add to reports
            reports.append(report_data)
            
            # Save back to file
            self._save_reports(reports)
            
            return report_id
            
        except Exception as e:
            logger.error(f"Failed to save report: {str(e)}")
            raise
    
    def get_report(self, report_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a report by ID
        
        Args:
            report_id: ID of the report to retrieve
            
        Returns:
            The report data or None if not found
        """
        reports = self._load_reports()
        for report in reports:
            if report.get('id') == report_id:
                return report
        return None
    
    def list_reports(
        self, 
        limit: int = 10, 
        offset: int = 0,
        sort_by: str = 'created_at',
        descending: bool = True
    ) -> List[Dict[str, Any]]:
        """
        List all reports with pagination and sorting
        
        Args:
            limit: Maximum number of reports to return
            offset: Number of reports to skip
            sort_by: Field to sort by
            descending: Sort in descending order
            
        Returns:
            List of report summaries
        """
        reports = self._load_reports()
        
        # Sort reports
        try:
            reports.sort(
                key=lambda x: x.get(sort_by, ''), 
                reverse=descending
            )
        except (KeyError, TypeError):
            logger.warning(f"Could not sort by {sort_by}, using default sorting")
        
        # Apply pagination
        return reports[offset:offset + limit]
    
    def delete_report(self, report_id: str) -> bool:
        """
        Delete a report by ID
        
        Args:
            report_id: ID of the report to delete
            
        Returns:
            True if deleted, False if not found
        """
        reports = self._load_reports()
        initial_count = len(reports)
        
        # Filter out the report to delete
        reports = [r for r in reports if r.get('id') != report_id]
        
        if len(reports) < initial_count:
            self._save_reports(reports)
            return True
        return False
    
    def _load_reports(self) -> List[Dict[str, Any]]:
        """Load all reports from storage"""
        try:
            if not self.storage_path.exists():
                return []
                
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            logger.warning("Report storage file is corrupted or not found, starting fresh")
            return []
    
    def _save_reports(self, reports: List[Dict[str, Any]]) -> None:
        """Save reports to storage"""
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(reports, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save reports: {str(e)}")
            raise
