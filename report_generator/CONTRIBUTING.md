# Contributing to Daily Report Generator

Thank you for considering contributing to the Daily Report Generator! We welcome contributions from everyone, regardless of experience level.

## How to Contribute

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine
3. **Create a new branch** for your changes
4. **Make your changes** and commit them
5. **Push your changes** to your fork
6. **Open a pull request** to the main repository

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use [Black](https://github.com/psf/black) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Use [mypy](http://mypy-lang.org/) for static type checking
- Use [flake8](https://flake8.pycqa.org/) for code linting

## Testing

Run the test suite with:

```bash
pytest
```

## Documentation

Documentation is generated using [MkDocs](https://www.mkdocs.org/). To build the documentation locally:

```bash
mkdocs serve
```

Then open http://127.0.0.1:8000 in your browser.

## Reporting Issues

When reporting issues, please include:

- A clear description of the issue
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any error messages

## Feature Requests

We welcome feature requests! Please open an issue to discuss your idea before implementing it.

## Code of Conduct

This project adheres to the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you are expected to uphold this code.
