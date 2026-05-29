#!/usr/bin/env python3
"""
TDA Client Commission Mini-Ad Generator v3
8 businesses × 3 tiers × 2 languages = 48 HTML ad units
v3: embeds real QR code images from jordan-qr-gen.py
"""

import os
import json
import sys
from pathlib import Path

OUTPUT_DIR = Path("/home/nemesis/targeted-design-site/ads/client-commission")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# QR code directory — populated by jordan-qr-gen.py
QR_DIR = OUTPUT_DIR / "qr-codes"
QR_MANIFEST_PATH = QR_DIR / "qr-manifest.json"

BUSINESSES = [
    {
        "slug": "dutson-pest",
        "name": "Dutson Pest Control",
        "service_en": "Pest Control",
        "service_es": "Control de Plagas",
        "tagline_en": "Family Owned — 25 Years on the West Side",
        "tagline_es": "Empresa Familiar — 25 Años en el West Side",
        "phone": "(210) 336-3291",
        "zip": "78228",
        "color": "#2d6a4f",
        "icon": "🐛",
    },
    {
        "slug": "carousel-childcare",
        "name": "Carousel Childcare Center",
        "service_en": "Childcare",
        "service_es": "Cuidado Infantil",
        "tagline_en": "4-Star Rated — Plant-Based, Holistic Learning",
        "tagline_es": "4 Estrellas — Comidas Basadas en Plantas, Aprendizaje Holístico",
        "phone": "(210) 980-5617",
        "zip": "78228",
        "color": "#0d9488",
        "icon": "🧒",
    },
    {
        "slug": "gabes-ac",
        "name": "Gabe's Priority AC",
        "service_en": "AC Repair",
        "service_es": "Reparación de AC",
        "tagline_en": "AC Not Cooling? We Fix It Fast",
        "tagline_es": "¿Su AC No Enfría? Lo Arreglamos Rápido",
        "phone": "(210) 430-9300",
        "zip": "78237",
        "color": "#1a365d",
        "icon": "❄️",
    },
    {
        "slug": "grass-company",
        "name": "The Grass Company",
        "service_en": "Landscaping & Sod",
        "service_es": "Jardinería y Césped",
        "tagline_en": "Sod, Landscaping & Irrigation — Free Estimates",
        "tagline_es": "Césped, Jardinería e Riego — Estimados Gratis",
        "phone": "(210) 622-7225",
        "zip": "78237",
        "color": "#2d6a4f",
        "icon": "🌿",
    },
    {
        "slug": "buffalo-plumbing",
        "name": "Buffalo Plumbing Co.",
        "service_en": "Plumbing",
        "service_es": "Plomería",
        "tagline_en": "Plumbing Since 1992 — Water Heaters, Emergency Repairs",
        "tagline_es": "Plomería Desde 1992 — Calentadores, Emergencias",
        "phone": "(210) 990-2833",
        "zip": "78207",
        "color": "#4263eb",
        "icon": "🔩",
    },
    {
        "slug": "sams-auto",
        "name": "Sam's Auto Repair",
        "service_en": "Auto Repair",
        "service_es": "Reparación de Autos",
        "tagline_en": "Honest · Hardworking · 4.9 Stars",
        "tagline_es": "Honesto · Trabajador · 4.9 Estrellas",
        "phone": "(210) 400-1000",
        "zip": "78211",
        "color": "#1a365d",
        "icon": "🔧",
    },
    {
        "slug": "veterans-barber",
        "name": "Veteran's Barber Shop",
        "service_en": "Barbershop",
        "service_es": "Barbería",
        "tagline_en": "Your Neighborhood Barbershop on Culebra",
        "tagline_es": "Su Barbería del Vecindario en Culebra",
        "phone": "(210) 432-9742",
        "zip": "78228",
        "color": "#0d9488",
        "icon": "💈",
    },
    {
        "slug": "henrys-tacos",
        "name": "Henry's Puffy Tacos",
        "service_en": "Restaurant & Taqueria",
        "service_es": "Restaurante y Taquería",
        "tagline_en": "224+ Reviews — Puffy Tacos on the West Side",
        "tagline_es": "224+ Reseñas — Tacos Esponjosos en el West Side",
        "phone": "(210) 433-7833",
        "zip": "78228",
        "color": "#d4a017",
        "icon": "🌮",
    },
]

