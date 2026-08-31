# How iusethis organizes itself

Founded 2026 by Paul Richeson <paulr@sdf.org>. MIT-licensed, contributor-run.

## The idea

iusethis is a register of software people *actually use*, written by the
people using it. The org exists to grow that register in three lanes:

1. **Records** — one-line entries on the site (`projects.js`, later one file
   per record).
2. **Write-ups & stacks** — first-person pieces on how a tool or a whole
   stack is used in practice (`writeups/`).
3. **Video** — screen-share walkthroughs of the same material, published to
   the YouTube channel by the video working group.

## Self-organization, not management

There is no roadmap owner and no task assignment. Structure comes from four
mechanisms, all defined in [CONTRIBUTING.md](../CONTRIBUTING.md):

- **Do-ocracy** — doing the work confers the authority over it.
- **Advice process** — consult affected people before acting; then act.
- **Lazy consensus** — 72 hours of silence accepts a proposal.
- **Working groups** — any ≥2 people can charter a group
  (`docs/groups/<name>.md`) that then owns its area. Groups die quietly
  after 90 idle days.

Decisions that matter get a short record in `docs/decisions/` —
`NNN-title.md`, a few sentences on context, decision, and who was consulted.
The log is the org's memory; it replaces meetings.

## Online tools (all free tier, all replaceable)

| Function | Tool | Why |
|----------|------|-----|
| Source of truth | This GitHub repo (org: `iusethis`) | Everything — content, charters, decisions — is a file under review |
| Discussion & proposals | GitHub Issues + Discussions | Async, public, linkable; lazy consensus needs timestamps |
| Publishing | GitHub Pages + Actions | Already deployed; Actions can build from data files when we outgrow `projects.js` |
| Chat (ephemeral) | IRC (`#iusethis` on libera.chat) or SDF `com` | Fits the culture; nothing binding happens in chat — decisions go back to issues |
| Video | YouTube channel, raw uploads mirrored via git-annex or archive.org | Working group's call once chartered |

Rule of thumb: if a tool's output can't be checked into git or linked from an
issue, it isn't a system of record here.

## Growth path for the tech stack

Stay static, add structure only when the data demands it:

1. **Now** — single `index.html` + `projects.js`. Zero build.
2. **~25 records** — one YAML file per record in `records/`, GitHub Action
   concatenates to JSON at deploy. PRs stop colliding on one file.
3. **Write-ups live** — static site generator (Eleventy or Hugo — the
   Action decides, the pages keep the greenbar design system).
4. **Later, maybe** — per-user pages, RSS, a JSON API dump. Never a
   database, never a server: the whole org runs on files.
