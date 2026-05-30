#!/usr/bin/env python3
"""Generate HTML card files for Batch 3 (Clients 035-051)"""

import os
import re

CLIENTS = [
    {"slug": "035-Biltmore-Insurance-Group", "biz_name": "Biltmore Insurance Group", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "One Lawsuit. That's All It Takes.", "headline_es": "Una Demanda. Eso es Todo lo que Necesita.",
     "subhead_en": "Free Commercial Coverage Audit — Protect What You've Built",
     "subhead_es": "Auditoría Gratuita de Cobertura Comercial",
     "body_en": "Small business owners on Loop 1604 are one workplace injury away from a $100K claim. Don't let a basic online policy leave you exposed.",
     "body_es": "Los dueños de negocios en Loop 1604 están a una lesión laboral de una reclamación de $100K. No permita que una póliza básica en línea lo deje expuesto.",
     "cta_en": "Call Today: (210) 349-7807", "cta_es": "Llame Hoy: (210) 349-7807",
     "disclaimer": "Insurance coverage subject to underwriting approval.",
     "colors": {"dark": "#1B3B5C", "surface": "#333132", "accent": "#C9A959", "muted": "#999999", "text": "#FFFFFF"}},
    
    {"slug": "036-Tezel-Veterinary-Hospital", "biz_name": "Tezel Veterinary Hospital", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Skip the Drive North.", "headline_es": "Evite el Viaje al Norte.",
     "subhead_en": "Full-Service Veterinary Hospital Right Here on Military Dr.",
     "subhead_es": "Hospital Veterinario de Servicio Completo Aquí en Military Dr.",
     "body_en": "Bloodwork • Surgery • Dental • X-Rays\nNew Client Special: First Exam FREE with Any Service",
     "body_es": "Análisis de Sangre • Cirugía • Dental • Rayos X\nEspecial Nuevo Cliente: Primera Consulta GRATIS con Cualquier Servicio",
     "cta_en": "Call Now: (210) 337-4400", "cta_es": "Llame Ahora: (210) 337-4400",
     "disclaimer": "New client special. Restrictions may apply.",
     "colors": {"dark": "#2D8B7E", "surface": "#E8D5B7", "accent": "#F47A5E", "muted": "#3D3D3D", "text": "#FFFFFF"}},
    
    {"slug": "037-Medina-Lake-Veterinary-Hospital", "biz_name": "Medina Lake Veterinary Hospital", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "One Vet. All Your Animals.", "headline_es": "Un Veterinario. Todos Sus Animales.",
     "subhead_en": "Dogs • Cats • Horses • Livestock",
     "subhead_es": "Perros • Gatos • Caballos • Ganado",
     "body_en": "Dual-capability practice serving IH-35 South corridor.\nNew Clients: 10% Off Your First Visit • Haul-Ins Welcome",
     "body_es": "Práctica de doble capacidad sirviendo el corredor IH-35 Sur.\nNuevos Clientes: 10% de Descuento en Su Primera Visita • Bienvenidos Transportes",
     "cta_en": "Call Today: (210) 625-3355", "cta_es": "Llame Hoy: (210) 625-3355",
     "disclaimer": "New client discount. Some restrictions apply.",
     "colors": {"dark": "#8B3A3A", "surface": "#8FA895", "accent": "#F5F0E8", "muted": "#5C4A3D", "text": "#F5F0E8"}},
    
    {"slug": "038-Spay-Neuter-San-Antonio-SN_SA", "biz_name": "Spay Neuter San Antonio", "tier": "ECONOMY", "tier_color": "#10b981",
     "headline_en": "Spay/Neuter for $40.", "headline_es": "Esterilización por $40.",
     "subhead_en": "Because Every Family Deserves Affordable Pet Care",
     "subhead_es": "Porque Cada Familia Merece Cuidado Veterinario Asequible",
     "body_en": "Low-cost spay/neuter clinic serving San Antonio.\nWalk-Ins Welcome • Vaccinations Available",
     "body_es": "Clínica de esterilización de bajo costo sirviendo San Antonio.\nBienvenidos Sin Cita • Vacunas Disponibles",
     "cta_en": "Visit Us: 1900 Rigsby Ave", "cta_es": "Visítenos: 1900 Rigsby Ave",
     "disclaimer": "Prices subject to change. Income restrictions may apply.",
     "colors": {"dark": "#4A90B8", "surface": "#FAFAFA", "accent": "#F4C45E", "muted": "#4A4A4A", "text": "#FFFFFF"}},
    
    {"slug": "039-Bandera-Road-Pet-Hospital", "biz_name": "Bandera Road Pet Hospital", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Is Your Senior Pet in Pain?", "headline_es": "¿Su Mascota Mayor Tiene Dolor?",
     "subhead_en": "Acupuncture & Laser Therapy for Dogs & Cats",
     "subhead_es": "Acupuntura y Terapia Láser para Perros y Gatos",
     "body_en": "First Assessment $49. Help them live better, pain-free.\nSpecializing in rehabilitation for aging pets.",
     "body_es": "Primera Evaluación $49. Ayúdelos a vivir mejor, sin dolor.\nEspecializados en rehabilitación para mascotas mayores.",
     "cta_en": "Schedule Today: (210) 545-3488", "cta_es": "Programe Hoy: (210) 545-3488",
     "disclaimer": "Assessment fee applies. Treatment costs separate.",
     "colors": {"dark": "#7B5A9E", "surface": "#E8DFF5", "accent": "#6BB8A6", "muted": "#3A3A3A", "text": "#FFFFFF"}},
    
    {"slug": "040-K9-Kitchen-Pet-Boarding-Resort", "biz_name": "K9 Kitchen Pet Boarding & Resort", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Going Out of Town?", "headline_es": "¿Sale de la Ciudad?",
     "subhead_en": "First Night of Boarding FREE",
     "subhead_es": "Primera Noche de Hospedaje GRATIS",
     "body_en": "Suite-Style Rooms • Webcam Access • Training Classes\nYour pet deserves more than a kennel.",
     "body_es": "Habitaciones Tipo Suite • Acceso a Cámara Web • Clases de Entrenamiento\nSu mascota merece más que una perrera.",
     "cta_en": "Book Now: (210) 545-4565", "cta_es": "Reserve Ahora: (210) 545-4565",
     "disclaimer": "First night free with minimum 3-night stay.",
     "colors": {"dark": "#2E5C8A", "surface": "#FFFFFF", "accent": "#FFD966", "muted": "#5A6B7C", "text": "#FFFFFF"}},
    
    {"slug": "041-Studio-450-Hair-Salon", "biz_name": "Studio 450 Hair Salon", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Ready for a Change?", "headline_es": "¿Lista para un Cambio?",
     "subhead_en": "25% Off Your First Color Service",
     "subhead_es": "25% de Descuento en Tu Primer Servicio de Color",
     "body_en": "Balayage • Vivids • Corrective Color\nBilingual Stylists Available",
     "body_es": "Balayage • Colores Vivos • Color Correctivo\nEstilistas Bilingües Disponibles",
     "cta_en": "Book Now: (210) 787-7070", "cta_es": "Reserve Ahora: (210) 787-7070",
     "disclaimer": "New clients only. Cannot combine with other offers.",
     "colors": {"dark": "#2B2B2B", "surface": "#F8F5F2", "accent": "#B76E79", "muted": "#B87333", "text": "#F8F5F2"}},
    
    {"slug": "042-Salon-Rosewood", "biz_name": "Salon Rosewood", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Planning a Wedding?", "headline_es": "¿Planeando una Boda?",
     "subhead_en": "20% Off Bridal Party Packages (5+ People)",
     "subhead_es": "20% de Descuento en Paquetes para Fiestas de Boda (5+ Personas)",
     "body_en": "Hair • Makeup • Extensions\nYour Day, Our Art",
     "body_es": "Cabello • Maquillaje • Extensiones\nSu Día, Nuestro Arte",
     "cta_en": "Consult: (210) 415-0019", "cta_es": "Consulta: (210) 415-0019",
     "disclaimer": "Bridal package discount. Advance booking required.",
     "colors": {"dark": "#6B2737", "surface": "#F7E7CE", "accent": "#F4C2C2", "muted": "#D4AF37", "text": "#F7E7CE"}},
    
    {"slug": "043-Fresh-Fades-Barbershop", "biz_name": "Fresh Fades Barbershop", "tier": "ECONOMY", "tier_color": "#10b981",
     "headline_en": "New to the Neighborhood?", "headline_es": "¿Nuevo en el Vecindario?",
     "subhead_en": "First Cut $10 — Walk-Ins Welcome",
     "subhead_es": "Primer Corte $10 — Bienvenidos Sin Cita",
     "body_en": "Kids • Fades • Beard Trims\nSe Habla Español",
     "body_es": "Niños • Degradados • Recortes de Barba\nSe Habla Español",
     "cta_en": "Stop By: 2802 S Presa St", "cta_es": "Visítenos: 2802 S Presa St",
     "disclaimer": "New customers only. Regular price $25.",
     "colors": {"dark": "#C41E3A", "surface": "#1C2B3A", "accent": "#C0C0C0", "muted": "#FFFFFF", "text": "#FFFFFF"}},
    
    {"slug": "044-Nails-by-Nelly", "biz_name": "Nails by Nelly", "tier": "ECONOMY", "tier_color": "#10b981",
     "headline_en": "First Full Set Only $20.", "headline_es": "Primer Set Completo Solo $20.",
     "subhead_en": "Gel • Dip • Acrylic",
     "subhead_es": "Gel • Dip • Acrílico",
     "body_en": "Walk-Ins Welcome • Open 7 Days\nSe Habla Español",
     "body_es": "Bienvenidos Sin Cita • Abierto 7 Días\nSe Habla Español",
     "cta_en": "Visit: 1307 S St Mary's St", "cta_es": "Visite: 1307 S St Mary's St",
     "disclaimer": "New clients only. Regular price $45+.",
     "colors": {"dark": "#E91E8C", "surface": "#E6D5F0", "accent": "#4A235A", "muted": "#FFFFFF", "text": "#FFFFFF"}},
    
    {"slug": "045-The-Grooming-Den", "biz_name": "The Grooming Den", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Time to Upgrade Your Grooming.", "headline_es": "Hora de Mejorar Tu Arreglo.",
     "subhead_en": "First Cut $25 (Reg. $45)",
     "subhead_es": "Primer Corte $25 (Regular $45)",
     "body_en": "Hot Towel Shaves • Beard Sculpting\nWalk-Ins Welcome",
     "body_es": "Afeitados con Toalla Caliente • Esculpido de Barba\nBienvenidos Sin Cita",
     "cta_en": "Visit: 1010 N Flores St", "cta_es": "Visite: 1010 N Flores St",
     "disclaimer": "New clients only. Regular price $45.",
     "colors": {"dark": "#8B6B4E", "surface": "#F5F1E8", "accent": "#2D4A3E", "muted": "#1A1A1A", "text": "#F5F1E8"}},
    
    {"slug": "046-CrossFit-Agua-Dulce", "biz_name": "CrossFit Agua Dulce", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "No Experience? No Problem.", "headline_es": "¿Sin Experiencia? No Hay Problema.",
     "subhead_en": "Your First 2 Weeks Are FREE",
     "subhead_es": "Tus Primeras 2 Semanas Son GRATIS",
     "body_en": "Real Coaches • Real Community • Real Results\nAll Levels Welcome",
     "body_es": "Entrenadores Reales • Comunidad Real • Resultados Reales\nTodos los Niveles Bienvenidos",
     "cta_en": "Start Today: (210) 520-0000", "cta_es": "Empieza Hoy: (210) 520-0000",
     "disclaimer": "New members only. Must attend orientation.",
     "colors": {"dark": "#FF5722", "surface": "#2C2C2C", "accent": "#FFFFFF", "muted": "#757575", "text": "#FFFFFF"}},
    
    {"slug": "047-Orangetheory-Fitness-Stone-Oak", "biz_name": "Orangetheory Fitness — Stone Oak", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Burn Up to 1,200 Calories.", "headline_es": "Quema Hasta 1,200 Calorías.",
     "subhead_en": "First Class FREE — Heart-Rate Based Training",
     "subhead_es": "Primera Clase GRATIS — Entrenamiento Basado en Frecuencia Cardíaca",
     "body_en": "1 Hour • Real Coaches • Real Results\nTry Orangetheory on Us",
     "body_es": "1 Hora • Entrenadores Reales • Resultados Reales\nPrueba Orangetheory por Nuestra Cuenta",
     "cta_en": "Book Now: (210) 978-0000", "cta_es": "Reserve Ahora: (210) 978-0000",
     "disclaimer": "First class free. Must be 18+ or have parental consent.",
     "colors": {"dark": "#FF6B35", "surface": "#000000", "accent": "#00B4D8", "muted": "#FFFFFF", "text": "#FFFFFF"}},
    
    {"slug": "048-Hot-Yoga-San-Antonio", "biz_name": "Hot Yoga San Antonio", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Detox. De-Stress. Transform.", "headline_es": "Desintoxica. Relaja. Transforma.",
     "subhead_en": "First Week Unlimited $19",
     "subhead_es": "Semana Ilimitada $19",
     "body_en": "Heated & Non-Heated Classes\nAll Levels Welcome",
     "body_es": "Clases Calentadas y No Calentadas\nTodos los Niveles Bienvenidos",
     "cta_en": "Start Now: (210) 854-0000", "cta_es": "Empieza Ahora: (210) 854-0000",
     "disclaimer": "New students only. Hydrate before class.",
     "colors": {"dark": "#5DB7B8", "surface": "#F4EBD9", "accent": "#4A374A", "muted": "#D4A574", "text": "#4A374A"}},
    
    {"slug": "049-Titan-Fitness", "biz_name": "Titan Fitness", "tier": "ECONOMY", "tier_color": "#10b981",
     "headline_en": "Real Equipment. Real Lifters.", "headline_es": "Equipo Real. Levantadores Reales.",
     "subhead_en": "7-Day Pass FREE — No Contracts, Just Iron",
     "subhead_es": "Pase de 7 Días GRATIS — Sin Contratos, Solo Hierro",
     "body_en": "Powerlifting • Strongman • Olympic Lifting\nTired of Commercial Gyms?",
     "body_es": "Levantamiento de Potencia • Strongman • Levantamiento Olímpico\n¿Cansado de los Gimnasios Comerciales?",
     "cta_en": "Train Free: (210) 865-0000", "cta_es": "Entrena Gratis: (210) 865-0000",
     "disclaimer": "7-day pass for new members only. ID required.",
     "colors": {"dark": "#B22234", "surface": "#1C1C1C", "accent": "#A8A9AD", "muted": "#FFFFFF", "text": "#FFFFFF"}},
    
    {"slug": "050-Pilates-on-the-Park", "biz_name": "Pilates on the Park", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Strengthen Your Core.", "headline_es": "Fortalece Tu Centro.",
     "subhead_en": "First Reformer Class FREE",
     "subhead_es": "Primera Clase en Reformer GRATIS",
     "body_en": "Improve Your Posture • Move Without Pain\nAll Levels Welcome",
     "body_es": "Mejora Tu Postura • Muévete Sin Dolor\nTodos los Niveles Bienvenidos",
     "cta_en": "Book Now: (210) 826-0000", "cta_es": "Reserve Ahora: (210) 826-0000",
     "disclaimer": "First reformer class free. Advance registration required.",
     "colors": {"dark": "#87A87D", "surface": "#FAF9F6", "accent": "#3E3E3E", "muted": "#F4A896", "text": "#3E3E3E"}},
    
    {"slug": "051-Stone-Oak-Chiropractic-Wellness", "biz_name": "Stone Oak Chiropractic & Wellness", "tier": "STANDARD", "tier_color": "#4263eb",
     "headline_en": "Feel Better. Move Better. Live Better.", "headline_es": "Siéntase Mejor. Muévase Mejor. Viva Mejor.",
     "subhead_en": "Free Posture & Spinal Health Assessment",
     "subhead_es": "Evaluación Postural y de Salud Espinal GRATIS",
     "body_en": "Wellness Care for the Whole Family\nAdjustments • Nutrition • Lifestyle Coaching",
     "body_es": "Cuidado de Bienestar para Toda la Familia\nAjustes • Nutrición • Coaching de Estilo de Vida",
     "cta_en": "Schedule: (210) 495-0000", "cta_es": "Programe: (210) 495-0000",
     "disclaimer": "Free assessment. Treatment costs separate.",
     "colors": {"dark": "#4A90A4", "surface": "#E8F4F0", "accent": "#2C3E50", "muted": "#F4B350", "text": "#2C3E50"}},
]

def generate_front_html(client):
    """Generate front-EN HTML for a client"""
    slug = client["slug"]
    biz_name = client["biz_name"]
    tier = client["tier"]
    tier_color = client["tier_color"]
    colors = client["colors"]
    
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
      <div class="cta-phone">{client["cta_en"].replace("Call Today: ", "").replace("Call Now: ", "").replace("Schedule Today: ", "").replace("Start Today: ", "").replace("Book Now: ", "").replace("Consult: ", "").replace("Train Free: ", "").replace("Start Now: ", "").replace("Schedule: ", "")}</div>
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
    
    # Extract phone from CTA
    phone = client["cta_es"]
    for prefix in ["Llame Hoy: ", "Llame Ahora: ", "Programe Hoy: ", "Empieza Hoy: ", "Reserve Ahora: ", "Consulta: ", "Visítenos: ", "Visite: ", "Empieza Ahora: ", "Entrena Gratis: ", "Programe: "]:
        phone = phone.replace(prefix, "")
    
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

def main():
    output_base = "/home/nemesis/.openclaw/workspace/design/cards"
    
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
    
    print("\n✓ All HTML files generated for Batch 3 (Clients 035-051)")

if __name__ == "__main__":
    main()
