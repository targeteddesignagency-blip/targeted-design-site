#!/usr/bin/env python3
"""
TDA 12×9 Card Generator — 8 clients per card, front (EN) + back (ES)
Matches template: light background, dark text, price ON ad, "Reserve your Campaign" CTA
3 requirements: clear branding, QR bottom right, readable sales copy
"""
from pathlib import Path

OUTPUT_DIR = Path("/home/nemesis/targeted-design-site/ads/eight-up-cards")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Card dimensions: 12.0" × 9.0" landscape
# At 150dpi: 1800 × 1350
CARD_W = 1800
CARD_H = 1350

# 1/4" bleed at 150dpi = 37.5px
BLEED = 37.5

# USPS indicia: min 1.5" × 0.75" at 150dpi = 225 × 112.5px
# Indicia bar height: 0.75" = 112.5px
INDICIA_H = 113

# Interior dimensions (inside bleed)
INT_W = CARD_W - 2 * BLEED   # 1725
INT_H = CARD_H - 2 * BLEED   # 1275

# 8 slots: 2 rows × 4 columns
# 0.25" gap between all ads at 150dpi = 37.5px
GAP = 37.5
# Horizontal: 4 slots + 3 gaps = INT_W - 3*GAP → each slot
SLOT_W = int((INT_W - 3 * GAP) / 4)   # 403
# Vertical: 2 slots + 2 margins (above/below indicia) + indicia = INT_H
# 2 * SLOT_H + 2 * GAP + INDICIA_H = INT_H
# SLOT_H = (INT_H - 2*GAP - INDICIA_H) / 2
SLOT_H = int((INT_H - 2 * GAP - INDICIA_H) / 2)  # 525

# 8 clients
CLIENTS = [
    {
        "slug": "dutson-pest",
        "name": "Dutson Pest Control",
        "service": "Pest Control",
        "service_es": "Control de Plagas",
        "headline": "Family Owned — 25 Years",
        "headline_es": "Empresa Familiar — 25 Años",
        "slogan": "We Eliminate Pests, Not Your Budget",
        "slogan_es": "Eliminamos Plagas, No Su Presupuesto",
        "phone": "(210) 336-3291",
        "color": "#2d6a4f",
        "icon": "🐛",
    },
    {
        "slug": "carousel-childcare",
        "name": "Carousel Childcare",
        "service": "Childcare",
        "service_es": "Cuidado Infantil",
        "headline": "4-Star Rated Learning",
        "headline_es": "Aprendizaje 4 Estrellas",
        "slogan": "Where Little Minds Grow Big",
        "slogan_es": "Donde Mentes Pequeñas Crecen",
        "phone": "(210) 980-5617",
        "color": "#0d9488",
        "icon": "🧒",
    },
    {
        "slug": "gabes-ac",
        "name": "Gabe's Priority AC",
        "service": "AC Repair",
        "service_es": "Reparación de AC",
        "headline": "AC Not Cooling?",
        "headline_es": "¿Su AC No Enfría?",
        "slogan": "We Fix It Fast — Same Day Service",
        "slogan_es": "Lo Arreglamos Rápido — Mismo Día",
        "phone": "(210) 430-9300",
        "color": "#1a365d",
        "icon": "❄️",
    },
    {
        "slug": "grass-company",
        "name": "The Grass Company",
        "service": "Landscaping",
        "service_es": "Jardinería",
        "headline": "Free Estimates",
        "headline_es": "Estimados Gratis",
        "slogan": "Transform Your Yard This Season",
        "slogan_es": "Transforme Su Jardín Esta Temporada",
        "phone": "(210) 622-7225",
        "color": "#2d6a4f",
        "icon": "🌿",
    },
    {
        "slug": "buffalo-plumbing",
        "name": "Buffalo Plumbing Co.",
        "service": "Plumbing",
        "service_es": "Plomería",
        "headline": "Since 1992",
        "headline_es": "Desde 1992",
        "slogan": "Water Heaters & Emergency Repairs",
        "slogan_es": "Calentadores y Emergencias",
        "phone": "(210) 990-2833",
        "color": "#4263eb",
        "icon": "🔩",
    },
    {
        "slug": "sams-auto",
        "name": "Sam's Auto Repair",
        "service": "Auto Repair",
        "service_es": "Reparación de Autos",
        "headline": "4.9 Stars — Honest & Hardworking",
        "headline_es": "4.9 Estrellas — Honesto y Trabajador",
        "slogan": "Quality Repairs, Fair Prices",
        "slogan_es": "Reparaciones de Calidad, Precios Justos",
        "phone": "(210) 400-1000",
        "color": "#1a365d",
        "icon": "🔧",
    },
    {
        "slug": "veterans-barber",
        "name": "Veteran's Barber Shop",
        "service": "Barbershop",
        "service_es": "Barbería",
        "headline": "Your Neighborhood Barbershop",
        "headline_es": "Su Barbería del Vecindario",
        "slogan": "Walk-Ins Welcome — Culebra Location",
        "slogan_es": "Bienvenidos Sin Cita — Culebra",
        "phone": "(210) 432-9742",
        "color": "#0d9488",
        "icon": "💈",
    },
    {
        "slug": "henrys-tacos",
        "name": "Henry's Puffy Tacos",
        "service": "Restaurant",
        "service_es": "Restaurante",
        "headline": "224+ Reviews",
        "headline_es": "224+ Reseñas",
        "slogan": "Best Puffy Tacos on the West Side",
        "slogan_es": "Mejores Tacos Esponjosos del West Side",
        "phone": "(210) 433-7833",
        "color": "#d4a017",
        "icon": "🌮",
    },
]


