#!/usr/bin/env python3
"""Export PDFs for Batch 5 HTML files (Clients 069-085)"""
import os
import subprocess

CLIENTS = [
    "069-Childcare-Network-NE-Side",
    "070-Little-Sprouts-Learning-Center",
    "071-Zero-Heating-AC-and-Refrigeration",
    "072-Gabes-Priority-AC-Service",
    "073-Beluga-Air",
    "074-Blastin-Air-Conditioning-and-Heating",
    "075-Air-Tex-Air-Conditioning-and-Heating-LLC",
    "076-Stay-Cool-Air-Conditioning-and-Heating",
    "077-Ocean-Breeze-Cooling-and-Refrigeration",
    "078-Sosa-The-Plumber",
    "079-Baileys-Plumbing-Services",
    "080-Richards-Plumbing-Repair-Shop",
    "081-Sams-Auto-Repair",
    "082-Baumann-Auto-Repair",
    "083-Guillermos-Auto-Repair",
    "084-Gonzalez-Auto-Repair",
    "085-DD-Auto-San-Antonio",
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
