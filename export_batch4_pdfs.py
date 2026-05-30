#!/usr/bin/env python3
"""Export PDFs for Batch 4 HTML files"""
import os
import subprocess

CLIENTS = [
    "052-Active-Life-Physical-Therapy",
    "053-Corrective-Chiropractic-Rehab",
    "054-Peak-Performance-Sports-Rehab",
    "055-Wellness-One-Chiropractic",
    "056-Guardian-Roofing-Construction",
    "057-Legacy-Home-Builders-LLC",
    "058-All-American-Roofing-Siding",
    "059-Hill-Country-Stoneworks",
    "060-Southtown-Construction-Remodeling",
    "061-HR-Block-Stone-Oak-District-Office",
    "062-Liberty-Tax-Service-South-Side",
    "063-Padron-CPA-Group-PLLC",
    "064-Tax-Accounting-Solutions-SA",
    "065-QuickBooks-ProAdvisor-SA-Sole-Proprietor",
    "066-Bright-Horizons-at-Stone-Oak",
    "067-La-Petite-Academy-Medical-Center",
    "068-Kiddie-Academy-of-Culebra",
]

def export_pdf(html_path, pdf_path):
    """Export HTML to PDF using Chrome headless"""
    cmd = [
        'google-chrome',
        '--headless',
        '--disable-gpu',
        '--print-to-pdf=' + pdf_path,
        '--print-to-pdf-no-header',
        '--print-to-pdf-no-footer',
        '--window-size=1238,919',
        html_path
    ]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=30)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Chrome error for {pdf_path}: {e}")
        return False
    except subprocess.TimeoutExpired:
        print(f"Timeout for {pdf_path}")
        return False
    except FileNotFoundError:
        print("Chrome not found")
        return False

def main():
    output_base = "/home/nemesis/.openclaw/workspace/design/cards"
    completed = []
    failed = []
    
    for slug in CLIENTS:
        output_dir = os.path.join(output_base, slug)
        
        front_html = os.path.join(output_dir, f"{slug}-front-en.html")
        back_html = os.path.join(output_dir, f"{slug}-back-es.html")
        front_pdf = os.path.join(output_dir, f"{slug}-front-en.pdf")
        back_pdf = os.path.join(output_dir, f"{slug}-back-es.pdf")
        
        front_ok = export_pdf(front_html, front_pdf)
        back_ok = export_pdf(back_html, back_pdf)
        
        if front_ok:
            print(f"✓ PDF: {front_pdf}")
        else:
            print(f"✗ PDF: {front_pdf}")
            failed.append(front_pdf)
        
        if back_ok:
            print(f"✓ PDF: {back_pdf}")
        else:
            print(f"✗ PDF: {back_pdf}")
            failed.append(back_pdf)
        
        if front_ok and back_ok:
            completed.append(slug)
    
    print(f"\n=== SUMMARY ===")
    print(f"Completed: {len(completed)}/{len(CLIENTS)} clients")
    if failed:
        print(f"Failed PDFs: {len(failed)}")
        for f in failed:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