TIERS = [
    {
        "slug": "economy",
        "price_en": "$150/mo",
        "price_es": "$150/mes",
        "label_en": "Economy",
        "label_es": "Económico",
        "desc_en": "Reserve your Campaign",
        "desc_es": "Reserve su Campaña",
        "features_en": ["1 EDDM Card", "2,000 Doors"],
        "features_es": ["1 Tarjeta EDDM", "2,000 Puertas"],
        "cta_en": "Scan Here to Reserve",
        "cta_es": "Escanee Aquí para Reservar",
        "tier_color": "#2d6a4f",
    },
    {
        "slug": "fullsize",
        "price_en": "$550/mo",
        "price_es": "$550/mes",
        "label_en": "Full-Size",
        "label_es": "Tamaño Completo",
        "desc_en": "Featured Campaign",
        "desc_es": "Campaña Destacada",
        "features_en": ["3 EDDM Cards", "5,000 Doors", "QR Tracking"],
        "features_es": ["3 Tarjetas EDDM", "5,000 Puertas", "Rastreo QR"],
        "cta_en": "Scan Here to Reserve",
        "cta_es": "Escanee Aquí para Reservar",
        "tier_color": "#b8860b",
    },
    {
        "slug": "premium",
        "price_en": "$1,000/mo",
        "price_es": "$1,000/mes",
        "label_en": "Premium",
        "label_es": "Premium",
        "desc_en": "Premium Campaign",
        "desc_es": "Campaña Premium",
        "features_en": ["5 EDDM Cards", "10,000 Doors", "QR Tracking", "Priority"],
        "features_es": ["5 Tarjetas EDDM", "10,000 Puertas", "Rastreo QR", "Prioridad"],
        "cta_en": "Scan Here to Reserve",
        "cta_es": "Escanee Aquí para Reservar",
        "tier_color": "#8b0000",
    },
]


def build_css():
    return """
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Inter:wght@400;600;700&display=swap');
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #2a2a2a; display: flex; justify-content: center; padding: 20px 0; }
  .card {
    width: 1200px; height: 900px;
    background: var(--brand-dark);
    color: var(--brand-text);
    font-family: var(--font-body);
    position: relative; overflow: hidden;
    display: flex; flex-direction: column;
    padding: 45px 60px 40px;
    border-radius: 4px;
  }
  .top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
  .brand { font-family: var(--font-headline); font-size: 18px; font-weight: 900; color: var(--brand-text); letter-spacing: -0.5px; }
  .brand span { color: var(--brand-primary); }
  .brand-sm { font-size: 9px; color: var(--brand-muted); letter-spacing: 3px; text-transform: uppercase; margin-top: 2px; }
  .tier-badge { background: var(--tier-color); color: #fff; font-family: var(--font-headline); font-size: 14px; font-weight: 800; padding: 8px 18px; border-radius: 4px; letter-spacing: 1px; text-transform: uppercase; }
  .hero { text-align: center; margin-bottom: 28px; }
  .icon-lg { font-size: 64px; margin-bottom: 8px; }
  .biz-name { font-family: var(--font-headline); font-size: 52px; font-weight: 900; color: var(--brand-text); letter-spacing: -1px; line-height: 1.05; text-transform: uppercase; }
  .service-type { font-family: var(--font-headline); font-size: 20px; font-weight: 700; color: var(--brand-primary); letter-spacing: 4px; text-transform: uppercase; margin-top: 4px; }
  .tagline { font-size: 15px; color: var(--brand-muted); margin-top: 8px; font-weight: 600; letter-spacing: 0.5px; }
  .price-block { background: var(--brand-surface); border-radius: 12px; padding: 20px 30px; margin: 0 auto 20px; width: fit-content; text-align: center; border-left: 4px solid var(--brand-primary); }
  .price-label { font-size: 11px; color: var(--brand-muted); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px; }
  .price-amt { font-family: var(--font-headline); font-size: 44px; font-weight: 900; color: var(--brand-primary); letter-spacing: -1px; line-height: 1; }
  .price-period { font-size: 14px; color: var(--brand-muted); margin-top: 2px; }
  .price-features { display: flex; gap: 12px; justify-content: center; margin-top: 10px; flex-wrap: wrap; }
  .feat { font-size: 11px; color: var(--brand-text); background: rgba(255,255,255,0.08); padding: 4px 10px; border-radius: 3px; }
  .bottom { display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto; }
  .cta-info { flex: 1; }
  .cta-headline { font-family: var(--font-headline); font-size: 14px; font-weight: 800; color: var(--brand-text); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px; }
  .cta-phone { font-family: var(--font-headline); font-size: 38px; font-weight: 900; color: var(--brand-primary); letter-spacing: 2px; line-height: 1; }
  .cta-zip { font-size: 13px; color: var(--brand-muted); margin-top: 6px; }
  .qr-area { text-align: center; margin-left: 30px; }
  .qr-img { width: 140px; height: 140px; border-radius: 8px; display: block; }
  .qr-label { font-size: 11px; color: var(--brand-muted); letter-spacing: 1px; text-transform: uppercase; margin-top: 4px; font-weight: 700; }
  .indicia { position: absolute; bottom: 12px; left: 60px; right: 60px; display: flex; justify-content: space-between; align-items: center; font-size: 8px; color: var(--brand-muted); letter-spacing: 1px; text-transform: uppercase; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 6px; }
"""


