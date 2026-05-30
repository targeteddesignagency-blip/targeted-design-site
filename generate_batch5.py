#!/usr/bin/env python3
"""
CARD PRODUCTION BATCH 5 of 8 (Clients 069-085)
Generate HTML ad files (front-EN and back-ES) for each client.
"""

import os
import json

# Client data extracted from DESIGN-FILES.md
CLIENTS = [
    {
        "slug": "069-Childcare-Network-NE-Side",
        "biz_name": "Childcare Network — NE Side",
        "tier": "Economy",
        "tier_color": "#4263eb",
        "headline_en": "Military Families: Before & After School Care",
        "headline_es": "Familias Militares: Cuidado Antes y Después de la Escuela",
        "subhead_en": "We Accept Military Subsidies — Now Enrolling",
        "subhead_es": "Aceptamos Subsidios Militares — Inscripción Abierta",
        "body_en": "Convenient location on Nacogdoches Rd. Safe, nurturing environment for your children while you serve. Flexible hours for military schedules.",
        "body_es": "Ubicación conveniente en Nacogdoches Rd. Ambiente seguro y cariñoso para sus hijos mientras usted sirve. Horarios flexibles para horarios militares.",
        "cta_en": "Schedule a Tour Today",
        "cta_es": "Programe una Visita Hoy",
        "phone": "(210) 650-0000",
        "disclaimer": "Licensed childcare facility. Enrollment subject to availability.",
        "colors": {"primary": "#1B3A5F", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#FFD93D"},
        "fonts": {"headline": "Poppins", "body": "Open Sans"}
    },
    {
        "slug": "070-Little-Sprouts-Learning-Center",
        "biz_name": "Little Sprouts Learning Center",
        "tier": "Economy",
        "tier_color": "#4263eb",
        "headline_en": "Montessori-Inspired Learning in a Home-Like Setting",
        "headline_es": "Aprendizaje Tipo Montessori en un Ambiente Hogareño",
        "subhead_en": "Only 40 Spots Available — Private Tours Daily",
        "subhead_es": "Solo 40 Lugares Disponibles — Tours Privados Diariamente",
        "body_en": "Personalized attention. Natural learning materials. Deco District location. Where your child grows at their own pace.",
        "body_es": "Atención personalizada. Materiales de aprendizaje natural. Ubicación en Deco District. Donde su niño crece a su propio ritmo.",
        "cta_en": "Schedule Your Private Tour",
        "cta_es": "Programe Su Tour Privado",
        "phone": "(210) 826-0000",
        "disclaimer": "Limited enrollment. Tours by appointment only.",
        "colors": {"primary": "#87A878", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#D4846A"},
        "fonts": {"headline": "Montserrat", "body": "Lora"}
    },
    {
        "slug": "071-Zero-Heating-AC-and-Refrigeration",
        "biz_name": "Zero Heating AC and Refrigeration",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "AC Not Cooling? We Fix It Same Day",
        "headline_es": "¿Su AC No Enfría? Lo Reparamos el Mismo Día",
        "subhead_en": "24/7 Emergency Service | Free Estimates",
        "subhead_es": "Servicio de Emergencia 24/7 | Estimados Gratis",
        "body_en": "Licensed technicians. Upfront pricing. No hidden fees. Serving San Antonio homes for over 10 years.",
        "body_es": "Técnicos con licencia. Precios claros. Sin cargos ocultos. Sirviendo hogares de San Antonio por más de 10 años.",
        "cta_en": "Call Now",
        "cta_es": "Llame Ahora",
        "phone": "(210) 900-0824",
        "disclaimer": "Licensed and insured. TACLB #12345.",
        "colors": {"primary": "#00A8E8", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#E63946"},
        "fonts": {"headline": "Roboto Condensed", "body": "Roboto"}
    },
    {
        "slug": "072-Gabes-Priority-AC-Service",
        "biz_name": "Gabes Priority AC Service",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Priority Service When You Need It Most",
        "headline_es": "Servicio Prioritario Cuando Más Lo Necesita",
        "subhead_en": "AC Repair • Maintenance • Installation",
        "subhead_es": "Reparación • Mantenimiento • Instalación de AC",
        "body_en": "Fast response. Honest pricing. Family-owned and operated. Your comfort is our priority.",
        "body_es": "Respuesta rápida. Precios honestos. Propiedad y operación familiar. Su comodidad es nuestra prioridad.",
        "cta_en": "Get Priority Service",
        "cta_es": "Obtenga Servicio Prioritario",
        "phone": "(210) 430-9300",
        "disclaimer": "Family-owned and operated. TACLB #23456.",
        "colors": {"primary": "#FF6B35", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#FFFFFF"},
        "fonts": {"headline": "Oswald", "body": "Source Sans Pro"}
    },
    {
        "slug": "073-Beluga-Air",
        "biz_name": "Beluga Air",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Stay Cool All Summer Long",
        "headline_es": "Manténgase Fresco Todo el Verano",
        "subhead_en": "Reliable AC Service You Can Trust",
        "subhead_es": "Servicio de AC Confiable en Que Puede Confiar",
        "body_en": "Expert technicians. Quality parts. Satisfaction guaranteed. Keeping San Antonio homes comfortable since day one.",
        "body_es": "Técnicos expertos. Piezas de calidad. Satisfacción garantizada. Manteniendo cómodos los hogares de San Antonio desde el primer día.",
        "cta_en": "Call for Service",
        "cta_es": "Llame para Servicio",
        "phone": "(210) 468-5977",
        "disclaimer": "Satisfaction guaranteed. TACLB #34567.",
        "colors": {"primary": "#2A9D8F", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#E76F51"},
        "fonts": {"headline": "Nunito", "body": "Nunito"}
    },
    {
        "slug": "074-Blastin-Air-Conditioning-and-Heating",
        "biz_name": "Blastin Air Conditioning and Heating",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Blastin' Hot Outside? We'll Cool You Down",
        "headline_es": "¿Hace Calor Afuera? Lo Enfriaremos",
        "subhead_en": "Fast AC Repair • Heating Service • Fair Prices",
        "subhead_es": "Reparación Rápida de AC • Servicio de Calefacción • Precios Justos",
        "body_en": "No job too big or small. Licensed and insured. West Side locals serving locals. Call today for immediate relief.",
        "body_es": "Ningún trabajo es demasiado grande o pequeño. Con licencia y seguro. Locales del Oeste sirviendo a locales. Llame hoy para alivio inmediato.",
        "cta_en": "Get Cool Now",
        "cta_es": "Enfríese Ahora",
        "phone": "(210) 737-7351",
        "disclaimer": "Licensed and insured. TACLB #45678.",
        "colors": {"primary": "#DC2F02", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#FFD60A"},
        "fonts": {"headline": "Anton", "body": "Rajdhani"}
    },
    {
        "slug": "075-Air-Tex-Air-Conditioning-and-Heating-LLC",
        "biz_name": "Air Tex Air Conditioning and Heating LLC",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Texas Tough AC Service Since Day One",
        "headline_es": "Servicio de AC Texas Resistente Desde el Primer Día",
        "subhead_en": "Heating & Cooling • Callaghan Rd Location",
        "subhead_es": "Calefacción y Enfriamiento • Ubicación en Callaghan Rd",
        "body_en": "Local experts. Competitive rates. Quality workmanship. Your neighbors at Air Tex are ready to help.",
        "body_es": "Expertos locales. Tarifas competitivas. Mano de obra de calidad. Sus vecinos en Air Tex están listos para ayudar.",
        "cta_en": "Call Air Tex",
        "cta_es": "Llame a Air Tex",
        "phone": "(210) 433-9871",
        "disclaimer": "Local experts since 2010. TACLB #56789.",
        "colors": {"primary": "#BF5700", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#87CEEB"},
        "fonts": {"headline": "Bebas Neue", "body": "PT Sans"}
    },
    {
        "slug": "076-Stay-Cool-Air-Conditioning-and-Heating",
        "biz_name": "Stay Cool Air Conditioning and Heating",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Your Name Says It All — Stay Cool",
        "headline_es": "Su Nombre Lo Dice Todo — Manténgase Fresco",
        "subhead_en": "AC Repair & Heating | San Fernando Street",
        "subhead_es": "Reparación de AC y Calefacción | Calle San Fernando",
        "body_en": "Don't sweat the heat. We handle everything from quick fixes to full installations. Local service, fair prices.",
        "body_es": "No se preocupe por el calor. Manejamos todo desde reparaciones rápidas hasta instalaciones completas. Servicio local, precios justos.",
        "cta_en": "Stay Cool Today",
        "cta_es": "Manténgase Fresco Hoy",
        "phone": "(210) 478-0012",
        "disclaimer": "Local service, fair prices. TACLB #67890.",
        "colors": {"primary": "#98FF98", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#32CD32"},
        "fonts": {"headline": "Comfortaa", "body": "Quicksand"}
    },
    {
        "slug": "077-Ocean-Breeze-Cooling-and-Refrigeration",
        "biz_name": "Ocean Breeze Cooling and Refrigeration",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Cool Like an Ocean Breeze",
        "headline_es": "Fresco Como una Brisa del Océano",
        "subhead_en": "AC & Refrigeration Specialists | Chihuahua Street",
        "subhead_es": "Especialistas en AC y Refrigeración | Calle Chihuahua",
        "body_en": "Commercial and residential. Refrigeration experts. Fast response. Let the breeze blow through your home.",
        "body_es": "Comercial y residencial. Expertos en refrigeración. Respuesta rápida. Deje que la brisa sople por su hogar.",
        "cta_en": "Feel the Breeze",
        "cta_es": "Sienta la Brisa",
        "phone": "(210) 802-5555",
        "disclaimer": "Commercial and residential specialists. TACLB #78901.",
        "colors": {"primary": "#0077BE", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#9FE2BF"},
        "fonts": {"headline": "Pacifico", "body": "Noto Sans"}
    },
    {
        "slug": "078-Sosa-The-Plumber",
        "biz_name": "Sosa The Plumber",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Sosa The Plumber — Your Drain's Best Friend",
        "headline_es": "Sosa El Plomero — El Mejor Amigo de Su Drenaje",
        "subhead_en": "Leaks • Clogs • Repairs | Same Day Service",
        "subhead_es": "Fugas • Obstrucciones • Reparaciones | Servicio el Mismo Día",
        "body_en": "No job too messy. Honest work, honest prices. Serving San Antonio with pride. Call when water goes the wrong way.",
        "body_es": "Ningún trabajo es demasiado sucio. Trabajo honesto, precios honestos. Sirviendo a San Antonio con orgullo. Llame cuando el agua va por el camino equivocado.",
        "cta_en": "Call Sosa",
        "cta_es": "Llame a Sosa",
        "phone": "(210) 779-9678",
        "disclaimer": "Honest work, honest prices. Licensed plumber.",
        "colors": {"primary": "#4682B4", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#00CED1"},
        "fonts": {"headline": "Righteous", "body": "Karla"}
    },
    {
        "slug": "079-Baileys-Plumbing-Services",
        "biz_name": "Bailey's Plumbing Services",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Bailey's — Plumbing Done Right",
        "headline_es": "Bailey's — Plomería Hecha Correctamente",
        "subhead_en": "Residential & Commercial | McNarney Street",
        "subhead_es": "Residencial y Comercial | Calle McNarney",
        "body_en": "Quality fixtures. Expert installation. Emergency available. When you need it fixed right the first time.",
        "body_es": "Accesorios de calidad. Instalación experta. Emergencias disponibles. Cuando necesita que se arregle bien la primera vez.",
        "cta_en": "Fix It Right",
        "cta_es": "Arréglelo Bien",
        "phone": "(210) 382-6424",
        "disclaimer": "Quality fixtures, expert installation. Licensed.",
        "colors": {"primary": "#001F3F", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#FFD700"},
        "fonts": {"headline": "Playfair Display", "body": "Raleway"}
    },
    {
        "slug": "080-Richards-Plumbing-Repair-Shop",
        "biz_name": "Richard's Plumbing & Repair Shop",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Richard's — Plumbing & Repair Under One Roof",
        "headline_es": "Richard's — Plomería y Reparación Bajo Un Techo",
        "subhead_en": "Full Service Shop | Ruiz Street Location",
        "subhead_es": "Tienda de Servicio Completo | Ubicación en Ruiz Street",
        "body_en": "Walk-ins welcome. Parts in stock. Fair estimates. Your one-stop shop for plumbing and home repair needs.",
        "body_es": "Bienvenidos sin cita. Partes en stock. Estimados justos. Su tienda única para necesidades de plomería y reparación del hogar.",
        "cta_en": "Visit Us",
        "cta_es": "Visítenos",
        "phone": "(210) 435-8426",
        "disclaimer": "Walk-ins welcome. Parts in stock.",
        "colors": {"primary": "#C41E3A", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#FF8C00"},
        "fonts": {"headline": "Teko", "body": "IBM Plex Sans"}
    },
    {
        "slug": "081-Sams-Auto-Repair",
        "biz_name": "Sam's Auto Repair",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Sam's — Honest Auto Repair",
        "headline_es": "Sam's — Reparación de Autos Honesta",
        "subhead_en": "Brakes • Oil • Tires • Engine | New Laredo Hwy",
        "subhead_es": "Frenos • Aceite • Llantas • Motor | New Laredo Hwy",
        "body_en": "No upselling. Clear explanations. Fair prices. Your car deserves honest care from people who care.",
        "body_es": "Sin ventas adicionales. Explicaciones claras. Precios justos. Su auto merece cuidado honesto de personas que se preocupan.",
        "cta_en": "Trust Sam's",
        "cta_es": "Confíe en Sam's",
        "phone": "(210) 400-1000",
        "disclaimer": "Honest auto repair. No upselling.",
        "colors": {"primary": "#1E3A8A", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#000000"},
        "fonts": {"headline": "Russo One", "body": "Barlow"}
    },
    {
        "slug": "082-Baumann-Auto-Repair",
        "biz_name": "Baumann Auto Repair",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Baumann — Quality Repair Since Day One",
        "headline_es": "Baumann — Reparación de Calidad Desde el Primer Día",
        "subhead_en": "Full Auto Service | Cincinnati Avenue",
        "subhead_es": "Servicio Completo de Auto | Avenida Cincinnati",
        "body_en": "Experienced mechanics. Quality parts. Warranty on work. Your car is in good hands at Baumann.",
        "body_es": "Mecánicos experimentados. Piezas de calidad. Garantía en el trabajo. Su auto está en buenas manos en Baumann.",
        "cta_en": "Call Baumann",
        "cta_es": "Llame a Baumann",
        "phone": "(210) 735-8081",
        "disclaimer": "Warranty on all work performed.",
        "colors": {"primary": "#2E8B57", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#FFFF00"},
        "fonts": {"headline": "Exo 2", "body": "Exo 2"}
    },
    {
        "slug": "083-Guillermos-Auto-Repair",
        "biz_name": "Guillermos Auto Repair",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Guillermos — Tu Mecánico de Confianza",
        "headline_es": "Guillermos — Your Trusted Mechanic",
        "subhead_en": "Reparaciones • Mantenimiento • Diagnósticos",
        "subhead_es": "Repairs • Maintenance • Diagnostics",
        "body_en": "Servicio en español. Precios justos. Trabajo garantizado. En Ruiz Street, sirviendo a nuestra comunidad.",
        "body_es": "Spanish service. Fair prices. Guaranteed work. On Ruiz Street, serving our community.",
        "cta_en": "Llame a Guillermos",
        "cta_es": "Call Guillermos",
        "phone": "(210) 299-1369",
        "disclaimer": "Servicio en español. Trabajo garantizado.",
        "colors": {"primary": "#006847", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#CE1126"},
        "fonts": {"headline": "Sora", "body": "Sora"}
    },
    {
        "slug": "084-Gonzalez-Auto-Repair",
        "biz_name": "Gonzalez Auto Repair",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "Gonzalez Auto — Castroville Road's Best Kept Secret",
        "headline_es": "Gonzalez Auto — El Mejor Secreto de Castroville Road",
        "subhead_en": "Complete Auto Care | Family Owned",
        "subhead_es": "Cuidado Completo de Autos | Propiedad Familiar",
        "body_en": "Generations of service. Expert diagnostics. Affordable rates. Your neighbors trust Gonzalez for all auto needs.",
        "body_es": "Generaciones de servicio. Diagnósticos expertos. Tarifas accesibles. Sus vecinos confían en Gonzalez para todas las necesidades del auto.",
        "cta_en": "Call Gonzalez",
        "cta_es": "Llame a Gonzalez",
        "phone": "(210) 433-0989",
        "disclaimer": "Family owned. Generations of service.",
        "colors": {"primary": "#FF7F50", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#E5E4E2"},
        "fonts": {"headline": "Orbitron", "body": "Rajdhani"}
    },
    {
        "slug": "085-DD-Auto-San-Antonio",
        "biz_name": "D&D Auto San Antonio",
        "tier": "Standard",
        "tier_color": "#4263eb",
        "headline_en": "D&D Auto — Double the Expertise",
        "headline_es": "D&D Auto — Doble Experiencia",
        "subhead_en": "Bandera Road • All Makes & Models",
        "subhead_es": "Bandera Road • Todas las Marcas y Modelos",
        "body_en": "Two D's, one promise: Quality work at fair prices. Foreign and domestic. From oil changes to engine rebuilds.",
        "body_es": "Dos D's, una promesa: Trabajo de calidad a precios justos. Extranjeros y nacionales. Desde cambios de aceite hasta reconstrucciones de motor.",
        "cta_en": "D&D Auto",
        "cta_es": "D&D Auto",
        "phone": "(210) 433-1151",
        "disclaimer": "Foreign and domestic specialists.",
        "colors": {"primary": "#1560BD", "surface": "#333132", "text": "#ffffff", "muted": "#999999", "accent": "#DC143C"},
        "fonts": {"headline": "Archivo Black", "body": "Archivo"}
    }
]

def generate_front_en(client):
    """Generate front-EN HTML for a client."""
    headline_font = client['fonts']['headline'].replace(' ', '+')
    body_font = client['fonts']['body'].replace(' ', '+')
    fonts_import = f"https://fonts.googleapis.com/css2?family={headline_font}:wght@400;600;700;800;900&family={body_font}:wght@400;600;700&display=swap"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{client['biz_name']} — {client['tier']} (EN)</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family={headline_font}:wght@400;600;700;800;900&family={body_font}:wght@400;600;700&display=swap');
  :root {{
    --brand-dark: {client['colors']['primary']};
    --brand-surface: {client['colors']['surface']};
    --brand-text: {client['colors']['text']};
    --brand-muted: {client['colors']['muted']};
    --brand-accent: {client['colors']['accent']};
    --tier-color: {client['tier_color']};
    --font-headline: '{client['fonts']['headline']}', sans-serif;
    --font-body: '{client['fonts']['body']}', sans-serif;
    --bleed: 18.75px;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #2a2a2a; display: flex; justify-content: center; padding: 20px 0; }}
  .card {{
    width: 1237.5px; height: 918.75px;
    background: var(--brand-dark);
    color: var(--brand-text);
    font-family: var(--font-body);
    position: relative; overflow: hidden;
    display: flex; flex-direction: column;
    padding: 45px 60px 40px;
    border-radius: 4px;
  }}
  .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
  .brand {{ font-family: var(--font-headline); font-size: 16px; font-weight: 900; color: var(--brand-text); letter-spacing: -0.5px; }}
  .brand .dot {{ color: #fe1616; }}
  .brand-sm {{ font-size: 8px; color: var(--brand-muted); letter-spacing: 3px; text-transform: uppercase; margin-top: 2px; }}
  .tier-badge {{ background: var(--tier-color); color: #fff; font-family: var(--font-headline); font-size: 12px; font-weight: 800; padding: 6px 14px; border-radius: 4px; letter-spacing: 1px; text-transform: uppercase; }}
  .hero {{ text-align: center; margin-bottom: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center; }}
  .biz-name {{ font-family: var(--font-headline); font-size: 48px; font-weight: 900; color: var(--brand-text); letter-spacing: -1px; line-height: 1.05; }}
  .headline {{ font-family: var(--font-headline); font-size: 42px; font-weight: 900; color: var(--brand-accent); letter-spacing: -0.5px; line-height: 1.1; margin-bottom: 12px; }}
  .subhead {{ font-family: var(--font-body); font-size: 22px; font-weight: 600; color: var(--brand-text); margin-bottom: 16px; opacity: 0.9; }}
  .body-text {{ font-size: 16px; color: var(--brand-muted); margin-bottom: 20px; line-height: 1.5; }}
  .cta-block {{ background: var(--brand-surface); border-radius: 10px; padding: 18px 24px; margin: 0 auto 16px; width: fit-content; text-align: center; border-left: 4px solid var(--brand-accent); }}
  .cta-headline {{ font-family: var(--font-headline); font-size: 13px; font-weight: 800; color: var(--brand-text); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px; }}
  .cta-phone {{ font-family: var(--font-headline); font-size: 32px; font-weight: 900; color: var(--brand-accent); letter-spacing: 2px; line-height: 1; }}
  .bottom {{ display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto; }}
  .qr-placeholder {{ width: 80px; height: 80px; background: #fff; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 9px; color: #000; text-align: center; padding: 4px; }}
  .disclaimer {{ font-size: 8px; color: var(--brand-muted); max-width: 400px; text-align: right; }}
</style>
</head>
<body>
<div class="card">
  <div class="top-bar">
    <div class="brand">TARGETED<span class="dot">.</span>DESIGN<br><span class="brand-sm">EDDM POSTCARD</span></div>
    <div class="tier-badge">{client['tier'].upper()}</div>
  </div>
  <div class="hero">
    <div class="biz-name">{client['biz_name']}</div>
    <div class="headline">{client['headline_en']}</div>
    <div class="subhead">{client['subhead_en']}</div>
    <div class="body-text">{client['body_en']}</div>
    <div class="cta-block">
      <div class="cta-headline">{client['cta_en']}</div>
      <div class="cta-phone">{client['phone']}</div>
    </div>
  </div>
  <div class="bottom">
    <div class="qr-placeholder">QR CODE<br>https://targeteddesignagency.com/landing/{client['slug'].lower()}</div>
    <div class="disclaimer">{client['disclaimer']}</div>
  </div>
</div>
</body>
</html>'''
    return html

def generate_back_es(client):
    """Generate back-ES HTML for a client."""
    headline_font = client['fonts']['headline'].replace(' ', '+')
    body_font = client['fonts']['body'].replace(' ', '+')
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{client['biz_name']} — {client['tier']} (ES)</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family={headline_font}:wght@400;600;700;800;900&family={body_font}:wght@400;600;700&display=swap');
  :root {{
    --brand-dark: {client['colors']['primary']};
    --brand-surface: {client['colors']['surface']};
    --brand-text: {client['colors']['text']};
    --brand-muted: {client['colors']['muted']};
    --brand-accent: {client['colors']['accent']};
    --tier-color: {client['tier_color']};
    --font-headline: '{client['fonts']['headline']}', sans-serif;
    --font-body: '{client['fonts']['body']}', sans-serif;
    --bleed: 18.75px;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #2a2a2a; display: flex; justify-content: center; padding: 20px 0; }}
  .card {{
    width: 1237.5px; height: 918.75px;
    background: var(--brand-dark);
    color: var(--brand-text);
    font-family: var(--font-body);
    position: relative; overflow: hidden;
    display: flex; flex-direction: column;
    padding: 45px 60px 40px;
    border-radius: 4px;
  }}
  .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
  .brand {{ font-family: var(--font-headline); font-size: 16px; font-weight: 900; color: var(--brand-text); letter-spacing: -0.5px; }}
  .brand .dot {{ color: #fe1616; }}
  .brand-sm {{ font-size: 8px; color: var(--brand-muted); letter-spacing: 3px; text-transform: uppercase; margin-top: 2px; }}
  .tier-badge {{ background: var(--tier-color); color: #fff; font-family: var(--font-headline); font-size: 12px; font-weight: 800; padding: 6px 14px; border-radius: 4px; letter-spacing: 1px; text-transform: uppercase; }}
  .hero {{ text-align: center; margin-bottom: 24px; flex: 1; display: flex; flex-direction: column; justify-content: center; }}
  .biz-name {{ font-family: var(--font-headline); font-size: 48px; font-weight: 900; color: var(--brand-text); letter-spacing: -1px; line-height: 1.05; }}
  .headline {{ font-family: var(--font-headline); font-size: 42px; font-weight: 900; color: var(--brand-accent); letter-spacing: -0.5px; line-height: 1.1; margin-bottom: 12px; }}
  .subhead {{ font-family: var(--font-body); font-size: 22px; font-weight: 600; color: var(--brand-text); margin-bottom: 16px; opacity: 0.9; }}
  .body-text {{ font-size: 16px; color: var(--brand-muted); margin-bottom: 20px; line-height: 1.5; }}
  .cta-block {{ background: var(--brand-surface); border-radius: 10px; padding: 18px 24px; margin: 0 auto 16px; width: fit-content; text-align: center; border-left: 4px solid var(--brand-accent); }}
  .cta-headline {{ font-family: var(--font-headline); font-size: 13px; font-weight: 800; color: var(--brand-text); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px; }}
  .cta-phone {{ font-family: var(--font-headline); font-size: 32px; font-weight: 900; color: var(--brand-accent); letter-spacing: 2px; line-height: 1; }}
  .bottom {{ display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto; }}
  .qr-placeholder {{ width: 80px; height: 80px; background: #fff; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 9px; color: #000; text-align: center; padding: 4px; }}
  .disclaimer {{ font-size: 8px; color: var(--brand-muted); max-width: 400px; text-align: right; }}
</style>
</head>
<body>
<div class="card">
  <div class="top-bar">
    <div class="brand">TARGETED<span class="dot">.</span>DESIGN<br><span class="brand-sm">EDDM POSTCARD</span></div>
    <div class="tier-badge">{client['tier'].upper()}</div>
  </div>
  <div class="hero">
    <div class="biz-name">{client['biz_name']}</div>
    <div class="headline">{client['headline_es']}</div>
    <div class="subhead">{client['subhead_es']}</div>
    <div class="body-text">{client['body_es']}</div>
    <div class="cta-block">
      <div class="cta-headline">{client['cta_es']}</div>
      <div class="cta-phone">{client['phone']}</div>
    </div>
  </div>
  <div class="bottom">
    <div class="qr-placeholder">QR CODE<br>https://targeteddesignagency.com/landing/{client['slug'].lower()}</div>
    <div class="disclaimer">{client['disclaimer']}</div>
  </div>
</div>
</body>
</html>'''
    return html

def main():
    base_dir = "/home/nemesis/.openclaw/workspace/design/cards"
    completed = []
    
    for client in CLIENTS:
        slug = client['slug']
        output_dir = os.path.join(base_dir, slug)
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate front-EN
        front_en = generate_front_en(client)
        front_en_path = os.path.join(output_dir, f"{slug}-front-en.html")
        with open(front_en_path, 'w') as f:
            f.write(front_en)
        
        # Generate back-ES
        back_es = generate_back_es(client)
        back_es_path = os.path.join(output_dir, f"{slug}-back-es.html")
        with open(back_es_path, 'w') as f:
            f.write(back_es)
        
        completed.append({
            'slug': slug,
            'front_en': front_en_path,
            'back_es': back_es_path
        })
        print(f"Generated: {slug}")
    
    print(f"\n=== BATCH 5 COMPLETE ===")
    print(f"Generated HTML files for {len(completed)} clients")
    
    # Save manifest
    manifest_path = "/home/nemesis/targeted-design-site/batch5_manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(completed, f, indent=2)
    print(f"Manifest saved to: {manifest_path}")

if __name__ == "__main__":
    main()
