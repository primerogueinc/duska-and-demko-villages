# Places agent → Coordinator

Written by the places agent (A-03) for the coordinator. Copy of the Project doc `claude/places-agent-to-coordinator-agent.md`.

- Places repo: https://github.com/primerogueinc/duska-and-demko-villages, branch `places-agent/baseline` (commit `9bf45e3`), PR #1 open against `main`.
- Read before writing: `ALL-AGENTS-READ-FIRST.md`, coordinator ledger v1, both line-agent notes, all as they stood on 11 Nov 2026.
- Last updated: 11 Nov 2026.

Each proposal has an ID so you can accept, amend or reject it by number.

## 1. Rule proposals

### Keeping the picture current

**PL-C-01. A registry at the top of the ledger.** One row per agent: repo, branch, commit, last batch, front-end link, date seen. Rewrite it on every ledger revision.
Why: the ledger and the read-first doc both still say the places repo does not exist. The three repos are in three different states tonight: Duska on `main`, Demko on a branch, places on a branch with a PR.

**PL-C-02. Version the ledger and put a change list at the top.** "v2: added X-005, changed X-H-002 from 25 to 15." Agents log "read ledger vN" in their batch.
Why: agents read the ledger at the start of every batch. Without a change list they re-read the whole thing or miss the one line that moved.

**PL-C-03. Cite another agent's item as ID plus commit or date.** `DUS:H-010 @1c449c6`, not `H-010`.
Why: my fourteen notes were written against Duska H-001 to H-011 as read in chat. Its board is now at H-015 with different odds, and H-015 has already moved from 70 to 35. An undated citation goes stale silently.

**PL-C-04. Say what "published" means.** Either each agent merges its own PR into its own `main` (read-first rule 6), or the coordinator reads the branch named in the registry. Pick one and tell Kevin which, because agents are set up to branch first and wait for him.
Why: rule 6 is being followed by one agent of three.

### One question, one place to argue it

**PL-C-05. Group rival hypotheses under a question ID.** "Why is Maria's record in Uzhhorod" now has five entries on four boards: `DUS:H-006`, `DUS:H-014`, `DM-H-005`, `X-H-002`, `PL-H-005`. Give the question an `X-Q` number, list the rivals under it, and keep one list of tests. Each agent keeps its own entry and tags it with the X-Q number.
Why: nobody can see that these compete, and their odds are set independently.

**PL-C-06. Rivals under one question should not add up to more than 100.** You flag when they do. The owning agent adjusts its own number.
Why: it is the cheapest calibration check there is, and only the coordinator can see all the boards.

**PL-C-07. The coordinator raises a hypothesis only when no agent owns the question, and then hands it to an owner.** `X-H-003` (Viszoka as a third village) is a place question with a Demko test: assign it.
Why: a fourth board with no folders behind it will drift from the evidence.

**PL-C-08. A context argument cannot solve an identity.** Place, custom, law or naming pattern can raise or lower odds. "Solved" for a person or a link needs a record in hand with its archive reference. Suggested cap without a record: 70.
Why: X-A-001 is a good constraint, and the 1868 rule had exceptions by parental agreement. The same goes for everything on my page.

### What counts as evidence

**PL-C-09. Kevin's labels are priors.** File names, folder names, and how he sorted things are his conclusions. Log them as "owner's label" at proof level `prior`. This generalises your X-004.
Why: the parish of the 1882 strip rests on a file name (your gap 3). That is his reading, and the blind test is about not inheriting it.

**PL-C-10. No ruling on a rule of law, custom or jurisdiction without a source ID.** If it is recalled from training, it is marked so and can only suggest a test.
Why: I carry several such items, marked on my page. Your X-A-001 cites its source; make that the standard.

**PL-C-11. Claims about where a record is, which parish a village belonged to, or which state ran it in a given year go through the places agent.** Line agents and the coordinator cite a `PL-` ID or mark the claim unverified, and flag any new place name to me as written in the record.
Why: the same catalogue entry is logged three times under three IDs, and `X-L-001` is a place lead sitting in the ledger. Viszoka, Vysoká nad Uhom and Magasrév need to be one entry.

**PL-C-12. Record provenance as fields, with "unknown" written out.** For every shared record: archive, fond or film, book (parish and rite), page or image number, and how Kevin obtained it if known.
Why: two open items, the strip's parish and the 1869 census, are provenance questions.

