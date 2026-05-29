# Pre-Close Dependencies — What Must Be Done Before River Sells
## "Design, Compliance, and Operations must already be complete. Justice and Echo validating."

### THE DEPENDENCY CHAIN

```
SAGE (Research)          IRIS (Design)          QUINN (Compliance)
─────── Leads ──────►    ───── Card ──────►    ───── Sign-off ──────►
     │                       │                       │
     │                       │                       │
     ▼                       ▼                       ▼
NOVA (Operations)        NOVA (Operations)       NOVA (Operations)
────── Outreach ──►     ──── Print/Drop ──►     ──── Attribution ──►
     │                       │                       │
     ▼                       ▼                       ▼
RIVER (Sales)            RIVER (Sales)            RIVER (Sales)
───── Consults ─────►   ───── Closes ─────►    ───── Onboards ─────►
     │                       │                       │
     │                       │                       │
     ▼                       ▼                       ▼
ECHO (Finance)          ECHO (Finance)          ECHO (Finance)
───── Payment ──────►   ───── Invoice ──────►   ───── Revenue ─────►
     │                       │                       │
     ▼                       ▼                       ▼
JUSTICE (Legal)         JUSTICE (Legal)         JUSTICE (Legal)
───── Contract ─────►   ───── Terms ──────►    ───── Protect ─────►
```

### WHAT MUST BE COMPLETE BEFORE RIVER CAN CLOSE

#### 1. IRIS — Design (Card Must Exist Physically)

River can't sell what doesn't exist. Before a single consultation:

| Deliverable | Status | Owner | Depends On |
|-------------|--------|-------|------------|
| Card design (12"×9") | 🟡 Copy written, design NOT final | Iris | Card copy (done ✅), brand guidelines |
| Card layout (8 industries × 2 languages) | 🟡 Copy structure done, visual layout NOT done | Iris | Card copy, brand colors |
| Print-ready files (CMYK, 300dpi, bleed) | ❌ Not started | Iris | Final design approval |
| Print vendor selected | ❌ Not started | Nova | Print specs finalized |
| Print vendor contract | ❌ Not started | Nova | Vendor selected |
| Cards printed and delivered | ❌ Not started | Nova | Print-ready files, contract |
| EDDM routes selected (USPS) | ❌ Not started | Nova | Cards printed |
| EDDM drop scheduled | ❌ Not started | Nova | Routes selected |

**River cannot close a deal until Iris has produced a card the client can see.**
"Trust me, it'll look great" is not a close. A mockup, a proof, a sample — that's a close.

#### 2. QUINN — Compliance (Legal Must Be Clean)

| Deliverable | Status | Owner | Depends On |
|-------------|--------|-------|------------|
| EDDM postal regulations verified | ❌ Not started | Quinn/Derek | Card design (mailability specs) |
| EDDM size/weight compliance check | ❌ Not started | Quinn/Derek/Piper | Print specs |
| Business license verification (SA) | ❌ Not started | Quinn | LLC/sole prop status |
| Terms of service for website | ❌ Not started | Justice | Legal review |
| Privacy policy for website | ❌ Not started | Justice | Legal review |
| Service agreement template | ❌ Not started | Justice | Pricing tiers finalized |
| Refund/cancellation policy | ❌ Not started | Justice/Echo | Pricing tiers |
| EDDM disclaimer language | ❌ Not started | Quinn/Piper | USPS regulations |

**River cannot close a deal until Quinn has verified the card is USPS-compliant AND Justice has a contract for the client to sign.**
A deal without a signed contract is a conversation, not a close.

#### 3. NOVA — Operations (Engine Must Be Running)

| Deliverable | Status | Owner | Depends On |
|-------------|--------|-------|------------|
| Voice Agent V2 — inbound call flow | 🟡 Working, needs persistent tunnel | Jordan | Cloudflare tunnel |
| Voice Agent — bilingual scripts (16) | ❌ Not started | Nova/Atlas | 8 industries × 2 languages |
| Voice Agent — qualification flow | ❌ Not started | Nova | Industry scripts |
| Voice Agent — booking to Google Calendar | ❌ Not started | Jordan | Calendar API |
| Voice Agent — SMS confirmation | ❌ Not started | Jordan | Twilio integration |
| Voice Agent — call logging to Sheet | ❌ Not started | Jordan | Maton API |
| Website — checkout flow tested | ✅ Working | Iris/Jordan | Square checkout |
| Website — mobile responsive verified | ✅ Done | Iris | — |
| Attribution — UTM tracking setup | ❌ Not started | Nova | EDDM routes defined |
| Attribution — call tracking per ZIP | ❌ Not started | Nova | Twilio numbers per route |
| Outreach — email templates (8 industries) | ❌ Not started | Nova/Iris | Card design, scripts |
| Outreach — SMS templates (8 industries) | ❌ Not started | Nova | Scripts |
| Outreach — social DM templates | ❌ Not started | Nova | Scripts |

