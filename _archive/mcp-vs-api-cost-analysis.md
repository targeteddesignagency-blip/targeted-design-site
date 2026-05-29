# MCP vs API Cost Analysis & ROI for Targeted Design Agency

**Date:** May 12, 2026
**Purpose:** Determine whether to integrate Composio MCP (as recommended by Orgo/Nick) vs. building direct API integrations, and calculate ROI for each tool in the premium tier stack.

---

## 1. COMPOSIO MCP — Pricing & ROI

### Composio Pricing (Verified 2026-05-12)

| Tier | Tool Calls/Mo | Price | Overage | Support |
|---|---|---|---|---|
| Free | 20,000 | $0/mo | N/A | Community |
| "Ridiculously Cheap" | 200,000 | $29/mo | $0.299/1K | Email |
| "Serious Business" | 2,000,000 | $229/mo | $0.249/1K | Slack |

### What You Get (vs. Building Direct API Integrations)

| Integration | Direct API Dev Cost | Direct API Monthly Maint. | Composio Cost (Included) |
|---|---|---|---|
| Gmail (read/send/search) | ~$2,000 one-time | ~$50/mo (OAuth token refresh, API changes) | $0 (included in tier) |
| Google Calendar | ~$1,500 one-time | ~$30/mo | $0 (included) |
| Google Sheets | ~$1,000 one-time | ~$20/mo | $0 (included) |
| Slack | ~$1,200 one-time | ~$30/mo | $0 (included) |
| Notion | ~$800 one-time | ~$15/mo | $0 (included) |
| HubSpot CRM | ~$2,500 one-time | ~$50/mo | $0 (included) |
| QuickBooks | ~$3,000 one-time | ~$75/mo | $0 (included) |
| Twilio (SMS/Voice) | ~$1,500 one-time | ~$25/mo | $0 (included) |
| GitHub | ~$800 one-time | ~$10/mo | $0 (included) |
| **TOTAL (9 integrations)** | **~$14,300 one-time** | **~$305/mo** | **$29/mo (Pro)** |

**Direct API = $14,300 + $305/mo ongoing**
**Composio = $29/mo (Pro tier covers 200K calls, more than enough for 10 customers)**

**ROI: 10x cheaper in Year 1, 10.5x cheaper ongoing.**

### Key MCP Advantage: Auth

The single biggest cost center for direct API integration isn't the initial build — it's **authentication**. OAuth flows break constantly:
- Token expiration handling
- Scope changes (Google deprecates APIs quarterly)
- Refresh token revocation
- Multi-tenant credential management

Composio handles all auth centrally. Your agent never touches credentials. When Google changes their OAuth flow, Composio updates — you do nothing.

**Estimated auth maintenance savings: ~$200/mo per integration set.**

---

## 2. ORGO (Cloud Computer Hosting) — Estimated Cost

Orgo doesn't publicly list pricing (JS-rendered site, no static content). Based on Nick's video:

| Component | Estimate | Notes |
|---|---|---|
| Per-customer workspace | ~$50-100/mo | Isolated cloud computer per customer |
| MCP management layer | Included | Orgo manages agent instances |

**Alternative: Our current stack**
- Cloudflare Pages: $0 (free tier, unlimited bandwidth)
- Ollama-cloud (GLM-5.1): Token-based (charity budget — free tier exhausted)
- Voice agent (qwen3.5:cloud): Token-based

**Our advantage:** We don't need Orgo. Hermes Agent runs locally + Cloudflare deploys free. Orgo is for operators who can't self-host.

---

## 3. FULL STACK COMPARISON: Nick's Model vs. Ours

### Nick/Orgo Premium Tier ($5,000/mo customer)

| Tool | Nick's Cost | Our Cost | Notes |
|---|---|---|---|
| Agent framework | Hermes (free) | Hermes (free) | Same |
| Hosting | Orgo ($50-100/mo per customer) | Cloudflare Pages ($0) | **We save $50-100/mo** |
| App integrations | Composio Pro ($29/mo) | Composio Pro ($29/mo) | Same |
| Agent email | AgentMail (~$10/mo) | Composio includes email | **We save $10/mo** |
| Knowledge base | Obsidian (free) | Obsidian (free) | Same |
| CRM/Leads | HubSpot (varies) | Google Sheets (free) | **We save $20-50/mo** |
| Voice agent | Not mentioned | Maton + qwen3.5:tbd | **We add this** |
| EDDM (direct mail) | Not mentioned | USPS + local knowledge | **We add this** |
| **Total per customer** | **$89-139/mo** | **$29/mo** | **~75% cheaper to deliver** |

