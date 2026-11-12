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

ID prefixes: `PL-P` place, `PL-S` source, `PL-R` record set, `PL-H` hypothesis, `PL-N` note for a line agent, `PL-B` batch, `PL-Q` request, `PL-DEC` decision, `PL-SR` search, `PL-E` epidemic or hunger year, `PL-CU` curiosity.

## Current state (2026-11-12)

- Batches PL-B-000 (baseline), PL-B-001 (Senné in depth), PL-B-002 (ledger v3), PL-B-003 (the line agents' villages), PL-B-004 (the archive's catalogue), PL-B-005 (ledger v14; no place data), PL-B-006 (ledger v16), PL-B-007 (ledger v18) PL-B-008 (ledger v19; third research pass), PL-B-009 (ledger v20), PL-B-010 (ledger v22; the Senné marriage book tested) and PL-B-011 (what 'Rusyn' means; a hypothesis given by the owner). PL-B-000 to PL-B-005 are on `main` and stamped (`641ba53`); a later batch is on a branch until merged. A merge needs the owner to say so in this agent's chat (PL-DEC-024).
- 33 places, 150 sources, 31 record sets, 38 notes for the line agents, 14 epidemic rows, 20 curiosities. Decisions in `data/decisions.json`, searches in `data/searches.json`, research briefs in `research/`.
- Hypotheses: PL-H-001 and PL-H-002 solved. PL-H-003, PL-H-004, PL-H-009 (X-Q-02), PL-H-010 and PL-H-012 supported. PL-H-014 and PL-H-017 supported. PL-H-006 supported. PL-H-005, PL-H-007, PL-H-011, PL-H-013, PL-H-018, and PL-H-015 and PL-H-016 (both X-Q-01) open. PL-H-008 refuted.
- Headline findings: the two villages were never one parish, and close to a third of Senné was Greek Catholic and registered at Iňačovce, shown by a record. The Viszoka of the line records is Vysoká nad Uhom; its Greek Catholics were registered at Čičarovce and its Roman Catholics at Pavlovce nad Uhom. Gyňov and Seňa were Greek Catholic filials of Belža. Volume numbers from the Prešov archive's catalogue are in `data/holdings.json` for every parish met so far.
- Places carry a `links` list (label, url, kind) and a `flag` (`hu-1938` or `hu-1939`). Cross-notes carry `as_of`. Hypotheses carry `log` and, where the ledger files them, `question`. Epidemic rows are `PL-E`.
- The coordinator's ledger is read at the start of every batch (X-025). Every batch blurb ends with a count of curiosities (X-024). DNA material is not opened (X-023).
- No online family trees are opened and the search of past chats is not used (X-011 item 7, X-021 item 4).
- This agent is blind (ledger X-021). It does not read the private repo of X-020, the open line's chats or documents, or memory notes about lines outside the test.
- Not yet done: which Iňačovce Greek Catholic volumes after 1898 survive (PL-Q-006); burial counts for the epidemic timeline (PL-Q-007); census sheets and tax lists for the new villages (PL-Q-008); the last pages of the catalogue (PL-Q-009); eleven village positions are approximate.

## When a line agent finds a place

Add it to `places.json`, cite where it was met (`PL-S-031` plus the agent's document ID in the fact text), and check whether it moves a place hypothesis. A house number, a residence written in a register, or an archive call number on an image is worth a note here.
