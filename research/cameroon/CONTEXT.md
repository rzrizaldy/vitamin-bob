# Cameroon pilot deck: working context

A record of how the Cameroon deck grew from 8 to 14 slides on 2026-11-05: what was merged in, what was researched, which numbers were changed, and what is still open. It covers the work done in Claude Code that day. Meet's parallel chat (MIS 2022 update, regional dashboard, Grand Nord slide plan) is saved separately in [`GRAND_NORD.md`](GRAND_NORD.md). It recommends Nord and Extrême-Nord over Est, so the two need reconciling before the deck goes out.

Speaker notes stay out of this repo (see [`DESIGN.md`](DESIGN.md)). This file summarises them but does not copy them.

## Links

| What | Where |
|---|---|
| Deck (Claude Slides, private, shared by Rizaldy) | https://claude.ai/artifact/LxWHdT5jeZ7aW7E4kRtgbV |
| Repo branch | `rizaldy_cameroon_research`, folder `research/cameroon` |
| Design guide | [`DESIGN.md`](DESIGN.md) |
| Research brief | [`README.md`](README.md) |
| Sources for every number | [`sources.csv`](sources.csv) |
| Health research deck merged in | `health research/Cameroon_Healthcare_Research_9_Slides.pptx` (local only, not in the repo) |

## What happened

1. Pulled `research/cameroon` from the branch and set the project folder up as a sparse git clone of that folder only (`git sparse-checkout set --no-cone '/research/cameroon/'`), so `git pull` works.
2. Read the 9-slide health research deck. Each slide is a single 506x335 image, so the content was read visually, not extracted as text.
3. Got edit access to Rizaldy's 8-slide deck and redid the health research in his design system instead of pasting images.
4. Researched current figures (malaria, programmes, districts, security) and logged each one in `sources.csv` (rows B01 to B11, S01 to S04).
5. Added four evidence slides, then a region map, two real photos, an executive summary and a gap and moat slide. Renumbered labels, exhibits and page numbers throughout.
6. Checked the new and changed slides in a local render (overflow, footer on one line, nothing past y 930). The live deck was not viewed because the browser pane is not signed in to claude.ai.

## Second pass: 17 slides (later on 2026-11-05)

Decision: the deck shows **both Est and Nord** as candidate pilot regions and asks MINSANTE to choose. The current order is in [`DESIGN.md`](DESIGN.md).

What changed:

- **New slide 5, Why families skip care (Exhibit 2):** MIS 2022 Table 4.5. No money 46.9%, not serious 43.6%, too far 4.2%. It maps each reason to what Bob does: core job, one clip, not Bob's lever.
- **New slide 13, Two candidate sites (Exhibit 15):** Est vs Nord, with Extrême-Nord for reference, on seven MIS 2022 measures, plus "Est: Bob as built" and "Nord: Bob adapted, health workers call".
- **New slide 16, Measuring impact (Exhibit 17):** metrics with 2022 baselines for Est and Nord, a comparison district, and a clinician review of every call.
- **Summary:** the gap is now 13% (2022) and names money and severity, not distance. The ask is Est or Nord, starting with a French keypad line and a free-care message.
- **Access gap slide:** "64% cite distance" replaced by "money tops the list (88%)"; the notes explain perceived vs actual barriers.
- **Proposal:** phase 1 is now "Protocol review, French keypad line, free-care clip, short code".
- **Renumbering:** labels 01 to 14, Exhibits 1 to 17, pages "/ 17".

Every new number was checked in the MIS 2022 report and logged as `sources.csv` rows M01 to M12. Two findings strengthen the free-care clip: free under-5 malaria treatment has been law since 2011 and 2014, yet only 5% of treated children got care free.

## First pass: 14 slides

