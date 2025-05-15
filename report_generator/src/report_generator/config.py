import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / 'data'
LOG_DIR = BASE_DIR / 'logs'
TEMPLATES_DIR = BASE_DIR / 'templates'

# Create directories if they don't exist
for directory in [DATA_DIR, LOG_DIR, TEMPLATES_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Gemini API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_MODEL = 'gemini-pro'  # or 'gemini-ultra' when available
GEMINI_TEMPERATURE = 0.7
GEMINI_MAX_TOKENS = 2048

# Report settings
DEFAULT_REPORT_TEMPLATE = 'default.md'
REPORT_HISTORY_FILE = DATA_DIR / 'report_history.json'

# UI Settings
DEFAULT_THEME = 'light'
THEMES = {
    'light': {
        'primary': '#1f77b4',
        'background': '#ffffff',
        'text': '#000000',
    },
    'dark': {
        'primary': '#90caf9',
        'background': '#121212',
        'text': '#e0e0e0',
    }
}

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'app.log',
            'formatter': 'standard',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True
        },
    },
}
