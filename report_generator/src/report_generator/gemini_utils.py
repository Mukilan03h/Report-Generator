import os
import google.generativeai as genai
from typing import Dict, Any, Optional
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class GeminiReportGenerator:
    """Handles report generation using Google's Gemini API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Gemini API client"""
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def generate_report(
        self,
        content: str,
        template: str = "default",
        max_tokens: int = 2048,
        temperature: float = 0.7
    ) -> str:
        """
        Generate a report using the Gemini API
        
        Args:
            content: Input content to generate report from
            template: Type of report template to use
            max_tokens: Maximum number of tokens to generate
            temperature: Controls randomness (0.0 to 1.0)
            
        Returns:
            Generated report as a string
        """
        try:
            # Prepare the prompt based on the template
            prompt = self._prepare_prompt(content, template)
            
            # Generate content
            response = self.model.generate_content(
                prompt,
                generation_config={
                    'temperature': temperature,
                    'max_output_tokens': max_tokens,
                }
            )
            
            return response.text
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise
    
    def _prepare_prompt(self, content: str, template: str) -> str:
        """Prepare the prompt based on the template"""
        templates = {
            "default": (
                "Please create a well-structured daily report based on the following notes. "
                "Include a summary, key points, and action items. Make it clear and professional.\n\n"
                "Notes:\n{content}"
            ),
            "operations": (
                "Create an operations report with the following information. "
                "Include metrics, issues, and recommendations.\n\n"
                "Input:\n{content}"
            ),
            "development": (
                "Generate a development status report. Include completed tasks, in-progress work, "
                "blockers, and next steps.\n\n"
                "Notes:\n{content}"
            ),
            "meetings": (
                "Create meeting minutes from the following notes. Include decisions made, "
                "action items with owners, and key discussion points.\n\n"
                "Meeting Notes:\n{content}"
            )
        }
        
        # Get the appropriate template or use default
        template_prompt = templates.get(template.lower(), templates["default"])
        return template_prompt.format(content=content)
    
    def validate_api_key(self) -> bool:
        """Validate the Gemini API key"""
        try:
            models = genai.list_models()
            return len(list(models)) > 0
        except Exception as e:
            logger.error(f"API key validation failed: {str(e)}")
            return False
