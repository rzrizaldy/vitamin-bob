# Vitamin Bob in Cameroon: research brief

Prepared 2026-11-02 for a pilot conversation with a World Bank health programme lead.
Every number below has a row in [`sources.csv`](sources.csv) (source, year, URL, status).
Status labels: **verified** (read from the source), **inferred** (reasoned from verified data), **guessed** (not yet checked).
Re-pull the WDI and DHS numbers with `python3 research/cameroon/pull_data.py`.
How the pilot deck grew to 14 slides, and what is still open: [`CONTEXT.md`](CONTEXT.md).
2022 data update, regional dashboard and the Extrême-Nord / Nord slide plan (numbers not yet re-checked): [`GRAND_NORD.md`](GRAND_NORD.md).

## The short version

Cameroon has far fewer health workers per person than our study threshold, but most households already have a phone. Rural women face the steepest barriers to care. The government has a legal basis for free emergency access over telecoms, and MINPOSTEL already runs a World Bank digital project. Vitamin Bob's design (missed call, callback, local-language triage, fixed rules) fits that gap. What is missing is a protocol reviewed by Cameroonian clinicians, French and Pidgin speech testing, and a confirmed emergency and clinic route in one district.

## 1. Tech and telco infrastructure

| What | Value | Year | Status |
|---|---|---|---|
| Mobile subscriptions | 108 per 100 people | 2024 | verified (WDI) |
| Households with a mobile phone: total / urban / rural | 85% / 94% / 74% | 2018 | verified (DHS) |
| Women who own a phone: total / rural | 64% / 42% | 2018 | verified (DHS) |
| Population covered by 2G+ / 3G-4G | about 88% / about 75% | 2023 | verified, secondary (ITU via press) |
| Internet users | 46% | 2024 | verified (WDI) |
| Household internet access: total / rural | 16% / 7% | 2018 | verified (DHS, quoted by MINPOSTEL) |
| Mobile market: Orange / MTN / Camtel | 50% / 47% / 3% | 2024 | verified, secondary (ART via press) |
| Electricity: total / urban / rural | 72% / 96% / 43% | 2024 | verified (WDI) |

Reading (inferred): voice coverage is far wider than internet use, especially in rural areas. A voice-first service reaches people an app cannot. Two operators carry 97% of subscribers, so a free number needs only two commercial agreements plus Camtel. Rural power is the hub constraint, not the patient's phone.

Gap to watch (inferred): only 42% of rural women own a phone. A household phone may be shared or held by a man, which affects who can call and privacy.

