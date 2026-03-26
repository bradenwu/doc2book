"""Main pipeline for Doc2Book."""
import os
from typing import Optional
from ..crawler.crawl4ai import crawl_docs
from ..builder.markdown_builder import sort_pages, merge_markdown
from ..exporter.pdf_exporter import export_pdf


def run_pipeline(
    url: str,
    output_dir: str = "./output",
    output_name: str = "output",
    max_pages: int = 200,
    format: str = "pdf"
) -> dict:
    """
    Run the complete Doc2Book pipeline.
    
    Args:
        url: Documentation site URL
        output_dir: Directory for output files
        output_name: Base name for output files
        max_pages: Maximum pages to crawl
        format: Output format (pdf, markdown, or both)
        
    Returns:
        Dict with paths to generated files
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Step 1: Crawl
    print(f"🕷️  Crawling: {url}")
    pages = crawl_docs(url, max_pages=max_pages)
    print(f"   Found {len(pages)} pages")
    
    # Step 2: Sort
    print("📚 Sorting pages...")
    pages = sort_pages(pages)
    
    # Step 3: Merge
    print("📝 Merging content...")
    markdown = merge_markdown(pages)
    
    # Step 4: Write Markdown
    md_path = os.path.join(output_dir, f"{output_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"   Saved: {md_path}")
    
    result = {"markdown": md_path}
    
    # Step 5: Export PDF (if requested)
    if format in ("pdf", "both"):
        print("📄 Generating PDF...")
        pdf_path = os.path.join(output_dir, f"{output_name}.pdf")
        export_pdf(md_path, pdf_path)
        print(f"   Saved: {pdf_path}")
        result["pdf"] = pdf_path
    
    print("✅ Done!")
    return result
