#!/usr/bin/env python3
"""
TDA Client Commission Mini-Ad Pipeline v3
Master script: generates QR codes → embeds in ads → outputs print-ready HTML

Usage:
    python3 run_pipeline.py [--output-dir PATH]

Steps:
    1. Generate QR codes (jordan-qr-gen.py)
    2. Build HTML ads with embedded QR images (build_client_ads.py)
    3. Verify output
"""

import subprocess
import sys
from pathlib import Path

ADS_DIR = Path("/home/nemesis/targeted-design-site/ads")
OUTPUT_DIR = Path("/home/nemesis/targeted-design-site/ads/client-commission")


def step(name, cmd, cwd=None):
    print(f"\n{'='*60}")
    print(f"▶ {name}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, cwd=str(cwd or ADS_DIR), capture_output=False)
    if result.returncode != 0:
        print(f"❌ FAILED: {name}")
        sys.exit(1)
    print(f"✅ {name} — complete")


def verify():
    print(f"\n{'='*60}")
    print("▶ Verification")
    print(f"{'='*60}")

    qr_dir = OUTPUT_DIR / "qr-codes"
    qr_files = list(qr_dir.glob("*.png")) if qr_dir.exists() else []
    print(f"  QR codes: {len(qr_files)} PNG files")

    html_files = list(OUTPUT_DIR.rglob("*.html"))
    # Exclude gallery.html from count
    ad_htmls = [f for f in html_files if f.name != "gallery.html"]
    print(f"  HTML ad units: {len(ad_htmls)} files")

    # Check QR embedding
    qr_embedded = 0
    placeholder_count = 0
    for f in ad_htmls:
        content = f.read_text()
        if 'class="qr-img"' in content:
            qr_embedded += 1
        if "QR CODE" in content and "Loading" in content:
            placeholder_count += 1

    print(f"  Ads with QR <img> tag: {qr_embedded}/{len(ad_htmls)}")
    print(f"  Ads with placeholder: {placeholder_count}")

    manifest_path = OUTPUT_DIR / "manifest.json"
    if manifest_path.exists():
        import json
        manifest = json.loads(manifest_path.read_text())
        print(f"  Manifest entries: {len(manifest)}")

    gallery_path = OUTPUT_DIR / "gallery.html"
    print(f"  Gallery: {'✅' if gallery_path.exists() else '❌'}")

    if qr_embedded == len(ad_htmls) and len(ad_htmls) == 48:
        print(f"\n✅ ALL 48 ADS VERIFIED — pipeline complete")
        return True
    else:
        print(f"\n⚠️  Expected 48 ads with QR images, got {qr_embedded}")
        return False


if __name__ == "__main__":
    print("🚀 TDA Client Commission Mini-Ad Pipeline v3")
    print(f"   Output: {OUTPUT_DIR}")

    # Step 1: Generate QR codes
    step("Generate QR codes", [sys.executable, "jordan-qr-gen.py"])

    # Step 2: Build HTML ads
    step("Build HTML ads", [sys.executable, "build_client_ads.py"])

    # Step 3: Verify
    success = verify()

    if success:
        print(f"\n📂 Open gallery: {OUTPUT_DIR / 'gallery.html'}")
        sys.exit(0)
    else:
        sys.exit(1)
