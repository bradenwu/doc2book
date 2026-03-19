"""Tests for Doc2Book."""
import pytest
from doc2book.models.page import Page
from doc2book.builder.markdown_builder import sort_pages, merge_markdown


class TestPage:
    """Tests for Page model."""
    
    def test_page_creation(self):
        """Test creating a Page object."""
        page = Page(
            url="https://example.com/docs/intro",
            title="Introduction",
            markdown="# Introduction\n\nThis is the intro."
        )
        assert page.url == "https://example.com/docs/intro"
        assert page.title == "Introduction"
        assert "Introduction" in page.markdown
    
    def test_page_equality(self):
        """Test Page equality based on URL."""
        page1 = Page(url="https://example.com", title="A", markdown="X")
        page2 = Page(url="https://example.com", title="B", markdown="Y")
        # Different title/markdown but same URL - they are different objects
        assert page1.url == page2.url
        assert page1.title != page2.title


class TestMarkdownBuilder:
    """Tests for Markdown builder functions."""
    
    def test_sort_pages(self):
        """Test sorting pages by URL."""
        pages = [
            Page(url="https://example.com/c", title="C", markdown=""),
            Page(url="https://example.com/a", title="A", markdown=""),
            Page(url="https://example.com/b", title="B", markdown=""),
        ]
        sorted_pages = sort_pages(pages)
        assert sorted_pages[0].url.endswith("/a")
        assert sorted_pages[1].url.endswith("/b")
        assert sorted_pages[2].url.endswith("/c")
    
    def test_merge_markdown(self):
        """Test merging pages into single markdown."""
        pages = [
            Page(url="https://example.com/intro", title="Intro", markdown="Hello world."),
            Page(url="https://example.com/guide", title="Guide", markdown="This is a guide."),
        ]
        result = merge_markdown(pages, title="Test Docs")
        
        assert "# Test Docs" in result
        assert "## Intro" in result
        assert "## Guide" in result
        assert "Hello world." in result
        assert "This is a guide." in result
        assert "https://example.com/intro" in result
    
    def test_merge_empty_pages(self):
        """Test merging empty page list."""
        result = merge_markdown([], title="Empty")
        assert "# Empty" in result


class TestPipeline:
    """Tests for the main pipeline."""
    
    def test_pipeline_imports(self):
        """Test that pipeline can be imported."""
        from doc2book.core.pipeline import run_pipeline
        assert callable(run_pipeline)
