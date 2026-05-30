#!/usr/bin/env python3
"""Generate HTML card files for Batch 4 (Clients 052-068)"""

import os
import subprocess

CLIENTS = [
    {"slug": "052-Active-Life-Physical-Therapy", "biz_name": "Active Life Physical Therapy", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Living With Pain?", "headline_es": "¿Viviendo Con Dolor?",
     "subhead_en": "Free 15-Minute Injury Screen — Find Out What's Really Going On",
     "subhead_es": "Evaluación Gratuita de 15 Minutos — Descubra Qué Está Pasando Realmente",
     "body_en": "Most Insurance Accepted • Same-Day Appointments\nOrthopedic Clinical Specialist on Staff",
     "body_es": "La Mayoría de los Seguros Aceptados • Citas el Mismo Día\nEspecialista Clínico Ortopédico en el Personal",
     "cta_en": "Call Today: (210) 590-0000", "cta_es": "Llame Hoy: (210) 590-0000",
     "disclaimer": "Orthopedic Clinical Specialist on staff. Restrictions may apply.",
     "colors": {"dark": "#006D77", "surface": "#EDF6F9", "accent": "#E29578", "muted": "#2D3436", "text": "#FFFFFF"}},
    
    {"slug": "053-Corrective-Chiropractic-Rehab", "biz_name": "Corrective Chiropractic & Rehab", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Tried Chiropractic Before and It Didn't Stick?", "headline_es": "¿Probó Quiropráctica Antes y No Funcionó?",
     "subhead_en": "Free Consultation — Corrective Care, Not Just Quick Adjustments",
     "subhead_es": "Consulta Gratuita — Cuidado Correctivo, No Solo Ajustes Rápidos",
     "body_en": "Structural Correction • Chronic Pain Specialists • Long-Term Results",
     "body_es": "Corrección Estructural • Especialistas en Dolor Crónico • Resultados a Largo Plazo",
     "cta_en": "Call: (210) 650-0000", "cta_es": "Llame: (210) 650-0000",
     "disclaimer": "Free consultation. Treatment plans customized per patient.",
     "colors": {"dark": "#1B3B5A", "surface": "#F9FAFB", "accent": "#D4A574", "muted": "#6B7280", "text": "#FFFFFF"}},
    
    {"slug": "054-Peak-Performance-Sports-Rehab", "biz_name": "Peak Performance Sports Rehab", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Hurt on the Field?", "headline_es": "¿Lesionado en el Campo?",
     "subhead_en": "Free Sports Injury Assessment — Get Back in the Game Faster",
     "subhead_es": "Evaluación Gratuita de Lesiones Deportivas — Regrese al Juego Más Rápido",
     "body_en": "Youth Sports • Weekend Warriors • Adult Leagues • Return-to-Play Protocols",
     "body_es": "Deportes Juveniles • Guerreros de Fin de Semana • Ligas de Adultos • Protocolos de Retorno",
     "cta_en": "Call: (210) 403-0000", "cta_es": "Llame: (210) 403-0000",
     "disclaimer": "Same-day evaluation available. Restrictions may apply.",
     "colors": {"dark": "#2563EB", "surface": "#FFFFFF", "accent": "#84CC16", "muted": "#000000", "text": "#FFFFFF"}},
    
    {"slug": "055-Wellness-One-Chiropractic", "biz_name": "Wellness One Chiropractic", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Expecting?", "headline_es": "¿Embarazada?",
     "subhead_en": "Gentle Chiropractic Care for a Healthier, More Comfortable Pregnancy",
     "subhead_es": "Cuidado Quiropráctico Suave para un Embarazo Más Saludable y Cómodo",
     "body_en": "Prenatal Certified • Webster Technique • Pediatric Care • Se Habla Español",
     "body_es": "Certificado Prenatal • Técnica Webster • Cuidado Pediátrico • Se Habla Español",
     "cta_en": "Call: (210) 375-0000", "cta_es": "Llame: (210) 375-0000",
     "disclaimer": "Free prenatal consultation. Wellness care for all ages.",
     "colors": {"dark": "#87A878", "surface": "#FDF6E3", "accent": "#D4A5A5", "muted": "#5D4E37", "text": "#FFFFFF"}},
    
    {"slug": "056-Guardian-Roofing-Construction", "biz_name": "Guardian Roofing & Construction", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Storm Damage?", "headline_es": "¿Daño por Tormenta?",
     "subhead_en": "Free Roof Inspection — We Work Directly With Your Insurance",
     "subhead_es": "Inspección Gratuita del Techo — Trabajamos Directamente con Su Seguro",
     "body_en": "Residential & Commercial • Licensed & Insured • Emergency Response • Local Since 2008",
     "body_es": "Residencial y Comercial • Con Licencia y Seguro • Respuesta de Emergencia • Local Desde 2008",
     "cta_en": "Call: (210) 885-0000", "cta_es": "Llame: (210) 885-0000",
     "disclaimer": "24/7 storm response. Free inspection, no obligation.",
     "colors": {"dark": "#374151", "surface": "#F3F4F6", "accent": "#F97316", "muted": "#9CA3AF", "text": "#FFFFFF"}},
    
    {"slug": "057-Legacy-Home-Builders-LLC", "biz_name": "Legacy Home Builders, LLC", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Own a Lot?", "headline_es": "¿Tiene un Lote?",
     "subhead_en": "Let's Build Your Dream Home — Free Design Consultation",
     "subhead_es": "Construyamos la Casa de Sus Sueños — Consulta de Diseño Gratuita",
     "body_en": "Custom Homes $400K-$1M+ • IH-10 Corridor Specialists • From Foundation to Finish",
     "body_es": "Casas Personalizadas $400K-$1M+ • Especialistas del Corredor IH-10 • De Cimientos a Terminados",
     "cta_en": "Call: (210) 698-0000", "cta_es": "Llame: (210) 698-0000",
     "disclaimer": "Free design consultation. Custom home builders since 2008.",
     "colors": {"dark": "#1E3A5F", "surface": "#FFFFFF", "accent": "#B87333", "muted": "#B8A99A", "text": "#FFFFFF"}},
    
    {"slug": "058-All-American-Roofing-Siding", "biz_name": "All American Roofing & Siding", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Don't Wait for the Leak", "headline_es": "No Espere la Fuga",
     "subhead_en": "Free Roof & Gutter Inspection. Financing Available",
     "subhead_es": "Inspección Gratuita del Techo y Canaletas. Financiamiento Disponible",
     "body_en": "Roof Repair • Siding Replacement • Gutter Installation • West Side Trusted",
     "body_es": "Reparación de Techos • Reemplazo de Fachadas • Instalación de Canaletas • Confianza del West Side",
     "cta_en": "Call: (210) 432-0000", "cta_es": "Llame: (210) 432-0000",
     "disclaimer": "Financing available. Licensed & insured.",
     "colors": {"dark": "#A52A2A", "surface": "#FAF9F6", "accent": "#2C5282", "muted": "#4A5568", "text": "#FFFFFF"}},
    
    {"slug": "059-Hill-Country-Stoneworks", "biz_name": "Hill Country Stoneworks", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Transform Your Backyard", "headline_es": "Transforme Su Patio Trasero",
     "subhead_en": "Free Design Consultation ($300 Value)",
     "subhead_es": "Consulta de Diseño Gratuita (Valor de $300)",
     "body_en": "Stone Patios, Outdoor Kitchens, Fire Features • Stone Oak Specialists • $5K-$50K Projects",
     "body_es": "Patios de Piedra, Cocinas al Aire Libre, Fogatas • Especialistas de Stone Oak • Proyectos $5K-$50K",
     "cta_en": "Call: (210) 852-0000", "cta_es": "Llame: (210) 852-0000",
     "disclaimer": "Free design consultation ($300 value). Hill Country craftsmanship.",
     "colors": {"dark": "#8B7355", "surface": "#F5F0E8", "accent": "#D97742", "muted": "#7D8F69", "text": "#FFFFFF"}},
    
    {"slug": "060-Southtown-Construction-Remodeling", "biz_name": "Southtown Construction & Remodeling", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Thinking of Remodeling?", "headline_es": "¿Piensa Remodelar?",
     "subhead_en": "Free In-Home Design Consultation. Kitchens, Baths & ADUs",
     "subhead_es": "Consulta de Diseño en Casa Gratuita. Cocinas, Baños y ADUs",
     "body_en": "Historic Home Specialists • King William / Southtown • Permits & Design Included",
     "body_es": "Especialistas en Casas Históricas • King William / Southtown • Permisos y Diseño Incluidos",
     "cta_en": "Call: (210) 541-0000", "cta_es": "Llame: (210) 541-0000",
     "disclaimer": "Free in-home consultation. Historic neighborhood specialists.",
     "colors": {"dark": "#8B4513", "surface": "#FFF8F0", "accent": "#B5A642", "muted": "#87A878", "text": "#FFFFFF"}},
    
    {"slug": "061-HR-Block-Stone-Oak-District-Office", "biz_name": "H&R Block — Stone Oak District Office", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "File Early, Get Your Refund Faster", "headline_es": "Presente Temprano, Reciba Su Reembolso Más Rápido",
     "subhead_en": "Walk-Ins Welcome. Tax Planning, Not Just Tax Filing",
     "subhead_es": "Se Atienden Sin Cita. Planificación Fiscal, No Solo Presentación de Impuestos",
     "body_en": "Stone Oak Office • Maximize Your Refund • Small Business Specialists",
     "body_es": "Oficina de Stone Oak • Maximice Su Reembolso • Especialistas en Pequeños Negocios",
     "cta_en": "Call: (210) 495-0000", "cta_es": "Llame: (210) 495-0000",
     "disclaimer": "Walk-ins welcome. Tax planning services available.",
     "colors": {"dark": "#006B4A", "surface": "#FFFFFF", "accent": "#FFD700", "muted": "#1B3B5A", "text": "#FFFFFF"}},
    
    {"slug": "062-Liberty-Tax-Service-South-Side", "biz_name": "Liberty Tax Service — South Side", "tier": "ECONOMY", "tier_color": "#10b981",
     "headline_en": "Need to File Your Taxes?", "headline_es": "¿Necesita Preparar Sus Impuestos?",
     "subhead_en": "ITIN Filing, Refunds, and Advances Available. Walk-Ins Welcome",
     "subhead_es": "ITIN, Reembolsos, y Adelantos Disponibles. ¡Se Habla Español!",
     "body_en": "South Side Location • Bilingual Staff • Maximum Refund Guarantee",
     "body_es": "Ubicación en el South Side • Personal Bilingüe • Garantía de Máximo Reembolso",
     "cta_en": "Call: (210) 923-0000", "cta_es": "Llame: (210) 923-0000",
     "disclaimer": "ITIN services available. Bilingual staff.",
     "colors": {"dark": "#FFC72C", "surface": "#FFFFFF", "accent": "#0057B8", "muted": "#228B22", "text": "#000000"}},
    
    {"slug": "063-Padron-CPA-Group-PLLC", "biz_name": "Padron CPA Group, PLLC", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Business Owner?", "headline_es": "¿Dueño de Negocio?",
     "subhead_en": "Free Tax Health Check — Are You Overpaying?",
     "subhead_es": "Chequeo Fiscal Gratuito — ¿Está Pagando de Más?",
     "body_en": "Bookkeeping, Payroll & Tax Planning Under One Roof • CPA Services • Medical Center Office",
     "body_es": "Contabilidad, Nómina y Planificación Fiscal en Un Solo Lugar • Servicios de CPA • Oficina del Medical Center",
     "cta_en": "Call: (210) 377-0000", "cta_es": "Llame: (210) 377-0000",
     "disclaimer": "Free tax health check. CPA services for small businesses.",
     "colors": {"dark": "#2C3E50", "surface": "#FFFFFF", "accent": "#27AE60", "muted": "#B8860B", "text": "#FFFFFF"}},
    
    {"slug": "064-Tax-Accounting-Solutions-SA", "biz_name": "Tax & Accounting Solutions SA", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "IRS Problems?", "headline_es": "¿Problemas con el IRS?",
     "subhead_en": "Don't Face Them Alone — Free Consultation",
     "subhead_es": "No Los Enfrente Solo — Consulta Gratuita",
     "body_en": "Enrolled Agent Representation, Tax Resolution • West Side Office • Se Habla Español",
     "body_es": "Representación de Agente Autorizado, Resolución Fiscal • Oficina del West Side • Se Habla Español",
     "cta_en": "Call: (210) 651-0000", "cta_es": "Llame: (210) 651-0000",
     "disclaimer": "Free IRS consultation. Enrolled Agent (EA) licensed.",
     "colors": {"dark": "#003366", "surface": "#F5F5F5", "accent": "#2E8B57", "muted": "#DC143C", "text": "#FFFFFF"}},
    
    {"slug": "065-QuickBooks-ProAdvisor-SA-Sole-Proprietor", "biz_name": "QuickBooks ProAdvisor SA", "tier": "ECONOMY", "tier_color": "#10b981",
     "headline_en": "Behind on Your Books?", "headline_es": "¿Atrasado en Su Contabilidad?",
     "subhead_en": "Free QuickBooks Health Check — Bookkeeping, Payroll & Tax Prep",
     "subhead_es": "Chequeo Gratuito de QuickBooks — Contabilidad, Nómina y Preparación Fiscal",
     "body_en": "QuickBooks ProAdvisor • 1-5 Employee Businesses • Contractors, Landscapers, Food Trucks",
     "body_es": "ProAdvisor de QuickBooks • Negocios de 1-5 Empleados • Contratistas, Jardineros, Food Trucks",
     "cta_en": "Call: (210) 852-0000", "cta_es": "Llame: (210) 852-0000",
     "disclaimer": "Free QuickBooks health check. ProAdvisor certified.",
     "colors": {"dark": "#2CA01C", "surface": "#FFFFFF", "accent": "#4A90D9", "muted": "#F5A623", "text": "#FFFFFF"}},
    
    {"slug": "066-Bright-Horizons-at-Stone-Oak", "biz_name": "Bright Horizons at Stone Oak", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Now Enrolling", "headline_es": "Inscripciones Abiertas",
     "subhead_en": "Infant Through Pre-K, 6 Weeks to 5 Years",
     "subhead_es": "Infantes a Pre-K, 6 Semanas a 5 Años",
     "body_en": "Bright Horizons — Where Learning Meets Loving Care • Stone Oak Location • National Brand, Local Care",
     "body_es": "Bright Horizons — Donde el Aprendizaje Encuentra el Cuidado Amoroso • Ubicación de Stone Oak • Marca Nacional, Cuidado Local",
     "cta_en": "Call: (210) 495-0000", "cta_es": "Llame: (210) 495-0000",
     "disclaimer": "Now enrolling. Tours available daily.",
     "colors": {"dark": "#0066B3", "surface": "#FFFEF7", "accent": "#FFD100", "muted": "#6CC24A", "text": "#FFFFFF"}},
    
    {"slug": "067-La-Petite-Academy-Medical-Center", "biz_name": "La Petite Academy — Medical Center", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Healthcare Workers: We've Got You Covered", "headline_es": "Trabajadores de Salud: Los Tenemos Cubiertos",
     "subhead_en": "Extended Hours Daycare — 5:30 AM to 7:30 PM",
     "subhead_es": "Guardería de Horario Extendido — 5:30 AM a 7:30 PM",
     "body_en": "Infant Through Pre-K • Medical Center Location • Shift Worker Friendly",
     "body_es": "Infantes a Pre-K • Ubicación del Medical Center • Amigable para Trabajadores de Turno",
     "cta_en": "Call: (210) 614-0000", "cta_es": "Llame: (210) 614-0000",
     "disclaimer": "Extended hours: 5:30 AM - 7:30 PM. Tours available 7 AM - 6 PM.",
     "colors": {"dark": "#6B4C9A", "surface": "#FFF8E7", "accent": "#F4A460", "muted": "#5B9BD5", "text": "#FFFFFF"}},
    
    {"slug": "068-Kiddie-Academy-of-Culebra", "biz_name": "Kiddie Academy of Culebra", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "STEM-Focused Learning for Your Little One", "headline_es": "Aprendizaje STEM para Su Pequeño",
     "subhead_en": "Now Enrolling, Ages 6 Weeks to 5 Years",
     "subhead_es": "Inscripciones Abiertas, 6 Semanas a 5 Años",
     "body_en": "Life Essentials® Curriculum • Science, Technology, Engineering, Math for Preschoolers • Culebra Location",
     "body_es": "Currículo Life Essentials® • Ciencia, Tecnología, Ingeniería, Matemáticas para Preescolares • Ubicación de Culebra",
     "cta_en": "Call: (210) 517-0000", "cta_es": "Llame: (210) 517-0000",
     "disclaimer": "Now enrolling. STEM-focused curriculum. Ages 6 weeks to 5 years.",
     "colors": {"dark": "#7B5BA8", "surface": "#FFFFFF", "accent": "#4A90D9", "muted": "#F5A623", "text": "#FFFFFF"}},
]

