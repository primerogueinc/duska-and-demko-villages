# Duska and Demko villages: protocol and current state

This file tells any analyst (human or AI) how this repository is worked and where things stand. Read it before touching the data.

## What this is

The places side of a three-part rebuild of Kevin J.S. Duska Jr.'s paternal line:

| Agent | Repo | Covers |
|---|---|---|
| A-01, Duska agent | `genealogu-duska-1` | The father's-father line |
| A-02, Demko agent | `genealogy-demko-1` | Maria Demko and her line |
| A-03, places agent | `duska-and-demko-villages` (this one) | Senné, Iňačovce and every place the other two meet |

The line agents work from Kevin's archive, one desktop folder at a time. This agent works from public sources and from their boards, and feeds place evidence back to them.

## Rules

1. Places, jurisdictions and record holdings only. No ancestor is named here; people belong to the line repos.
2. Every statement about a place cites a source ID from `data/sources.json`. Anything recalled from training and not checked carries the source `training` and shows as such on the page.
3. `data/sources.json` says how each source was read (page read, search extract, catalogue record only, second-hand). Do not upgrade that without reading the source.
4. A place fact can lean on a line hypothesis. It cannot solve one. Notes go in `data/crossnotes.json` with a lean and a next step; the line agent rules on its own board.
5. Place hypotheses (`PL-H-…`) have a confidence, a basis and a named test. Statuses: open, supported, solved, refuted. Log every change.
6. Blind test. Do not read Kevin's published tree or his one-name study site. Only the Scorer reads them. Do not read the Scorer's output either. Research agents sent out from here work under the same exclusions and search no family surname (ledger X-011).
7. Coordinates: GeoNames or Wikipedia where available. A village placed from memory has `"coord": "approximate"` and is drawn hollow. Distances are computed in `build.py`, never typed by hand.
8. Living people: none appear in this repo.
9. After any data change run `python3 build.py` and commit `index.html` with the data.

## Layout

    data/        places, jurisdictions, holdings, hypotheses, crossnotes, timeline,
                 batches, requests, sources, role, basemap (all JSON)
    interagent/  copies of notes sent to the other agents
    research/    briefs and summaries of research passes
    .github/     stamp.yml, copied unchanged from the Site agent
    site/        template.html
    build.py     validates source references, computes distances, builds index.html
    index.html   the front end (static, data inlined)

ID prefixes: `PL-P` place, `PL-S` source, `PL-R` record set, `PL-H` hypothesis, `PL-N` note for a line agent, `PL-B` batch, `PL-Q` request, `PL-DEC` decision, `PL-SR` search.

## Current state (2026-11-12)

- Batches PL-B-000 (baseline) and PL-B-001 (Senné in depth). Work is on `main`. Ledger v2 read.
- 25 places, 66 sources, 20 record sets, 16 notes for the line agents. Decisions in `data/decisions.json`, searches in `data/searches.json`, research briefs in `research/`.
- Hypotheses: PL-H-002 solved. PL-H-001, PL-H-003 and PL-H-004 supported. PL-H-005 (X-Q-01), PL-H-006, PL-H-007 and PL-H-008 (X-Q-02) open.
- Headline findings: the two villages were never one parish, and close to a third of Senné was Greek Catholic and registered at Iňačovce. Senné was in the Nagykapos district and Iňačovce in the Szobránc district. Both stayed in Slovakia in 1938-1945. The catalogued Senné register begins baptisms only in 1866.
- Places carry a `links` list (label, url, kind). Cross-notes carry `as_of`. Hypotheses carry `log` and, where the ledger files them, `question`.
- Not yet done: the other villages met by the line agents (Vysoká nad Uhom, Čičarovce, Belža, Gyňov, Seňa) and a full pass on Iňačovce; six village positions are still approximate.

## When a line agent finds a place

Add it to `places.json`, cite where it was met (`PL-S-031` plus the agent's document ID in the fact text), and check whether it moves a place hypothesis. A house number, a residence written in a register, or an archive call number on an image is worth a note here.
