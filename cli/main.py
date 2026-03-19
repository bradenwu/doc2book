"""Doc2Book CLI - Convert documentation sites to PDF/EPUB."""
import typer
from typing import Optional
from ..core.pipeline import run_pipeline

app = typer.Typer(
    name="doc2book",
    help="Convert documentation websites to PDF/EPUB books"
)


@app.command()
def convert(
    url: str = typer.Argument(..., help="Documentation site URL"),
    output: str = typer.Option("output.pdf", "--output", "-o", help="Output file path"),
    format: str = typer.Option("pdf", "--format", "-f", help="Output format: pdf, markdown, both"),
    max_pages: int = typer.Option(200, "--max-pages", "-m", help="Maximum pages to crawl"),
):
    """
    Convert a documentation site to PDF/Markdown.
    
    Example:
        doc2book https://docs.example.com
        doc2book https://docs.example.com -o mybook.pdf
    """
    # Extract output name and directory
    output_name = output.rsplit(".", 1)[0] if "." in output else output
    output_dir = "./output"
    
    run_pipeline(
        url=url,
        output_dir=output_dir,
        output_name=output_name,
        max_pages=max_pages,
        format=format
    )


@app.command()
def version():
    """Show version information."""
    typer.echo("Doc2Book v0.1.0 (MVP)")


if __name__ == "__main__":
    app()
