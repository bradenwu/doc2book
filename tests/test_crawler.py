"""Test crawler module with Crawl4AI."""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from doc2book.crawler.crawl4ai import crawl_docs, _extract_title


class TestCrawl4AI:
    """Test cases for Crawl4AI crawler."""
    
    @patch('doc2book.crawler.crawl4ai.AsyncWebCrawler')
    def test_crawl_single_page_success(self, mock_crawler_class):
        """Test successful single page crawl."""
        # Mock the crawler and result
        mock_crawler = AsyncMock()
        mock_crawler_class.return_value.__aenter__.return_value = mock_crawler
        
        mock_result = MagicMock()
        mock_result.success = True
        mock_result.url = "https://example.com/docs"
        mock_result.markdown.fit_markdown = "# Test Content\n\nThis is test."
        mock_result.markdown.raw_markdown = "# Test Content\n\nThis is test."
        mock_result.metadata = {"title": "Test Page"}
        mock_result.deep_crawl_result = None
        
        mock_crawler.arun = AsyncMock(return_value=mock_result)
        
        # Run the crawler
        pages = crawl_docs("https://example.com/docs", max_pages=1)
        
        # Assertions
        assert len(pages) == 1
        assert pages[0].url == "https://example.com/docs"
        assert pages[0].title == "Test Page"
        assert "Test Content" in pages[0].markdown
    
    @patch('doc2book.crawler.crawl4ai.AsyncWebCrawler')
    def test_crawl_deep_crawl(self, mock_crawler_class):
        """Test deep crawl with multiple pages."""
        mock_crawler = AsyncMock()
        mock_crawler_class.return_value.__aenter__.return_value = mock_crawler
        
        # Mock deep crawl results
        mock_results = []
        for i in range(3):
            result = MagicMock()
            result.success = True
            result.url = f"https://example.com/docs/page{i}"
            result.markdown.fit_markdown = f"# Page {i}"
            result.markdown.raw_markdown = f"# Page {i}"
            result.metadata = {"title": f"Page {i}"}
            mock_results.append(result)
        
        mock_main_result = MagicMock()
        mock_main_result.success = True
        mock_main_result.deep_crawl_result = mock_results
        
        mock_crawler.arun = AsyncMock(return_value=mock_main_result)
        
        # Run the crawler
        pages = crawl_docs("https://example.com/docs", max_pages=10)
        
        # Assertions
        assert len(pages) == 3
        assert pages[0].title == "Page 0"
        assert pages[2].url == "https://example.com/docs/page2"
    
    def test_extract_title_from_metadata(self):
        """Test title extraction from metadata."""
        result = MagicMock()
        result.metadata = {"title": "Custom Title"}
        
        title = _extract_title(result)
        assert title == "Custom Title"
    
    def test_extract_title_fallback(self):
        """Test title extraction fallback when no metadata."""
        result = MagicMock()
        result.metadata = None
        result.response_headers = {}
        
        title = _extract_title(result)
        assert title == "Untitled"
    
    @patch('doc2book.crawler.crawl4ai.AsyncWebCrawler')
    def test_crawl_uses_fit_markdown(self, mock_crawler_class):
        """Test that fit_markdown is preferred over raw_markdown."""
        mock_crawler = AsyncMock()
        mock_crawler_class.return_value.__aenter__.return_value = mock_crawler
        
        mock_result = MagicMock()
        mock_result.success = True
        mock_result.url = "https://example.com"
        mock_result.markdown.fit_markdown = "Clean content"
        mock_result.markdown.raw_markdown = "Raw content with noise"
        mock_result.metadata = {}
        mock_result.deep_crawl_result = None
        
        mock_crawler.arun = AsyncMock(return_value=mock_result)
        
        pages = crawl_docs("https://example.com")
        
        assert pages[0].markdown == "Clean content"
    
    @patch('doc2book.crawler.crawl4ai.AsyncWebCrawler')
    def test_crawl_fallback_to_raw_markdown(self, mock_crawler_class):
        """Test fallback to raw_markdown when fit_markdown is None."""
        mock_crawler = AsyncMock()
        mock_crawler_class.return_value.__aenter__.return_value = mock_crawler
        
        mock_result = MagicMock()
        mock_result.success = True
        mock_result.url = "https://example.com"
        mock_result.markdown.fit_markdown = None
        mock_result.markdown.raw_markdown = "Raw content"
        mock_result.metadata = {}
        mock_result.deep_crawl_result = None
        
        mock_crawler.arun = AsyncMock(return_value=mock_result)
        
        pages = crawl_docs("https://example.com")
        
        assert pages[0].markdown == "Raw content"
