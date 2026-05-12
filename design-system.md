# Targeted Design — Card Design System
## Component Library for EDDM Variants

### Brand Color Palette (Base)

| Token | Hex | Usage | Variant Ready |
|-------|-----|-------|--------------|
| `--brand-primary` | #fe1616 | CTAs, headlines, accent | Swap for client brand |
| `--brand-dark` | #000000 | Background, header | Fixed |
| `--brand-surface` | #333132 | Cards, sections, grid | Fixed |
| `--brand-text` | #ffffff | Body text, headlines | Fixed |
| `--brand-muted` | #999999 | Secondary text, captions | Fixed |

### Client Color Swap System

When a client wants their brand color instead of red:

| Request | Swap `--brand-primary` from #fe1616 to | Example Use |
|---------|---------------------------------------|-------------|
| Navy blue | #1a365d | Auto repair, HVAC |
| Royal blue | #4263eb | Plumbing, childcare |
| Forest green | #2d6a4f | Landscaping, pest control |
| Gold | #d4a017 | Restaurants, premium tier |
| Orange | #e85d04 | HVAC emergency, pest control |
| Teal | #0d9488 | Salons, childcare |
| Purple | #7c3aed | — (avoid per brand rules) |
| Sea foam | — | **NEVER** (explicit brand rule) |

**Process:** Copy base template → swap `--brand-primary` → export print-ready PDF. 5 minutes.

### Design Tokens (Typography)

| Token | Value | Usage |
|-------|-------|-------|
| `--font-headline` | Montserrat Bold, 36-48pt, ALL CAPS | Primary hook |
| `--font-sub` | Inter SemiBold, 18-24pt | Industry names in grid |
| `--font-body` | Inter Regular, 12-14pt | Descriptions, price anchor |
| `--font-cta` | Montserrat Bold, 24pt+ | Phone number |
| `--font-micro` | Inter Regular, 8-10pt | Indicia, legal, guarantee |

### Layout Components

#### Logo Block
- Centered, 140px height
- "Targeted.Design" below in `--font-headline`
- White on black background

#### Hook Block
- Two-line ALL CAPS headline
- English: "YOUR PHONE SHOULD BE RINGING. NOT YOUR COMPETITOR'S."
- Spanish: "SU TELÉFONO DEBERÍA ESTAR SONANDO. NO EL DE SU COMPETENCIA."
- `--font-headline`, `--brand-primary`

#### Industry Grid
- 4×2 grid (or 2×4 on mobile/vertical layout)
- Each cell: `--brand-surface` background, `--font-sub`, white text
- Icon + industry name in both languages
- Swap icon SVG per industry variant

| Slot | English | Spanish | Icon |
|------|---------|---------|------|
| 1 | Restaurants/Tacos | Restaurantes/Tacos | 🌮 |
| 2 | Auto Repair | Reparación de Autos | 🔧 |
| 3 | HVAC | Climatización | ❄️ |
| 4 | Plumbing | Plomería | 🔩 |
| 5 | Hair Salons & Barbers | Salón de Belleza y Barbería | 💈 |
| 6 | Childcare & Learning | Cuidado Infantil y Aprendizaje | 🧒 |
| 7 | Landscaping | Jardinería y Paisaje | 🌿 |
| 8 | Pest Control | Control de Plagas | 🐛 |

#### Tagline Block
- English: "EVERY DOOR. EVERY HOME. YOUR NEXT CUSTOMER."
- Spanish: "CADA PUERTA. CADA HOGAR. SU PRÓXIMO CLIENTE."
- `--font-body`, `--brand-text`

#### CTA Block
- Phone: (210) 903-5551 in `--font-cta`, `--brand-primary`
- URL: targeted-design.com in `--font-body`
- Price anchor: "Starting at $150 / Desde $150"
- Guarantee: "Results Guaranteed / Resultados Garantizados"

#### Indicia Block (Back/Spanish side only)
- Upper-right: ECRWSS / EDDM / U.S. POSTAGE PAID / SAN ANTONIO, TX
- Lower-right clear zone: 4.5" × 2.75" for postal processing
- Address: "LOCAL POSTAL CUSTOMER"
- `--font-micro`, `--brand-muted`

### Reference Image Stockpile Structure

