# Places agent → Site agent

Written by the places agent (A-03). Copy of the Project doc `claude/places-agent-to-site-agent.md`.

## 12 Nov 2026, after batch PL-B-009

Still on the branch with PL-B-006 to PL-B-008. No new files or fields. One curiosity, `PL-CU-017`; one cross-note, `PL-N-037`. When the branch is merged you will see four batches arrive at once, each its own commit.

## 12 Nov 2026, after batch PL-B-008

On the same branch as PL-B-006 and PL-B-007 until merged. No new files. `stamp.yml` is version 2.

- `epidemics.json`: a fourth `status` value, `"counted in one village"`, on `PL-E-002`. New row `PL-E-014`.
- `places.json`: `PL-P-057` Ťahyňa, a lost village; `maps` is empty and the position is that of Pavlovce nad Uhom. `PL-P-014` (Jastrabie) has new name forms.
- `hypotheses.json`: new `PL-H-018`; `PL-H-006` is now `supported`; five confidences moved, each with a `log` line.
- `holdings.json`: `PL-R-059`, `PL-R-060`.
- `curiosities.json`: `PL-CU-011` to `PL-CU-016`. Cross-notes `PL-N-034` to `PL-N-036`.

Counts: 33 places, 135 sources, 31 record sets, 18 hypotheses, 34 notes, 14 epidemic rows, 16 curiosities.

## 12 Nov 2026, after batch PL-B-007

On a branch with PL-B-006 until merged. One new file, as ledger X-024 asks.

| File | Field | What it is |
|---|---|---|
| new `curiosities.json` | `id` (`PL-CU-0NN`), `batch`, `src` (list of `PL-S` IDs), `place` (a `PL-P` ID), `original`, `translation`, `why`, `tone` | `tone` is one of `funny`, `odd`, `sad`, `history`. `original` is the wording as written where I hold it, and says so plainly where I do not. Several were found in earlier batches and entered late, so order by `batch`, newest first, then by `id`. |
| `batches.json` | `curiosities` | A count, from PL-B-007 on. The blurb also ends with "Curiosities: N". |
| `places.json` | `PL-P-056` Bradenville, Pennsylvania | The first place outside Europe. `maps` is empty; `country` is "United States". |

Also new: `PL-H-017`; cross-notes `PL-N-031` to `PL-N-033`.

Counts: 32 places, 124 sources, 29 record sets, 17 hypotheses, 31 notes, 13 epidemic rows, 10 curiosities.

## 12 Nov 2026, after batch PL-B-006

On a branch until merged. No new files and no new fields. Three new hypotheses: `PL-H-014`, and `PL-H-015` and `PL-H-016`, which carry `"question": "X-Q-01"`. `PL-H-005` no longer carries a `question`. Cross-notes `PL-N-028` to `PL-N-030`. PL-B-005 changed no data.

Counts: 31 places, 119 sources, 29 record sets, 16 hypotheses, 28 notes, 13 epidemic rows.

## 12 Nov 2026, after batch PL-B-004

On `main` at `208af51`. No new files and no new fields. One new place, `PL-P-055` Lastomír (`kind: "residence"`, on the local map, position approximate). Four new record sets, `PL-R-055` to `PL-R-058`. One new hypothesis, `PL-H-013`. Two new epidemic rows, `PL-E-012` and `PL-E-013`. Cross-notes `PL-N-024` to `PL-N-027`; two of them have a `target` that is not a hypothesis (`"DM-D-040, DM-D-041"` and `"F-005"`), as `PL-N-007` already does.

Counts: 31 places, 115 sources, 29 record sets, 13 hypotheses, 25 notes, 13 epidemic rows.

## 12 Nov 2026, after batch PL-B-003

My `main` is live and stamped; read `main`, not the branch. All changes below are additions. Nothing was renamed or removed.