Policy hooks (verified, MINPOSTEL's April 2024 ITU presentation):
- Decree 2013/0398/PM puts **free access to emergency services** inside universal service.
- Operators pay **3% of pre-tax revenue** into the Special Telecommunications Fund (FST), which has universal service and rural coverage windows.
- Target: every community over 200 people has a public access point within 3 km.

## 2. Health infrastructure

| What | Value | Year | Status |
|---|---|---|---|
| Doctors + nurses per 10,000 (project threshold 44.5) | 7.5 | 2022-24 | verified (WHO GHO) |
| Physicians per 1,000 (WDI) | 0.14 | 2022 | verified; differs from WHO GHO 0.09, reconcile before use |
| Health pyramid | 10 regions, 189 districts, about 1,800 health areas | 2016 map | verified, may be outdated |
| Public facilities: health centres / hospitals | 2,829 / 184 | Maina 2019 | verified |
| UHC service coverage index | 48 | WHO GHO | verified |
| Health spending per person / out-of-pocket share | USD 79 / 68% | 2023 | verified (WDI) |
| National HMIS | DHIS2 nationwide since 2015 (2014 in other sources) | | verified, secondary |
| Digital health strategy 2026-2030 | about USD 51 million | 2026 | verified, secondary |
| Universal health coverage (CSU) phase 1 | launched April 2023 in Est; 5 regions | 2023 | verified, secondary |

Public facilities by type (Maina et al. 2019, 3,061 Cameroon facilities, verified): 2,241 integrated health centres, 362 listed as health centres, 223 district medical centres, 165 district hospitals, 14 regional, 3 general and 2 central hospitals, 48 dispensaries.

Benchmarks against Sub-Saharan Africa (SSA) and lower-middle income (LMIC), WDI API, verified (`wdi_benchmarks.csv`):

| Measure | Cameroon | SSA | LMIC | Year |
|---|---|---|---|---|
| Physicians per 10,000 | 1.4 | 2.5 | 7.1 | 2022 |
| Nurses and midwives per 10,000 | 6.6 | 16.2 | 16.5 | 2022 |
| Health spending per person, USD | 79 | 79 | 85 | 2023 |
| Out-of-pocket share of spending | 68% | 30% | 47% | 2023 |
| Births with skilled attendant | 69% | 64% | 77% | 2018 / 2019 |
| Under-5 deaths per 1,000 births | 65 | 71 | 44 | 2024 |

Reading (inferred): spending per person is at the regional average, but households carry more than twice the regional out-of-pocket share and the workforce is less than half the regional level.

### Tech backbone (added 2026-11-03)

| What | Value | Year | Status |
|---|---|---|---|
| Submarine cables | SAT-3, WACS, SAIL, NCSCS (Kribi, Douala) | 2021 | verified, secondary |
| National fibre backbone | close to 12,000 km (Camtel) | 2021 | verified, secondary |
| Council towns with a fibre point | about 25% of 360 | 2020 | verified, secondary (Camtel document) |
| Account ownership incl. mobile money | 61% (SSA 55% in 2021, LMIC 70%) | 2024 | verified (WDI) |

Not found: a reliable mobile-money-only rate, ITU price baskets for Cameroon, tower counts, district coverage maps.

### Readiness by region (added 2026-11-03)

`regions_cmr.csv` joins DHS 2018 regional measures with public facility density (Maina 2019 counts / region area). Est is in the weakest third of the ten regions on six of seven measures (calculated, inferred): power, household phones, women's phones, facility density, distance and timely fever care. Nord and Extrême-Nord have weaker phone and power coverage. Centre and Littoral DHS values exclude Yaoundé and Douala; North-West and South-West were surveyed during the crisis.

## 3. Access to care

DHS 2018 (EDSC-V), women 15-49 and children under 5. All verified from the DHS API.

| | Total | Rural | Est region |
|---|---|---|---|
| Women: any problem accessing care | 72% | 82% | 90% |
| Women: getting money | 67% | 77% | 88% |
| Women: distance to facility | 40% | 55% | 64% |
| Child with fever: care sought at all | 61% | 56% | 36% |
| Child with fever: care sought same or next day | 34% | 26% | 15% |
| Malaria prevalence, children 6-59 months (RDT) | 24% | 32% | 35% |
| Households with a mobile phone | 85% | 74% | 75% |

Other burden (verified, WDI): under-5 mortality 64.8 per 1,000 (2024); malaria incidence 260 per 1,000 at risk (2024); maternal mortality 258 per 100,000 (2023); TB 132 per 100,000 (2024).

Reading (inferred): in Est, three in four households have a phone but only one in seven feverish children reaches care within a day. That gap between phone reach and timely care is what Bob is built for. Bob's current protocol already covers fever, cough and diarrhoea.

## 4. Tech feasibility

| Bob today (repo, verified) | Cameroon need | Work needed | Status |
|---|---|---|---|
| Hindi, Gujarati | French (about 58% speak it), English (about 25%), Pidgin in NW/SW, Fulfulde in the north (2005 census, Ethnologue) | Test Gemma 4 E2B on French and Pidgin call audio; keypad-first fallback for other languages | needs test |
| Prompts generated with Sarvam TTS | Cameroonian voices | Record human voice clips (Bob only plays fixed clips) | inferred cheap |
| Emergency line 108 | 112 / 119 SAMU reported | Confirm which line answers in the pilot district | guessed |
| IMCI-draft protocol, not clinician-reviewed | Malaria-heavy, child fever | MINSANTE clinician review; add malaria RDT referral wording | needs review |
| Android phone + SIM + laptop per district | Rural electricity 43% | Solar kit per hub; cost it | inferred |
| Patient gives missed call, service pays callback | Missed calls ("bip") are familiar | Toll-free or zero-rated short code with Orange and MTN | inferred |
| Records sync over loopback / SMS (over-air not validated) | DHIS2 is the national system | Keep pilot standalone; DHIS2 export is a later step | design only |

## 5. How Vitamin Bob fits (inferred, for discussion)

**A pilot in one health district**, chosen with MINSANTE. Est is a strong candidate: highest barrier rates in the survey, three in four households with a phone, and the first CSU region. The North-West and South-West have different security and language conditions and need separate judgement.

**Who does what**
- MINSANTE and district team: protocol review, clinic list and hours, referral and emergency route, clinician alerts.
- MINPOSTEL and operators: free short code, zero-rating of callbacks, coverage data for the district; possibly under universal service or FST.
- World Bank: link to a health operation and the digital project (P173240, run by MINPOSTEL), plus evaluation design.
- Vitamin Bob team: adapt languages and clips, run the hub, report.

**What to measure**: share of callers routed; time from first call to care; urgent cases caught (with clinician review); clinician time saved per case; callback cost per case. The project has not measured any of these yet.

**Not claimed**: clinical safety, outcomes, or performance outside the team's synthetic and recorded tests.

## Open gaps

- Travel time to the nearest facility (Malaria Atlas Project raster), not yet computed.
- ART's own 2024 report, and ITU DataHub coverage figures, instead of press summaries.
- Call and SMS tariffs to price the callback.
- Current count of health districts and CSU status in 2026.
- Active World Bank health operations in Cameroon in 2026 (HeSP3 reported, not confirmed).
