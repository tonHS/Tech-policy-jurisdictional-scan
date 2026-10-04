# Sources — Tech Policy Jurisdictional Scan

A record of where this scan's information comes from. It has three parts:

1. **Monitored sources**: where each update looks for new developments.
2. **Cited in the current edition**: every source linked on the live page (brief, comparison grid and items), rebuilt from `scan.json` by `python3 tools/sources.py`.
3. **Update log**: one row per update, recording what was checked and what changed.

Older editions' sources stay in the git history of this file.

## 1. Monitored sources

### Canada

| Source | What to check |
|---|---|
| [LEGISinfo](https://www.parl.ca/legisinfo) / [openparliament.ca](https://openparliament.ca) | Bill stages: C-36, C-34, C-22, new tech bills |
| [Office of the Privacy Commissioner](https://www.priv.gc.ca) | Findings, guidance, advice to Parliament |
| [CRTC](https://crtc.gc.ca) and [Canadian Heritage](https://www.canada.ca/en/canadian-heritage.html) | Online Streaming Act, Online News Act, online harms |
| [ISED](https://ised-isde.canada.ca) | AI policy and consultations |
| [Competition Bureau](https://competition-bureau.canada.ca) | Digital markets, algorithmic pricing |
| [Global Affairs Canada](https://www.international.gc.ca) | CUSMA review, digital trade |
| [Canada Gazette](https://gazette.gc.ca) | Regulations, policy directions, coming-into-force orders |
| [Canadian Privacy Scan](https://tonhs.github.io/Privacy-and-AI-Reg-Scan/) | Canadian privacy items worth carrying over |

### United States

| Source | What to check |
|---|---|
| [Congress.gov](https://www.congress.gov) | KIDS Act / KOSA, AI preemption, federal privacy bills |
| [White House](https://www.whitehouse.gov) and [DOJ](https://www.justice.gov) | AI executive orders and framework; AI Litigation Task Force; antitrust cases |
| [FTC](https://www.ftc.gov) | COPPA, TAKE IT DOWN Act, AI and data enforcement |
| [CISA](https://www.cisa.gov) | CIRCIA final rule, cyber directives |
| [USTR](https://ustr.gov) | Digital trade, digital services taxes, CUSMA |
| State legislatures | California, Colorado, Texas, New York and others for AI, privacy and kids' online safety laws |

### United Kingdom

| Source | What to check |
|---|---|
| [UK Parliament Bills](https://bills.parliament.uk) | Cyber Security and Resilience Bill, King's Speech bills |
| [DSIT](https://www.gov.uk/government/organisations/department-for-science-innovation-and-technology) | Tech policy announcements, under-16 ban, AI |
| [Ofcom](https://www.ofcom.org.uk/online-safety) | Online Safety Act enforcement and codes |
| [CMA](https://www.gov.uk/government/organisations/competition-and-markets-authority) | Digital markets (SMS) decisions and conduct requirements |
| [ICO / Information Commission](https://ico.org.uk) | Data (Use and Access) Act guidance and enforcement |
| [Intellectual Property Office](https://www.gov.uk/government/organisations/intellectual-property-office) | Copyright and AI |
| [HM Treasury](https://www.gov.uk/government/organisations/hm-treasury) | Digital services tax |

### News (use to spot developments; cite only when no primary source exists)

| Source | Notes |
|---|---|
| [The Globe and Mail](https://www.theglobeandmail.com) | Canadian technology, politics and business. Paywalled. |
| [The Washington Post](https://www.washingtonpost.com) | US technology and policy. Paywalled. |

### Secondary analysis (used when no primary source is published)

Law firm bulletins, IAPP, Tech Policy Press, Michael Geist's blog, Congressional Research Service reports. Prefer the government or regulator's own document when it exists.

## 2. Cited in the current edition

<!-- cited:start -->
_Generated from `scan.json` (current to 2026-10-04). Do not edit by hand._

### Monthly brief

- **Kids are being moved off social media.**
  - [UK announcement (A&O Shearman)](https://www.aoshearman.com/en/insights/ao-shearman-on-data/uk-government-announces-social-media-ban-and-other-measures-to-protect-children-online)
  - [Canada Bill C-34](https://www.canada.ca/en/canadian-heritage/news/2026/06/government-of-canada-introduces-legislation-to-combat-online-harms-particularly-those-impacting-children.html)
  - [US KIDS Act](https://techpolicy.press/bipartisan-smorgasbord-of-childrens-online-safety-legislation-passes-the-house)
- **None of the three has a general AI law, and Washington wants to keep it that way.**
  - [White House AI framework (Jenner)](https://www.jenner.com/en/news-insights/client-alerts/takeaways-from-the-white-houses-framework-for-artificial-intelligence)
  - [King's Speech 2026 (DLA Piper)](https://privacymatters.dlapiper.com/2026/05/uk-the-kings-speech-2026-cybersecurity-at-the-forefront/)
- **Tech rules are now trade issues.**
  - [CUSMA review (Blakes)](https://www.blakes.com/insights/u-s-declines-to-renew-cusma-at-first-joint-review-what-businesses-need-to-know/)
  - [Streaming reset (CP24)](https://www.cp24.com/news/canada/2026/07/29/ottawa-to-eliminate-streamers-cancon-payments-provide-government-funding-instead/)
- **Cyber incident reporting is arriving everywhere.**
  - [Canada C-8](https://openparliament.ca/bills/45-1/C-8/)
  - [UK bill tracker](https://bills.parliament.uk/bills/4035)
  - [US CIRCIA status (Covington)](https://www.cov.com/-/media/files/corporate/publications/2026/09/cisa-town-halls-signal-key-cyber-rule-changes-ahead.pdf)

### Where each country stands (comparison grid)

- **CA · Privacy & data**: PIPEDA in force; replacement bill C-36 at second reading
  - [Bill C-36 (openparliament.ca)](https://openparliament.ca/bills/45-1/C-36/)
- **CA · AI**: No AI law; national strategy and transparency consultation
  - [ISED consultation](https://www.canada.ca/en/innovation-science-economic-development/news/2026/07/government-of-canada-launches-public-consultation-on-ai-transparency.html)
- **CA · Online safety & kids**: C-34 Safe Social Media Act at second reading
  - [Bill C-34 backgrounder](https://www.canada.ca/en/canadian-heritage/news/2026/06/government-of-canada-introduces-legislation-to-combat-online-harms-particularly-those-impacting-children.html)
- **CA · Competition & digital markets**: Competition Act; Bureau studying algorithmic pricing
  - [Competition Bureau report](https://www.canada.ca/en/competition-bureau/news/2026/01/competition-bureau-report-highlights-public-feedback-on-algorithmic-pricing-and-competition.html)
- **CA · Cybersecurity**: Critical Cyber Systems Protection Act passed June 2026
  - [Bill C-8 (openparliament.ca)](https://openparliament.ca/bills/45-1/C-8/)
- **CA · Digital trade & tax**: CUSMA on annual review; streaming payments being scrapped
  - [CUSMA review (Blakes)](https://www.blakes.com/insights/u-s-declines-to-renew-cusma-at-first-joint-review-what-businesses-need-to-know/)
  - [Streaming reset (CP24)](https://www.cp24.com/news/canada/2026/07/29/ottawa-to-eliminate-streamers-cancon-payments-provide-government-funding-instead/)
- **US · Privacy & data**: No federal law; about 20 state laws in force
  - [MultiState](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026)
- **US · AI**: State laws (CO, CA, TX); federal push to preempt them
  - [White House framework (Jenner)](https://www.jenner.com/en/news-insights/client-alerts/takeaways-from-the-white-houses-framework-for-artificial-intelligence)
  - [Colorado rewrite (Ballard Spahr)](https://www.consumerfinancemonitor.com/2026/05/12/colorado-rewrites-its-landmark-ai-law-unpacking-sb-26-189-and-what-it-means-for-businesses/)
- **US · Online safety & kids**: TAKE IT DOWN Act in force; KIDS Act passed House
  - [FTC](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act)
  - [KIDS Act (Tech Policy Press)](https://techpolicy.press/bipartisan-smorgasbord-of-childrens-online-safety-legislation-passes-the-house)
- **US · Competition & digital markets**: Antitrust law enforced through courts; Google search remedies under appeal by both sides
  - [Google appeal (PYMNTS/CPI)](https://www.pymnts.com/cpi-posts/us-justice-department-states-challenge-google-antitrust-remedies-in-appeal/)
- **US · Cybersecurity**: CIRCIA reporting rule overdue
  - [Covington](https://www.cov.com/-/media/files/corporate/publications/2026/09/cisa-town-halls-signal-key-cyber-rule-changes-ahead.pdf)
- **US · Digital trade & tax**: Using tariffs against foreign tech rules and taxes
  - [UK DST threat (Morningstar)](https://www.morningstar.co.uk/uk/news/AN_1776990152554627800/trump-threatens-big-tariff-on-uk-over-digital-tax-on-us-tech-firms.aspx)
  - [CUSMA review (Blakes)](https://www.blakes.com/insights/u-s-declines-to-renew-cusma-at-first-joint-review-what-businesses-need-to-know/)
- **UK · Privacy & data**: UK GDPR amended by Data (Use and Access) Act, phasing in
  - [Kennedys](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-data-use-and-access-act-2025-commencement-dates-and-planned-guidance-for-2026)
- **UK · AI**: No AI bill; sector regulators and sandboxes
  - [King's Speech (DLA Piper)](https://privacymatters.dlapiper.com/2026/05/uk-the-kings-speech-2026-cybersecurity-at-the-forefront/)
- **UK · Online safety & kids**: Online Safety Act enforced; under-16 ban coming 2027
  - [Ofcom](https://ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery)
  - [Under-16 ban (A&O Shearman)](https://www.aoshearman.com/en/insights/ao-shearman-on-data/uk-government-announces-social-media-ban-and-other-measures-to-protect-children-online)
- **UK · Competition & digital markets**: DMCC Act: CMA has imposed first conduct requirements
  - [CMA case page](https://www.gov.uk/cma-cases/sms-investigation-into-googles-general-search-and-search-advertising-services)
- **UK · Cybersecurity**: Cyber Security and Resilience Bill in the Lords
  - [UK Parliament](https://bills.parliament.uk/bills/4035)
- **UK · Digital trade & tax**: 2% DST under US tariff threat
  - [Morningstar](https://www.morningstar.co.uk/uk/news/AN_1776990152554627800/trump-threatens-big-tariff-on-uk-over-digital-tax-on-us-tech-firms.aspx)

### Items

- **UK Cyber Security and Resilience Bill reaches final stages in the Lords** · UK · 2026-09-16 · last checked 2026-10-04
  - Citation: Cyber Security and Resilience (Network and Information Systems) Bill (DSIT).
  - [UK Parliament bill page](https://bills.parliament.uk/bills/4035)
  - [DLA Piper on King's Speech](https://privacymatters.dlapiper.com/2026/05/uk-the-kings-speech-2026-cybersecurity-at-the-forefront/)
- **US critical infrastructure cyber reporting rule is overdue but close** · US · 2026-09-04 · last checked 2026-10-04
  - Citation: 6 U.S.C. § 681 et seq. (CIRCIA).
  - [Covington (Sept. 2026)](https://www.cov.com/-/media/files/corporate/publications/2026/09/cisa-town-halls-signal-key-cyber-rule-changes-ahead.pdf)
  - [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cisa-plans-to-finalize-cyber-incident-reporting-regulations-in-september-2026)
- **Canada to scrap streamers' Canadian-content payments** · CA · 2026-07-29 · last checked 2026-10-04
  - Citation: Online Streaming Act, S.C. 2023, c. 8.
  - [CP24 / Canadian Press](https://www.cp24.com/news/canada/2026/07/29/ottawa-to-eliminate-streamers-cancon-payments-provide-government-funding-instead/)
  - [Michael Geist](https://www.michaelgeist.ca/2026/07/starting-over-court-filing-confirms-the-crtcs-streamer-contribution-decisions-are-dead-with-a-full-online-streaming-act-reset-to-come/)
  - [CRS report](https://www.everycrsreport.com/files/2026-07-23_IN12716_1b3d55784138785dd6e8f61dd7b211036ab7d33a.html)
- **Canada's AI approach: a national strategy and a transparency consultation, but no AI law** · CA · 2026-07-23 · last checked 2026-10-04
  - Citation: ISED, AI transparency consultation (2026); National AI Strategy (June 4, 2026).
  - [ISED consultation](https://www.canada.ca/en/innovation-science-economic-development/news/2026/07/government-of-canada-launches-public-consultation-on-ai-transparency.html)
  - [Gowling WLG on strategy](https://gowlingwlg.com/en/insights-resources/articles/2026/canada-launches-ai-for-all-national-artificial-intelligence-strategy)
- **US declines to renew CUSMA; digital rules are part of the dispute** · CA + US · 2026-07-01 · last checked 2026-10-04
  - Citation: CUSMA/USMCA Art. 34.7 joint review (July 1, 2026).
  - [Blakes](https://www.blakes.com/insights/u-s-declines-to-renew-cusma-at-first-joint-review-what-businesses-need-to-know/)
  - [MPA on US concerns](https://www.mpamag.com/ca/news/general/cusma-deadline-now-in-doubt-as-july-1-looms/571211)
- **US House passes KIDS Act children's online safety package** · US · 2026-06-29 · last checked 2026-10-04
  - Citation: Kids Internet and Digital Safety Act, H.R. 7757 (119th Cong.), passed House June 29, 2026.
  - [Tech Policy Press](https://techpolicy.press/bipartisan-smorgasbord-of-childrens-online-safety-legislation-passes-the-house)
  - [IAPP on scope](https://iapp.org/news/a/unpacking-the-scope-of-the-kids-act)
- **UK data law changes are phasing in; a complaints procedure was due in June** · UK · 2026-06-19 · last checked 2026-10-04
  - Citation: Data (Use and Access) Act 2025, c. 18.
  - [Kennedys commencement guide](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-data-use-and-access-act-2025-commencement-dates-and-planned-guidance-for-2026)
  - [Mayer Brown on complaints](https://www.mayerbrown.com/zh-hans/insights/publications/2026/02/preparing-for-the-data-use-and-access-act-2025-upcoming-complaints-procedure-requirement)
- **Canada's lawful access bill C-22 is in the Senate** · CA · 2026-06-18 · last checked 2026-10-04
  - Citation: Bill C-22, Lawful Access Act, 2026.
  - [OPC submission](https://www.priv.gc.ca/en/opc-actions-and-decisions/advice-to-parliament/2026/parl_260526/)
  - [openparliament.ca](https://openparliament.ca/bills/45-1/C-22/)
- **UK competition regulator imposes first digital markets rules on Google search** · UK · 2026-06-17 · last checked 2026-10-04
  - Citation: Digital Markets, Competition and Consumers Act 2024, Part 1.
  - [CMA case page](https://www.gov.uk/cma-cases/sms-investigation-into-googles-general-search-and-search-advertising-services)
  - [Kennedys analysis](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-uk-digital-markets-regime-in-action-the-cma-s-first-conduct-requirements-for-google-and-commitments-for-apple-and-google-mobile-platforms)
- **UK will ban under-16s from social media, starting spring 2027** · UK · 2026-06-15 · last checked 2026-10-04
  - Citation: UK government announcement, June 15, 2026.
  - [A&O Shearman summary](https://www.aoshearman.com/en/insights/ao-shearman-on-data/uk-government-announces-social-media-ban-and-other-measures-to-protect-children-online)
  - [WSGR summary](https://www.wsgrdataadvisor.com/2026/06/uk-announces-social-media-ban-and-broader-online-restrictions-for-users-under-16/)
- **Canada's Bill C-36 would replace PIPEDA with a tougher privacy law** · CA · 2026-06-15 · last checked 2026-10-04
  - Citation: Bill C-36, 45th Parl., 1st Sess. First reading June 15, 2026.
  - [openparliament.ca](https://openparliament.ca/bills/45-1/C-36/)
  - [Canadian Privacy Scan (detail)](https://tonhs.github.io/Privacy-and-AI-Reg-Scan/)
- **Canada's critical infrastructure cyber law receives Royal Assent** · CA · 2026-06-15 · last checked 2026-10-04
  - Citation: S.C. 2026, c. 9 (former Bill C-8).
  - [openparliament.ca](https://openparliament.ca/bills/45-1/C-8/)
- **Canada's Bill C-34 would restrict under-16 accounts and regulate AI chatbots** · CA · 2026-06-10 · last checked 2026-10-04
  - Citation: Bill C-34, 45th Parl., 1st Sess. Introduced June 10, 2026.
  - [Government backgrounder](https://www.canada.ca/en/canadian-heritage/news/2026/06/government-of-canada-introduces-legislation-to-combat-online-harms-particularly-those-impacting-children.html)
  - [openparliament.ca](https://openparliament.ca/bills/45-1/C-34/)
- **TAKE IT DOWN Act: platforms must remove intimate images within 48 hours** · US · 2026-05-19 · last checked 2026-10-04
  - Citation: TAKE IT DOWN Act, Pub. L. 119-12 (2025).
  - [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act)
- **UK King's Speech: digital ID, police facial recognition rules and AI sandboxes, but no AI bill** · UK · 2026-05-13 · last checked 2026-10-04
  - Citation: King's Speech, May 13, 2026.
  - [DLA Piper](https://privacymatters.dlapiper.com/2026/05/uk-the-kings-speech-2026-cybersecurity-at-the-forefront/)
- **Colorado rewrites its AI law, which now takes effect January 2027** · US (Colorado) · 2026-05-12 · last checked 2026-10-04
  - Citation: Colorado SB 26-189.
  - [Consumer Finance Monitor (Ballard Spahr)](https://www.consumerfinancemonitor.com/2026/05/12/colorado-rewrites-its-landmark-ai-law-unpacking-sb-26-189-and-what-it-means-for-businesses/)
  - [Venable](https://www.venable.com/insights/publications/2026/07/colorados-sb26189-sets-new-rules-for-ai)
- **Canadian privacy regulators find OpenAI broke privacy law in building ChatGPT** · CA · 2026-05-06 · last checked 2026-10-04
  - Citation: Joint investigation of OpenAI OpCo, LLC (May 6, 2026).
  - [OPC statement](https://www.priv.gc.ca/en/opc-news/speeches-and-statements/2026/s-d_260506/)
- **US threatens tariffs over the UK's digital services tax** · UK + US · 2026-04-24 · last checked 2026-10-04
  - Citation: Finance Act 2020, Part 2 (UK DST).
  - [Morningstar / Reuters](https://www.morningstar.co.uk/uk/news/AN_1776990152554627800/trump-threatens-big-tariff-on-uk-over-digital-tax-on-us-tech-firms.aspx)
  - [CSIS on the Tech Prosperity Deal](https://www.csis.org/analysis/us-uk-trade-and-tech-agreements-update-after-state-visit)
- **Updated COPPA rule now fully in force** · US · 2026-04-22 · last checked 2026-10-04
  - Citation: 16 C.F.R. Part 312, as amended (2025); compliance date April 22, 2026.
  - [Davis Polk](https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect)
- **UK shelves plan to let AI firms train on copyrighted work by default** · UK · 2026-03-23 · last checked 2026-10-04
  - Citation: UK Government report on copyright and AI, March 23, 2026.
  - [Mishcon de Reya summary](https://www.mishcon.com/news/copyright-and-ai-the-uk-governments-report)
- **White House pushes to override state AI laws with one national standard** · US · 2026-03-20 · last checked 2026-10-04
  - Citation: E.O. 14365 (Dec. 11, 2025); White House national AI legislative framework (Mar. 20, 2026).
  - [Jenner & Block on the framework](https://www.jenner.com/en/news-insights/client-alerts/takeaways-from-the-white-houses-framework-for-artificial-intelligence)
  - [Ropes & Gray on preemption limits](https://www.ropesgray.com/en/insights/alerts/2026/03/examining-the-landscape-and-limitations-of-the-federal-push-to-override-state-ai-regulation)
  - [BakerHostetler on DOJ task force](https://www.bakerlaw.com/insights/navigating-the-emerging-federal-state-ai-showdown-doj-establishes-ai-litigation-task-force/)
- **Competition Bureau reports on algorithmic pricing** · CA · 2026-01-22 · last checked 2026-10-04
  - Citation: Competition Bureau, What We Heard: Algorithmic Pricing and Competition (Jan. 22, 2026).
  - [Competition Bureau](https://www.canada.ca/en/competition-bureau/news/2026/01/competition-bureau-report-highlights-public-feedback-on-algorithmic-pricing-and-competition.html)
- **Ofcom is enforcing the Online Safety Act, including against AI features** · UK · Jan–May 2026 · last checked 2026-10-04
  - Citation: Online Safety Act 2023; Ofcom investigation into X (Jan. 12, 2026).
  - [Ofcom: X/Grok investigation](https://ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery)
  - [Linklaters roundup](https://techinsights.linklaters.com/post/102n7pm/the-uks-online-safety-act-heats-up-fines-battlelines-and-even-more-regulatio)
- **State AI rules now in force: frontier model transparency and companion chatbots** · US (States) · 2026-01-01 · last checked 2026-10-04
  - Citation: Cal. SB 53 (2025); Cal. SB 243 (2025); Tex. HB 149 (TRAIGA).
  - [Perkins Coie on California AI bills](https://legacy.perkinscoie.com/insights/update/california-governor-newsom-signs-several-ai-bills-vetoes-three)
  - [Hunton: laws effective January 2026](https://www.hunton.com/privacy-and-information-security-law/new-u-s-state-privacy-social-media-and-ai-laws-take-effect-in-january-2026)
- **Three more US state privacy laws took effect, bringing the total to about 20** · US (States) · 2026-01-01 · last checked 2026-10-04
  - Citation: Ind. SB 5; Ky. HB 15; R.I. HB 7787/SB 2500.
  - [MultiState](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026)

_25 items, 44 unique source links._
<!-- cited:end -->

## 3. Update log

| Date | Checked | Added | Changed | Removed |
|---|---|---|---|---|
| 2026-10-04 | First edition. Federal and UK parliaments, Ofcom, CMA, FTC, CISA, White House framework, state AI laws, CUSMA review, CRTC/streaming, Canadian Privacy Scan items | 25 items, comparison grid, brief | Comparison grid: source links added to every cell; US competition cell now reflects Google search remedies appeal | — |
