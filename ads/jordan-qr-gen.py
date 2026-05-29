#!/usr/bin/env python3
"""
jordan-qr-gen.py — Batch QR code generator for TDA client commission mini-ads.
Generates one QR code per business+tier combo with UTM tracking URLs.

Usage:
    python3 jordan-qr-gen.py [--output-dir PATH] [--base-url URL]

Output:
    PNG QR codes in output_dir/
    manifest.json with all QR metadata
"""

import os
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
except ImportError:
    print("ERROR: qrcode library not installed. Run: pip install qrcode[pil]")
    sys.exit(1)

# ── Configuration ──────────────────────────────────────

OUTPUT_DIR = Path("/home/nemesis/targeted-design-site/ads/client-commission/qr-codes")
BASE_URL = "https://targeted-design.com/r"
QR_SIZE = 600       # pixels (2" @ 300dpi)
QR_BOX_SIZE = 10    #模块像素
QR_BORDER = 4        # quiet zone modules

BUSINESSES = [
    {
        "slug": "dutson-pest",
        "name": "Dutson Pest Control",
        "service": "Pest Control",
        "zip": "78228",
    },
    {
        "slug": "carousel-childcare",
        "name": "Carousel Childcare Center",
        "service": "Childcare",
        "zip": "78228",
    },
    {
        "slug": "gabes-ac",
        "name": "Gabe's Priority AC",
        "service": "AC Repair",
        "zip": "78237",
    },
    {
        "slug": "grass-company",
        "name": "The Grass Company",
        "service": "Landscaping",
        "zip": "78237",
    },
    {
        "slug": "buffalo-plumbing",
        "name": "Buffalo Plumbing Co.",
        "service": "Plumbing",
        "zip": "78207",
    },
    {
        "slug": "sams-auto",
        "name": "Sam's Auto Repair",
        "service": "Auto Repair",
        "zip": "78211",
    },
    {
        "slug": "veterans-barber",
        "name": "Veteran's Barber Shop",
        "service": "Barbershop",
        "zip": "78228",
    },
    {
        "slug": "henrys-tacos",
        "name": "Henry's Puffy Tacos",
        "service": "Restaurant",
        "zip": "78228",
    },
]

TIERS = [
    {"slug": "economy", "label": "Economy"},
    {"slug": "fullsize", "label": "Full-Size"},
    {"slug": "premium", "label": "Premium"},
]

CAMPAIGN_ID = "client-commission-2026"


# ── Functions ──────────────────────────────────────────

def slugify(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s)
    return s[:60]


def build_tracking_url(business_slug: str, tier_slug: str) -> str:
    """Build UTM-tagged tracking URL for a business+tier combo."""
    base = f"{BASE_URL}/{business_slug}"
    params = (
        f"?utm_source=eddm"
        f"&utm_medium=direct_mail"
        f"&utm_campaign={CAMPAIGN_ID}"
        f"&utm_content={business_slug}"
        f"&utm_term={tier_slug}"
    )
    return base + params


def generate_qr_image(url: str, output_path: Path) -> dict:
    """Generate a single QR code PNG."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=QR_BOX_SIZE,
        border=QR_BORDER,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Ensure exact 600x600
    if img.size != (QR_SIZE, QR_SIZE):
        from PIL import Image
        img = img.resize((QR_SIZE, QR_SIZE), Image.LANCZOS)

    img.save(str(output_path), "PNG")

    return {
        "file": str(output_path),
        "size_px": [QR_SIZE, QR_SIZE],
        "url": url,
    }


def batch_generate(output_dir: Path, base_url: str = BASE_URL) -> dict:
    """Generate all QR codes for all businesses and tiers."""
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "campaign": CAMPAIGN_ID,
        "base_url": base_url,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_qr_codes": 0,
        "qr_codes": [],
    }

    for biz in BUSINESSES:
        for tier in TIERS:
            tracking_url = build_tracking_url(biz["slug"], tier["slug"])
            filename = f"{biz['slug']}-{tier['slug']}.png"
            output_path = output_dir / filename

            result = generate_qr_image(tracking_url, output_path)

            entry = {
                "business_name": biz["name"],
                "business_slug": biz["slug"],
                "service": biz["service"],
                "zip": biz["zip"],
                "tier": tier["slug"],
                "tier_label": tier["label"],
                "tracking_url": tracking_url,
                "qr_file": str(output_path),
                "qr_filename": filename,
            }
            manifest["qr_codes"].append(entry)
            manifest["total_qr_codes"] += 1

            print(f"  ✅ {biz['name']} [{tier['slug']}] → {filename}")

    # Save manifest
    manifest_path = output_dir / "qr-manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\n📋 Generated {manifest['total_qr_codes']} QR codes")
    print(f"📋 Manifest: {manifest_path}")
    return manifest


# ── CLI ────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate QR codes for TDA client mini-ads")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR), help="Output directory")
    parser.add_argument("--base-url", default=BASE_URL, help="Base tracking URL")
    args = parser.parse_args()

    print(f"🔍 Generating QR codes → {args.output_dir}")
    manifest = batch_generate(Path(args.output_dir), args.base_url)
    print(f"✅ Done. {manifest['total_qr_codes']} QR codes ready.")