def load_qr_map() -> dict:
    """Load QR manifest and return a dict keyed by 'biz_slug-tier_slug' -> relative path."""
    if not QR_MANIFEST_PATH.exists():
        print("⚠️  QR manifest not found. Run jordan-qr-gen.py first. Using placeholders.")
        return {}
    with open(QR_MANIFEST_PATH) as f:
        data = json.load(f)
    qr_map = {}
    for entry in data.get("qr_codes", []):
        key = f"{entry['business_slug']}-{entry['tier']}"
        qr_map[key] = f"../qr-codes/{entry['qr_filename']}"
    return qr_map


def get_qr_img_tag(biz_slug: str, tier_slug: str, qr_map: dict) -> str:
    """Return an <img> tag for the QR code, or a placeholder if not found."""
    key = f"{biz_slug}-{tier_slug}"
    qr_path = qr_map.get(key)
    if qr_path:
        return f'<img class="qr-img" src="{qr_path}" alt="Scan to reserve your campaign" width="140" height="140">'
    else:
        return '<div style="width:140px;height:140px;background:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:11px;color:#333;text-align:center;padding:10px;">QR CODE<br>Loading...</div>'


def front_en(b, t, qr_map):
    feats = ''.join(f'<span class="feat">{f}</span>' for f in t['features_en'])
    qr_img = get_qr_img_tag(b['slug'], t['slug'], qr_map)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{b["name"]} — {t["label_en"]} (EN)</title>
<style>
  :root {{
    --brand-primary: {b["color"]};
    --brand-dark: #000000;
    --brand-surface: #333132;
    --brand-text: #ffffff;
    --brand-muted: #999999;
    --tier-color: {t["tier_color"]};
    --font-headline: 'Montserrat', sans-serif;
    --font-body: 'Inter', sans-serif;
  }}
{build_css()}
</style>
</head>
<body>
<div class="card">
  <div class="top-bar">
    <div>
      <div class="brand">Targeted<span>.</span>Design</div>
      <div class="brand-sm">EDDM Marketing</div>
    </div>
    <div class="tier-badge">{t["label_en"]}</div>
  </div>
  <div class="hero">
    <div class="icon-lg">{b["icon"]}</div>
    <div class="biz-name">{b["name"]}</div>
    <div class="service-type">{b["service_en"]}</div>
    <div class="tagline">{b["tagline_en"]}</div>
  </div>
  <div class="price-block">
    <div class="price-label">Campaign Participation</div>
    <div class="price-amt">{t["price_en"]}</div>
    <div class="price-period">{t["desc_en"]}</div>
    <div class="price-features">{feats}</div>
  </div>
  <div class="bottom">
    <div class="cta-info">
      <div class="cta-headline">Call Now &mdash; {b["zip"]}</div>
      <div class="cta-phone">{b["phone"]}</div>
      <div class="cta-zip">Serving ZIP {b["zip"]}</div>
    </div>
    <div class="qr-area">
      {qr_img}
      <div class="qr-label">{t["cta_en"]}</div>
    </div>
  </div>
  <div class="indicia">
    <span>PRSRT STD | ECRWSS | U.S. POSTAGE PAID | EDDM RETAIL | SAN ANTONIO, TX</span>
    <span>Local Postal Customer</span>
  </div>
</div>
</body>
</html>'''


def front_es(b, t, qr_map):
    feats = ''.join(f'<span class="feat">{f}</span>' for f in t['features_es'])
    qr_img = get_qr_img_tag(b['slug'], t['slug'], qr_map)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{b["name"]} — {t["label_es"]} (ES)</title>
<style>
  :root {{
    --brand-primary: {b["color"]};
    --brand-dark: #000000;
    --brand-surface: #333132;
    --brand-text: #ffffff;
    --brand-muted: #999999;
    --tier-color: {t["tier_color"]};
    --font-headline: 'Montserrat', sans-serif;
    --font-body: 'Inter', sans-serif;
  }}
{build_css()}
</style>
</head>
<body>
<div class="card">
  <div class="top-bar">
    <div>
      <div class="brand">Targeted<span>.</span>Design</div>
      <div class="brand-sm">Marketing EDDM</div>
    </div>
    <div class="tier-badge">{t["label_es"]}</div>
  </div>
  <div class="hero">
    <div class="icon-lg">{b["icon"]}</div>
    <div class="biz-name">{b["name"]}</div>
    <div class="service-type">{b["service_es"]}</div>
    <div class="tagline">{b["tagline_es"]}</div>
  </div>
  <div class="price-block">
    <div class="price-label">Participación en la Campaña</div>
    <div class="price-amt">{t["price_es"]}</div>
    <div class="price-period">{t["desc_es"]}</div>
    <div class="price-features">{feats}</div>
  </div>
  <div class="bottom">
    <div class="cta-info">
      <div class="cta-headline">Llame Ahora &mdash; {b["zip"]}</div>
      <div class="cta-phone">{b["phone"]}</div>
      <div class="cta-zip">Sirviendo el ZIP {b["zip"]}</div>
    </div>
    <div class="qr-area">
      {qr_img}
      <div class="qr-label">{t["cta_es"]}</div>
    </div>
  </div>
  <div class="indicia">
    <span>PRSRT STD | ECRWSS | FRANQUEO PAGADO EE.UU. | EDDM RETAIL | SAN ANTONIO, TX</span>
    <span>Cliente Postal Local</span>
  </div>
</div>
</body>
</html>'''