### Our Margins at Different Price Points

| Price Point | Our Cost/Mo | Gross Margin | Margin % |
|---|---|---|---|
| $150/mo (current) | $29 | $121 | 81% |
| $550/mo (current premium) | $29 | $521 | 95% |
| $2,000/mo (law firms) | $29 | $1,971 | 99% |
| $5,000/mo (Nick's price) | $29 | $4,971 | 99% |

**Key insight: At $5K/mo, Nick's cost is $89-139/mo per customer. Ours is $29/mo. Same revenue, 4x better margin.**

---

## 4. MCP vs API: DETAILED COMPARISON

| Dimension | MCP (Composio) | Direct API |
|---|---|---|
| **Setup time** | Minutes (connect, auth, done) | Weeks per integration |
| **Discovery** | Agent auto-discovers tools | Developer hardcodes endpoints |
| **Auth** | Server-managed (never touches credentials) | You manage OAuth, tokens, refresh |
| **Maintenance** | Provider updates (zero cost to you) | You update when APIs change |
| **Scope** | 250+ integrations for $29/mo | Each integration = $1-3K build + $20-75/mo |
| **Reliability** | Provider handles retries, rate limits | You build retry logic, rate limiting |
| **New tools** | Instantly available | Weeks of development |
| **Lock-in risk** | Medium (vendor dependency) | Low (you own the code) |
| **Customization** | Limited to provider's tool definitions | Unlimited |
| **Observability** | Built-in logging/dashboards | You build monitoring |

---

## 5. RECOMMENDATION

### Phase 1: Now (Free Tier — $0/mo)
- **Composio Free** (20K tool calls/mo) for internal use only
- Covers our CRM (Sheets), calendar, email operations
- Zero cost, zero risk

### Phase 2: Premium Tier Launch ($2K-5K/mo customers)
- **Composio Pro** ($29/mo) — 200K tool calls covers 5-10 customers easily
- Each customer gets: Gmail, Calendar, Sheets, Slack, CRM integration
- **Break-even:** 1 customer at $2K/mo covers 69 months of Composio ($29/mo)

### Phase 3: Scale (20+ customers)
- **Composio Serious Business** ($229/mo) — 2M tool calls
- Still orders of magnitude cheaper than building direct API integrations

### What NOT to use
- **Orgo hosting** — unnecessary overhead. We run on Cloudflare + local. Our infra is free; Orgo's adds $50-100/mo per customer.
- **AgentMail** — Composio includes email tool; no need for separate service.

---

## 6. BREAKEVEN ANALYSIS

### Scenario: Premium Tier at $2,500/mo per customer

| Customers | Revenue/mo | Composio Cost | Marginal Cost | Profit/mo |
|---|---|---|---|---|
| 1 | $2,500 | $29 | $29 | $2,471 |
| 5 | $12,500 | $29 | $29 | $12,471 |
| 10 | $25,000 | $29 | $29 | $24,971 |
| 20 | $50,000 | $229 | $229 | $49,771 |

**First customer pays for Composio for 86 months. That's 7+ years of integration coverage from a single $2.5K/mo sale.**

### vs. Direct API Build

| Approach | Upfront | Monthly | 12-Month Total | 3-Year Total |
|---|---|---|---|---|
| Composio (Pro) | $0 | $29 | $348 | $1,044 |
| Direct API (9 integrations) | $14,300 | $305 | $17,960 | $25,260 |
| **Savings** | **$14,300** | **$276/mo** | **$17,612** | **$24,216** |

---

## 7. ACTION ITEMS

1. **Sign up for Composio Free tier** — 20K calls/mo, zero cost
2. **Test MCP connection with Hermes Agent** — verify Gmail + Sheets integration
3. **Build Obsidian template** for customer knowledge bases (free)
4. **Create premium tier landing page** — "Unlimited AI Employees" positioning
5. **Document 48-hour onboarding SLA** — first agent live within 2 days
6. **Set up watchdog/alert system** — agents email us when things break (free)
7. **Wait on Orgo** — our Cloudflare + local stack works; no need to add $50-100/mo overhead

---

*Analysis based on: Composio pricing page (verified 2026-05-12), Orgo video transcript (Greg Isenberg + Nick), current Targeted Design Agency infrastructure costs.*