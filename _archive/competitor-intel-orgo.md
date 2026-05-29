# Orgo (Nick) Business Framework - Competitor Intelligence
**Source:** Greg Isenberg Podcast featuring Nick from Orgo (48 min)
**Date Analyzed:** May 12, 2026
**Relevance:** Directly applicable to Targeted Design Agency's solo AI agent business model

---

## 1. BUSINESS MODEL / OFFER STRUCTURE

### Pricing
- **$5,000/month** per customer (Nick's current offer)
- Position as premium - "Hermes agents can charge 10K/month" vs "OpenClaw is commoditized at 5K"

### Packaging
- **Unlimited agents** (customers typically only need 1-3)
- **Unlimited usage/tokens** (never mention token limits to customers)
- **Unlimited monitoring, support, security**
- **Ongoing changes/improvements** included

### Key Positioning Insights
| Do | Don't |
|---|---|
| Sell an "AI employee" | Sell an "AI agent" |
| Focus on business outcomes (revenue generated) | Focus on time saved |
| Create abundance in offer | Mention tokens/credits/usage limits |
| Remove all friction | Make customer think about infrastructure |

> **Critical Insight:** Customers don't actually need unlimited agents. They might think they need 5-100, but 1-2 properly configured agents delivers most value. This is how you control costs while offering "unlimited."

---

## 2. TARGET INDUSTRIES

### Recommended Verticals (Low Regulatory Burden)
- Marketing agencies
- Law firms
- Insurance agencies
- Manufacturers
- Wholesalers
- Real estate agencies

### Avoid (Initially)
- Healthcare (HIPAA/regulatory burden)
- Finance (compliance red tape)

### Niche Strategy
- Start broad, then niche down based on market pull
- Examples: "Real estate agencies in Florida" or "Commercial real estate agencies"
- Common executive problems across all verticals:
  - Too many emails
  - Too many meetings
  - Too many follow-ups
  - Too many open loops
  - Context switching across projects/people

---

## 3. ONBOARDING PROCESS (Zero to Live in 30 Days)

### Week 1: Setup & First Agent
- **First agent live within 48 hours** (critical for momentum)
- Use agents to build agents (Claude Code installs Hermes automatically)
- Set up Orgo workspace per customer

### Week 2-4: Iteration & Expansion
- **Trello board** for customer-facing project management:
  - Backlog → To-Do → Doing → Done
  - Customer drags requests into To-Do
- **Limit 1-2 requests per 48 hours** (prevent scope creep)
- **Granola** for meeting notes → auto-sync to Trello
- **Loom** for video updates to customers (send updates at 2am, throughout day)

### Tools for Onboarding Flow
| Tool | Purpose |
|---|---|
| Granola | Meeting notes with MCP |
| Trello | Customer-facing request board |
| Loom | Async video updates |
| Calendly | Booking calls |
| Superhuman | Email management (keyboard shortcuts, speed) |
| Asana | Internal project tracking |

---

## 4. TECH STACK (Nick's Exact Setup)

### Agent Framework
| Tool | Why Nick Uses It |
|---|---|
| **Hermes Agent** | Doesn't break, self-evolving, can switch models anytime |
| Claude Code | Best desktop app, most generous limits, simplest |
| CodeX | Good alternative |
| OpenClaw | "Commoditized" - less self-evolving |

### Hosting/Infrastructure
- **Orgo** (Nick's company - biased recommendation but detailed reasoning):
  - Gives agents a full computer to live in (not headless VPS)
  - Isolated cloud computers per customer
  - Can delete/recreate in under 1 second
  - One workspace per customer with multiple agents
  - Orgo MCP allows your agent to manage customer agents remotely
  - **Why not Mac Minis?** Hardware failures, updates, can't remote debug, security blast radius

### Agent Tools (Install for Every Agent)
| Tool | Purpose | One-liner |
|---|---|---|
| **Composio** | One MCP connector to thousands of apps (Gmail, Slack, Notion, GitHub) | Handles authentication + tool calling - biggest time sink eliminated |
| **Agent Mail** | Give each agent their own email address | "Mia needs her own email" - makes it feel like a real employee |
| **Obsidian** | Knowledge base / second brain in markdown | Perfect context over people, projects, workflows - agents never forget |

### Model Recommendations (as of recording)
| Model | Use Case |
|---|---|
| **GPT-5.5** | Default for Hermes/OpenClaw - efficient with tool calls, doesn't eat tokens |
| GLM-5.1 (ZAI) | Lighter tasks, open source, affordable |
| Kimi | Close second for open source |
| Opus 4.7 | Long-horizon coding tasks (can have agent connect to Claude Code) |

### Memory/Context Layers (MCPs for Agent Setup)
| MCP | Purpose |
|---|---|
| Perplexity MCP | Up-to-date docs and best practices |
| Exa AI MCP | Real-time web search |
| Context 7 MCP | GitHub docs (Hermes, etc.) |
| XMCP (Twitter) | Community setups and configs |

> **Pro Tip:** Spawn 5 sub-agents, each with one MCP, then aggregate findings to main agent for best practices.

---

## 5. SALES STRATEGY

### Customer Acquisition
1. **Content is king in 2026** - most leveraged activity
   - Use AI to automate research, editing, production
   - Content helps: get customers, get on podcasts, hire talent
2. **Never sell cold** - warm leads convert fastest
   - Start free if needed for case studies + referrals
3. **Go vertical** - you're not selling Claude Code, you're selling industry-specific solutions

### Sales Conversation Framework
- Talk to **executives/decision makers** directly
- They have universal problems (emails, meetings, follow-ups, open loops)
- Show demo in Orgo playground - let them see agent controlling computer in real-time
- Visual demos "light people up" more than explanations

### Pricing Psychology
- Unlimited framing removes friction
- Customers don't want to think about tokens, models, infrastructure
- They want a "digital employee that knows their business and gets better every week"

---

## 6. COMMON MISTAKES / PITFALLS

### What Nick Warns Against
| Mistake | Solution |
|---|---|
| **Scope creep** | Limit 1-2 requests per 48 hours via Trello |
| **Mentioning tokens/credits** | Never use these words - ruins the magic |
| **Starting in healthcare/finance** | Too much regulatory burden initially |
| **Using Mac Minis for hosting** | Hardware failures, can't remote debug, security risks |
| **Gateway crashes (OpenClaw)** | Set up watchdog that auto-restores gateways |
| **No observability** | Have agents email you when cron jobs fail or skills break |
| **Trying to niche too early** | Diverge first, test multiple verticals, then converge |
| **Cold calling** | Build content, get warm leads, start free for case studies |

### Reliability Must-Haves
1. **Watchdog** - Auto-restore crashed gateways
2. **Alerts** - Agents email you when something breaks (before customer notices)
3. **Sandbox isolation** - Cloud computers prevent blast radius

---

## 7. ACTIONABLE INTELLIGENCE FOR TARGETED DESIGN AGENCY

### Current Position vs. Nick's Model
| Aspect | Targeted Design | Nick/Orgo | Gap/Opportunity |
|---|---|---|---|
| **Price** | $150-550/mo | $5,000/mo | 10x pricing headroom if positioned as "AI employee" |
| **Offer** | EDDM + bilingual voice agents | Unlimited AI employees | Consider unlimited framing |
| **Vertical** | Hispanic SMBs in San Antonio | Multiple verticals | Your niche is stronger - lean into it |
| **Tech** | Hermes Agent | Hermes + Orgo + Composio | Add Composio for app integrations |

### Immediate Actions
1. **Reframe offer** - "Unlimited AI employees" vs. per-agent pricing
2. **Add Composio** - One connector for all app integrations (Gmail, Slack, etc.)
3. **Build Obsidian vaults** per customer - structured knowledge = better agents
4. **Set up watchdog** - Auto-restore gateways before customer notices issues
5. **Create alert system** - Agents email you when things break
6. **Use Orgo or similar** - Cloud computers vs. local hosting for reliability
7. **Content strategy** - Document your builds, post on social, get warm inbound

### Pricing Strategy Recommendation
- Keep entry tier at $150-550/mo for Hispanic SMBs (price-sensitive market)
- Create premium tier at $2,000-5,000/mo for law firms, agencies, manufacturers
- Premium includes: Unlimited agents, dedicated Orgo workspace, Composio integrations, Obsidian knowledge base

### Competitive Advantages You Have
- **Bilingual capability** - Nick doesn't mention this at all
- **EDDM integration** - Physical + digital is unique
- **Geographic focus** - Deep local knowledge vs. Nick's broad approach
- **Lower price point** - Can capture market Nick ignores

### What to Copy Directly
1. 48-hour first agent deployment SLA
2. Trello board for customer requests (limits scope creep)
3. Loom updates for async communication
4. "AI employee" positioning (not "AI agent")
5. Outcome-based selling (revenue, not time saved)
6. Obsidian vaults for each customer's agent memory

---

## 8. TIMESTAMPS FOR KEY SECTIONS

| Timestamp | Topic |
|---|---|
| 00:00-02:50 | Intro + value proposition |
| 02:50-06:40 | Offer structure ($5K/mo, unlimited framing) |
| 06:40-12:50 | Target industries + niche strategy |
| 12:50-17:50 | Executive problems + content strategy |
| 17:50-27:30 | Full tech stack breakdown |
| 27:30-30:20 | Nick's exact tool choices + why |
| 30:20-38:50 | Orgo demo + cloud computer setup |
| 38:50-44:00 | MCPs for context layers |
| 44:00-46:10 | Watchdogs, alerts, reliability |
| 46:10-end | Closing thoughts |

---

## 9. QUOTES WORTH STEALING

> "You're selling an AI employee. You're not selling an AI agent."

> "The customer doesn't touch tokens or models or any infrastructure. They just get a digital employee that knows their business and it gets better every single week."

> "The point is not that the customer needs infinite agents. They don't need infinite tokens or infinite computers. Most customers, they just need one, maybe two, maybe three."

> "The minute that things start to break, the business owners become so reliant, so dependent on these agents that if something does start to break, it is very painful for them."

> "Content is king in 2026. It's the most leveraged thing you can do."

> "Use agents to build agents. If you're confused on how to set something up, have your agent do it."

---

**Document created for:** Targeted Design Agency
**Location:** `/home/nemesis/targeted-design-site/competitor-intel-orgo.md`
**Next steps:** Review pricing tiers, implement Composio, build Obsidian templates, set up watchdog monitoring