| # | Id | Label | Takeaway | Exhibits | Origin |
|---|---|---|---|---|---|
| 1 | `cover` | Pilot proposal | Free voice triage for Cameroon: a one-district pilot | | Rizaldy |
| 2 | `summary` | Executive summary | Phones and malaria tools exist; the missing piece is a fast, free route from a sick child to the right clinic | | New |
| 3 | `moat` | The gap and our moat | Each channel misses part of the gap; Bob combines free voice, a local model and fixed rules | Comparison table (unnumbered) | New |
| 4 | `gap` | 01 · The access gap | Phones are in most homes, timely care is not; Est is furthest behind | 1 | Rizaldy |
| 5 | `burden` | 02 · The disease burden | Infections cause half of deaths; malaria leads with about 3M recorded cases | 2, 3 | New (health deck slides 1 to 3) |
| 6 | `malaria` | 03 · Malaria care today | Prevention, testing and treatment exist; the weak link is reaching a test in time | 4, 5 | New (health deck slides 4, 5) |
| 7 | `health` | 04 · The health system | A deep pyramid on a thin workforce and household money | 6, 7 | Rizaldy |
| 8 | `network` | 05 · Tech infrastructure | Backbone in place; last mile and power are the gap | 8, 9 | Rizaldy |
| 9 | `rails` | 06 · The rails | Voice reaches nearly everyone; data and power do not | 10, 11 | Rizaldy |
| 10 | `regions` | 07 · Readiness by region | Est is in the weakest third on six of seven measures | 12 | Rizaldy |
| 11 | `safety` | 08 · Security and access | Three regions need separate judgement; Est needs a security check | 13 (map) | New (health deck slide 7) |
| 12 | `bob` | 09 · The product | Missed call to routed case: the model listens, fixed rules decide | | Rizaldy |
| 13 | `questions` | 10 · What we still need to learn | Four questions to answer in the district before going live | 14 | New (health deck slides 8, 9) |
| 14 | `pilot` | 11 · The proposal | A small, evaluated pilot in one health district | | Rizaldy |

Deck sections: s1 summary, gap and moat (cover to moat); s2 the evidence (gap to safety); s3 product, open questions and proposal (bob to pilot).

## How the 9 health slides were used

| Health deck slide | Where it went |
|---|---|
| 1 Country context | Facts already on Rizaldy's slides; conflicting numbers checked (below) |
| 2 Disease burden | Slide 5, Exhibit 2, with sourced WDI figures instead of the 40/60 split |
| 3 Malaria threat | Slide 5, Exhibit 3 |
| 4 Prevent, test, treat pathway | Slide 6, Exhibit 4, plus the "reach care in time" step where Bob fits |
| 5 Programmes (RTS,S, NMCP, mMIST) | Slide 6, Exhibit 5, plus seasonal chemoprevention |
| 6 Tiered system and gaps | Already covered by Rizaldy's health system slide |
| 7 Geography and safety map | Slide 11, rebuilt as a region map with 2025 to 2026 UN data |
| 8 Research questions | Slide 13, Exhibit 14 |
| 9 Stakeholders and research needs | Slide 13, merged into the "who to engage" column |

The health deck's images (mosquito, vaccine vial, generated map) were not reused. Real, credited photos replace them.

## Numbers changed or dropped

