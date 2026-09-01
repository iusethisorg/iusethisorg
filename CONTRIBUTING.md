# Contributing to iusethis

iusethis runs as a do-ocracy: the people doing the work make the decisions
about it. Nobody assigns tasks and nobody needs permission to start — this
document is the standard operating procedure that keeps that workable.

## Ground rules

1. **Only register what you actually use.** No promotion, no vaporware, no
   "looks neat, might try it." Every record and write-up is first-person and
   in-use.
2. **Work in the open.** Anything worth deciding gets an issue or PR; anything
   decided gets written down. If it isn't in the repo, it didn't happen.
3. **Advice process.** Before acting on something that affects others' work,
   ask the people it affects (comment on their issue/PR, or open one). Then
   act — advice is input, not a veto.
4. **Lazy consensus.** A proposal that sits 72 hours without objection is
   accepted. Silence is consent for reversible decisions; irreversible ones
   (deleting content, changing the license, spending money) need explicit
   approval from a maintainer of the affected area.

## SOP: add a project record

1. Fork, edit `projects.js`, add one object (fields documented in the file).
2. Open a PR titled `record: <project-name>`.
3. One approval from any maintainer merges it. Records are self-reported —
   review checks format and the "actually in use" rule, not your taste.

## SOP: suggest a write-up

A write-up is a longer piece: *how* someone uses a tool day to day, or a
whole stack that hangs together.

1. Open an issue using the **Write-up suggestion** template: the tool or
   stack, the angle, and who might write it (yourself included).
2. Anyone may claim it by commenting `claiming` — first claim wins; a claim
   goes stale after 30 days of no draft.
3. Draft as a PR adding `articles/<slug>.md` (scaffold it with
   `make new SLUG=<slug>`; `make build` renders the page and the
   front-page gallery card), following the **ledger format**.
   An entry is a review in the iusethis sense — a love story, a historical
   tale, of an expert and the tools — with five images separating the
   sections (Meeting, Practice, Expertise, Care), a required Register data
   block (in use since, hours logged, hours to fluency, expected remaining
   life, provenance, care ritual), and an appendix with what the object
   makes. Copy `article.html` as the starting point; the format and its
   rationale are specified in `docs/proposals/001-editorial-identity.md`.
4. Review = one approval from any maintainer plus the 72-hour lazy-consensus
   window. Reviewers edit for clarity, never for opinion — a write-up is the
   author's experience.

## SOP: start a working group

Want a YouTube channel, a stacks section, a build pipeline? Don't ask — charter it:

1. PR a one-page charter into `docs/groups/<name>.md`: purpose, initial
   members (≥2), what it owns, how to join.
2. Lazy consensus (72h) merges it. The group now owns its area and its own
   decisions, logged in the repo.
3. A group with no activity for 90 days is archived by anyone who notices.

## Governance: titles, votes, and joining

Authority here is held as **titles** (Registrar, Editor, Herald, Keeper,
Moderator, Archivist, Steward), granted for demonstrated care and recorded
in `docs/TITLES.md`. Proposals are PRs into `docs/proposals/`; title-holders
cast binding votes, everyone else advisory — the full machine is
`docs/GOVERNANCE.md`, and the SOP for joining and holding titles is
`docs/ONBOARDING.md` (start with the *Join governance* issue template).
Titles lapse after 6 months of inactivity — no ceremony either way.
