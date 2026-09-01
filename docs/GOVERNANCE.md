# iusethis Governance Charter

Governance-as-files: this charter, the titles registry, and every vote
live in the repository `iusethis/iusethis` and change only by pull
request. If it isn't merged, it isn't governance. (Pattern: GitHub's
Minimum Viable Governance — governance documents amended by recorded
vote — run entirely on GitHub controls, no tokens, no chain.)

## 1. Phases: full control now, handoff by design

Most founder-led projects never write a succession plan and improvise one
in a crisis. We write it on day one.

- **Phase 0 — Stewardship (now).** The Steward (Paul Richeson) holds all
  titles and final say, including veto. *Every* veto must be written into
  the proposal file it vetoes, with reasons — logged power is
  transferable power.
- **Phase 1 — Council.** Triggers automatically when five independent
  people (not delegates of the same person) hold titles. The Steward's
  veto becomes a tie-break only; formal votes decide.
- **Phase 2 — Handoff.** The Steward title itself becomes transferable by
  formal vote, or the Steward may resign it onto the council. Because
  everything — charter, titles, votes, content — is already files in an
  org-owned repo, handoff is a `git blame`-able event, not a migration.

## 2. GitHub controls as the voting machine

| Governance act | GitHub mechanism |
|---|---|
| Propose | PR adding `docs/proposals/NNN-title.md` |
| Discuss | The PR thread (pre-proposal: GitHub Discussions) |
| Vote | PR review — Approve = +1, Request changes = −1, comment = abstain with concern |
| Who binds | Holders of titles in `docs/TITLES.md` cast **binding** votes; anyone else casts **advisory** votes, always welcome, always logged |
| Tally | Written into the proposal file at close, then merged (or closed) |
| Enforce | Branch protection + CODEOWNERS: governance paths require Steward (later: council) approval; GitHub teams mirror titles |
| Backlog | The `iusethis/iusethis` project board tracks two queues: write-ups and governance proposals |

**Vote types.**
- *Lazy consensus* (default): 72 hours without objection merges any
  reversible proposal.
- *Formal vote*: 7 days, majority of binding voters — required for
  charter changes, granting/removing titles, money, licensing, and
  removing published content.
- *Steward veto* (Phase 0 only): written and logged, or it didn't happen.

## 3. Titles

A title is a named area of authority. One person may hold many titles and
may **delegate** any of them: the delegate acts with full authority, the
delegation is revocable by the delegator, and both names appear in
`docs/TITLES.md`. Titles lapse after 6 months of inactivity.

| Title | Owns |
|---|---|
| **Steward** | The charter, the domain, the org account, final say in Phase 0 |
| **Registrar** | The register: records, `projects.js`/`records/` |
| **Editor** | Write-ups: the ledger format, review, the write-up backlog |
| **Herald** | The carnival, announcements, syndication relationships |
| **Keeper** | The site: build, deploy, DNS, tokens.css discipline |
| **Moderator** | Conduct process (§4) — never content taste |
| **Archivist** | Decision log, history, the archive's integrity |
| **Bursar** | Money (dormant title — activates only if money ever exists) |

The current registry of holders and delegations is `docs/TITLES.md`.
Joining is a documented SOP: `docs/ONBOARDING.md`.

## 4. Positive-reinforcement governance

This charter assumes good-faith actors and spends its energy on
recognition, not restriction.

- **Assume good faith.** A mistaken contributor is a contributor who
  cared enough to act. Correct the work, thank the person.
- **Merit is visible and rewarded.** Titles are granted for demonstrated
  care, Apache-style — the path from contributor to title-holder is short
  and documented. Praise is logged: any title-holder may add a
  **citation** line to someone's entry in `TITLES.md` for work worth
  remembering. Citations are the currency; they're what nomination
  letters quote.
- **Calling out bad actors — graduated sanctions** (after Ostrom: flat
  bans breed resentment; escalate instead, weighing intent and harm):
  1. *Call-in* — a private note from any Moderator or title-holder.
  2. *Call-out* — a public comment on the issue/PR naming the behavior,
     not the person's character.
  3. *Suspension* — a Moderator (or Steward) suspends the person's titles
     and merge rights for 14 days; logged.
  4. *Removal* — formal vote.
- **The limit of governance.** Governance bounds harm; it does not repair
  relationships — humans do, off the record, at their own pace.
  No automated punishments, no reputation scores, no rules where a
  conversation would do. When the process ends, the process is over:
  a person who returns after a sanction returns whole.

## 5. Amendment

This charter changes by formal vote (Phase 0: plus Steward assent).
Proposal 002 adopts it.
