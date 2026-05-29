# Nova Packet — Conduit, Voice Agent Wiring
## Output: Updated /home/nemesis/voice-agent/agent.py

## CONTEXT
Voice agent runs at port 8443, uses Ollama (qwen3.5) for AI, Twilio for phone. Currently handles calls with scripts from batch-001-voice-agent-scripts.md. Needs wiring to Maton APIs for automation.

## MATON CONNECTIONS (all verified working)
- Google Calendar: ID `0d4a4ea5-f9ae-46a2-9c69-82b60effdbe5`
  - POST `https://api.maton.ai/v1/connections/0d4a4ea5-f9ae-46a2-9c69-82b60effdbe5/proxy`
  - Path: `/google-calendar/calendar/v3/calendars/primary/events`
  - Body: `{"summary": "TDA Consultation - {biz_name}", "start": {"dateTime": "..."}, "end": {"dateTime": "..."}}`

- Google Sheets: ID `06dd4428-14ed-433f-b279-90f0eea7f764`
  - Sheet ID: `1yGDvkbGUB0wrQ_TkXhNBbFjxZkvhN9MPLceRfmUmKKE`
  - POST to append rows to Call Log tab
  - Fields: timestamp, phone, business_name, industry, language, zip_code, outcome, notes

- Gmail: ID `49fe06fa-9683-452a-84b6-6fe0f2541cd8`
  - POST to send confirmation emails after booking

- Twilio SMS: ID `dce9c019-e277-4f68-957b-297349391bf0`
  - POST to send SMS confirmations (~$0.0079/msg)

## MATON API PATTERN
```
POST https://api.maton.ai/v1/connections/{connection_id}/proxy
Headers: Authorization: Bearer {MATON_API_KEY}
Body: {
  "method": "GET|POST|PUT",
  "path": "{service_api_path}",
  "body": { ... },
  "headers": { ... }
}
```

MATON_API_KEY is in /home/nemesis/.hermes/secrets/ (check there for the actual key)

## WHAT TO ADD TO agent.py
1. After every call: log to Google Sheets (timestamp, caller phone, business name, industry, language, ZIP, outcome)
2. After qualification: offer to book consultation
3. If they say yes: create Google Calendar event for next business day 10am
4. After booking: send SMS confirmation to caller via Twilio
5. After booking: send confirmation email via Gmail (nice-to-have)

## AGENT.py LOCATION
/home/nemesis/voice-agent/agent.py

Read it first, understand the structure, then add the Maton integrations. Don't break existing functionality.

## VOICE SCRIPTS REF
/home/nemesis/targeted-design-site/batch-001-voice-agent-scripts.md