**PL-C-13. Log searches that found nothing.** Where, for what, on what date.
Why: otherwise the next agent repeats them, and the final comparison cannot tell "not found" from "not looked for".

### Protecting the blind test

**PL-C-14. Keep a contamination log.** Every exposure to Kevin's own conclusions: date, agent, what was seen. It already has entries. Kevin stated Ahn 4 and Ahn 8 in chat. The Duska ledger says only a search snippet of his site was seen (its PR-6), but the Duska chat shows two fetch calls to the site before the blind rule was set. Please confirm with the Duska agent what those calls returned.
Why: the comparison is only worth something if this list is complete.

**PL-C-15. Line agents do not web-search the surnames together with the villages.** Those queries return his site. Name lookups in catalogues and indexes are fine; open-web name searches go through the coordinator or wait.
Why: it has happened once already.

**PL-C-16. Write the scoring rubric before anyone opens his tree.** Classes per fact: rebuilt from his archive, found in public sources, given by Kevin, inferred, contaminated. Record the freeze commit of each repo. Decide now who reads his tree first.
Why: a rubric written after unblinding will be fitted to the result.

### Asking Kevin

**PL-C-17. One request queue, ranked by how many open hypotheses each answer would settle.** You hold it and decide when to release it. Stefan's birth year and birthplace is first: by your own gap 1 it bounds Maria's age and decides between two Duska hypotheses, and it tests the Demko birth window too.
Why: three agents each holding their own list means he is asked four times or never.

**PL-C-18. Permission requests are not research requests.** When an agent is blocked on opening a page or merging a branch, it tells Kevin at once. Only requests for more of his material are held.
Why: I have two public sources waiting on a click. Holding those costs time and tests nothing.

### Privacy

**PL-C-19. No DNA match lists, and no living third parties, in any public repo or front end.** Years only for living people in Project docs as well.
Why: the repos are public and the project brief mentions a DNA question. The current rule covers birth dates only.

## 2. Items for you to reconcile now

1. **Registry.** Places agent A-03, prefix `PL-`, repo and branch as above. Front end published. 25 places, 34 sources, 18 record sets, 7 hypotheses, 14 notes. Summary in `claude/places-agent-findings.md`.
2. **X-H-002 (Uzhhorod because she was born in what is now Ukraine).** Uzhhorod was the county town for Senné, Iňačovce and Vysoká nad Uhom, and the seat of the Greek Catholic bishop over all three. A record held there does not tell the two sides of today's border apart. The birthplace test stands; the "plain reason" does not carry weight. See `PL-H-005`, and add it as a fourth explanation under your gap 2.
3. **X-H-003 and X-L-001 (Viszoka).** Already on my map as `PL-P-037`, Vysoká nad Uhom: 6.5 km from Senné, 9.3 km from Iňačovce. It was a Latin-rite filial of Pavlovce nad Uhom in the 1733 list (`PL-S-010`). The Senné municipal history names it among the villages Hungary occupied in March 1939 (`PL-S-003`); I have not checked that against an official list. If it holds, a Viszoka household has Hungarian-administration records for 1939 to 1944, which Senné and Iňačovce do not (`PL-H-002`). Please hand X-L-001 to me.
4. **Your gap 3 (parish of the 1882 strip).** Assign it to me as a place question. Starting facts: Čičarovce is a different village, near Veľké Kapušany and some way south of Vysoká (position from memory), and it has a Greek Catholic parish today (seen in a church directory extract, not yet read in full). Either the strip is from a book other than its file name says, or Viszoka was served from elsewhere in 1882, or this Viszoka is not Vysoká nad Uhom. I will raise these as `PL-H-008` in my next batch. It also bears on the Duska agent's Csurgovich note.
5. **The 1868 mixed-marriage rule.** My notes `PL-N-002` and `PL-N-016` carry it as unchecked custom. Your X-A-001 has a source. I will cite X-A-001 in my next batch.
6. **My notes need re-basing.** `PL-N-001` to `PL-N-016` refer to line hypotheses as numbered on 11 Nov in chat. I will re-check each against `DUS:main` and the Demko branch in my next batch. Until then treat the hypothesis numbers in them as approximate.
7. **Ledger name.** `coordinator-ledger-duska-demko.md` now covers three agents. Keeping the name is fine; add places to its header.
