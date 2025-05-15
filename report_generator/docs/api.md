# API Reference

This document provides detailed information about the Daily Report Generator's API.

## Table of Contents

- [Core Modules](#core-modules)
- [Configuration](#configuration)
- [Report Generation](#report-generation)
- [File Handling](#file-handling)
- [Report Management](#report-management)
- [CLI Reference](#cli-reference)

## Core Modules

### `app`

The main Streamlit application module.

#### Functions

##### `main()`
The main entry point for the Streamlit application.

### `config`

Configuration management for the application.

#### Classes

##### `Config`
Handles loading and accessing configuration settings.

###### Methods
- `load_config()`: Load configuration from environment variables and .env file
- `get(key, default=None)`: Get a configuration value
- `__getitem__(key)`: Get a configuration value (dictionary-style access)

## Configuration

### Environment Variables

See [Configuration Guide](configuration.md) for a complete list of environment variables.

## Report Generation

### `gemini_utils`

Provides functionality for generating reports using the Gemini API.

#### Classes

##### `GeminiReportGenerator`
Handles report generation using the Gemini API.

###### Methods
- `__init__(api_key: str, model: str = "gemini-pro")`: Initialize with API key and model
- `generate_report(content: str, template: str = "default", max_tokens: int = 2048, temperature: float = 0.7) -> str`: Generate a report
- `_prepare_prompt(content: str, template: str) -> str`: Prepare the prompt for the Gemini API
- `_call_gemini_api(prompt: str, max_tokens: int, temperature: float) -> str`: Make the API call to Gemini

## File Handling

### `file_utils`

Provides utilities for handling file uploads and processing.

#### Functions

- `save_uploaded_file(uploaded_file, directory: str = "uploads") -> str`: Save an uploaded file
- `extract_text(file_path: str) -> str`: Extract text from various file formats
- `is_allowed_file(filename: str) -> bool`: Check if a file has an allowed extension

## Report Management

### `report_utils`

Provides functionality for managing reports.

#### Classes

##### `ReportManager`
Manages report storage and retrieval.

###### Methods
- `__init__(storage_file: str = "data/reports.json")`: Initialize with storage file
- `save_report(report_data: dict) -> str`: Save a report
- `get_report(report_id: str) -> Optional[dict]`: Get a report by ID
- `list_reports(limit: int = 10, offset: int = 0, descending: bool = True) -> List[dict]`: List reports with pagination
- `delete_report(report_id: str) -> bool`: Delete a report by ID
- `get_report_count() -> int`: Get the total number of reports

## CLI Reference

The application provides a command-line interface for batch processing.

### Commands

#### `generate`
Generate reports from input files.

```bash
python -m src.report_generator.cli generate --input input.txt --output output.md --template default
```

##### Options
- `-i, --input`: Input file or directory (required)
- `-o, --output`: Output file or directory (default: stdout)
- `-t, --template`: Report template to use (default: "default")
- `--max-tokens`: Maximum number of tokens for generation (default: 2048)
- `--temperature`: Temperature for generation (default: 0.7)

#### `list-templates`
List available report templates.

```bash
python -m src.report_generator.cli list-templates
```

## Error Handling

The API uses custom exceptions for error handling.

### Exceptions

- `ReportGenerationError`: Raised when report generation fails
- `InvalidTemplateError`: Raised when an invalid template is specified
- `FileProcessingError`: Raised when file processing fails
- `APIError`: Raised for API-related errors

## Examples

### Basic Usage

```python
from src.report_generator.gemini_utils import GeminiReportGenerator
from src.report_generator.config import Config

# Initialize config
config = Config()


# Initialize report generator
generator = GeminiReportGenerator(api_key=config["GEMINI_API_KEY"])

# Generate a report
report = generator.generate_report(
    content="Project meeting notes...",
    template="meetings",
    max_tokens=1024,
    temperature=0.7
)

print(report)
```

### Using the Report Manager

```python
from src.report_generator.report_utils import ReportManager

# Initialize report manager
manager = ReportManager("data/reports.json")


# Save a report
report_id = manager.save_report({
    "title": "Weekly Report",
    "content": "This is a test report.",
    "template": "default",
    "date": "2023-01-01"
})

# Retrieve the report
report = manager.get_report(report_id)
print(report)

# List recent reports
recent_reports = manager.list_reports(limit=5)
for r in recent_reports:
    print(f"{r['date']} - {r['title']}")
```

## Rate Limiting

The application implements rate limiting for the Gemini API to prevent hitting usage limits. The default rate limit is 60 requests per minute.
