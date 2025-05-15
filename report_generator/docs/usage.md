# Usage Guide

This guide explains how to use the Daily Report Generator application to create, manage, and export reports.

## Table of Contents

- [Creating a New Report](#creating-a-new-report)
- [Using Templates](#using-templates)
- [Importing Content](#importing-content)
- [Generating Reports](#generating-reports)
- [Viewing Report History](#viewing-report-history)
- [Exporting Reports](#exporting-reports)
- [Keyboard Shortcuts](#keyboard-shortcuts)

## Creating a New Report

1. Launch the application by running:
   ```bash
   streamlit run src/report_generator/app.py
   ```

2. The application will open in your default web browser at `http://localhost:8501`

3. In the main text area, enter your notes, meeting minutes, or any content you want to include in the report.

## Using Templates

The application includes several report templates to help you get started:

- **Default**: A general-purpose report template
- **Operations**: For operational reports with metrics and KPIs
- **Development**: For software development progress reports
- **Meetings**: For meeting minutes and action items

To use a template:

1. In the sidebar, under "Report Templates", select your preferred template
2. The AI will format your content according to the selected template

## Importing Content

You can import content from various file formats:

1. Click on the "Upload a file" button in the sidebar
2. Select a file from your computer (supported formats: TXT, MD, DOCX, PDF, CSV, XLSX)
3. The content will be automatically extracted and loaded into the editor

## Generating Reports

1. After entering or importing your content, click the "Generate Report" button
2. The application will process your content using the Gemini API
3. The generated report will appear below the input area

## Viewing Report History

1. The sidebar displays your 5 most recent reports
2. Click on any report to view it
3. To view older reports, check the `data/report_history.json` file

## Exporting Reports

You can export your reports in multiple formats:

1. Click on one of the export buttons below the generated report:
   - **Markdown (.md)**: For use in Markdown-compatible applications
   - **HTML (.html)**: For viewing in web browsers or embedding in websites
   - **PDF (.pdf)**: For printing or sharing (coming soon)

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Generate report |
| `Ctrl+S` | Save current report |
| `Ctrl+O` | Open file |
| `Ctrl+D` | Toggle dark mode |
| `Ctrl+H` | View history |

## Advanced Usage

### Custom Templates

You can create custom templates by adding new template files to the `templates` directory. Each template should be a Markdown file with placeholders for dynamic content.

### API Integration

The application can be integrated with other tools via its API (documentation coming soon).

### Batch Processing

For processing multiple files at once, you can use the command-line interface:

```bash
python -m src.report_generator.cli --input-dir ./input --output-dir ./output --template default
```

## Troubleshooting

### Report Generation Fails

- Check your internet connection
- Verify your Gemini API key is valid
- Ensure your input content is not empty
- Check the application logs for error messages

### File Import Issues

- Make sure the file format is supported
- Check file permissions
- For large files, try breaking them into smaller chunks

### Performance Issues

- For large documents, processing may take some time
- Close other applications to free up system resources
- Consider upgrading your Gemini API plan for faster response times
