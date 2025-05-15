# Daily Report Generator

![Daily Report Generator](img/logo.png)

A powerful Streamlit application that helps you generate structured daily reports from various inputs using Google's Gemini API.

## Features

- 📝 Generate reports from text input or file uploads
- 🎨 Multiple report templates (Operations, Development, Meetings, Custom)
- 📂 Support for various file formats (TXT, MD, DOCX, CSV, XLSX, PDF)
- 🌓 Dark/Light mode toggle
- 📊 Report history and archiving
- 📤 Export functionality (Markdown, HTML, PDF)
- 🔒 Secure API key management

## Quick Start

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

3. Run the application:
   ```bash
   streamlit run src/report_generator/app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`

## Documentation

- [Installation](installation.md)
- [Usage](usage.md)
- [Configuration](configuration.md)
- [API Reference](api.md)
- [Development Guide](development.md)

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
