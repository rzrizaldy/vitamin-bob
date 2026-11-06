# Grand Nord focus: 2022 data update, regional dashboard and slide plan

Saved on 2026-11-05 from a team chat shared by Meet ([claude.ai/share/7702cd69-...](https://claude.ai/share/7702cd69-93fd-42c8-977a-5b3038e42c7d)). That chat updated the deck's 2018 numbers with the 2022 Malaria Indicator Survey, built a regional dashboard, and drafted a storyline that focuses on **Extrême-Nord and Nord**.

**Status of these numbers.** They were copied from that chat and have **not been re-checked** against the sources yet, so treat them as *guessed* in this repo's terms. Add each one to [`sources.csv`](sources.csv) only after reading it in the cited source (mostly the MIS 2022 final report).

**This file conflicts with the current deck.** The 14-slide deck (see [`CONTEXT.md`](CONTEXT.md)) proposes **Est** as the pilot candidate. This chat ranks Est 4th and recommends **Nord first, then scaling to Extrême-Nord**. The team needs to settle this before the deck goes out. See "Reconciling with the deck" below.

## 1. The data situation

- The 2018 EDSC-V (DHS) is still the latest full DHS. Its fieldwork ran from June 2018 to January 2019.
- The newest national survey is the **2022 Malaria Indicator Survey (MIS)**, with fieldwork from August to December 2022. It covers fever care, phones, internet, travel time and cost for 12 regions. Microdata: World Bank Microdata Library, `CMR_2022_MIS`.
- MIS caveats:
  - 11 of 41 clusters in Nord-Ouest and 11 of 40 in Sud-Ouest (mostly rural) could not be surveyed.
  - It ran in the rainy season.
  - Est has only 84 children with fever in the sample.
- Indicators still only available by region from 2018: household phones, household electricity, births in a facility.
- Not published by region: network coverage, mobile connections, market share. ART's 2021 decision requires operators to publish coverage maps; the team does not have them yet.
- Other recent sources: CamPHIA 2024/25 (HIV); ECAM5 2021/22 (poverty 38.6%, about 10M people).

## 2. National update, 2018 deck figures vs latest

| Measure | In the deck | Latest (per the chat) |
|---|---|---|
| Mobile connections | 108 per 100 (2024) | 29.0M at end of 2025 (96.4% of population); 87.5% are 3G/4G/5G-capable (DataReportal 2026) |
| Internet users | 46% (2024) | 12.6M or 41.9% in Oct 2025 (DataReportal); World Bank 46.3% (2024) |
| Households with a phone | 85 · rural 74 (2018) | 89.4 · urban 96.8 · rural 80.3 (MIS 2022) |
| Women who own a phone | 64 · rural 42 (2018) | 69.5 · urban 82.9 · rural 52.7 (MIS 2022) |
| Women who own a smartphone | not in deck | 37.9 · urban 55.2 · rural 16.1 (MIS 2022) |
| Women who used the internet in the past 12 months | not in deck | 43.2 · rural 17.9 · Extrême-Nord 9.4 · Nord 13.1 (MIS 2022) |
| Household electricity | 72 · rural 43 (WDI 2024) | 65.1 · rural 37.0 (MIS 2022) |
| Network coverage | about 88% 2G / 75% 3G-4G | ITU April 2025 similar; ITU IDI 2024 says 70% for 3G and 4G. Sources conflict, so get operator maps. |
| Market share | Orange 50 / MTN 47 / Camtel 3 | Unchanged. Active subscribers 2024: Orange 15.67M, MTN 13.71M, Camtel 2.08M |

Context:
- SIM connections grew about 8 times faster than internet users (+13.7% vs +1.6%).
- Call quality is a live issue: ART fined Orange and MTN nearly €4M in 2025, and content creators called for an operator boycott on 30 Oct 2026.

## 3. Access to care, 2018 vs 2022

Children with fever who got advice or treatment the same or next day (%):

| Region | 2018 (deck) | 2022 (MIS) | Women owning a phone, 2022 |
|---|---|---|---|
| Est | 15 | 12.9 | 59.7 |
| Centre* | 24 | 18.9 | 71.4 |
| Adamaoua | 20 | 26.2 | 65.8 |
| Extrême-Nord | 32 | 28.9 | 46.0 |
| Nord | 32 | 45.1 | 49.0 |
| Sud-Ouest | 57 | 48.6 | 76.9 |
| National | n/a | 31.8 (any care sought 55.6) | 69.5 |

*Excludes Yaoundé.

**The finding that challenges the deck: distance is rarely why parents skip care.** Reasons mothers gave for not taking a feverish child to a facility (MIS 2022):

| Reason | % |
|---|---|
| No money | 46.9 |
| Did not think it was serious | 43.6 |
| Facility too far | 4.2 (rural 6.0) |

- In Est, 60.7% of households are under 30 minutes from a public facility and 4.5% are 2 hours or more away. The deck's "64% cite distance" comes from a DHS question about perceived barriers, not from what families actually did.
- Distance is real in Extrême-Nord (13.5% of households 2 hours or more away), Nord-Ouest (11.8%) and Nord (11.6%).
- About two in three children with fever were given medicine without any health professional's advice.
- The average paid fever episode cost 9,107 FCFA.
- Only 16% of women in Est had heard a message about free malaria treatment for under-5s in the past 12 months.

**Implication:** "is it serious?" is about half the gap, and triage answers it. Cost is the other half, and Bob does nothing about it. The deck should say that.

## 4. Disease burden and health system, latest

- **Malaria:**
  - WHO estimate for 2023: 7.3M cases, 11.6K deaths (World Malaria Report 2024).
  - MINSANTE for 2025: nearly 2M cases, over 1,100 deaths, and a 70% funding gap of over 260bn FCFA.
  - MIS 2022: 26% of children aged 6 to 59 months tested positive; highest in Centre 49%, Sud 46%, Est 41%.
- **HIV and TB:** HIV 2.6% prevalence, 509,766 people living with HIV (CamPHIA 2024/25), lowest in Extrême-Nord (1.4%) and Nord (about 1.5%). TB: 38,472 cases recorded in 2024, about 132 per 100,000.
- **Mortality:** under-5 65 per 1,000 (2024); neonatal 25 (2024); maternal 258 per 100,000 (2023).
- **Outbreaks:**
  - 10 epidemics recorded in 2025 (mpox, cholera, measles, dengue, polio).
  - Cholera: 2,683 cumulative cases (situation report, 14 Sept 2026), including 800+ cases and 25 deaths in Extrême-Nord by July 2026.
  - An mpox outbreak has been running since 14 Nov 2025.
- **US aid cuts:** USAID funding to Cameroon fell 74% in 2025. Malaria deaths in the north rose after community health worker support stopped.
- **Universal health coverage (CSU):** 3.5M enrolled as of Sept 2025; more than 9M beneficiaries cited to the Senate in June 2026; 318bn FCFA spent in three years with mixed results.
- **Financing and coverage:** out-of-pocket share 67.65% (2023), the same as the deck. UHC service coverage index 44 (2021), against an LMIC average of 58.
- **Workforce:** a 2026 source says fewer than 1 doctor per 10,000 people, and up to 27% of trained health workers are unemployed. This conflicts with the deck's 1.4 per 10,000; check the WHO health workforce database before using either.

## 5. Regional dashboard

The chat built a map dashboard as a Claude artifact ([/artifact/K8QjwpXRYf1KwwpnXixB7F](https://claude.ai/artifact/K8QjwpXRYf1KwwpnXixB7F)). It is Meet's and is **not shared with this account**, so its dataset could not be copied here. Ask Meet to share it, or to export its CSVs from the dashboard's Sources panel into this folder.

What it does, per the chat:

- Maps each indicator by region, switched with a "Show" dropdown. The default view is the hypothesis score; darker means a stronger fit. Centre and Littoral are coloured by their values outside Yaoundé and Douala, and the two cities are shown as circles.
- Scores each region from 0 (best of the ten) to 100 (worst) on three parts:
  - **Need:** fever, malaria and severe anaemia in children.
  - **Access gap:** delayed care, travel time, facility density and births outside facilities.
  - **Digital gap:** internet and smartphone use.

  Phone reach is shown separately, not folded into the score. Exact weights were not stated in the chat.
- Estimates the children without prompt care in each region as population × fever rate × share without care the same or next day (MIS 2022, BUCREP 2025 projections).
- Region outlines: geoBoundaries.

| Rank | Region | Score | Need | Access gap | Digital gap | Phone reach | Children without prompt care (per fortnight) |
|---|---|---|---|---|---|---|---|
| 1 | Extrême-Nord | 84 | 72 | 79 | 100 | 0 | about 271k |
| 2 | Nord | 81 | 75 | 76 | 93 | 16 | about 144k |
| 3 | Adamaoua | 70 | 68 | 70 | 71 | 54 | about 72k |
| 4 | Est | 62 | 57 | 70 | 60 | 31 | about 65k |

Extrême-Nord and Nord hold about 44% of Cameroon's under-5s with fever who do not get prompt care: about 415,000 children in any two-week window in the rainy season (estimate). The ranking holds even without the digital part.

## 6. The Grand Nord case

| # | Problem | Extrême-Nord | Nord | Source |
|---|---|---|---|---|
| 1 | Under-5s with fever in the past two weeks (highest in the country) | 40.7% | 44.3% | MIS 2022 |
| 2 | Feverish children seen the same or next day | 28.9% | 45.1% | MIS 2022 |
| 3 | Households 1 hour or more from a public facility (Ouest, Sud-Ouest about 9%) | 32.3% | 36.5% | MIS 2022 |
| 4 | Births in a health facility | 39% | 40% | DHS 2018 |
| 5 | Women who own a phone / a smartphone / used the internet (all lowest in the country) | 46 / 10 / 9% | 49 / 12 / 13% | MIS 2022 |
| 6 | Literate women / women with no weekly media contact | 34 / 85% | 29 / 73% | MIS 2022 |

- **Scale:** about 5.5M people in Extrême-Nord and 3.5M in Nord, out of 29.4M (BUCREP 2025 projections). Together that is about 30% of the country.
- **Framing corrections:**
  - "Highest density" holds only for Extrême-Nord (about 160 per km², roughly tied with Ouest); Nord is about 53 per km². Say "largest population".
  - "Lowest network access" cannot be shown, because coverage is not published by region. Say "lowest internet use and phone ownership".
- **Aggravating context:** 1.4M people in Extrême-Nord need humanitarian aid in 2026, with attacks on health facilities (OCHA); cholera in 2026; US aid cuts ended community health worker support.
- **The tension:** the regions that best fit the hypothesis have the fewest phones. Only 46 to 49% of women own one, so a missed call from the mother's own phone reaches about half the target group. However, 82% of women in Extrême-Nord and 74% in Nord know a community health worker nearby, the highest share in the country. In the north, the person calling Bob may need to be the community health worker or a shared household phone.
- **Pilot suggestion from the chat:** start in Nord and design for scaling to Extrême-Nord. Nord has the same profile, the worst travel times, and less conflict.
- **Est fits a different problem:** it has the worst prompt-care rate (13%), but 90% of households are under an hour from a facility and 32% of women use the internet. Its gap is judging severity, plus cost.

**One-line problem statement:** In Cameroon's two northern regions, about 9 million people face the country's highest child illness rates, long travel to care and the lowest phone and internet use. Sick children reach care late, and today's digital health tools cannot reach their families.

## 7. Slide plan from the chat (6 slides)

Storyline: problem, evidence, data gap to validate, hypothetical solution, metrics before and after.

| # | Slide | Content |
|---|---|---|
| 1 | Storyline | Problem → Evidence → Data gap to validate → Hypothetical solution → Metrics |
| 2 | Why Extrême-Nord and Nord | Scale (about 9M people, about 30% of the country) and burden (about 44% of under-5s with fever who get no prompt care) |
| 3 | Problem statements | The six-row table in section 6, the aggravating context, and the one-line problem statement |
| 4 | Our data is partly outdated, so we validate first | What we have (DHS 2018, updated with MIS 2022), what we lack (regional coverage, post-2025 effects), and the validation steps |
| 5 | Hypothetical solution: Vitamin Bob for the Grand Nord | Component table below |
| 6 | Metrics before and after | Metrics table below |

**Validation before any design work (slide 4):**
1. Recompute the 2018-only indicators by region from the MIS 2022 microdata.
2. Get operator coverage maps and subscriber counts by region from ART, MINPOSTEL, Orange and MTN.
3. Pull facility data from MINSANTE's DHIS2: consultations, severe malaria cases, referrals.
4. Interview caregivers, community health workers and clinic staff in the field.

**Hypothetical solution (slide 5).** It is a hypothesis and changes if the validated data changes.

| Component | What it does | Why (data) |
|---|---|---|
| Free voice call (missed call, then callback) | Works on any basic phone, no internet | Only 9 to 13% of women use the internet |
| Shared-phone and community health worker mode | A health worker or household phone calls on a family's behalf | 46 to 49% of women own a phone; 82% / 74% know a community health worker |
| Spoken prompts in local languages; keypad or voice answers | No reading needed | 29 to 34% of women are literate |
| Fixed rules for fever danger signs | Emergency / go now / routine; the AI never decides urgency | Fever is the dominant burden |
| Routing plus clinic alert | Nearest open facility, with a summary sent ahead | A third of households are an hour or more away |
| Offline, solar-ready district hub | Runs without internet or reliable power | 37% of rural households have electricity |

Dependency: operators must make the line free. Orange and MTN hold about 97% of the market (ART 2024).

**Metrics (slide 6).** Measure the pilot district against a similar comparison district, so seasonal malaria swings do not look like an effect of the pilot.

| Metric | Baseline | Baseline source | How measured after |
|---|---|---|---|
| Feverish children seen the same or next day (primary) | Extrême-Nord 28.9% · Nord 45.1% | MIS 2022 | Household survey in the pilot district |
| Any care sought for fever | Extrême-Nord 56.1% · Nord 62.5% | MIS 2022 | Household survey |
| Feverish children given a blood test | Extrême-Nord 34.0% · Nord 22.5% | MIS 2022 | Household survey and DHIS2 |
| Households reached | 0 | n/a | Unique callers per 1,000 children under 5 |
| Danger signs correctly flagged (safety) | n/a | n/a | Clinician review of call logs (target: none missed) |
| Under-triage and "unsure" rates | n/a | n/a | Clinician review of call logs |
| Wasted trips to closed or full clinics | Not measured | Collect in validation | Caller follow-up survey |
| Time from symptom onset to care | Not measured | Collect in validation | Caller follow-up survey |
| Severe malaria admissions and deaths at facilities | Pull in validation | MINSANTE DHIS2 | DHIS2 trend, pilot vs comparison district |
| Cost per contact | n/a | n/a | Hub and telecom costs ÷ calls |

## 8. Reconciling with the deck

These slides in the 14-slide deck would change if the team adopts the Grand Nord focus:

| Deck slide | Now says | Would change to |
|---|---|---|
| 2 Executive summary, 4 Access gap | Est: 75% of homes have a phone, 15% timely care | MIS 2022 values; the gap is severity and cost, not distance; focus on Extrême-Nord and Nord |
| 4 Access gap | "64% cite distance" in Est | Drop for Est; keep distance only for the north (32 to 37% of households an hour or more away) |
| 10 Readiness by region (Exhibit 12) | DHS 2018 table | MIS 2022 values where available, or the dashboard's ranking |
| 11 Security and access (map) | Est candidate; Extrême-Nord not for phase 1 | Nord first; Extrême-Nord to scale into, after a security check |
| 12 Product, 3 Moat | Missed call from the caller's own phone | Add a shared-phone and community health worker mode |
| 14 Proposal | Est as lead candidate | Nord pilot plus a comparison district |
| New | n/a | Data gap and validation slide; before and after metrics slide |

Malaria prevalence also differs by survey: the deck uses DHS 2018 (Centre 47, Est 35), while MIS 2022 gives Centre 49, Sud 46, Est 41.

## Sources named in the chat

- Cameroon Malaria Indicator Survey 2022, Final Report (INS/ICF, Sept 2023), tables 2.11, 2.15 to 2.17, 4.1 and 5.1.2; microdata `CMR_2022_MIS` on the World Bank Microdata Library
- Cameroon DHS 2018 (EDSC-V)
- BUCREP regional projections, via citypopulation.de
- CamPHIA 2024/25 summary sheet; CRTV on CamPHIA and TB
- DataReportal, Digital 2026: Cameroon; Digital Business Africa, Oct 2026; EcoMatin (ART 2024 market data, CSU spending)
- WHO World Malaria Report 2024 and malaria country profile; Journal du Cameroun (malaria 2025)
- OCHA Cameroon HNRP 2026; ART coverage-map decision, 2021
- Humangle and Reuters on the USAID cuts
- geoBoundaries (region outlines)
