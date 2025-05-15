from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="daily-report-generator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Streamlit application for generating daily reports using Google's Gemini API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/daily-report-generator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "streamlit>=1.32.0",
        "google-generativeai>=0.3.2",
        "python-dotenv>=1.0.1",
        "python-dateutil>=2.9.0",
        "PyYAML>=6.0.1",
        "pandas>=2.2.1",
        "markdown>=3.5.2",
        "python-docx>=1.1.0",
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "report-generator=report_generator.app:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
    ],
)
