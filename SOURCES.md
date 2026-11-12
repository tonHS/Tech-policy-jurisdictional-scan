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
| [Canadian Centre for Cyber Security](https://www.cyber.gc.ca) | Critical alerts and national cyber statements |
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
_Generated from `scan.json` (current to 2026-11-12). Do not edit by hand._

### Monthly brief

- **A new US Congress changes the odds.**
  - [IAPP](https://iapp.org/news/a/democratic-midterm-wins-set-stage-for-tougher-tech-and-ai-scrutiny)
  - [Foley & Lardner](https://www.foley.com/insights/publications/2026/11/blue-wave-new-ai-rules-what-democratic-control-of-congress-means-for-ai-regulation/)
- **UK online safety enforcement gets firmer footing.**
  - [High Court press summary](https://www.judiciary.uk/wp-content/uploads/2026/10/R-Meta-X-TikTok-v-OFCOM-press-summary.pdf)
  - [Ofcom age checks at 16](https://www.ofcom.org.uk/online-safety/protecting-children/rapid-assessment-of-highly-effective-age-assurance-at-16)
- **Canada moves its online safety bill and funds a regulator.**
  - [LEGISinfo: C-34](https://www.parl.ca/legisinfo/en/bill/45-1/c-34)
  - [Budget 2026 in brief](https://budget.canada.ca/2026/report-rapport/pdf/budget-2026-in-brief.pdf)
  - [BetaKit](https://betakit.com/?p=412048)
- **Cyber rules are close but not final.**
  - [UK Parliament: CSR Bill](https://bills.parliament.uk/bills/4035/stages)
  - [HIPAA Journal on CIRCIA](https://www.hipaajournal.com/cisa-circia-final-rule-white-house-review/)

### Where each country stands (comparison grid)

- **CA · Privacy & data**: PIPEDA in force; replacement bill C-36 awaiting debate; Children's Privacy Code issued Oct 2026
  - [Bill C-36 (openparliament.ca)](https://openparliament.ca/bills/45-1/C-36/)
  - [OPC Children's Privacy Code](https://www.priv.gc.ca/en/opc-news/news-and-announcements/2026/nr-c_261020/)
- **CA · AI**: No AI law; national strategy and transparency consultation
  - [ISED consultation](https://www.canada.ca/en/innovation-science-economic-development/news/2026/07/government-of-canada-launches-public-consultation-on-ai-transparency.html)
- **CA · Online safety & kids**: C-34 Safe Social Media Act: at House committee since Oct 29
  - [LEGISinfo: C-34](https://www.parl.ca/legisinfo/en/bill/45-1/c-34)
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
- **US · AI**: State laws (CO, CA, TX); federal preemption push now less likely after Democrats' midterm wins; voluntary safety accord; FTC and state AGs using consumer law
  - [White House framework (Jenner)](https://www.jenner.com/en/news-insights/client-alerts/takeaways-from-the-white-houses-framework-for-artificial-intelligence)
  - [Colorado rewrite (Ballard Spahr)](https://www.consumerfinancemonitor.com/2026/05/12/colorado-rewrites-its-landmark-ai-law-unpacking-sb-26-189-and-what-it-means-for-businesses/)
  - [White House AI accord](https://www.presidency.ucsb.edu/documents/white-house-accord-super-intelligence)
  - [State AG suits (Troutman)](https://www.troutman.com/insights/eight-state-ags-sue-openai-over-chatgpt-safety-and-consumer-protection/)
  - [IAPP on midterms](https://iapp.org/news/a/democratic-midterm-wins-set-stage-for-tougher-tech-and-ai-scrutiny)
- **US · Online safety & kids**: TAKE IT DOWN Act in force; KIDS Act passed House
  - [FTC](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act)
  - [KIDS Act (Tech Policy Press)](https://techpolicy.press/bipartisan-smorgasbord-of-childrens-online-safety-legislation-passes-the-house)
- **US · Competition & digital markets**: Antitrust law enforced through courts; Google search remedies under appeal by both sides
  - [Google appeal (PYMNTS/CPI)](https://www.pymnts.com/cpi-posts/us-justice-department-states-challenge-google-antitrust-remedies-in-appeal/)
- **US · Cybersecurity**: CIRCIA final reporting rule at White House review
  - [Security.io](https://www.security.io/articles/2026/10/05/circia-final-rule-enters-omb-review)
- **US · Digital trade & tax**: Using tariffs against foreign tech rules and taxes
  - [UK DST threat (Morningstar)](https://www.morningstar.co.uk/uk/news/AN_1776990152554627800/trump-threatens-big-tariff-on-uk-over-digital-tax-on-us-tech-firms.aspx)
  - [CUSMA review (Blakes)](https://www.blakes.com/insights/u-s-declines-to-renew-cusma-at-first-joint-review-what-businesses-need-to-know/)
- **UK · Privacy & data**: UK GDPR amended by Data (Use and Access) Act, phasing in
  - [Kennedys](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-data-use-and-access-act-2025-commencement-dates-and-planned-guidance-for-2026)
- **UK · AI**: No AI bill; sector regulators and sandboxes
  - [King's Speech (DLA Piper)](https://privacymatters.dlapiper.com/2026/05/uk-the-kings-speech-2026-cybersecurity-at-the-forefront/)
- **UK · Online safety & kids**: Online Safety Act enforced (court upheld Ofcom data powers Oct 30); under-16 ban coming 2027
  - [Ofcom](https://ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery)
  - [Under-16 ban (A&O Shearman)](https://www.aoshearman.com/en/insights/ao-shearman-on-data/uk-government-announces-social-media-ban-and-other-measures-to-protect-children-online)
  - [High Court press summary](https://www.judiciary.uk/wp-content/uploads/2026/10/R-Meta-X-TikTok-v-OFCOM-press-summary.pdf)
- **UK · Competition & digital markets**: DMCC Act: first conduct requirements on Google; Microsoft designation proposed
  - [CMA case page](https://www.gov.uk/cma-cases/sms-investigation-into-googles-general-search-and-search-advertising-services)
  - [CMA on Microsoft](https://gov.uk/government/news/cma-takes-first-steps-to-ensure-choice-in-business-software)
- **UK · Cybersecurity**: Cyber Security and Resilience Bill: Lords stages done; Commons to consider Lords amendments
  - [UK Parliament: bill stages](https://bills.parliament.uk/bills/4035/stages)
- **UK · Digital trade & tax**: 2% DST under US tariff threat
  - [Morningstar](https://www.morningstar.co.uk/uk/news/AN_1776990152554627800/trump-threatens-big-tariff-on-uk-over-digital-tax-on-us-tech-firms.aspx)

### Items

- **Canada's Budget 2026 funds a new digital safety and data protection regulator** · CA · 2026-11-05 · last checked 2026-11-12
  - Citation: Budget 2026, tabled Nov. 5, 2026.
  - [Budget 2026 in brief (PDF)](https://budget.canada.ca/2026/report-rapport/pdf/budget-2026-in-brief.pdf)
  - [Gowling WLG](https://gowlingwlg.com/en-ca/insights-resources/articles/2026/investing-in-intelligence)
- **Democrats are projected to win both houses of Congress, raising the odds of tech oversight** · US · 2026-11-03 · last checked 2026-11-12
  - Citation: 2026 US midterm elections, Nov. 3, 2026.
  - [IAPP](https://iapp.org/news/a/democratic-midterm-wins-set-stage-for-tougher-tech-and-ai-scrutiny)
  - [TIME](https://time.com/article/2026/11/04/midterm-elections-results-ai-industry-data-centers/)
  - [Foley & Lardner](https://www.foley.com/insights/publications/2026/11/blue-wave-new-ai-rules-what-democratic-control-of-congress-means-for-ai-regulation/)
- **UK Cyber Security and Resilience Bill finishes its Lords stages and returns to the Commons** · UK · 2026-11-02 · last checked 2026-11-12
  - Citation: Cyber Security and Resilience (Network and Information Systems) Bill (DSIT).
  - [UK Parliament: bill stages](https://bills.parliament.uk/bills/4035/stages)
  - [Hansard: Lords report stage (Oct. 26)](https://hansard.parliament.uk/Lords/2026-10-26/debates/B413EFAE-E7D4-4742-986D-092884E0D8D1/CyberSecurityAndResilience(NetworkAndInformationSystems)Bill)
  - [DLA Piper on King's Speech](https://privacymatters.dlapiper.com/2026/05/uk-the-kings-speech-2026-cybersecurity-at-the-forefront/)
- **UK High Court backs Ofcom's power to demand data from Meta, X and TikTok** · UK · 2026-10-30 · last checked 2026-11-12
  - Citation: R (Meta Platforms, X Corp and TikTok) v Ofcom [High Court, Oct. 30, 2026].
  - [Judiciary: press summary (PDF)](https://www.judiciary.uk/wp-content/uploads/2026/10/R-Meta-X-TikTok-v-OFCOM-press-summary.pdf)
  - [Judgment (PDF)](https://www.judiciary.uk/wp-content/uploads/2026/10/R-Meta-X-TikTok-v-OFCOM-FINAL-jdgmnt-for-30-October.pdf)
  - [Courthouse News](https://www.courthousenews.com/meta-x-and-tiktok-lose-challenge-to-uk-online-safety-regulator/)
- **Critical PHP flaws: cyber agencies urge immediate patching; some Canadian government sites taken offline** · CA + US · 2026-10-21 · last checked 2026-10-22
  - Citation: Canadian Centre for Cyber Security, AL26-026 and statement (Oct. 21, 2026); CISA alert (Oct. 21, 2026).
  - [Cyber Centre statement](https://www.cyber.gc.ca/en/news-events/statement-regarding-critical-vulnerabilities-php-affecting-websites-online-services)
  - [Cyber Centre alert AL26-026](https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619)
  - [CISA alert](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)
  - [CP24 / Canadian Press](https://cp24.com/news/canada/2026/10/21/canadian-apps-and-government-websites-go-offline-to-ward-off-online-danger)
- **Canada's Privacy Commissioner launches a Children's Privacy Code** · CA · 2026-10-20 · last checked 2026-10-22
  - Citation: OPC, Children's Privacy Code (Oct. 20, 2026).
  - [OPC news release](https://www.priv.gc.ca/en/opc-news/news-and-announcements/2026/nr-c_261020/)
  - [Canadian Privacy Scan (detail)](https://tonhs.github.io/Privacy-and-AI-Reg-Scan/)
- **UK competition regulator proposes special rules for Microsoft's business software, including Copilot** · UK · 2026-10-16 · last checked 2026-11-12
  - Citation: CMA, proposed SMS decision: Microsoft's business software ecosystem (Oct. 16, 2026).
  - [CMA news release](https://gov.uk/government/news/cma-takes-first-steps-to-ensure-choice-in-business-software)
  - [CMA consultation](https://gov.uk/government/consultations/proposed-decision-sms-investigation-into-microsofts-business-software-ecosystem)
- **FTC demands documents from OpenAI and Anthropic, and eight states sue OpenAI** · US · 2026-10-14 · last checked 2026-10-22
  - Citation: FTC civil investigative demands (reported Oct. 15, 2026); state AG complaints filed Oct. 14, 2026.
  - [Axios (Oct. 15, 2026)](https://www.axios.com/2026/10/15/ftc-openai-anthropic-ai-safety-investigation)
  - [Troutman Pepper Locke on the state suits](https://www.troutman.com/insights/eight-state-ags-sue-openai-over-chatgpt-safety-and-consumer-protection/)
  - [UPI](https://www.upi.com/Top_News/US/2026/10/15/states-sue-OpenAI-ChatGPT/5571792042846/)
- **Ofcom investigates Meta over risk checks before launching Instagram's disappearing-photo feature** · UK · 2026-10-06 · last checked 2026-10-22
  - Citation: Online Safety Act 2023, ss. 9(4), 11(4); Ofcom investigation into Meta Platforms Inc. (Oct. 6, 2026).
  - [Ofcom investigation page](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/investigation-into-metas-compliance-with-illegal-content-risk-assessment-duties)
  - [LBC report](https://www.lbc.co.uk/article/ofcom-meta-online-safety-act-5HjdjSQ_2/)
- **US critical infrastructure cyber reporting rule is at final White House review** · US · 2026-10-01 · last checked 2026-11-12
  - Citation: 6 U.S.C. § 681 et seq. (CIRCIA).
  - [Security.io: final rule enters OMB review (Oct. 5, 2026)](https://www.security.io/articles/2026/10/05/circia-final-rule-enters-omb-review)
  - [HIPAA Journal (Oct. 5, 2026)](https://www.hipaajournal.com/cisa-circia-final-rule-white-house-review/)
  - [Covington (Sept. 2026)](https://www.cov.com/-/media/files/corporate/publications/2026/09/cisa-town-halls-signal-key-cyber-rule-changes-ahead.pdf)
- **California enacts new rules on AI at work, kids' feeds and privacy deletion rights** · US (California) · Sept 2026 · last checked 2026-10-06
  - Citation: Cal. SB 947, AB 1883, SB 951, SB 1000, AB 2713 (signed Sept. 30, 2026); AB 1709, AB 2246 (Sept. 10, 2026); SB 923 (Sept. 27, 2026).
  - [Governor of California (Sept. 30, 2026)](https://www.gov.ca.gov/2026/09/30/californias-nation-leading-ai-framework-just-got-stronger-governor-newsom-signs-more-first-in-the-nation-worker-protections-and-more/)
  - [WilmerHale summary](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20261002-california-finalizes-next-wave-of-state-ai-and-privacy-regulation)
  - [AB 1709 (National Law Review)](https://natlawreview.com/article/california-enacts-covered-platform-age-restrictions-and-establishes-e-safety)
- **White House turns to voluntary AI safety: an industry accord and a new "Super Intelligence" task force** · US · Sept–Oct 2026 · last checked 2026-11-12
  - Citation: White House Accord on Super Intelligence (Sept. 29, 2026); E.O. 14434, 91 Fed. Reg. 63129 (Oct. 2, 2026); Super Intelligence Force announcement (Oct. 4, 2026); E.O. of June 2, 2026.
  - [Accord text (American Presidency Project)](https://www.presidency.ucsb.edu/documents/white-house-accord-super-intelligence)
  - [E.O. 14434 (Federal Register)](https://www.federalregister.gov/documents/2026/10/02/2026-20321/inaugurating-the-era-of-super-intelligence)
  - [Nextgov/FCW on the order and accord](https://www.nextgov.com/artificial-intelligence/2026/09/white-house-unveils-super-intelligence-executive-order-and-industry-accord/416325/)
  - [TechCrunch on the Super Intelligence Force](https://techcrunch.com/2026/10/04/trump-unveils-his-new-super-intelligence-force/)
  - [Latham & Watkins on the June order](https://www.lw.com/en/insights/president-trump-signs-executive-order-establishing-ai-cybersecurity-and-frontier-model-framework)
  - [The Next Web on first meeting](https://thenextweb.com/news/super-intelligence-force-charter-first-meeting-anthropic)
- **Canada to scrap streamers' Canadian-content payments** · CA · 2026-07-29 · last checked 2026-10-22
  - Citation: Online Streaming Act, S.C. 2023, c. 8.
  - [CP24 / Canadian Press](https://www.cp24.com/news/canada/2026/07/29/ottawa-to-eliminate-streamers-cancon-payments-provide-government-funding-instead/)
  - [Michael Geist](https://www.michaelgeist.ca/2026/07/starting-over-court-filing-confirms-the-crtcs-streamer-contribution-decisions-are-dead-with-a-full-online-streaming-act-reset-to-come/)
  - [CRS report](https://www.everycrsreport.com/files/2026-07-23_IN12716_1b3d55784138785dd6e8f61dd7b211036ab7d33a.html)
- **Canada's AI approach: a national strategy and a transparency consultation, but no AI law** · CA · 2026-07-23 · last checked 2026-11-12
  - Citation: ISED, AI transparency consultation (2026); National AI Strategy (June 4, 2026).
  - [ISED consultation](https://www.canada.ca/en/innovation-science-economic-development/news/2026/07/government-of-canada-launches-public-consultation-on-ai-transparency.html)
  - [Gowling WLG on strategy](https://gowlingwlg.com/en/insights-resources/articles/2026/canada-launches-ai-for-all-national-artificial-intelligence-strategy)
  - [BetaKit: Canada signs AI safety declaration](https://betakit.com/?p=412048)
  - [Global News](https://globalnews.ca/news/12144853/canada-joins-ai-safety-statement/)
- **US declines to renew CUSMA; digital rules are part of the dispute** · CA + US · 2026-07-01 · last checked 2026-10-22
  - Citation: CUSMA/USMCA Art. 34.7 joint review (July 1, 2026).
  - [Blakes](https://www.blakes.com/insights/u-s-declines-to-renew-cusma-at-first-joint-review-what-businesses-need-to-know/)
  - [MPA on US concerns](https://www.mpamag.com/ca/news/general/cusma-deadline-now-in-doubt-as-july-1-looms/571211)
- **US House passes KIDS Act children's online safety package** · US · 2026-06-29 · last checked 2026-11-12
  - Citation: Kids Internet and Digital Safety Act, H.R. 7757 (119th Cong.), passed House June 29, 2026.
  - [Tech Policy Press](https://techpolicy.press/bipartisan-smorgasbord-of-childrens-online-safety-legislation-passes-the-house)
  - [IAPP on scope](https://iapp.org/news/a/unpacking-the-scope-of-the-kids-act)
  - [Sen. Blackburn release (Aug. 5, 2026)](https://www.blackburn.senate.gov/2026/8/blackburn-blumenthal-celebrate-commerce-committee-passage-of-bipartisan-kids-online-safety-act)
- **UK data law changes are phasing in; a complaints procedure was due in June** · UK · 2026-06-19 · last checked 2026-10-04
  - Citation: Data (Use and Access) Act 2025, c. 18.
  - [Kennedys commencement guide](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-data-use-and-access-act-2025-commencement-dates-and-planned-guidance-for-2026)
  - [Mayer Brown on complaints](https://www.mayerbrown.com/zh-hans/insights/publications/2026/02/preparing-for-the-data-use-and-access-act-2025-upcoming-complaints-procedure-requirement)
- **Canada's lawful access bill C-22 is before a Senate committee** · CA · 2026-06-18 · last checked 2026-11-12
  - Citation: Bill C-22, Lawful Access Act, 2026.
  - [OPC submission](https://www.priv.gc.ca/en/opc-actions-and-decisions/advice-to-parliament/2026/parl_260526/)
  - [CBC: Commissioner urges Senate amendments](https://www.cbc.ca/news/politics/senate-bill-c-22-lawful-access-9.7406213)
  - [openparliament.ca](https://openparliament.ca/bills/45-1/C-22/)
- **UK competition regulator imposes first digital markets rules on Google search** · UK · 2026-06-17 · last checked 2026-10-04
  - Citation: Digital Markets, Competition and Consumers Act 2024, Part 1.
  - [CMA case page](https://www.gov.uk/cma-cases/sms-investigation-into-googles-general-search-and-search-advertising-services)
  - [Kennedys analysis](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-uk-digital-markets-regime-in-action-the-cma-s-first-conduct-requirements-for-google-and-commitments-for-apple-and-google-mobile-platforms)
- **UK will ban under-16s from social media, starting spring 2027** · UK · 2026-06-15 · last checked 2026-11-12
  - Citation: UK government announcement, June 15, 2026.
  - [A&O Shearman summary](https://www.aoshearman.com/en/insights/ao-shearman-on-data/uk-government-announces-social-media-ban-and-other-measures-to-protect-children-online)
  - [WSGR summary](https://www.wsgrdataadvisor.com/2026/06/uk-announces-social-media-ban-and-broader-online-restrictions-for-users-under-16/)
  - [Ofcom industry bulletin (Oct. 2026)](https://www.ofcom.org.uk/online-safety/protecting-children/online-safety-industry-bulletin-october-2026)
  - [Ofcom: rapid assessment of age assurance at 16](https://www.ofcom.org.uk/online-safety/protecting-children/rapid-assessment-of-highly-effective-age-assurance-at-16)
- **Canada's Bill C-36 would replace PIPEDA with a tougher privacy law** · CA · 2026-06-15 · last checked 2026-11-12
  - Citation: Bill C-36, 45th Parl., 1st Sess. First reading June 15, 2026.
  - [openparliament.ca](https://openparliament.ca/bills/45-1/C-36/)
  - [Canadian Privacy Scan (detail)](https://tonhs.github.io/Privacy-and-AI-Reg-Scan/)
- **Canada's critical infrastructure cyber law receives Royal Assent** · CA · 2026-06-15 · last checked 2026-10-04
  - Citation: S.C. 2026, c. 9 (former Bill C-8).
  - [openparliament.ca](https://openparliament.ca/bills/45-1/C-8/)
- **Canada's Bill C-34 is at committee: under-16 account limits and AI chatbot duties** · CA · 2026-06-10 · last checked 2026-11-12
  - Citation: Bill C-34, 45th Parl., 1st Sess. Introduced June 10, 2026.
  - [LEGISinfo: Bill C-34](https://www.parl.ca/legisinfo/en/bill/45-1/c-34)
  - [CHPC study page](https://www.ourcommons.ca/Committees/en/CHPC/StudyActivity?studyActivityId=13668976)
  - [Government backgrounder](https://www.canada.ca/en/canadian-heritage/news/2026/06/government-of-canada-introduces-legislation-to-combat-online-harms-particularly-those-impacting-children.html)
- **TAKE IT DOWN Act: platforms must remove intimate images within 48 hours** · US · 2026-05-19 · last checked 2026-10-04
  - Citation: TAKE IT DOWN Act, Pub. L. 119-12 (2025).
  - [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act)
- **UK King's Speech: digital ID, police facial recognition rules and AI sandboxes, but no AI bill** · UK · 2026-05-13 · last checked 2026-10-04
  - Citation: King's Speech, May 13, 2026.
  - [DLA Piper](https://privacymatters.dlapiper.com/2026/05/uk-the-kings-speech-2026-cybersecurity-at-the-forefront/)
- **Colorado rewrites its AI law, which now takes effect January 2027** · US (Colorado) · 2026-05-12 · last checked 2026-11-12
  - Citation: Colorado SB 26-189.
  - [Consumer Finance Monitor (Ballard Spahr)](https://www.consumerfinancemonitor.com/2026/05/12/colorado-rewrites-its-landmark-ai-law-unpacking-sb-26-189-and-what-it-means-for-businesses/)
  - [Venable](https://www.venable.com/insights/publications/2026/07/colorados-sb26189-sets-new-rules-for-ai)
  - [Morrison Foerster (Oct. 14, 2026)](https://www.mofo.com/resources/insights/261014-colorados-new-rules)
- **Canadian privacy regulators find OpenAI broke privacy law in building ChatGPT** · CA · 2026-05-06 · last checked 2026-10-04
  - Citation: Joint investigation of OpenAI OpCo, LLC (May 6, 2026).
  - [OPC statement](https://www.priv.gc.ca/en/opc-news/speeches-and-statements/2026/s-d_260506/)
- **US threatens tariffs over the UK's digital services tax** · UK + US · 2026-04-24 · last checked 2026-10-22
  - Citation: Finance Act 2020, Part 2 (UK DST).
  - [Morningstar / Reuters](https://www.morningstar.co.uk/uk/news/AN_1776990152554627800/trump-threatens-big-tariff-on-uk-over-digital-tax-on-us-tech-firms.aspx)
  - [CSIS on the Tech Prosperity Deal](https://www.csis.org/analysis/us-uk-trade-and-tech-agreements-update-after-state-visit)
- **Updated COPPA rule now fully in force** · US · 2026-04-22 · last checked 2026-10-04
  - Citation: 16 C.F.R. Part 312, as amended (2025); compliance date April 22, 2026.
  - [Davis Polk](https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect)
- **UK shelves plan to let AI firms train on copyrighted work by default** · UK · 2026-03-23 · last checked 2026-10-04
  - Citation: UK Government report on copyright and AI, March 23, 2026.
  - [Mishcon de Reya summary](https://www.mishcon.com/news/copyright-and-ai-the-uk-governments-report)
- **White House pushes to override state AI laws with one national standard** · US · 2026-03-20 · last checked 2026-11-12
  - Citation: E.O. 14365 (Dec. 11, 2025); White House national AI legislative framework (Mar. 20, 2026).
  - [Jenner & Block on the framework](https://www.jenner.com/en/news-insights/client-alerts/takeaways-from-the-white-houses-framework-for-artificial-intelligence)
  - [Ropes & Gray on preemption limits](https://www.ropesgray.com/en/insights/alerts/2026/03/examining-the-landscape-and-limitations-of-the-federal-push-to-override-state-ai-regulation)
  - [BakerHostetler on DOJ task force](https://www.bakerlaw.com/insights/navigating-the-emerging-federal-state-ai-showdown-doj-establishes-ai-litigation-task-force/)
- **Competition Bureau reports on algorithmic pricing** · CA · 2026-01-22 · last checked 2026-10-04
  - Citation: Competition Bureau, What We Heard: Algorithmic Pricing and Competition (Jan. 22, 2026).
  - [Competition Bureau](https://www.canada.ca/en/competition-bureau/news/2026/01/competition-bureau-report-highlights-public-feedback-on-algorithmic-pricing-and-competition.html)
- **Ofcom is enforcing the Online Safety Act, including against AI features** · UK · Jan–May 2026 · last checked 2026-11-12
  - Citation: Online Safety Act 2023; Ofcom investigation into X (Jan. 12, 2026).
  - [Ofcom: X/Grok investigation](https://ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery)
  - [Linklaters roundup](https://techinsights.linklaters.com/post/102n7pm/the-uks-online-safety-act-heats-up-fines-battlelines-and-even-more-regulatio)
  - [Ofcom update on X and Grok (Oct. 14, 2026)](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-update-monitoring-xs-response-to-hate-and-terror-content-and-grok-investigation-latest)
- **State AI rules now in force: frontier model transparency and companion chatbots** · US (States) · 2026-01-01 · last checked 2026-10-04
  - Citation: Cal. SB 53 (2025); Cal. SB 243 (2025); Tex. HB 149 (TRAIGA).
  - [Perkins Coie on California AI bills](https://legacy.perkinscoie.com/insights/update/california-governor-newsom-signs-several-ai-bills-vetoes-three)
  - [Hunton: laws effective January 2026](https://www.hunton.com/privacy-and-information-security-law/new-u-s-state-privacy-social-media-and-ai-laws-take-effect-in-january-2026)
- **Three more US state privacy laws took effect, bringing the total to about 20** · US (States) · 2026-01-01 · last checked 2026-10-04
  - Citation: Ind. SB 5; Ky. HB 15; R.I. HB 7787/SB 2500.
  - [MultiState](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026)

_35 items, 84 unique source links._
<!-- cited:end -->

## 3. Update log

| Date | Checked | Added | Changed | Removed |
|---|---|---|---|---|
| 2026-10-04 | First edition. Federal and UK parliaments, Ofcom, CMA, FTC, CISA, White House framework, state AI laws, CUSMA review, CRTC/streaming, Canadian Privacy Scan items | 25 items, comparison grid, brief | Comparison grid: source links added to every cell; US competition cell now reflects Google search remedies appeal | — |
| 2026-10-06 | LEGISinfo (C-36, C-34, C-22), Ofcom, bills.parliament.uk, CISA/OIRA, Governor of California, Federal Register, White House / Congress child-safety and preemption coverage | Ofcom investigation into Meta (Instagram Instants); California 2026 AI, kids and privacy laws; White House AI accord, E.O. 14434 and Super Intelligence Force (with June 2 order) | CIRCIA final rule now at OIRA review (received Oct 1); UK Cyber Security and Resilience Bill corrected to Lords committee from Sept 1, report stage Oct 26 (was shown as report stage Sept 16); brief points 1, 2 and 4, comparison grid (US AI and cyber, UK cyber cells) and watch list updated | — |
| 2026-10-22 | LEGISinfo / openparliament.ca (C-36, C-34, C-22), OPC news, Ofcom (news, Oct. industry bulletin), bills.parliament.uk (CSR Bill), CMA, FTC / state AG coverage, White House Super Intelligence Force, Colorado AG rulemaking, Senate KOSA, Cyber Centre and CISA, CRTC/streaming, CUSMA, UK DST | FTC demands to OpenAI and Anthropic plus eight state AG suits against OpenAI; critical PHP vulnerabilities (Cyber Centre, CISA); Canada's Children's Privacy Code; CMA proposed SMS designation of Microsoft business software | Super Intelligence Force first meeting (Oct. 15); Ofcom Grok update in UK OSA item; Ofcom age-check assessment timing in UK under-16 item; Colorado revised draft rules and Oct. 26 hearing; Senate Commerce KOSA (Aug. 5) added to KIDS Act item; C-34 second-reading debate began Oct. 21; C-36 text corrected (not yet debated); all four brief points rewritten; comparison grid (CA privacy and online safety, US AI, UK competition) and watch list updated; Cyber Centre added to monitored sources | — |
| 2026-11-12 | LEGISinfo / openparliament.ca (C-36, C-34, C-22), CHPC, Senate SECD coverage, Budget 2026, bills.parliament.uk and Hansard (CSR Bill), Ofcom (age assurance at 16, Grok update), judiciary.uk, CMA, OIRA / CISA (CIRCIA), Colorado AG rulemaking, White House E.O. 14434, US midterm coverage, CRTC/streaming, CUSMA | US midterms (Democrats projected to win Congress); High Court upholds Ofcom information notices (Meta, X, TikTok); Canada Budget 2026 and new digital regulator funding | C-34 at committee (track 2); C-22 at Senate committee with OPC call for amendments; Canada signs AI incident early-warning declaration (Nov. 9) added to AI item; UK CSR Bill through Lords stages, back to Commons; Ofcom age checks at 16 findings in UK under-16 item; Colorado rules not yet final; CIRCIA still pending at OIRA; all four brief points rewritten; comparison grid (CA online safety, US AI, UK online safety, UK cyber) and watch list updated | Watch: CSR Lords report (Oct 26), Ofcom age-check assessment, Colorado Oct 26 hearing (all resolved) |
