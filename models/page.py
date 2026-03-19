"""Core data model for Doc2Book."""
from dataclasses import dataclass


@dataclass
class Page:
    """Represents a crawled documentation page."""
    url: str
    title: str
    markdown: str