| Claim | Health deck | Used in the deck | Why |
|---|---|---|---|
| Health districts | 205 | 189 on slide 7 (Rizaldy, 2016 map) | No source found for 205; UNAIDS 2024 boundaries give about 200. Slide 7 should be updated. |
| Out-of-pocket share | 61% | 68% | WDI 2023 (Rizaldy's figure) |
| Population | 28.4M (2023) | 29.9M (2025, WDI) | Newer figure |
| Causes of death | 40% NCD / 60% communicable (2023) | 38 / 52 / 10 with injuries (2019, WDI) | No source found for the 40/60 split |
| Malaria share of under-5 deaths | 14% | Dropped | No source found yet; noted as guessed |
| Malaria deaths 2024 | 2,016 | 2,016, labelled recorded | Single press source (NMCP via Cameroun Actu Online); confirm with NMCP |

## New research, with status

Detailed rows with URLs are in `sources.csv`.

**Disease burden**
- Deaths by cause, 2019 (WDI, verified): communicable, maternal, newborn and nutrition 51.8%; non-communicable 37.7%; injuries 10.5%. WHO's 2014 NCD profile gave 31%.
- Malaria (verified, secondary unless noted): about 3.0M cases recorded in facilities in 2024; 2,016 recorded deaths in 2024, against about 4,500 in 2019 and 1,756 in 2023; WHO estimate about 11,600 deaths in 2023 (primary); Nord and Extrême-Nord hold nearly 60% of under-5 malaria deaths (Malaria Journal 2023).
- Malaria prevalence in children 6 to 59 months, DHS 2018 (verified): national 24.0%; Centre 46.8, Est 35.3, Sud 33.4, Adamaoua 32.2, Nord 26.0, Extrême-Nord 21.8, Littoral 20.6, Ouest 15.8, Sud-Ouest 9.8, Nord-Ouest 9.5. Centre and Littoral exclude Yaoundé (14.4) and Douala (7.8).

**Programmes**
- RTS,S malaria vaccine: routine rollout from 22 January 2024 in 42 health districts, four doses (verified, secondary). Early first-dose coverage about 70%, later doses lower (Nigeria Health Watch 2025).
- Seasonal malaria chemoprevention: 2,162,984 children in Nord and Extrême-Nord in 2025, funded via GiveWell after US funding was disrupted (Jhpiego, verified).
- National Malaria Strategic Plan 2024 to 2028 exists (MESA); its referral chapter has not been read.
- mMIST: clinician-to-clinician maternal helpline, piloted in Ndop (North-West) from March 2022, then 16 districts, 566+ calls, 1,148+ providers trained (UAB, verified). It serves clinicians, so it complements Bob.

**Security and access (2025 to 2026)**
- 2.9M people need humanitarian aid in 2026: 1.4M in Extrême-Nord, 1.1M in North-West and South-West, 337,000 Central African and urban refugees (OCHA HNRP 2026, verified).
- North-West and South-West: at least 269 access constraints in 2025; Monday ghost towns, lockdowns, IEDs (OCHA, verified).
- Over 288,000 refugees from the Central African Republic in Est, Adamaoua and Nord (UNHCR, undated).
- 30 incidents of violence against or obstruction of health care in 2025; 18 health workers kidnapped (Insecurity Insight, verified).

## Judgements to discuss (inferred)

- **Map status per region:** Extrême-Nord not for phase 1; North-West and South-West separate judgement; Est the pilot candidate after a district security check; Adamaoua and Nord caution; Centre, Littoral, Ouest and Sud feasible but with a smaller gap.
- **Channel comparison (slide 3):** smartphone app, staffed hotline, SMS service and Bob rated on six needs of a rural caregiver with a basic phone. This compares types of channel, not named products. No full scan has been done for other patient-facing call lines in Cameroon.
- **Moat:** two parts built (safety by design: the model never sets urgency and unclear calls go up; cheap to run: a phone and laptop hub with the model running offline) and one still to build (MINSANTE rules, district clinic lists, an operator short code). "Cheap to run" has not been costed, solar included.
- Never claimed: clinical safety, patient outcomes, French or Pidgin performance, or any agreed partnership.

## Assets added to the deck

- Photos, public domain, US President's Malaria Initiative (Jhpiego/D. Burke, Kribi District, January 2015), via Wikimedia Commons:
  - [Children under a treated bed net](https://commons.wikimedia.org/wiki/File:Children_under_mosquito_net_(26483462482).jpg), slide 5
  - [Nurse counselling mothers on malaria](https://commons.wikimedia.org/wiki/File:Jhpiego_3_(26549668746).jpg), slide 13
- Region map: [geoBoundaries](https://www.geoboundaries.org/) CMR ADM1 simplified GeoJSON (CC BY 3.0), projected with a cos(7°) longitude correction, points under 2.2 px apart dropped, drawn as a 16 KB inline SVG. Labels inside the larger regions; leader lines for Nord-Ouest, Ouest, Sud-Ouest, Littoral and Extrême-Nord.
- Map colours: `#72419b` not for phase 1, `#c7a9e0` separate judgement, `#0f6b31` candidate, `#fcd116` caution, `#9fb3a5` feasible. Each status is also written in words.

## Devil's advocate review (2026-11-05)

Where the plan is weakest:

1. **Wrong main problem.** In MIS 2022, mothers who skipped care cite no money (47%) and not thinking it was serious (44%); only 4% say the facility is too far. Bob addresses severity only, so at most about half the gap.
2. **Families' first stop is not a clinic.** About two in three feverish children got medicine with no health worker's advice. Bob routes to clinics most families are not going to.
3. **Language is the hard part.** Bob speaks Hindi and Gujarati; the north needs Fulfulde, and about a third of women there can read. No Cameroonian language has been tested.
4. **Half the target group cannot call.** 46 to 49% of women in the north own a phone.
5. **The moat is not built yet.** Fixed-rule phone triage can be copied; the durable part (short code, reviewed protocol, clinic list) does not exist yet.
6. **No real-patient evidence.** Only team-written cases and team recordings.
7. **Two regions in play.** This deck says Est; GRAND_NORD.md says Nord.

The MIS 2022 figures here come from Meet's chat and are not yet re-checked.

## Quick wins

| # | Quick win | Effort | Why it is easy |
|---|---|---|---|
| 1 | Fix the deck's weak claims: drop "64% cite distance", use 2022 numbers, pick one region | Hours | Material is in GRAND_NORD.md |
| 2 | Recompute regional indicators from the MIS 2022 microdata | 1 to 2 days | Free on the World Bank Microdata Library (`CMR_2022_MIS`) |
| 3 | Start with community health workers calling, not mothers | Small design change | 82% (Extrême-Nord) and 74% (Nord) of women know one; CHWs speak French and have phones |
| 4 | Keypad answers in French, no speech AI, for the pilot | Already built | Bob's keypad questions exist; takes the untested speech model off the critical path |
| 5 | One clip: malaria treatment for under-5s is free | One recording | Hits the 47% "no money" reason; only 16% of women in Est heard such a message. Confirm the policy with MINSANTE first |
| 6 | District clinic list with opening hours | A few calls | Useful alone (fewer wasted trips), and Bob needs it anyway |
| 7 | Ask Meet to share the dashboard | One message | Unblocks the regional data |

Recommended first step: a free, keypad-only French line for community health workers in one district, plus a free-care message for caregivers. Mother-facing calls and local-language speech come after the pilot.

## Open items

- Confirm the 2,016 malaria deaths with NMCP or the WHO World Malaria Report.
- Update slide 7's 189 health districts (about 200 on 2024 boundaries).
- Find a source for "malaria causes 14% of under-5 deaths", or keep it out.
- Read the National Malaria Strategic Plan's referral rules before drafting Bob's malaria test referral step.
- District-level security check for Est with MINSANTE and UN security.
- Cost a solar-powered district hub.
- Scan for any existing patient-facing call or IVR health line in Cameroon.
- View the live deck once signed in, to confirm the published rendering matches the local check.
- MINSANTE to choose between Est and Nord (the deck now shows both).
- Check the remaining MIS 2022 and other figures in `GRAND_NORD.md` (sections 2, 4 and 5) that are not yet in `sources.csv`.
- Update Exhibit 13 (readiness by region) and the map's malaria labels from DHS 2018 to MIS 2022 where regional values exist.
- Ask Meet to share the regional dashboard, or export its CSVs into this folder.

## Files changed in this folder (not committed)

- `sources.csv`: rows B01 to B11 and S01 to S04.
- `DESIGN.md`: photo and map credits.
- `CONTEXT.md`: this file.
- `GRAND_NORD.md`: Meet's chat (MIS 2022 update, dashboard summary, Grand Nord slide plan and metrics).
- `README.md`: links to both.
