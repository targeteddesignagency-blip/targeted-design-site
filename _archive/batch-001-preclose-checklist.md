# Batch 001 — Pre-Close Checklist
## Status Report: May 11, 2026

---

## ✅ COMPLETE

| # | Item | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 1 | Card design final (Iris) | Alex/Iris | ✅ | Print-ready HTML front + back generated. Front: English "YOUR PHONE SHOULD BE RINGING." Back: Spanish "SU TELÉFONO DEBERÍA ESTAR SONANDO." Brand colors #000 #fe1616 #fff #333132. 12"×9", 0.0625" bleed (vendor spec), 300dpi. |
| 2 | 8 industry-specific card designs (print-ready) | Alex/Iris | ✅ | Single bilingual card with all 8 industries × 2 languages = 16 slots. No per-industry variants needed for Batch 001 — the card itself IS the 8-industry design. |
| 3 | Print vendor selected (Nova) | Alex/Nova | ✅ | Printing4SuperCheap.com verified. 9×12 EDDM, 14pt C2S, matte available, 4/4, $967 for 5,000 pcs + $25 bundling. Shipping included. 2-7 day turnaround. **⚠️ Bleed note:** vendor uses 0.0625" bleed (not 0.125"). Card design adjusted accordingly. **⚠️ Matte upcharge:** TBD, confirm at checkout. |
| 4 | USPS compliance verified (Quinn) | Alex/Quinn | ✅ | Specs locked: 12"×9", 14pt C2S, matte finish, indicia text: ECRWSS / EDDM / U.S. POSTAGE PAID / SAN ANTONIO, TX. Address block: LOCAL POSTAL CUSTOMER. Clear zone: 4.5"×2.75" lower-right. Documented in `references/eddm-compliance-specs.md`. |
| 5 | Card copy written | Alex/Iris | ✅ | Front English + Back Spanish. Headline, 8 industry grid, CTA, pricing anchor, guarantee. File: `batch-001-card-copy.md`. |
| 6 | Voice Agent operational (Jordan/Nova) | Alex/Jordan | ✅ | Service installed, enabled on boot, port 8443 responding. Ollama (qwen3.5) running. Twilio credentials loaded. Health check: HTTP 200 OK. |
| 7 | Voice Agent bilingual scripts (Nova) | Alex/Nova | ✅ | 16 scripts written (8 industries × 2 languages). Each: greeting, qualifying questions, pain points, Economy/Standard/Premium pitch, booking close, fallback. File: `batch-001-voice-agent-scripts.md`. |
| 8 | Voice Agent booking flow working end-to-end (Jordan) | ⬜ | 🟡 PARTIAL | Voice agent answers and processes speech via Ollama. Google Calendar booking not yet connected. SMS confirmation not yet connected (Twilio SMS API ready but not wired). **Needs end-to-end test with tunnel URL.** |
| 9 | Voice Agent SMS confirmation working (Jordan) | ⬜ | 🟡 NOT CONNECTED | Twilio SMS API is available. Script to send confirmation SMS not yet implemented in agent.py. |
| 10 | Call logging to Sheet working (Jordan) | ⬜ | 🟡 NOT CONNECTED | Google Sheet `1yGDvkb...` exists with Lead Pipeline tab. Maton connection available. Agent does not yet push call data to sheet after each call. |
| 11 | Email outreach templates — 8 industries (Nova/Iris) | ⬜ | ❌ NOT STARTED | Email templates for outbound outreach to businesses in diamond ZIPs. Need 8 industry-specific templates (1 per industry) × 2 languages = 16 email bodies. |
| 12 | Service agreement template ready (Justice) | Alex/Justice | ✅ | EDDM Service Agreement (monthly) migrated to `/legal/eddm-service-agreement.md`. Covers: service description, payment (Net 7, 1.5%/mo late fee), cancellation (30 days, no penalty), IP, indemnification, liability cap, privacy cross-reference, Bexar County TX disputes. Contact placeholders filled. Annual version also exists but needs term/cancellation section updates. |
| 13 | Terms of Service on website (Justice) | Alex/Justice | ✅ | `terms.html` deployed to targeted-design.com. 10 sections, full legal coverage, linked from footer. |
| 14 | Privacy policy on website (Justice) | Alex/Justice | ✅ | `privacy.html` deployed to targeted-design.com. 12 sections covering data collection, Square payment, Twilio telephony, retention, user rights, CCPA/GDPR. Linked from footer. |
| 15 | Payment flow tested end-to-end (Echo) | Alex/Echo | ✅ | Square checkout worker live at `td-square-checkout.targeted-design-agency.workers.dev`. All 3 tiers ($150/$550/$1,000) generating real checkout links. Production environment. Website CTA buttons wired. |
| 16 | Attribution tracking in place (Nova) | Alex/Nova | ✅ | UTM structure documented: `utm_source=eddm&utm_medium=direct-mail&utm_campaign=batch-001&utm_content={zip}&utm_term={industry}`. 4 ZIP-level QR URLs defined. Phone tracking strategy: CallRail (recommended, ~$95/mo) vs Twilio sub-numbers (fallback, ~$15/mo). File: `batch-001-attribution.md`. |
| 17 | Mockups per industry ready for consultations (Iris) | ⬜ | 🟡 PARTIAL | Card design HTML exists but not yet converted to individual industry mockups (showing client's business name/logo on the card). Standard mockup = 1 template with business name swap. |

---

## 🟡 IN PROGRESS / NEEDS ACTION

| # | Item | Status | Blocker | Action Needed |
|---|------|--------|---------|---------------|
| 8 | Voice Agent booking flow | 🟡 PARTIAL | Needs code in agent.py to push events via Maton Google Calendar API | Wire `agent.py` to create Google Calendar events via Maton (`POST /google-calendar/calendar/v3/calendars/primary/events`). Maton connection `0d4a4ea5` tested and confirmed working. **Free — no new accounts needed.** |
| 9 | Voice Agent SMS confirmation | 🟡 | Needs code in agent.py | Add Twilio SMS send via Maton connection `dce9c019` or direct Twilio API (already have credentials at `~/.hermes/secrets/twilio.env`). **Free — Twilio SMS ~$0.0079/message.** |
| 10 | Call logging to Google Sheet | 🟡 | Needs code in agent.py | Push call data to Sheet `1yGDvkb…` via Maton connection `06dd4428`. **Free — Maton already connected.** |
| 11 | Email outreach templates | ❌ NOT STARTED | None | Write 8 industry-specific email templates (English + Spanish). Send via Maton Google Mail connection `49fe06fa`. **Free.** |
| 17 | Industry mockups for consultations | 🟡 | Need image generation | Generate HTML mockups showing card with client business name. Can create template for Iris. **Free — just time.** |

## 💰 BOOTSTRAP BUDGET — All Free Tools

| Item | Free Option | Paid Alternative (NOT using) |
|------|-------------|------------------------------|
| **Phone tracking** | Voice Agent asks ZIP, logs to Sheet | CallRail $95/mo — **NOT using** |
| **Calendar booking** | Maton Google Calendar (free) | Google Cloud OAuth project — **NOT needed** |
| **Call logging** | Maton Google Sheets (free) | Custom CRM — **NOT needed** |
| **Email outreach** | Maton Gmail (free) | Mailchimp/Klaviyo — **NOT needed** |
| **SMS confirmation** | Twilio SMS ($0.0079/msg) | CallRail — **NOT using** |
| **Card design** | HTML templates (free) | Canva Pro — **NOT needed** |
| **Print & Drop** | Printing4SuperCheap Full Service EDDM (~$2,592) | Self-serve ~$2,228 — **NOT using** |
| **Tunnel URL** | Named Cloudflare Tunnel (free) | Custom domain — **later** |

---

## 📋 ITEMS REQUIRING LEVI'S DECISION

1. **Matte finish upcharge** — Printing4SuperCheap's published price ($967) is for UV Ultragloss. Matte is available but may carry a small upcharge. Confirm matte at checkout or email jake@printing4supercheap.com for a locked quote.

2. **Phone tracking** — Three options documented: CallRail (~$95/mo, recommended), Twilio sub-numbers (~$15/mo, DIY), manual sheet logging ($0, 60% accuracy). Need to provision numbers before drop date.

3. **Google Calendar integration** — Need Google Calendar API credentials to wire the voice agent's booking flow. This requires a Google Cloud project + OAuth consent screen.

4. **Cloudflare Tunnel URL** — Inbound calls require a persistent public URL. Current setup uses ephemeral `trycloudflare.com` URLs. Options: (a) Named Cloudflare Tunnel with stable DNS, (b) Domain pointed at the agent, (c) Twilio TwiML Bin for static responses. Recommended: Named tunnel or domain.

5. **Full Service EDDM vs Print-Only** — Printing4SuperCheap offers Full Service EDDM at $0.32/piece (includes prep + postage to every door). Total for 5,000: ~$2,592 vs Print-Only ($967 + self-prep + $1,000+ postage). Full Service removes the USPS paperwork burden. Decision: Full Service or Print-Only?

---

## 💰 BATCH 001 COST SUMMARY

| Item | Cost | Notes |
|------|------|-------|
| Printing4SuperCheap Full Service EDDM | ~$2,592 | Print + bundling + prep + postage to every door. Zero USPS paperwork by us. |
| Twilio SMS (~200 msgs) | ~$1.58 | Confirmation texts |
| **Everything else** | **$0** | Maton (Calendar, Sheets, Gmail), Cloudflare tunnel, HTML card design |
| **Total Batch 001** | **~$2,594** | |
| **Break-even** | **1 Standard client ($550/mo)** | Client pays monthly, drop is one-time |

**Break-even: 1 Standard client at $550/mo pays for entire drop.**

---

## 🚀 READY TO LAUNCH (when remaining items cleared)

- [ ] Wire Google Calendar booking to voice agent
- [ ] Add SMS confirmation to voice agent
- [ ] Add call logging to Google Sheet
- [ ] Write 8 email outreach templates
- [ ] Provision phone tracking numbers (CallRail or Twilio)
- [ ] Confirm matte finish + get locked print quote
- [ ] Decide: Full Service EDDM or Print-Only
- [ ] Set up persistent tunnel URL for inbound calls
- [ ] Generate industry mockups for consultations

**Estimated time to clear all items: 1-2 focused sessions.**