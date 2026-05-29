# Sage Packet — Intel, Lead Pipeline
## Output: Populate Google Sheet via Maton API

## CONTEXT
Targeted Design Agency needs real business leads from 4 diamond ZIPs in San Antonio. Drop order: 78237 → 78207 → 78228 → 78211.

## TARGET INDUSTRIES (8)
Restaurants/Tacos, Auto Repair, HVAC, Plumbing, Hair/Barber, Childcare, Landscaping, Pest Control

## GOOGLE SHEET
- Sheet ID: `1yGDvkbGUB0wrQ_TkXhNBbFjxZkvhN9MPLceRfmUmKKE`
- Maton Connection ID: `06dd4428-14ed-433f-b279-90f0eea7f764`
- Write to tab: "Leads"
- Columns: Business Name | Address | Phone | Industry | ZIP | Language (English/Spanish/Both) | Has Website (Y/N) | Has GMB (Y/N) | Source

## HOW TO SEARCH
For each ZIP × Industry combination (32 total):
1. Google Maps / Yelp search: "{industry} near {ZIP} San Antonio TX"
2. Extract: business name, address, phone, website status
3. Check if they have a Google Business Profile
4. Note language preference (name indicates Spanish-primary, or check website/greeting)

## MATON SHEETS API PATTERN
```
POST https://api.maton.ai/v1/connections/06dd4428-14ed-433f-b279-90f0eea7f764/proxy
Body: {
  "method": "POST",
  "path": "/v4/spreadsheets/1yGDvkbGUB0wrQ_TkXhNBbFjxZkvhN9MPLceRfmUmKKE/values/Leads!A1:append",
  "body": {
    "values": [["Business Name", "Address", "Phone", "Industry", "ZIP", "Language", "Has Website", "Has GMB", "Source"]]
  },
  "headers": {"valueInputOption": "USER_ENTERED"}
}
```

## PRIORITY
Start with 78237 (our #1 drop). Then 78207. Aim for 20-30 businesses per ZIP minimum.

## ALSO: Business Spot Check (from Sage Validation)
While researching leads, note for 10 businesses per ZIP:
- Do they have GMB? Optimized or bare?
- Do they have a website?
- Is there evidence of marketing services?
- What language is their phone greeting?

Write spot check results to: /home/nemesis/targeted-design-site/batch-001-sage-validation-{ZIP}.md