# Configuration Guide

This guide explains all the configuration options available in the Daily Report Generator application.

## Table of Contents

- [Environment Variables](#environment-variables)
- [Application Settings](#application-settings)
- [UI Customization](#ui-customization)
- [Report Generation](#report-generation)
- [File Handling](#file-handling)
- [Logging](#logging)
- [Advanced Configuration](#advanced-configuration)

## Environment Variables

Configuration is primarily done through environment variables, which can be set in a `.env` file in the project root or in your system environment.

## Application Settings

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `LOG_LEVEL` | string | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) |
| `DATA_DIR` | path | `./data` | Directory to store application data |
| `TEMPLATES_DIR` | path | `./templates` | Directory containing report templates |
| `MAX_UPLOAD_SIZE` | int | `10` | Maximum file upload size in MB |
| `ALLOWED_EXTENSIONS` | string | `.txt,.md,.docx,.pdf,.csv,.xlsx` | Comma-separated list of allowed file extensions |

## UI Customization

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `DEFAULT_THEME` | string | `light` | Default theme (`light` or `dark`) |
| `PRIMARY_COLOR` | hex | `#1f77b4` | Primary color for the UI |
| `BACKGROUND_COLOR` | hex | `#ffffff` | Background color |
| `TEXT_COLOR` | hex | `#000000` | Text color |

## Report Generation

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `GEMINI_API_KEY` | string | - | **Required** Google Gemini API key |
| `GEMINI_MODEL` | string | `gemini-2.0-flash-001` | Gemini model to use |
| `DEFAULT_TEMPLATE` | string | `default` | Default report template |
| `MAX_TOKENS` | int | `2048` | Maximum tokens for generated content |
| `TEMPERATURE` | float | `0.7` | Controls randomness (0.0 to 1.0) |
| `TOP_P` | float | `0.9` | Nucleus sampling parameter |
| `TOP_K` | int | `40` | Top-k sampling parameter |

## File Handling

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `MAX_FILE_SIZE` | int | `10485760` | Maximum file size in bytes (10MB) |
| `UPLOAD_FOLDER` | path | `./uploads` | Directory for uploaded files |
| `ALLOWED_EXTENSIONS` | string | `.txt,.md,.docx,.pdf` | Allowed file extensions |

## Logging

Logging is configured to output to both console and file. Log files are stored in the `logs` directory.

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `LOG_LEVEL` | string | `INFO` | Minimum log level |
| `LOG_FILE` | path | `./logs/app.log` | Log file path |
| `LOG_FORMAT` | string | `%(asctime)s - %(name)s - %(levelname)s - %(message)s` | Log message format |

## Advanced Configuration

### Custom Templates

1. Create a new Markdown file in the `templates` directory
2. Use placeholders for dynamic content (e.g., `{{content}}`, `{{date}}`)
3. Reference the template by its filename (without extension) in the `DEFAULT_TEMPLATE` variable

### Custom CSS

To customize the application's appearance, create a `static` directory and add a `custom.css` file with your styles.

### Database Configuration

By default, the application uses a JSON file for data storage. To use a different database:

1. Install the required database driver
2. Update the database configuration in `src/report_generator/config.py`

## Example Configuration

```env
# Application
LOG_LEVEL=DEBUG
DATA_DIR=./app_data
TEMPLATES_DIR=./custom_templates

# UI
DEFAULT_THEME=dark
PRIMARY_COLOR=#4a90e2
BACKGROUND_COLOR=#121212
TEXT_COLOR=#f5f5f5

# Gemini API
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-pro
MAX_TOKENS=4096
TEMPERATURE=0.7

# File Handling
MAX_UPLOAD_SIZE=20
ALLOWED_EXTENSIONS=.txt,.md,.docx,.pdf,.csv,.xlsx

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/app.log
```

## Configuration Precedence

1. Command-line arguments (highest priority)
2. Environment variables
3. `.env` file
4. Default values (lowest priority)

## Security Considerations

- Never commit your `.env` file to version control
- Keep your API keys secure
- Restrict file uploads to trusted sources
- Use HTTPS in production
