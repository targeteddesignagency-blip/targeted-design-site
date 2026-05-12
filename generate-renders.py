#!/usr/bin/env python3
"""Generate 8 industry lifestyle renders via Pollinations.ai."""

import base64
import hashlib
import os
import sys
import time
import urllib.parse
import urllib.request

API_KEY = os.environ.get("POLLINATIONS_API_KEY", "sk_POGi1YNOTiqK4Q2UqS0GLV8BzmZ05xzr")
BASE_URL = "https://image.pollinations.ai/prompt/"
MODEL = "flux"
OUTPUT_DIR = "/home/nemesis/targeted-design-site/samples/renders"

os.makedirs(OUTPUT_DIR, exist_ok=True)

industries = [
    {
        "slug": "restaurant",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "with a taco restaurant theme, lying at a slight 30-degree angle on a dark "
            "granite kitchen countertop. The card has bold black background with bright "
            "red #FE1616 accent stripe at top, minimalist layout. Only text visible on card: "
            "\"(210) 903-5551\" in white Montserrat font and \"Targeted.Design\" as small "
            "logo. Paper texture visible, soft natural window lighting from the left, "
            "subtle drop shadow. Professional studio product shot. Dark moody aesthetic."
        ),
    },
    {
        "slug": "auto-repair",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "for an auto repair shop, propped at a slight angle on a dark metallic "
            "workbench. Wrench icon motif. The card has bold black background with bright "
            "red #FE1616 accent stripe. Only text visible: \"(210) 903-5551\" in white "
            "and \"Targeted.Design\" small logo. Paper texture visible, workshop lighting, "
            "subtle shadow. Professional product shot."
        ),
    },
    {
        "slug": "hvac",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "for HVAC services, angled on a doorstep. Snowflake icon motif. Bold black "
            "background with bright red #FE1616 accent stripe. Only text visible: "
            "\"(210) 903-5551\" in white and \"Targeted.Design\" small logo. Paper texture, "
            "natural outdoor light, warm porch tones. Professional product shot."
        ),
    },
    {
        "slug": "plumbing",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "for a plumbing company, lying on a dark tile floor next to a kitchen sink "
            "pipe. Pipe wrench icon motif. Bold black background with bright red #FE1616 "
            "accent stripe. Only text visible: \"(210) 903-5551\" in white and "
            "\"Targeted.Design\" small logo. Paper texture, under-cabinet warm lighting. "
            "Professional product shot."
        ),
    },
    {
        "slug": "hair-barber",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "for a hair salon and barbershop, lying on a dark marble salon counter next to "
            "scissors. Barber pole icon motif. Bold black background with bright red "
            "#FE1616 accent stripe. Only text visible: \"(210) 903-5551\" in white and "
            "\"Targeted.Design\" small logo. Paper texture, warm salon lighting. "
            "Professional product shot."
        ),
    },
    {
        "slug": "childcare",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "for a childcare and learning center, lying on a dark wooden kitchen counter "
            "where a parent sorts mail. Childrens blocks icon motif. Bold black background "
            "with bright red #FE1616 accent stripe. Only text visible: "
            "\"(210) 903-5551\" in white and \"Targeted.Design\" small logo. Paper texture, "
            "warm afternoon kitchen light. Professional product shot."
        ),
    },
    {
        "slug": "landscaping",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "for a landscaping and lawn care service, propped on a stone patio with green "
            "plants visible. Leaf icon motif. Bold black background with bright red "
            "#FE1616 accent stripe. Only text visible: \"(210) 903-5551\" in white and "
            "\"Targeted.Design\" small logo. Paper texture, natural outdoor dappled light. "
            "Professional product shot."
        ),
    },
    {
        "slug": "pest-control",
        "prompt": (
            "Photorealistic product photography of a black and red direct mail postcard "
            "for pest control, sticking out of a dark metal mailbox on a house exterior. "
            "Bug shield icon motif. Bold black background with bright red #FE1616 accent "
            "stripe. Only text visible: \"(210) 903-5551\" in white and \"Targeted.Design\" "
            "small logo. Paper texture, bright daylight. Professional product shot."
        ),
    },
]

MIN_INTERVAL = 5.0  # seconds between requests for rate limiting
last_time = 0.0

for item in industries:
    slug = item["slug"]
    prompt = item["prompt"]
    encoded = urllib.parse.quote(prompt)
    seed = int(hashlib.md5(prompt.encode()).hexdigest()[:8], 16) % 999999

    url = (
        f"{BASE_URL}{encoded}"
        f"?width=1344&height=768&seed={seed}"
        f"&model={MODEL}&nologo=true&enhance=true"
        f"&apikey={API_KEY}"
    )

    # Rate limit
    now = time.time()
    wait = max(0, MIN_INTERVAL - (now - last_time))
    if wait > 0:
        print(f"Rate limit: waiting {wait:.1f}s before next request...")
        time.sleep(wait)

    print(f"\n🎨 Generating {slug}...")
    last_time = time.time()

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Hermes-Agent/1.0"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            if resp.status != 200:
                print(f"  ❌ HTTP {resp.status}")
                continue
            img_data = resp.read()

        if len(img_data) < 1000:
            print(f"  ❌ Suspiciously small response: {len(img_data)} bytes")
            continue

        outpath = os.path.join(OUTPUT_DIR, f"{slug}-lifestyle-render.jpg")
        with open(outpath, "wb") as f:
            f.write(img_data)

        print(f"  ✅ Saved {outpath} ({len(img_data):,} bytes)")

    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", errors="replace")[:200]
        except Exception:
            pass
        print(f"  ❌ HTTP {e.code}: {body}")
        if e.code == 429:
            print("  ⏳ Rate limited, waiting 30s...")
            time.sleep(30)
            last_time = time.time()

    except Exception as exc:
        print(f"  ❌ Error: {exc}")

print("\n🏁 Done! Check /home/nemesis/targeted-design-site/samples/renders/")