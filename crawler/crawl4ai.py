"""Crawl4AI-based document crawler."""
import asyncio
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import WebScrapingStrategy
from ..models.page import Page


async def _crawl_docs_async(base_url: str, max_pages: int = 200) -> List[Page]:
    """
    Async implementation of crawl using Crawl4AI.
    
    Args:
        base_url: The base URL of the documentation site
        max_pages: Maximum number of pages to crawl
        
    Returns:
        List of Page objects containing crawled content
    """
    # Configure browser for headless operation
    browser_config = BrowserConfig(
        headless=True,
        verbose=False
    )
    
    # Configure crawler with deep crawl strategy
    # max_depth: how deep to follow links (3 is reasonable for docs)
    # score_threshold: filter out low-quality pages
    run_config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=3,
            max_pages=max_pages,
            include_external=False
        ),
        cache_mode=CacheMode.ENABLED,
        scraping_strategy=WebScrapingStrategy(),
        excluded_tags=['nav', 'footer', 'aside'],
    )
    
    pages = []
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=base_url,
            config=run_config
        )
        
        # Handle deep crawl results
        if hasattr(result, 'deep_crawl_result') and result.deep_crawl_result:
            # Deep crawl returns multiple results
            for crawl_result in result.deep_crawl_result:
                if crawl_result.success and crawl_result.markdown:
                    page = Page(
                        url=crawl_result.url,
                        title=_extract_title(crawl_result),
                        markdown=crawl_result.markdown.fit_markdown or crawl_result.markdown.raw_markdown
                    )
                    pages.append(page)
        elif result.success and result.markdown:
            # Single page result
            page = Page(
                url=result.url,
                title=_extract_title(result),
                markdown=result.markdown.fit_markdown or result.markdown.raw_markdown
            )
            pages.append(page)
    
    return pages


def _extract_title(result) -> str:
    """Extract title from crawl result."""
    # Try metadata first
    if hasattr(result, 'metadata') and result.metadata:
        if result.metadata.get('title'):
            return result.metadata['title']
    # Try response_headers
    if hasattr(result, 'response_headers') and result.response_headers:
        if result.response_headers.get('title'):
            return result.response_headers['title']
    # Fallback to URL
    return "Untitled"


def crawl_docs(base_url: str, max_pages: int = 200) -> List[Page]:
    """
    Crawl a documentation site using Crawl4AI.
    
    Args:
        base_url: The base URL of the documentation site
        max_pages: Maximum number of pages to crawl
        
    Returns:
        List of Page objects containing crawled content
    """
    return asyncio.run(_crawl_docs_async(base_url, max_pages))
