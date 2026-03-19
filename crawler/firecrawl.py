"""Firecrawl-based document crawler."""
from typing import List
from firecrawl import FirecrawlApp
from ..models.page import Page
from ..config.settings import FIRECRAWL_API_KEY


def crawl_docs(base_url: str, max_pages: int = 200) -> List[Page]:
    """
    Crawl a documentation site using Firecrawl.
    
    Args:
        base_url: The base URL of the documentation site
        max_pages: Maximum number of pages to crawl
        
    Returns:
        List of Page objects containing crawled content
    """
    if not FIRECRAWL_API_KEY:
        raise ValueError("FIRECRAWL_API_KEY environment variable not set")
    
    app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
    
    # Crawl the documentation site
    result = app.crawl_url(
        base_url,
        params={
            "limit": max_pages,
            "scrapeOptions": {
                "formats": ["markdown"],
            }
        },
        poll_interval=30
    )
    
    # Convert to Page objects
    pages = []
    for item in result.get("data", []):
        page = Page(
            url=item.get("metadata", {}).get("sourceURL", item.get("url", "")),
            title=item.get("metadata", {}).get("title", "Untitled"),
            markdown=item.get("markdown", "")
        )
        pages.append(page)
    
    return pages
