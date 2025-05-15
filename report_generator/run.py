#!/usr/bin/env python3
"""
Main entry point for the Daily Report Generator application.
"""
import sys
import os
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent))

def main():
    """Run the Streamlit application."""
    try:
        # Import streamlit here to catch any import errors early
        import streamlit as st
        from src.report_generator.app import main as app_main
        
        # Run the main application
        app_main()
        
    except ImportError as e:
        print(f"Error: {e}")
        print("Please install the required dependencies using:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