```
/design-system/
├── base/
│   ├── card-base-en.psd      # English front, all layers editable
│   ├── card-base-es.psd      # Spanish back, all layers editable
│   ├── grid-4x2.psd          # Industry grid component
│   └── cta-block.psd         # CTA component
├── icons/
│   ├── restaurant.svg          # 🌮 taco/restaurant icon
│   ├── auto-repair.svg         # 🔧 wrench icon
│   ├── hvac.svg                # ❄️ snowflake/AC icon
│   ├── plumbing.svg            # 🔩 pipe/wrench icon
│   ├── salon.svg               # 💈 scissors icon
│   ├── childcare.svg           # 🧒 child icon
│   ├── landscaping.svg          # 🌿 leaf icon
│   └── pest-control.svg         # 🐛 bug icon
├── colors/
│   ├── brand-red.key.json      # --brand-primary: #fe1616
│   ├── navy.key.json           # --brand-primary: #1a365d
│   ├── royal-blue.key.json     # --brand-primary: #4263eb
│   ├── forest-green.key.json   # --brand-primary: #2d6a4f
│   ├── gold.key.json           # --brand-primary: #d4a017
│   ├── orange.key.json         # --brand-primary: #e85d04
│   └── teal.key.json           # --brand-primary: #0d9488
├── variants/
│   ├── restaurant/
│   │   ├── restaurant-en-red.pdf
│   │   ├── restaurant-en-gold.pdf
│   │   ├── restaurant-es-red.pdf
│   │   └── restaurant-es-gold.pdf
│   ├── auto-repair/
│   │   ├── autorepair-en-navy.pdf
│   │   ├── autorepair-en-orange.pdf
│   │   ├── autorepair-es-navy.pdf
│   │   └── autorepair-es-orange.pdf
│   ├── hvac/
│   │   ├── hvac-en-navy.pdf
│   │   ├── hvac-en-orange.pdf
│   │   ├── hvac-es-navy.pdf
│   │   └── hvac-es-orange.pdf
│   ├── plumbing/
│   │   ├── plumbing-en-royalblue.pdf
│   │   ├── plumbing-en-orange.pdf
│   │   ├── plumbing-es-royalblue.pdf
│   │   └── plumbing-es-orange.pdf
│   ├── salon/
│   │   ├── salon-en-red.pdf
│   │   ├── salon-en-teal.pdf
│   │   ├── salon-es-red.pdf
│   │   └── salon-es-teal.pdf
│   ├── childcare/
│   │   ├── childcare-en-teal.pdf
│   │   ├── childcare-en-royalblue.pdf
│   │   ├── childcare-es-teal.pdf
│   │   └── childcare-es-royalblue.pdf
│   ├── landscaping/
│   │   ├── landscaping-en-forestgreen.pdf
│   │   ├── landscaping-en-orange.pdf
│   │   ├── landscaping-es-forestgreen.pdf
│   │   └── landscaping-es-orange.pdf
│   └── pest-control/
│       ├── pestcontrol-en-forestgreen.pdf
│       ├── pestcontrol-en-orange.pdf
│       ├── pestcontrol-es-forestgreen.pdf
│       └── pestcontrol-es-orange.pdf
└── compliance/
    ├── eddm-indicia-block.psd   # USPS indicia component, positioned
    ├── eddm-address-block.psd   # LOCAL POSTAL CUSTOMER block
    └── eddm-safe-zones.psd     # Safe zone + bleed guides overlay
```

### Variant Workflow (5 minutes)

1. Open base template (`card-base-en.psd` or `card-base-es.psd`)
2. Swap `--brand-primary` color token (e.g., #fe1616 → #1a365d for navy)
3. Swap icon in industry grid cell (e.g., 🌮 → 🔧)
4. Update industry name text (English or Spanish)
5. Verify safe zones and bleed guides overlay (`eddm-safe-zones.psd`)
6. Export as PDF/X-1a, 300 DPI, CMYK, 0.125" bleed
7. Save variant to `/variants/{industry}/{industry}-{lang}-{color}.pdf`

**Total time: 5 minutes per variant if base templates are built.**

### Print Specs (Locked)

| Spec | Value |
|------|-------|
| Size | 12" × 9" (trim), 12.25" × 9.25" (bleed) |
| Paper | 14pt C2S (coated both sides), matte finish |
| Color | CMYK |
| Resolution | 300 DPI minimum |
| Bleed | 0.125" all sides |
| Safe Zone | 0.25" inside trim for critical text |
| Format | PDF/X-1a |
| Sides | 2 (English front, Spanish back) |

### Stockpile Priority (Build Order)

| Priority | Industry | Primary Color | Variants |
|----------|----------|---------------|----------|
| 1 | Restaurants/Tacos | Gold (#d4a017) | red, gold |
| 2 | Auto Repair | Navy (#1a365d) | navy, orange |
| 3 | HVAC | Navy (#1a365d) | navy, orange |
| 4 | Plumbing | Royal Blue (#4263eb) | royal, orange |
| 5 | Hair Salons & Barbers | Teal (#0d9488) | red, teal |
| 6 | Childcare & Learning | Teal (#0d9488) | teal, royal |
| 7 | Landscaping | Forest Green (#2d6a4f) | green, orange |
| 8 | Pest Control | Forest Green (#2d6a4f) | green, orange |