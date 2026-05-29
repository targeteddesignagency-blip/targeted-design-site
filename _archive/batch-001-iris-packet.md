# Iris Packet — Design Engine, Industry Mockups
## Output: /home/nemesis/targeted-design-site/batch-001-mockup-template.html

## CONTEXT
Targeted Design Agency needs a consultation mockup system. When we book a consultation with a business owner, we want to show them THEIR business name and brand colors on our EDDM card within 5 minutes.

## WHAT TO BUILD
A single HTML file that:
1. Takes URL params: ?biz=BusinessName&phone=210-555-1234&industry=restaurant&color=%23fe1616
2. Renders a 9x12 card preview with their info overlaid
3. Front shows: business name, phone, bilingual tagline, QR code placeholder, brand color accent
4. Industry-specific icon or imagery (CSS-only, no external images)
5. Color can swap instantly via the URL param
6. Print-ready CSS (@media print)

## DESIGN SPECS
- 9"×9" safe area on 9×12 card (per USPS EDDM)
- Brand colors: #fff #000 #fe1616 #333132
- Client accent color replaces #fe1616 when param provided
- Font: system sans-serif (fast load)
- Dark mode compatible
- Must look professional enough that an owner says "that's MY card"

## INDUSTRY HINTS
- Restaurant → fork/knife icon, "Tu mejor sabor en el barrio"
- Auto Repair → wrench, "Tu taller de confianza"
- HVAC → thermostat, "Aire 24/7 — cuando más lo necesitas"
- Plumbing → pipe, "Emergencias las 24 horas"
- Hair/Barber → scissors, "Tu estilo, tu barrio"
- Childcare → heart, "Donde tus pequeños están seguros"
- Landscaping → leaf, "Tu jardín en las mejores manos"
- Pest Control → shield, "Tu hogar protegido"

## SPEED MATTERS
This template must render in under 2 seconds. No external fonts, no heavy assets. CSS icons only.