# Cameroon pilot deck: design guide

How the 17-slide Vitamin Bob Cameroon deck is built, so new slides match it. The slides and speaker notes are kept outside this repo. Every number on them has a row in [`sources.csv`](sources.csv).

Audience: a World Bank health programme lead. The ask is a small, evaluated pilot in one health district.

## Style

Consulting-style and dense, but readable. Colours and fonts come from the Vitamin Bob website (`site/src/app/globals.css`).

| Token | Value | Use |
|---|---|---|
| Paper | `#fbfdf9` | Slide background |
| Ink | `#22322a` | Titles, body |
| Muted | `#4e6a55` | Captions, footers, secondary text |
| Purple | `#72419b` | Labels, key number, "gap" or "adapt" status |
| Panel green | `#e4f1df` | Callouts, built or in-place boxes |
| LCD green | `#c9e6c1` | Pyramid base |
| Status green | `#0f6b31` | BUILT and IN PLACE labels |
| Chart green | `#138a3e` | Voice bars, household phone dots |
| Shading | `#e3d3f0`, `#efe6f6` | Weakest-third cells, shaded table rows |
| Rules | `#b9c7bc`, `#d5ddd6`, `#9fb3a5` | Dividers, gridlines, connectors |
| Flag | `#007a5e`, `#ce1126`, `#fcd116` | Top stripe and cover flag |

Fonts: Space Grotesk (titles, body), IBM Plex Mono (labels, sources, numbers in value columns).

## Slide anatomy

- 1920x1080 canvas, padding `96px 128px 150px`; keep flow content above y 930.
- 12px Cameroon flag stripe across the top of every slide.
- Label: mono 24px, uppercase, 2px spacing, purple, numbered ("02 · The health system").
- Title: a full sentence stating the takeaway, 48px bold, line height 1.12, two lines at most.
- Numbered exhibits run across the deck (Exhibit 1 to 17), with their title at 24px, weight 600.
- Footer pinned at bottom 56px: clickable sources in mono 24px on one line, page number at right ("03 / 17").
- Nothing under 24px. Status is always said in words as well as colour.
- Solid green box = in place or built; dashed purple box = gap or adapt.

## Order

| # | Id | Slide | Exhibits |
|---|---|---|---|
| 1 | `cover` | Cover and executive summary | |
| 2 | `summary` | Executive summary (need, gap, fit, ask) | |
| 3 | `moat` | The gap and our moat | Channel comparison table (unnumbered) |
| 4 | `gap` | 01 The access gap | 1 dumbbell by region |
| 5 | `why` | 02 Why families skip care | 2 reasons bars (MIS 2022) |
| 6 | `burden` | 03 The disease burden | 3 deaths by cause, 4 malaria numbers |
| 7 | `malaria` | 04 Malaria care today | 5 care pathway, 6 programmes |
| 8 | `health` | 05 The health system | 7 pyramid, 8 benchmarks |
| 9 | `network` | 06 Tech infrastructure | 9 cable-to-caller chain, 10 benchmarks |
| 10 | `rails` | 07 The rails | 11 reach bars, 12 market share |
| 11 | `regions` | 08 Readiness by region | 13 weakest-third table |
| 12 | `safety` | 09 Security and access | 14 region map |
| 13 | `sites` | 10 Two candidate sites | 15 Est vs Nord table |
| 14 | `bob` | 11 The product | Six-step flow, alert screenshot |
| 15 | `questions` | 12 What we still need to learn | 16 open questions table |
| 16 | `metrics` | 13 Measuring impact | 17 metrics and baselines |
| 17 | `pilot` | 14 The proposal | Partners, phases, three asks |

Since 2026-11-07 the Claude deck opens with a 10-slide main deck: cover, context, causes, need, map, north, firstsite, bob, pilot, thanks. It has pages "N / 10", larger 56px titles and no exhibit numbers. The 17 slides above follow it as an appendix. The main deck's top 10 causes of death slide (`causes`) uses data from WHO data.who.int; see [`CONTEXT.md`](CONTEXT.md).

The deck brings two candidate pilot regions, Est and Nord, and asks MINSANTE to choose (decided 2026-11-05). See [`CONTEXT.md`](CONTEXT.md) and [`GRAND_NORD.md`](GRAND_NORD.md).

## Content rules

- No em dashes. Label claims verified, inferred or guessed.
- Never claim a partnership, clinical safety, patient outcomes, or that Bob already handles French or Pidgin.
- Credit photos on the slide that uses them, with a link to the source.
- Speaker notes: a spoken script first, then backup facts with exact figures. Keep notes out of this public repo.

## Photo credits

All from Wikimedia Commons, CC BY-SA 4.0:

- [Health clinic sign, Nkoulou](https://commons.wikimedia.org/wiki/File:Centre_de_sant%C3%A9_%C3%A0_Nkoulou.jpg), Eric Freyssinge
- [Patient registration, Ntemndzem](https://commons.wikimedia.org/wiki/File:Consultation_at_the_Catholic_Health_Post_at_Ntemndzem.jpg), Fotang
- [Phone accessories vendor](https://commons.wikimedia.org/wiki/File:Vendeur_ambulant_d%27accessoires_electroniques.jpg), Minette Lontsie

The dashboard screenshot on the product slide is from the team's India demo, with dummy cases.

Public domain, US President's Malaria Initiative (Jhpiego/D. Burke, Kribi District, 2015), via Wikimedia Commons:

- [Children under a treated bed net](https://commons.wikimedia.org/wiki/File:Children_under_mosquito_net_(26483462482).jpg) (disease burden slide)
- [Nurse counselling mothers on malaria](https://commons.wikimedia.org/wiki/File:Jhpiego_3_(26549668746).jpg) (open questions slide)

Region map outlines: [geoBoundaries](https://www.geoboundaries.org/) CMR ADM1, CC BY 3.0, simplified.
