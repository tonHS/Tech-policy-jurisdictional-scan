# Tech Policy Jurisdictional Scan — update instructions for Claude

This repo publishes a public GitHub Pages site (https://tonhs.github.io/Tech-policy-jurisdictional-scan/) covering the top tech and internet policy developments in Canada, the United States and the United Kingdom: new legislation and key soft law (guidance, regulator action, government announcements). Only the top items a busy policy or compliance professional needs. Sources cited and linked.

When Kate asks to "update the scan" (or similar), follow the routine below.

## Files

- `scan.json` — ALL content: `brief`, `compare` grid, `watch` list, `items`. Routine updates touch only this file.
- `index.html` — design and rendering. Do not edit for routine updates.
- `.nojekyll` — leave it.

## Update routine

1. **Check sources** for developments since `asOf`:
   - Canada: LEGISinfo / openparliament.ca (C-36, C-34, C-22, new bills), OPC, CRTC and Canadian Heritage (streaming/news), ISED (AI), Competition Bureau, Global Affairs (CUSMA).
   - US: Congress.gov (KIDS Act, AI preemption, privacy), White House and DOJ (AI task force), FTC (COPPA, TAKE IT DOWN, AI), CISA (CIRCIA final rule), USTR (digital trade), key states (California, Colorado, Texas, New York).
   - UK: bills.parliament.uk (Cyber Security and Resilience Bill, digital ID, King's Speech bills), DSIT, Ofcom (Online Safety Act, under-16 ban), CMA (digital markets), ICO / Information Commission (DUAA), IPO (copyright & AI), HMT (DST).
   - The Canadian Privacy Scan repo (tonHS/Privacy-and-AI-Reg-Scan) for Canadian privacy items that belong here too.
2. **Decide what belongs.** Top items only, across privacy, AI, online safety and kids, competition, cyber, digital trade and tax, internet and content law. Prefer primary sources; use firm or news summaries only when no primary source exists.
3. **Edit `scan.json`:** add or update items, move resolved `watch` entries into items, retire items older than about 12 months unless still live, rewrite the `brief` (2–4 points, each with sources), update `compare` cells if a country's status changed, set `asOf` and `checked` dates.
4. **Validate:** `python3 -m json.tool scan.json`; serve locally and confirm the page renders.
5. **Show Kate a short summary** of what was added, changed and removed, and wait for her OK before committing and pushing to `main`.

## Item schema (`items[]`)

| field | meaning |
|---|---|
| `id` | short unique slug |
| `date` / `dateText` | ISO date; optional display override |
| `type` | `legislation` · `regulation` · `enforcement` · `guidance` · `announcement` · `consultation` · `trade` |
| `jur` | `CA` · `US` · `UK`; `also` lists other countries involved; `sub` names a state or sub-jurisdiction |
| `topics` | `privacy` · `ai` · `safety` · `competition` · `cyber` · `trade` · `internet` |
| `priority` | `act` · `prepare` · `watch` · `context` |
| `title`, `what`, `why` | plain-language headline, what happened, why it matters |
| `track` | optional `{stages: [...], at: n}` for bills and phased rules |
| `expert` | specialist bullets: provisions, dates, citations |
| `cite`, `sources`, `checked` | citation line, `[label, url]` pairs (primary first), last-verified date |

`compare.rows[CA|US|UK]` holds one `[status, text]` per topic; status is `law`, `pending`, `patchwork`, `mixed`, `none`, `soft` or `friction`.

## Writing rules

- Plain language first; precision goes in `expert`.
- Never call a bill law before it is enacted, or say a law applies before it is in force.
- State scope limits; never round up a law's reach. If a detail can't be verified, leave it out or say it is unconfirmed.
- Paraphrase sources; any direct quote under 15 words.
- Keep the "AI-assisted" and "Not legal advice" footer notes.