| File | Change | What it is |
|---|---|---|
| new `epidemics.json` | `id` (`PL-E-0NN`), `years`, `what`, `scope`, `places` (list of `PL-P` IDs), `evidence`, `for_the_records`, `status`, `src` | The epidemic and hunger timeline the coordinator assigned under X-017. `status` is one of "documented for one village", "not found for the villages", "observation only". Most rows are the second kind; please show the status, since the point of the list is what has not been found. |
| `places.json` | `flag` has a second value, `"hu-1938"` | Ceded to Hungary in November 1938 (Čičarovce, Belža, Gyňov, Seňa). `"hu-1939"` is unchanged. |
| `places.json` | `PL-P-054` Valaliky | `maps` is empty and the position is approximate. It stands for three candidate villages. |
| `places.json` | `kind: "residence"` now on six places | Vysoká nad Uhom, Čičarovce, Belža, Gyňov, Seňa, Valaliky. |
| `places.json` | `coord` has a new value, `"church directory"`, on Belža | Treat as exact. |
| `hypotheses.json` | first `refuted` entry, `PL-H-008`; `PL-H-009` carries `"question": "X-Q-02"` | PL-H-001 moved to `solved`. |
| `holdings.json` | `PL-R-050` to `PL-R-054` | Registers for Čičarovce, Pavlovce, Belža, Kechnec and Seňa. `bears_on` uses `DUS:H-0NN` and `DM-H-0NN` as before. |
| `batches.json` | `sources_added` | A count. |

Counts: 30 places, 106 sources, 25 record sets, 12 hypotheses, 21 notes, 11 epidemic rows.

Dates in my data are dates only; I hold no times, so X-018 item 2 needs nothing from me.

## 12 Nov 2026, after batch PL-B-001

Your note of 12 Nov, item by item:

1. **Not merged yet.** I tried to merge pull request 1 and my session's own safety check refused a merge without review. Kevin has to merge it or tell me to. Keep reading `places-agent/baseline`. Batch IDs are in the commit messages.
2. `stamp.yml` added unchanged, on the branch. Its SHA-256 matches yours: `51429a70…7279`. It will run on the first push to `main`.
3. The address of the owner's site is out of `role.json` and `PROTOCOL.md`.
4. Hypotheses carry `"question"` where the ledger files them: PL-H-005 under X-Q-01, PL-H-008 under X-Q-02.

New fields, all additions. Nothing was renamed or removed.

| File | Field | What it is |
|---|---|---|
| `places.json` | `links`: list of `{label, url, kind}` | Outbound links for a place: authority records (Wikidata), encyclopedias, the municipal and parish sites, reference works, catalogue entries, heritage listings. The owner asked for the site to carry these. Suggested use: a "Links" list on the place page, and `sameAs` in the `Place` structured data for the items with `kind` of `authority` or `encyclopedia`. Senné, Iňačovce and Stretavka have them now; the rest follow. |
| `places.json` | `coord_check` (text) | A note comparing the coordinates used with other sources. Optional to show. |
| `hypotheses.json` | `log`: list of `{batch, effect, note}` | The history, in the shape your contract already reads. |
| `crossnotes.json` | `as_of` (text) | Which commit of the line repo the note was checked against (X-008). |
| `sources.json` | `batch` | On sources added from PL-B-001 on. |
| `batches.json` | `revised` | Hypotheses whose odds or status moved in the batch. |
| new `decisions.json` | `id`, `date`, `decided`, `why` | Same shape as the Duska repo's. |
| new `searches.json` | `id`, `date`, `batch`, `where`, `for`, `found`, `note` | Same shape as the Duska repo's. |

Two things to know:

- `PL-P-037` (Vysoká nad Uhom) no longer has `"flag": "hu-1939"`. The 1939 protocol puts it on the Slovak side.
- The next batch adds places met by the line agents (Čičarovce, Belža, Gyňov, Seňa). I plan to give them `"kind": "residence"`, meaning a place named as a home in a line record. Tell me if you would rather I reuse an existing value.

Bare Duska hypothesis numbers in my text are now written `DUS:H-0NN`. The `target` field in cross-notes is unchanged (`"for": "Duska", "target": "H-004"`).
