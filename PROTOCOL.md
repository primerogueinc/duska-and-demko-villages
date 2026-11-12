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
6. Blind test. Do not read Kevin's published tree or duskagenealogy.primerogueinc.com until the comparison phase.
7. Coordinates: GeoNames or Wikipedia where available. A village placed from memory has `"coord": "approximate"` and is drawn hollow. Distances are computed in `build.py`, never typed by hand.
8. Living people: none appear in this repo.
9. After any data change run `python3 build.py` and commit `index.html` with the data.

## Layout

    data/        places, jurisdictions, holdings, hypotheses, crossnotes, timeline,
                 batches, requests, sources, role, basemap (all JSON)
    interagent/  notes addressed to the Duska and Demko agents
    site/        template.html
    build.py     validates source references, computes distances, builds index.html
    index.html   the front end (static, data inlined)

ID prefixes: `PL-P` place, `PL-S` source, `PL-R` record set, `PL-H` hypothesis, `PL-N` note for a line agent, `PL-B` batch, `PL-Q` request.

## Current state (2026-11-11)

- Batch PL-B-000, baseline. 25 places, 34 sources, 18 record sets, 14 notes for the line agents.
- Hypotheses: PL-H-002 solved (both villages stayed in Slovakia 1938-1945). PL-H-001 and PL-H-003 to PL-H-007 open.
- Headline finding: the two villages were never one parish. Senné was the Roman Catholic parish (Eger, then Szatmár from 1804). Iňačovce was the Greek Catholic parish (Mukachevo eparchy, bishop at Uzhhorod) with a Reformed congregation. A family's village does not fix its church.
- Not yet done: the 1782-1787 Greek Catholic parish papers (PL-Q-001) and the FamilySearch catalogue locality lists (PL-Q-002) need the owner's approval to open; six village positions are approximate (PL-Q-004).
- Neither line repo had been pushed when this was built. Hypothesis numbers in `crossnotes.json` were read from the agents' chats; re-check them against their repos.

## When a line agent finds a place

Add it to `places.json`, cite where it was met (`PL-S-031` plus the agent's document ID in the fact text), and check whether it moves a place hypothesis. A house number, a residence written in a register, or an archive call number on an image is worth a note here.
