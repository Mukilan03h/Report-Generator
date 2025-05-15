# Daily Report Generator

A Streamlit web application that generates structured daily reports from various inputs using Google's Gemini API.

## Features

- Generate reports from text input or file uploads
- Multiple report templates (Operations, Development, Meetings, Custom)
- Support for various file formats (TXT, MD, DOCX, CSV, XLSX, PDF)
- Dark/Light mode toggle
- Report history and archiving
- Export functionality (Markdown, HTML, PDF)
- Secure API key management

## Prerequisites

- Python 3.10+
- Google Gemini API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/daily-report-generator.git
   cd daily-report-generator
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run src/report_generator/app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

3. Select a report template, enter your content or upload a file, and click "Generate Report"

## Project Structure

```
report_generator/
├── data/                   # Data storage for reports
├── logs/                   # Application logs
├── src/
│   └── report_generator/
│       ├── __init__.py
│       ├── app.py          # Main Streamlit application
│       ├── config.py       # Application configuration
│       ├── gemini_utils.py # Gemini API integration
│       ├── report_utils.py # Report management
│       └── file_utils.py   # File handling utilities
├── .env.example           # Example environment variables
├── .gitignore
├── README.md
└── requirements.txt       # Python dependencies
```

## Configuration

Configuration options can be set in `.env`:

```
# Required
GEMINI_API_KEY=your_api_key_here

# Optional
LOG_LEVEL=INFO
DATA_DIR=./data
TEMPLATES_DIR=./templates
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Google Gemini](https://ai.google.dev/) for the powerful AI capabilities
- All contributors who have helped improve this project