#!/usr/bin/env python3
"""Export all 48 client commission HTML ads to PDF using Chrome headless."""
import subprocess
import json
from pathlib import Path

OUTPUT_DIR = Path("/home/nemesis/targeted-design-site/ads/client-commission")
PDF_DIR = OUTPUT_DIR / "pdfs"
PDF_DIR.mkdir(parents=True, exist_ok=True)
MANIFEST_PATH = OUTPUT_DIR / "manifest.json"
manifest = json.loads(MANIFEST_PATH.read_text())
CHROME = "/usr/bin/google-chrome-stable"
HTML_DIR = OUTPUT_DIR

success = 0
fail = 0
total = len(manifest) * 2

print(f"Exporting {total} PDFs...")
for entry in manifest:
    for lang in ['en', 'es']:
        html_rel = entry[lang]
        html_path = HTML_DIR / html_rel
        slug = entry['slug']
        tier = entry['tier']
        pdf_name = f"{slug}-{tier}-{lang}.pdf"
        pdf_path = PDF_DIR / pdf_name

        cmd = [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={pdf_path}",
            "--window-size=1200,900",
            str(html_path)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if result.returncode == 0 and pdf_path.exists():
            size = pdf_path.stat().st_size
            print(f"  ✅ {pdf_name} ({size:,} bytes)")
            success += 1
        else:
            print(f"  ❌ {pdf_name}: {result.stderr[:100]}")
            fail += 1

print(f"\n✅ {success}/{total} PDFs exported → {PDF_DIR}")
if fail:
    print(f"❌ {fail} failures")