def extract_phone(cta):
    """Extract phone number from CTA string"""
    import re
    match = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', cta)
    return match.group(0) if match else ""

def generate_front_html(client):
    """Generate front-EN HTML for a client"""
    slug = client["slug"]
    biz_name = client["biz_name"]
    tier = client["tier"]
    tier_color = client["tier_color"]
    colors = client["colors"]
    phone = extract_phone(client["cta_en"])
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{biz_name} — {tier} (EN)</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Inter:wght@400;600;700&family=Playfair+Display:wght@700;800&display=swap');
  :root {{
    --brand-dark: {colors["dark"]};
    --brand-surface: {colors["surface"]};
    --brand-text: {colors["text"]};
    --brand-muted: {colors["muted"]};
    --brand-accent: {colors["accent"]};
    --tier-color: {tier_color};
    --font-headline: 'Montserrat', sans-serif;
    --font-body: 'Inter', sans-serif;
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
  .body-text {{ font-size: 16px; color: var(--brand-muted); margin-bottom: 20px; line-height: 1.5; white-space: pre-line; }}
  .cta-block {{ background: var(--brand-surface); border-radius: 10px; padding: 18px 24px; margin: 0 auto 16px; width: fit-content; text-align: center; border-left: 4px solid var(--brand-accent); }}
  .cta-headline {{ font-family: var(--font-headline); font-size: 13px; font-weight: 800; color: var(--brand-text); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px; }}
  .cta-phone {{ font-family: var(--font-headline); font-size: 32px; font-weight: 900; color: var(--brand-accent); letter-spacing: 2px; line-height: 1; }}
  .bottom {{ display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto; }}
  .qr-placeholder {{ width: 80px; height: 80px; background: #fff; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 9px; color: #000; text-align: center; padding: 4px; }}
  .disclaimer {{ font-size: 8px; color: var(--brand-muted); max-width: 400px; text-align: right; }}
  @media print {{
    @page {{ size: 4.125in 3.0625in; margin: 0; }}
    body {{ background: none; padding: 0; }}
    .card {{ border-radius: 0; }}
  }}
</style>
</head>
<body>
<div class="card">
  <div class="top-bar">
    <div class="brand">TARGETED<span class="dot">.</span>DESIGN<br><span class="brand-sm">EDDM POSTCARD</span></div>
    <div class="tier-badge">{tier}</div>
  </div>
  <div class="hero">
    <div class="biz-name">{biz_name}</div>
    <div class="headline">{client["headline_en"]}</div>
    <div class="subhead">{client["subhead_en"]}</div>
    <div class="body-text">{client["body_en"]}</div>
    <div class="cta-block">
      <div class="cta-headline">Call Now</div>
      <div class="cta-phone">{phone}</div>
    </div>
  </div>
  <div class="bottom">
    <div class="qr-placeholder">QR CODE<br>https://targeteddesignagency.com/landing/{slug.lower()}</div>
    <div class="disclaimer">{client["disclaimer"]}</div>
  </div>
</div>
</body>
</html>'''
    return html

def generate_back_html(client):
    """Generate back-ES HTML for a client"""
    slug = client["slug"]
    biz_name = client["biz_name"]
    tier = client["tier"]
    tier_color = client["tier_color"]
    colors = client["colors"]
    phone = extract_phone(client["cta_es"])
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{biz_name} — {tier} (ES)</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Inter:wght@400;600;700&family=Playfair+Display:wght@700;800&display=swap');
  :root {{
    --brand-dark: {colors["dark"]};
    --brand-surface: {colors["surface"]};
    --brand-text: {colors["text"]};
    --brand-muted: {colors["muted"]};
    --brand-accent: {colors["accent"]};
    --tier-color: {tier_color};
    --font-headline: 'Montserrat', sans-serif;
    --font-body: 'Inter', sans-serif;
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
  .body-text {{ font-size: 16px; color: var(--brand-muted); margin-bottom: 20px; line-height: 1.5; white-space: pre-line; }}
  .cta-block {{ background: var(--brand-surface); border-radius: 10px; padding: 18px 24px; margin: 0 auto 16px; width: fit-content; text-align: center; border-left: 4px solid var(--brand-accent); }}
  .cta-headline {{ font-family: var(--font-headline); font-size: 13px; font-weight: 800; color: var(--brand-text); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px; }}
  .cta-phone {{ font-family: var(--font-headline); font-size: 32px; font-weight: 900; color: var(--brand-accent); letter-spacing: 2px; line-height: 1; }}
  .bottom {{ display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto; }}
  .qr-placeholder {{ width: 80px; height: 80px; background: #fff; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 9px; color: #000; text-align: center; padding: 4px; }}
  .disclaimer {{ font-size: 8px; color: var(--brand-muted); max-width: 400px; text-align: right; }}
  @media print {{
    @page {{ size: 4.125in 3.0625in; margin: 0; }}
    body {{ background: none; padding: 0; }}
    .card {{ border-radius: 0; }}
  }}
</style>
</head>
<body>
<div class="card">
  <div class="top-bar">
    <div class="brand">TARGETED<span class="dot">.</span>DESIGN<br><span class="brand-sm">TARJETA EDDM</span></div>
    <div class="tier-badge">{tier}</div>
  </div>
  <div class="hero">
    <div class="biz-name">{biz_name}</div>
    <div class="headline">{client["headline_es"]}</div>
    <div class="subhead">{client["subhead_es"]}</div>
    <div class="body-text">{client["body_es"]}</div>
    <div class="cta-block">
      <div class="cta-headline">Llame Ahora</div>
      <div class="cta-phone">{phone}</div>
    </div>
  </div>
  <div class="bottom">
    <div class="qr-placeholder">CÓDIGO QR<br>https://targeteddesignagency.com/landing/{slug.lower()}</div>
    <div class="disclaimer">{client["disclaimer"]}</div>
  </div>
</div>
</body>
</html>'''
    return html

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
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Chrome error: {e}")
        return False
    except FileNotFoundError:
        print("Chrome not found, trying chromium-browser...")
        cmd[0] = 'chromium-browser'
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            return True
        except:
            return False

def main():
    output_base = "/home/nemesis/.openclaw/workspace/design/cards"
    completed = []
    
    for client in CLIENTS:
        slug = client["slug"]
        output_dir = os.path.join(output_base, slug)
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate front-EN
        front_html = generate_front_html(client)
        front_path = os.path.join(output_dir, f"{slug}-front-en.html")
        with open(front_path, 'w') as f:
            f.write(front_html)
        print(f"Created: {front_path}")
        
        # Generate back-ES
        back_html = generate_back_html(client)
        back_path = os.path.join(output_dir, f"{slug}-back-es.html")
        with open(back_path, 'w') as f:
            f.write(back_html)
        print(f"Created: {back_path}")
        
        # Export PDFs
        front_pdf = os.path.join(output_dir, f"{slug}-front-en.pdf")
        back_pdf = os.path.join(output_dir, f"{slug}-back-es.pdf")
        
        if export_pdf(front_path, front_pdf):
            print(f"Exported: {front_pdf}")
            completed.append(f"{slug}: {front_path}, {back_path}, {front_pdf}, {back_pdf}")
        else:
            print(f"PDF export failed for {slug}")
            completed.append(f"{slug}: {front_path}, {back_path} (PDF export pending)")
        
        if export_pdf(back_path, back_pdf):
            print(f"Exported: {back_pdf}")
        else:
            print(f"PDF export failed for {slug} back")
    
    print(f"\n✓ Batch 4 complete: {len(CLIENTS)} clients processed")
    print("\n=== COMPLETED CLIENTS ===")
    for c in completed:
        print(c)

if __name__ == "__main__":
    main()
