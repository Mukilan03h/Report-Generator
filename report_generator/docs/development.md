# Development Guide

This guide provides information for developers who want to contribute to the Daily Report Generator project.

## Table of Contents

- [Project Structure](#project-structure)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Version Control](#version-control)
- [Release Process](#release-process)

## Project Structure

```
daily-report-generator/
├── .github/                  # GitHub workflows and issue templates
├── data/                     # Application data (not versioned)
├── docs/                     # Documentation files
│   ├── css/                  # Custom CSS for documentation
│   ├── img/                  # Documentation images
│   ├── js/                   # Custom JavaScript for documentation
│   └── *.md                  # Documentation pages
├── logs/                     # Application logs (not versioned)
├── src/                      # Source code
│   └── report_generator/     # Main package
│       ├── __init__.py       # Package initialization
│       ├── app.py            # Main Streamlit application
│       ├── cli.py            # Command-line interface
│       ├── config.py         # Configuration management
│       ├── file_utils.py     # File handling utilities
│       ├── gemini_utils.py   # Gemini API integration
│       └── report_utils.py   # Report generation utilities
├── static/                   # Static files (CSS, JS, images)
├── templates/                # Report templates
├── tests/                    # Test files
│   ├── __init__.py
│   ├── conftest.py
│   └── test_*.py
├── .env.example              # Example environment variables
├── .gitignore
├── .pre-commit-config.yaml   # Pre-commit hooks
├── CONTRIBUTING.md
├── LICENSE
├── mkdocs.yml               # MkDocs configuration
├── pyproject.toml           # Build system configuration
├── README.md
└── requirements.txt         # Production dependencies
```

## Setting Up the Development Environment

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/daily-report-generator.git
   cd daily-report-generator
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Code Style

We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide with the following tools:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for static type checking

Run the following commands before committing:

```bash
black src tests
iSort src tests
flake8 src tests
mypy src tests
```

## Testing

We use **pytest** for testing. To run the test suite:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

## Documentation

Documentation is built using **MkDocs** with the **Material** theme. To build and serve the documentation locally:

```bash
mkdocs serve
```

Then open `http://127.0.0.1:8000` in your browser.

## Version Control

### Branching Strategy

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `hotfix/*`: Critical production fixes

### Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code changes that neither fixes a bug nor adds a feature
- `perf`: Performance improvements
- `test`: Adding or modifying tests
- `chore`: Changes to the build process or auxiliary tools

## Release Process

1. Update the version number in `setup.py` and `src/report_generator/__init__.py`
2. Update `CHANGELOG.md`
3. Create a release tag:
   ```bash
   git tag -a v1.0.0 -m "Initial release"
   git push origin v1.0.0
   ```
4. Create a GitHub release with release notes

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.
