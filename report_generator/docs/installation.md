# Installation Guide

This guide will help you set up the Daily Report Generator application on your local machine.

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git (optional, for development)
- A Google Gemini API key

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/daily-report-generator.git
cd daily-report-generator
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

=== "macOS/Linux"
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

=== "Windows"
    ```powershell
    python -m venv venv
    .\\venv\\Scripts\\activate
    ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with your Gemini API key:

```env
# Required
GEMINI_API_KEY=your_api_key_here

# Optional: Application Settings
LOG_LEVEL=INFO
DATA_DIR=./data
TEMPLATES_DIR=./templates

# UI Settings
DEFAULT_THEME=light  # or 'dark'

# Report Generation
DEFAULT_TEMPLATE=default  # default, operations, development, meetings
MAX_TOKENS=2048
TEMPERATURE=0.7

# File upload settings
MAX_UPLOAD_SIZE=10  # in MB
ALLOWED_EXTENSIONS=.txt,.md,.markdown,.docx,.csv,.xlsx,.xls,.pdf
```

## Verifying the Installation

To verify that everything is set up correctly, run:

```bash
streamlit run src/report_generator/app.py
```

Then open your web browser and navigate to `http://localhost:8501`. You should see the Daily Report Generator interface.

## Updating

To update to the latest version:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Troubleshooting

### Missing Dependencies

If you encounter any `ModuleNotFoundError` errors, make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### API Key Issues

If you see authentication errors, verify that:

1. Your Gemini API key is correctly set in the `.env` file
2. The API key has the necessary permissions
3. You have an active internet connection

### File Permission Issues

On some systems, you might encounter file permission errors. Try running the application with administrator/root privileges or adjust the file permissions accordingly.

## Next Steps

- [Usage Guide](usage.md)
- [Configuration Options](configuration.md)
