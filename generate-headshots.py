#!/usr/bin/env python3
"""Generate AI headshots for Targeted Design Agency team members."""
import hashlib, os, time, urllib.parse, urllib.request

BASE_URL = "https://image.pollinations.ai/prompt/"
OUTPUT_DIR = "/home/nemesis/targeted-design-site/team/"

TEAM = [
    {"slug": "luna-park", "prompt": "Professional creative headshot, Korean woman in her 20s, image designer, artistic serene expression, dark straight hair, wearing minimal black top, dark studio background, creative portrait photography, 85mm lens"},
    {"slug": "sage-mitchell", "prompt": "Professional corporate headshot, older man in his 50s, research director, wise owlish analytical gaze, silver hair distinguished, wearing navy blazer, dark studio background, business portrait photography, 85mm lens"},
    {"slug": "marcus-webb", "prompt": "Professional corporate headshot, Black man in his 30s, head of sales, warm confident smile, clean shaven, wearing white shirt with dark vest, dark studio background, business portrait photography, 85mm lens"},
    {"slug": "quinn-washington", "prompt": "Professional corporate headshot, Black woman in her 40s, compliance director, stern authoritative gaze, natural hair pulled back, wearing black blazer with red pin, dark studio background, business portrait photography, 85mm lens"},
    {"slug": "derek-cole", "prompt": "Professional corporate headshot, man in his 30s, code compliance officer, serious focused expression, short brown hair, wearing gray button-down shirt, dark studio background, business portrait photography, 85mm lens"},
    {"slug": "piper-hale", "prompt": "Professional corporate headshot, woman in her 30s, print compliance specialist, meticulous detail-oriented expression, auburn hair in bun, wearing black turtleneck, dark studio background, business portrait photography, 85mm lens"},
    {"slug": "jordan-reed", "prompt": "Professional corporate headshot, young person in their 20s, chief technology officer, sharp tech-focused expression, dark hair, wearing black hoodie under blazer, dark studio background, tech portrait photography, 85mm lens"},
    {"slug": "atlas-warren", "prompt": "Professional corporate headshot, man in his 30s, R&D engineer, intense analytical expression, beard, wearing dark gray crew neck, dark studio background, tech portrait photography, 85mm lens"},
    {"slug": "worthington-miles", "prompt": "Professional corporate headshot, man in his 40s, crypto manager, sharp forward-thinking expression, graying temples, wearing dark suit with subtle red tie, dark studio background, business portrait photography, 85mm lens"},
    {"slug": "carmen-diaz", "prompt": "Professional corporate headshot, Latina woman in her 30s, operations lead, efficient organized expression, dark hair in sleek ponytail, wearing black blazer, dark studio background, business portrait photography, 85mm lens"},
    {"slug": "levi-jones", "prompt": "Professional corporate headshot, man in his 30s, founder and visionary leader, determined confident expression, dark beard, wearing dark crew neck t-shirt, dark studio background, business portrait photography, 85mm lens, dramatic side lighting, San Antonio entrepreneur"},
]

for i, member in enumerate(TEAM):
    encoded = urllib.parse.quote(member["prompt"])
    seed = int(hashlib.md5(member["prompt"].encode()).hexdigest()[:8], 16) % 999999
    url = f"{BASE_URL}{encoded}?width=1024&height=1024&seed={seed}&model=flux-realism&nologo=true&enhance=true"
    
    if i > 0:
        print(f"⏳ Rate limit pause (10s)...")
        time.sleep(10)
    
    outpath = os.path.join(OUTPUT_DIR, f"{member['slug']}.jpg")
    print(f"🎨 Generating {member['slug']}...", end=" ", flush=True)
    
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Hermes-Agent/1.0"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                img_data = resp.read()
            with open(outpath, "wb") as f:
                f.write(img_data)
            print(f"✅ ({len(img_data):,} bytes)")
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"⏳ 429 rate limited, waiting 30s... (attempt {attempt+1})")
                time.sleep(30)
            else:
                print(f"❌ HTTP {e.code}")
                break
        except Exception as exc:
            print(f"❌ {exc}")
            break

print("\n✅ Done! Headshots saved to:", OUTPUT_DIR)
print("Files:", sorted(os.listdir(OUTPUT_DIR)))