def generate_all():
    count = 0
    manifest = []
    qr_map = load_qr_map()

    for b in BUSINESSES:
        biz_dir = OUTPUT_DIR / b['slug']
        biz_dir.mkdir(parents=True, exist_ok=True)

        for t in TIERS:
            en_html = front_en(b, t, qr_map)
            en_path = biz_dir / f"{b['slug']}-{t['slug']}-en.html"
            en_path.write_text(en_html)

            es_html = front_es(b, t, qr_map)
            es_path = biz_dir / f"{b['slug']}-{t['slug']}-es.html"
            es_path.write_text(es_html)

            manifest.append({
                "business": b['name'],
                "slug": b['slug'],
                "tier": t['slug'],
                "price": t['price_en'],
                "en": str(en_path.relative_to(OUTPUT_DIR)),
                "es": str(es_path.relative_to(OUTPUT_DIR)),
                "qr_url": qr_map.get(f"{b['slug']}-{t['slug']}", "PLACEHOLDER"),
            })
            count += 2

    # Write index gallery
    gallery = generate_gallery(BUSINESSES, TIERS, manifest)
    gallery_path = OUTPUT_DIR / "gallery.html"
    gallery_path.write_text(gallery)
    print(f"📸 Gallery: {gallery_path}")

    # Write manifest
    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))

    print(f"✅ Generated {count} HTML ad units ({len(BUSINESSES)} businesses × {len(TIERS)} tiers × 2 languages)")
    print(f"   Output: {OUTPUT_DIR}")
    return manifest


def generate_gallery(businesses, tiers, manifest):
    """Generate a single-page gallery with links to all ad units."""
    cards = ""
    for entry in manifest:
        slug = entry['slug']
        tier = entry['tier']
        biz = entry['business']
        price = entry['price']
        lang = entry['en'].split('-')[-1].replace('.html', '').upper()
        en_path = entry['en']
        es_path = entry['es']
        cards += f'''
    <div class="card-link">
      <a href="{en_path}" target="_blank"><div class="thumb en">EN ↗</div></a>
      <a href="{es_path}" target="_blank"><div class="thumb es">ES ↗</div></a>
      <div class="meta">
        <strong>{biz}</strong><br>
        <span class="tier-{tier}">{tier.upper()}</span> · {price} · {lang}
      </div>
    </div>'''

    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Client Commission Ad Library — 48 Ads</title>
<style>
  body {{ font-family: 'Inter', sans-serif; background: #1a1a1a; color: #eee; padding: 30px; }}
  h1 {{ font-family: 'Montserrat', sans-serif; color: #fff; margin-bottom: 4px; }}
  .sub {{ color: #999; margin-bottom: 24px; font-size: 14px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }}
  .card-link {{ background: #2a2a2a; border-radius: 8px; padding: 16px; border: 1px solid #333; }}
  .thumb {{ display: inline-block; width: 46%; text-align: center; padding: 10px; border-radius: 4px; margin: 2%; font-size: 13px; font-weight: 700; }}
  .en {{ background: #1a365d; color: #fff; }}
  .es {{ background: #333132; color: #fff; }}
  .meta {{ margin-top: 8px; font-size: 13px; color: #ccc; }}
  .tier-economy {{ color: #2d6a4f; }}
  .tier-fullsize {{ color: #b8860b; }}
  .tier-premium {{ color: #dc2626; }}
  a {{ text-decoration: none; color: inherit; }}
</style></head>
<body>
<h1>📇 Client Commission Mini-Ad Library</h1>
<p class="sub">8 Businesses × 3 Tiers × 2 Languages = <strong>48 Ad Units</strong> · Bilingual EDDM Format</p>
<div class="grid">{cards}</div>
</body></html>'''


if __name__ == "__main__":
    generate_all()
