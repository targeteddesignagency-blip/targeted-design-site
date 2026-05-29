# Campaign #001 — Pipeline: Lead → Print → Home
## Decision Points & Data Correlation Strategy

### STAGE 1: LEAD GENERATION

**Rule: The truth is always a correlation. Never rely on a single data source.**

#### Primary Data Sources (Correlation Layer)

| Source | What It Gives | Cost | Fallback Priority |
|--------|---------------|------|-------------------|
| **Yelp** | Business name, phone, address, reviews, hours, category | Free API (fusion), Apify scraper | PRIMARY — richest local biz data |
| **Google Maps** | Business name, phone, address, website, hours, service area | $0.016/query (Apify) or free API | PRIMARY — broadest coverage |
| **Census ZBP** | Establishment count by ZIP/NAICS, employee size | Free | CORRELATION — validates density |
| **City of SA Open Data** | Business establishments by ZIP | Free | CORRELATION — confirms counts |
| **ZipAtlas** | Demographics, Hispanic %, income by ZIP | Free | CORRELATION — validates market size |

#### Scraping / Enrichment Layer

| Tool | What It Gives | Cost | Fallback Priority |
|------|---------------|------|-------------------|
| **Apify** | Yelp scraper, Google Maps scraper, Yellow Pages, any site | $0.016-0.05/result | PRIMARY — programmable, scales |
| **Firecrawl** | Web scraping, site extraction, structured data from any URL | Free tier, then usage-based | PRIMARY — handles JS, dynamic sites |
| **USPS EDDM Tool** | Carrier route counts, residential/business per route | Free | VALIDATION — confirms deliverability |

#### Decision Point: Data Source Fails

```
IF Yelp API down / rate-limited / defunded:
  → Apify Yelp scraper (cached, no API dependency)
  → IF Apify Yelp fails:
    → Google Maps scraper via Apify (@ $0.016/query)
    → IF Google Maps fails:
      → Firecrawl: scrape Yellow Pages, BBB, industry directories
      → IF all scrapers fail:
        → Census ZBP + City Open Data (establishment count only, no contact info)
        → Manual: drive the route, photograph every business sign
```

#### Correlation Protocol (Before We Trust Any Data Point)

For every business we target, we require **2+ sources to confirm**:

| Data Point | Source A | Source B | Source C (tiebreaker) |
|-----------|----------|----------|----------------------|
| Business exists | Yelp listing | Google Maps pin | Firecrawl of their website |
| Phone number | Yelp | Google Maps | Call and verify |
| Address | Yelp | USPS carrier route | Google Street View |
| Hours | Yelp | Google Maps | Business website (Firecrawl) |
| Language served | Yelp reviews (Spanish) | Google reviews | Website language (Firecrawl) |
| Industry classification | Yelp category | Google category | NAICS code from Census |

**A business that only appears in ONE source = low confidence. We note it but don't prioritize it until confirmed.**

---

### STAGE 2: DATA → TARGETING

#### Decision Point: Route Selection

```
FOR each ZIP in target list:
  1. Pull business count from City Open Data (correlation baseline)
  2. Pull demographic data from ZipAtlas (Hispanic %, median income)
  3. Pull carrier route counts from USPS EDDM tool (deliverable addresses)
  4. Cross-reference Yelp + Google Maps for biz density by category
  5. Score: (biz_count × bilingual_weight × income_affordability) / route_cost
  6. Rank routes by score
  7. IF data sources disagree on biz count:
     → Use the HIGHER count (under-targeting = missed revenue)
     → Flag for field verification
```

#### Decision Point: Industry Selection Per Route

```
FOR each diamond route:
  1. Search Yelp for [8 industries] in [ZIP code]
  2. Search Google Maps for same
  3. Correlate: which industries have 10+ businesses in this ZIP?
  4. Rank by: # businesses × bilingual need × price sensitivity
  5. Top 8 = card slots for this route
  6. IF a route has 15+ restaurants but only 3 HVAC:
     → Restaurants get prominent placement, HVAC gets smaller
     → Card layout adapts to route density
```

