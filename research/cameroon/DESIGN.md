# Cameroon pilot deck: design guide

How the 8-slide Vitamin Bob Cameroon deck is built, so new slides match it. The slides and speaker notes are kept outside this repo. Every number on them has a row in [`sources.csv`](sources.csv).

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
- Numbered exhibits run across the deck (Exhibit 1 to 8), with their title at 24px, weight 600.
- Footer pinned at bottom 56px: clickable sources in mono 24px on one line, page number at right ("03 / 08").
- Nothing under 24px. Status is always said in words as well as colour.
- Solid green box = in place or built; dashed purple box = gap or adapt.

## Order

| # | Slide | Exhibits |
|---|---|---|
| 1 | Cover and executive summary | |
| 2 | 01 The access gap | 1 dumbbell by region |
| 3 | 02 The health system | 2 pyramid, 3 benchmarks |
| 4 | 03 Tech infrastructure | 4 cable-to-caller chain, 5 benchmarks |
| 5 | 04 The rails | 6 reach bars, 7 market share |
| 6 | 05 Readiness by region | 8 weakest-third table |
| 7 | 06 The product | Six-step flow, alert screenshot |
| 8 | 07 The proposal | Partners, phases, three asks |

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
