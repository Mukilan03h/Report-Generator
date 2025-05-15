import os
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime, date
from pathlib import Path
import logging
import json
from typing import Dict, Any, Optional, List

# Local imports
from .config import (
    BASE_DIR, DATA_DIR, LOG_DIR, TEMPLATES_DIR,
    GEMINI_API_KEY, GEMINI_MODEL, GEMINI_TEMPERATURE, GEMINI_MAX_TOKENS,
    DEFAULT_REPORT_TEMPLATE, REPORT_HISTORY_FILE, THEMES
)
from .gemini_utils import GeminiReportGenerator
from .report_utils import ReportManager
from .file_utils import FileProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / 'app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv(BASE_DIR / '.env')

# Set page config
st.set_page_config(
    page_title="Daily Report Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize report manager and file processor
report_manager = ReportManager(REPORT_HISTORY_FILE)
file_processor = FileProcessor()

# Initialize Gemini API client
gemini_client = GeminiReportGenerator(GEMINI_API_KEY)
GEMINI_AVAILABLE = True

def init_session_state():
    """Initialize session state variables"""
    defaults = {
        'dark_mode': False,
        'report_history': [],
        'current_report': None,
        'template': 'default',
        'report_content': '',
        'report_date': date.today(),
        'report_priority': 'Medium',
        'uploaded_file': None,
        'generated_report': None
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def setup_ui():
    """Setup the main UI components"""
    st.title("📝 Daily Report Generator")
    st.markdown("Generate structured daily reports from various inputs using AI")

def render_sidebar() -> Dict[str, Any]:
    """Render the sidebar and return settings"""
    with st.sidebar:
        st.header("Settings")
        
        # Theme toggle
        st.session_state.dark_mode = st.toggle(
            "Dark Mode", 
            value=st.session_state.dark_mode,
            key="dark_mode_toggle"
        )
        
        # Template selection
        st.subheader("Report Templates")
        template = st.radio(
            "Select a template:",
            ["Default", "Operations", "Development", "Meetings"],
            key="template_radio"
        ).lower()
        
        # File upload
        st.subheader("Import Content")
        uploaded_file = st.file_uploader(
            "Upload a file",
            type=['txt', 'md', 'docx', 'pdf', 'csv', 'xlsx'],
            key="file_uploader"
        )
        
        # Display file info if uploaded
        if uploaded_file is not None:
            file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
            st.write(file_details)
        
        # Add a divider
        st.markdown("---")
        
        # Display app info
        st.markdown("### About")
        st.markdown("""
        This app helps you generate structured daily reports using AI.
        
        **Features:**
        - Multiple report templates
        - File upload support
        - Dark/Light mode
        - Report history
        """)
        
        return {
            'template': template,
            'uploaded_file': uploaded_file
        }

def render_report_form(template: str, uploaded_file: Any = None) -> Dict[str, Any]:
    """Render the report form and return form data"""
    form_data = {}
    
    with st.expander("📝 Enter Report Details", expanded=True):
        # Content input
        if uploaded_file:
            try:
                # Save the uploaded file and extract text
                saved_file = file_processor.save_uploaded_file(uploaded_file, DATA_DIR)
                form_data['content'] = file_processor.extract_text(saved_file)
                st.success("File processed successfully!")
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
                form_data['content'] = ""
        else:
            form_data['content'] = st.text_area(
                "Enter your report content:",
                height=200,
                placeholder="Paste your notes, meeting minutes, or bullet points here...",
                key="report_content"
            )
        
        # Additional options
        col1, col2 = st.columns(2)
        with col1:
            form_data['date'] = st.date_input(
                "Report Date",
                value=st.session_state.report_date,
                key="report_date"
            )
        with col2:
            form_data['priority'] = st.select_slider(
                "Priority",
                options=["Low", "Medium", "High"],
                value=st.session_state.report_priority,
                key="report_priority"
            )
        
        # Template-specific options
        form_data['template'] = template
        
    return form_data

def generate_report(form_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Generate a report using the Gemini API"""
    if not form_data.get('content', '').strip():
        st.warning("Please enter some content to generate a report.")
        return None
    
    if not GEMINI_AVAILABLE:
        st.error("Gemini API is not available. Please check your API key and internet connection.")
        return None
    
    with st.spinner("Generating your report..."):
        try:
            # Generate the report using Gemini
            generated_content = gemini_client.generate_report(
                content=form_data['content'],
                template=form_data['template'],
                max_tokens=GEMINI_MAX_TOKENS,
                temperature=GEMINI_TEMPERATURE
            )
            
            # Create report object
            report = {
                'id': f"report_{int(datetime.now().timestamp())}",
                'title': f"{form_data['template'].capitalize()} Report - {form_data['date']}",
                'content': generated_content,
                'template': form_data['template'],
                'date': form_data['date'].isoformat(),
                'priority': form_data['priority'],
                'created_at': datetime.now().isoformat(),
                'metadata': {
                    'model': GEMINI_MODEL,
                    'max_tokens': GEMINI_MAX_TOKENS,
                    'temperature': GEMINI_TEMPERATURE
                }
            }
            
            # Save the report
            report_id = report_manager.save_report(report)
            st.session_state.current_report = report
            st.session_state.report_history = report_manager.list_reports()
            
            st.success("Report generated successfully!")
            st.balloons()
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            st.error(f"An error occurred while generating the report: {str(e)}")
            return None

def render_report(report: Dict[str, Any]):
    """Render the generated report"""
    if not report:
        return
    
    st.subheader(report.get('title', 'Generated Report'))
    
    # Display metadata
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Template", report.get('template', 'N/A').capitalize())
    with col2:
        st.metric("Date", report.get('date', 'N/A'))
    with col3:
        st.metric("Priority", report.get('priority', 'N/A'))
    
    # Display report content
    st.markdown("---")
    st.markdown(report.get('content', ''))
    
    # Add export options
    st.markdown("---")
    st.subheader("Export Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(
            label="📄 Save as Markdown",
            data=report.get('content', ''),
            file_name=f"{report.get('id', 'report')}.md",
            mime="text/markdown"
        )
    
    with col2:
        # HTML export
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1 {{ color: #1f77b4; }}
                .metadata {{ display: flex; justify-content: space-between; margin-bottom: 20px; }}
                .metadata-item {{ margin-right: 20px; }}
            </style>
        </head>
        <body>
            <h1>{title}</h1>
            <div class="metadata">
                <div class="metadata-item"><strong>Date:</strong> {date}</div>
                <div class="metadata-item"><strong>Priority:</strong> {priority}</div>
                <div class="metadata-item"><strong>Template:</strong> {template}</div>
            </div>
            <div class="content">
                {content}
            </div>
        </body>
        </html>
        """.format(
            title=report.get('title', 'Generated Report'),
            date=report.get('date', 'N/A'),
            priority=report.get('priority', 'N/A'),
            template=report.get('template', 'N/A').capitalize(),
            content=report.get('content', '')
        )
        
        st.download_button(
            label="🌐 Save as HTML",
            data=html_content,
            file_name=f"{report.get('id', 'report')}.html",
            mime="text/html"
        )
    
    with col3:
        # PDF export would require additional dependencies like reportlab or weasyprint
        st.button(
            "📝 Save as PDF (Coming Soon)",
            disabled=True,
            help="PDF export will be available in a future update"
        )

def render_report_history():
    """Display a list of previously generated reports"""
    st.sidebar.markdown("---")
    st.sidebar.subheader("Recent Reports")
    
    reports = report_manager.list_reports(limit=5)
    
    if not reports:
        st.sidebar.info("No reports generated yet.")
        return
    
    for report in reports:
        if st.sidebar.button(
            f"{report.get('title', 'Untitled Report')}",
            key=f"report_{report.get('id')}",
            use_container_width=True
        ):
            st.session_state.current_report = report
            st.rerun()

def main():
    """Main application function"""
    # Initialize session state
    init_session_state()
    
    # Setup UI
    setup_ui()
    
    # Apply theme
    apply_theme(st.session_state.dark_mode)
    
    # Render sidebar and get settings
    sidebar_data = render_sidebar()
    
    # Render report form
    form_data = render_report_form(
        template=sidebar_data['template'],
        uploaded_file=sidebar_data['uploaded_file']
    )
    
    # Generate report button
    if st.button("Generate Report", type="primary", key="generate_btn"):
        report = generate_report(form_data)
        if report:
            st.session_state.generated_report = report
    
    # Display generated report if available
    if 'generated_report' in st.session_state and st.session_state.generated_report:
        render_report(st.session_state.generated_report)
    
    # Display report history in sidebar
    render_report_history()

def apply_theme(dark_mode: bool = False):
    """Apply the selected theme"""
    theme = THEMES['dark'] if dark_mode else THEMES['light']
    
    # This is a simplified example. For full theme control, you would need to use custom CSS
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {theme['background']};
                color: {theme['text']};
            }}
            .stButton>button {{
                background-color: {theme['primary']};
                color: white;
            }}
            .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {{
                color: {theme['text']};
                background-color: {theme['background']};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
