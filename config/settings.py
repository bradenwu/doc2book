"""Configuration for Doc2Book."""
import os

# Firecrawl API key (set via environment variable)
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY", "")

# Default output settings
DEFAULT_OUTPUT_DIR = "./output"
DEFAULT_MAX_PAGES = 200
