"""Markdown builder for merging pages."""
from typing import List
from ..models.page import Page


def sort_pages(pages: List[Page]) -> List[Page]:
    """
    Sort pages by URL for consistent ordering.
    
    Args:
        pages: List of Page objects
        
    Returns:
        Sorted list of Page objects
    """
    return sorted(pages, key=lambda p: p.url)


def merge_markdown(pages: List[Page], title: str = "Documentation") -> str:
    """
    Merge multiple pages into a single Markdown document.
    
    Args:
        pages: List of Page objects to merge
        title: Title for the combined document
        
    Returns:
        Combined Markdown string
    """
    sections = [f"# {title}\n\n"]
    
    for page in pages:
        # Add page title as section header
        sections.append(f"## {page.title}\n\n")
        sections.append(f"<!-- Source: {page.url} -->\n\n")
        sections.append(page.markdown)
        sections.append("\n\n---\n\n")
    
    return "".join(sections)
