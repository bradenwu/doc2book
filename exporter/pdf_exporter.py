"""PDF exporter using Pandoc."""
import subprocess
import os


def export_pdf(markdown_path: str, output_path: str) -> str:
    """
    Export Markdown to PDF using Pandoc with xelatex.
    
    Args:
        markdown_path: Path to the input Markdown file
        output_path: Path for the output PDF file
        
    Returns:
        Path to the generated PDF file
    """
    cmd = [
        "pandoc",
        markdown_path,
        "-o", output_path,
        "--pdf-engine=xelatex",
        "-V", "mainfont=DejaVu Sans",
        "-V", "geometry:margin=1in"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc failed: {result.stderr}")
    
    return output_path
