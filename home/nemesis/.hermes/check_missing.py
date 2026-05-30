import json, re

# Check enriched_leads_may28.json for leads that might not be in the sheet
with open('/home/nemesis/.hermes/sheet_data.json', 'r') as f:
    sheet_data = json.load(f)
with open('/home/nemesis/.hermes/enriched_leads_may28.json', 'r') as f:
    enriched = json.load(f)

# Build sheet dedup set
sheet_names = set()
sheet_phones = set()
for row in sheet_data.get('values', [])[1:]:
    if row and row[0]:
        norm = re.sub(r'[^a-z0-9]', '', row[0].lower().strip())
        if norm:
            sheet_names.add(norm)
    if len(row) > 2 and row[2]:
        phone = re.sub(r'[^\d]', '', row[2])
        if len(phone) >= 10:
            sheet_phones.add(phone[-10:])

# Check enriched leads
missing = []
for lead in enriched:
    # enriched format: [name, address, phone, industry, zip, lang, has_web, has_email/gmb, source, notes]
    name = lead[0] if len(lead) > 0 else ""
    phone = lead[2] if len(lead) > 2 else ""
    norm = re.sub(r'[^a-z0-9]', '', name.lower().strip()) if name else ""
    clean_phone = re.sub(r'[^\d]', '', phone) if phone else ""
    
    is_dup = False
    if norm and norm in sheet_names:
        is_dup = True
    if clean_phone and len(clean_phone) >= 10 and clean_phone[-10:] in sheet_phones:
        is_dup = True
    
    if not is_dup and norm:
        missing.append(lead)

print(f"Enriched leads file has {len(enriched)} entries")
print(f"Missing from sheet: {len(missing)}")

if missing:
    matrix = {}
    for lead in missing:
        ind = lead[3] if len(lead) > 3 else "?"
        z = lead[4] if len(lead) > 4 else "?"
        key = (ind, z)
        matrix[key] = matrix.get(key, 0) + 1
    
    print("\n=== Missing Leads by Industry × ZIP ===")
    for (ind, z), count in sorted(matrix.items()):
        print(f"  {ind:<30} {z}: {count}")
    
    # Show first 5
    print("\n=== First 5 missing leads ===")
    for lead in missing[:5]:
        print(f"  {lead[0][:40]:<40} | {lead[3]:<25} | {lead[4]}")