---

### STAGE 3: CARD DESIGN → PRINT

#### Decision Point: Print Specs

| Spec | Value | Why |
|------|-------|-----|
| Size | 12" × 9" | USPS EDDM flat maximum |
| Weight | 70-80lb cover | USPS minimum for flats |
| Finish | Matte | Looks premium, not glossy junk mail |
| Sides | 2 (English front, Spanish back) | Bilingual in one card |
| Quantity | 5,000 per drop | One carrier route per ZIP |
| Print vendor | TBD (Vistaprint? Local? PrintRunner?) | Decision point below |

#### Decision Point: Print Vendor Selection

```
Criteria:
  - Cost per card (target: ≤ $0.25)
  - Turnaround time (target: ≤ 5 business days)
  - Matte finish availability
  - Bulk discount tiers
  - Local vendor = faster + supports local economy (good for brand story)

Options to evaluate:
  1. Vistaprint — $0.15-0.25/card, 5-7 day turnaround
  2. PrintRunner — $0.18-0.30/card, 3-5 day turnaround
  3. Local SA print shop — TBD, need to quote
  4. Overnight Prints — $0.20-0.35/card, fast turnaround
```

---

### STAGE 4: PRINT → HOME (EDDM Drop)

#### Decision Point: USPS EDDM Submission

```
1. Log into USPS EDDM tool
2. Select carrier routes for target ZIPs
3. Verify residential + business counts per route
4. Generate mailing statement
5. Drop off at San Antonio Main Post Office
6. RETAIN: mailing statement #, route IDs, drop date

Cost breakdown per drop:
  - Print: ~$1,250 (5,000 × $0.25)
  - Postage: ~$0.20/piece = $1,000 (EDDM Retail rate)
  - Total per drop: ~$2,250
  - Revenue potential: $850-4,000/mo recurring from automation upsells
  - Break-even: 1 Standard client pays for the entire drop
```

#### Decision Point: Drop Timing

```
Best days: Tuesday-Wednesday delivery (mail processed Mon-Tue)
Avoid: Friday-Saturday (gets buried in weekend mail, lower response)
Seasonal: Avoid holiday weeks, first of month (bill-paying stress)

FOR Batch 001:
  - Print by: [TBD — 5 business days after design approval]
  - Drop: Following Tuesday
  - Track: Voice Agent call log captures all inbound
```

---

### STAGE 5: HOME → RESPONSE → CLOSE

#### Decision Point: Call Handling Protocol

```
WHEN (210) 903-5551 rings:
  1. Voice Agent answers (bilingual — detects language automatically)
  2. Qualifies: industry, business name, size, pain point
  3. IF qualified:
     → Books consultation (Google Calendar)
     → Sends confirmation SMS (Twilio)
  4. IF after hours / voicemail:
     → Captures voicemail (Whisper STT)
     → Sends follow-up SMS next morning
     → Logs to Google Sheet
  5. ALL calls logged to Call Log sheet

Response rate targets:
  - 3-5% call rate from 5,000 doors = 150-250 calls
  - Voice Agent qualifies 100%
  - 15-30 consultation bookings
  - 5-10 Economy ($150)
  - 2-5 Standard upsell ($550/mo)
  - 1-2 Premium upsell ($1,000/mo)
```

---

### DECISION POINT SUMMARY

| Stage | Decision | Rule |
|-------|----------|------|
| Lead Gen | Single source fails | Correlate 2+ sources, Apify/Firecrawl as fallback |
| Targeting | Route priority | Score by biz density × demand gap × economics |
| Design | Which industries | Top 8 by count + bilingual need in that specific route |
| Print | Vendor | Cost ≤ $0.25, matte, ≤ 5 day turnaround |
| Drop | Timing | Tuesday-Wednesday, avoid holidays/first of month |
| Response | Call handling | Voice Agent 24/7 bilingual, auto-qualify, book consult |
| Close | Pricing | Card = $150 hook, automation = $550/$1,000/mo product |

**The truth is always a correlation. Every data point requires confirmation from a second source before we act on it.**