#!/usr/bin/env python3
"""Export PDFs from HTML files using Chrome headless for Batch 3"""

import os
import subprocess

CLIENTS = [
    "035-Biltmore-Insurance-Group",
    "036-Tezel-Veterinary-Hospital",
    "037-Medina-Lake-Veterinary-Hospital",
    "038-Spay-Neuter-San-Antonio-SN_SA",
    "039-Bandera-Road-Pet-Hospital",
    "040-K9-Kitchen-Pet-Boarding-Resort",
    "041-Studio-450-Hair-Salon",
    "042-Salon-Rosewood",
    "043-Fresh-Fades-Barbershop",
    "044-Nails-by-Nelly",
    "045-The-Grooming-Den",
    "046-CrossFit-Agua-Dulce",
    "047-Orangetheory-Fitness-Stone-Oak",
    "048-Hot-Yoga-San-Antonio",
    "049-Titan-Fitness",
    "050-Pilates-on-the-Park",
    "051-Stone-Oak-Chiropractic-Wellness",
]

def export_pdf(html_path, output_dir):
    """Export HTML to PDF using Chrome headless"""
    slug = os.path.basename(os.path.dirname(html_path))
    filename = os.path.basename(html_path).replace('.html', '.pdf')
    pdf_path = os.path.join(output_dir, filename)
    
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf=" + pdf_path,
        "--print-to-pdf-no-header",
        "--print-to-pdf-no-footer",
        f"file://{html_path}"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Created: {pdf_path}")
        return True
    else:
        print(f"ERROR: {result.stderr}")
        return False

def main():
    output_base = "/home/nemesis/.openclaw/workspace/design/cards"
    
    for slug in CLIENTS:
        output_dir = os.path.join(output_base, slug)
        
        # Export front-EN
        front_html = os.path.join(output_dir, f"{slug}-front-en.html")
        if os.path.exists(front_html):
            export_pdf(front_html, output_dir)
        
        # Export back-ES
        back_html = os.path.join(output_dir, f"{slug}-back-es.html")
        if os.path.exists(back_html):
            export_pdf(back_html, output_dir)
    
    print("\n✓ All PDFs exported for Batch 3 (Clients 035-051)")

if __name__ == "__main__":
    main()