**River cannot close a deal until Nova's engine answers the phone, books the consultation, and logs the lead.**
If River lands a client and they call (210) 903-5551 and it doesn't work — that's not a close, that's a disaster.

#### 4. ECHO — Finance (Money Must Flow)

| Deliverable | Status | Owner | Depends On |
|-------------|--------|-------|------------|
| Square checkout — all 3 tiers | ✅ Working | Echo/Jordan | — |
| Square webhook — payment confirmation | ✅ Handler exists | Echo | Webhook URL setup |
| Invoice template | ❌ Not started | Echo | Service agreement |
| Payment tracker in Sheet | ✅ Tab exists | Echo | — |
| Revenue recognition system | ❌ Not started | Echo | Invoice template |
| Monthly billing automation | ❌ Not started | Echo | Revenue recognition |

**River cannot close a deal until Echo can take the money, confirm the payment, and start billing.**
A signed contract means nothing if the payment link is broken.

#### 5. JUSTICE — Legal (Protection Must Exist)

| Deliverable | Status | Owner | Depends On |
|-------------|--------|-------|------------|
| Service agreement / contract | ❌ Not started | Justice | Pricing tiers, scope definition |
| Terms of service (website) | ❌ Not started | Justice | Legal review |
| Privacy policy (website) | ❌ Not started | Justice | Data collection practices |
| EDDM USPS compliance | ❌ Not started | Justice/Quinn | Card design, print specs |
| LLC formation (after revenue) | ❌ Later | Justice/Echo | Revenue ≥ costs |
| Intellectual property (brand, logo) | ❌ Not started | Justice | Brand finalization |

**Justice validates what River sells. A close without legal is a liability, not an asset.**

### THE PRE-CLOSE CHECKLIST

Before River makes a single outbound call:

- [ ] ✅ Card copy written and approved (done)
- [ ] ❌ Card design final (Iris)
- [ ] ❌ Print vendor selected (Nova)
- [ ] ❌ Cards printed (Nova)
- [ ] ❌ EDDM routes selected (Nova/Quinn)
- [ ] ❌ USPS compliance verified (Quinn/Derek/Piper)
- [ ] ❌ Voice Agent bilingual scripts complete (Nova, 16 scripts)
- [ ] ❌ Voice Agent booking flow working (Jordan)
- [ ] ❌ Voice Agent SMS confirmation working (Jordan)
- [ ] ❌ Call logging to Sheet working (Jordan)
- [ ] ❌ Email outreach templates ready (Nova/Iris, 8 industries)
- [ ] ❌ Service agreement template ready (Justice)
- [ ] ❌ Terms of service on website (Justice)
- [ ] ❌ Privacy policy on website (Justice)
- [ ] ❌ Payment flow tested end-to-end (Echo)
- [ ] ❌ Attribution tracking in place (Nova)

**River's success rate is proportional to how much of this list is done BEFORE the first call.**
Every unchecked box is a hole River has to talk around. Every checked box is a close waiting to happen.

### PARALLEL EXECUTION ORDER

```
WEEK 1 (NOW):
├── IRIS: Card design final → print-ready files
├── NOVA: Voice Agent scripts (16) → booking flow → SMS → logging
├── JUSTICE: Service agreement → ToS → Privacy policy
├── QUINN: EDDM compliance check → print specs
├── ECHO: Invoice template → payment flow testing
└── SAGE: Continue generating leads (100/day cron)

WEEK 2:
├── IRIS: Design approved → send to print vendor
├── NOVA: Attribution setup → email templates → outreach sequences
├── JUSTICE: Final review of contracts + ToS
├── QUINN: USPS route selection → compliance sign-off
├── ECHO: Revenue recognition → monthly billing setup
└── SAGE: Continue leads, begin outreach for top diamonds

WEEK 3:
├── NOVA: Drop cards (Tuesday-Wednesday)
├── RIVER: Begin consultations (only after checkmarks above)
├── SAGE: Continue leads
└── ALL: Monitor, iterate, fill gaps

NOTE: River does NOT start until the pre-close checklist has green checkmarks.
Sage can work ahead. Design, compliance, and operations must be BUILT first.
```

### VALIDATION GATES

- **Iris completes design → Quinn validates for USPS compliance → Nova sends to print**
- **Justice completes contracts → Echo validates pricing matches → River uses to close**
- **Nova completes Voice Agent → Jordan validates end-to-end → River can take inbound calls**
- **Echo completes payment flow → test with real card → River can accept money**

**Each gate must pass before the next phase begins. No skipping.**