def build_css():
    return f"""
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Inter:wght@400;600;700&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #f5f5f5; margin: 0; padding: 0; font-family: 'Inter', sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .card {{
    width: {CARD_W}px; height: {CARD_H}px;
    background: #ffffff;
    position: relative; overflow: hidden;
    display: flex; flex-direction: column;
    padding: {BLEED}px;
    box-sizing: border-box;
  }}
  .row {{
    display: flex;
    flex: 1;
    min-height: 0;
    gap: {GAP}px;
  }}
  .slot {{
    width: {SLOT_W}px; height: {SLOT_H}px;
    padding: 10px 12px;
    border: 0.5px solid #ccc;
    display: flex; flex-direction: column;
    position: relative; overflow: hidden;
    background: #fff;
    box-sizing: border-box;
  }}
  .slot-top {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; flex-shrink: 0; }}
  .biz-name {{ font-family: 'Montserrat', sans-serif; font-size: 15px; font-weight: 900; color: #111; line-height: 1.1; flex: 1; text-transform: uppercase; }}
  .biz-icon {{ font-size: 26px; margin-left: 6px; flex-shrink: 0; }}
  .headline {{ font-family: 'Montserrat', sans-serif; font-size: 12px; font-weight: 800; color: var(--brand); margin-bottom: 3px; flex-shrink: 0; }}
  .slogan {{ font-size: 10px; color: #444; line-height: 1.3; margin-bottom: 6px; flex: 1; font-weight: 600; }}
  .slot-bottom {{ display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto; flex-shrink: 0; }}
  .cta {{ flex: 1; }}
  .cta-phone {{ font-family: 'Montserrat', sans-serif; font-size: 13px; font-weight: 900; color: #111; }}
  .cta-tagline {{ font-size: 8px; color: var(--brand); font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }}
  .qr-area {{ text-align: center; margin-left: 8px; flex-shrink: 0; }}
  .qr-img {{ width: 56px; height: 56px; border-radius: 4px; display: block; }}
  .qr-label {{ font-size: 7px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; font-weight: 700; }}
  .indicia {{
    display: flex; justify-content: space-between; align-items: center;
    height: {INDICIA_H}px; flex-shrink: 0;
    padding: 0 20px;
    margin: {GAP}px 0;
    border-top: 1px solid #999; border-bottom: 1px solid #999;
    background: #e8e8e8;
    box-sizing: border-box;
    font-size: 8px; color: #555; letter-spacing: 1.5px; text-transform: uppercase;
    font-family: 'Montserrat', sans-serif; font-weight: 700;
  }}
"""


def build_slot(client, lang="en"):
    name = client["name"]
    headline = client["headline"] if lang == "en" else client["headline_es"]
    slogan = client["slogan"] if lang == "en" else client["slogan_es"]
    phone = client["phone"]
    color = client["color"]
    icon = client["icon"]
    slug = client["slug"]
    cta_label = "Scan to Reserve" if lang == "en" else "Escanee para Reservar"
    reserve = "Reserve your Campaign" if lang == "en" else "Reserve su Campaña"

    return f"""
    <div class="slot" style="--brand: {color}">
      <div class="slot-top">
        <div class="biz-name">{name}</div>
        <div class="biz-icon">{icon}</div>
      </div>
      <div class="headline">{headline}</div>
      <div class="slogan">{slogan}</div>
      <div class="slot-bottom">
        <div class="cta">
          <div class="cta-phone">{phone}</div>
          <div class="cta-tagline">{reserve}</div>
        </div>
        <div class="qr-area">
          <img class="qr-img" src="../qr-codes/{slug}.png" alt="{cta_label}" width="56" height="56">
          <div class="qr-label">{cta_label}</div>
        </div>
      </div>
    </div>"""


def build_card(clients, lang="en"):
    title = "EDDM Front — English" if lang == "en" else "EDDM Back — Español"
    row1 = "".join(build_slot(c, lang) for c in clients[:4])
    row2 = "".join(build_slot(c, lang) for c in clients[4:])
    indicia_left = "PRSRT STD | ECRWSS | U.S. POSTAGE PAID | EDDM RETAIL | SAN ANTONIO, TX"
    indicia_right = "Local Postal Customer"

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>TDA 12×9 Card — {title}</title>
<style>{build_css()}</style>
</head>
<body>
<div class="card">
  <div class="row">
{row1}
  </div>
  <div class="indicia">
    <span>{indicia_left}</span>
    <span>{indicia_right}</span>
  </div>
  <div class="row">
{row2}
  </div>
</div>
</body>
</html>"""


def generate():
    front_html = build_card(CLIENTS, "en")
    back_html = build_card(CLIENTS, "es")

    front_path = OUTPUT_DIR / "card-front-en.html"
    back_path = OUTPUT_DIR / "card-back-es.html"

    front_path.write_text(front_html)
    back_path.write_text(back_html)

    print(f"✅ Front (EN): {front_path}")
    print(f"✅ Back (ES):  {back_path}")
    print(f"   Card: {CARD_W}×{CARD_H}px (12.0×9.0 in)")
    print(f"   Bleed: {BLEED}px (1/4\")")
    print(f"   Interior: {INT_W}×{INT_H}px")
    print(f"   Indicia: {INDICIA_H}px (0.75\")")
    print(f"   Slot: {SLOT_W}×{SLOT_H}px")
    print(f"   Grid: 4 cols × 2 rows = {len(CLIENTS)} slots")
    return front_path, back_path


if __name__ == "__main__":
    generate()
