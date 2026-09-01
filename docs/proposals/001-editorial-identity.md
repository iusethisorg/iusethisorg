# Proposal 001 — The editorial identity: love stories of objects

- **Status:** open for review (72h lazy consensus per CONTRIBUTING.md)
- **Proposed:** 2026-08-31, from a research session for paulr@sdf.org
- **Decides:** what an iusethis article *is*, the article format, the
  site-wide color system, the logo, and how we find collaborators

## 1. The claim

"iusethis" is a claim, broken into three words:

- **I** — the expert. Not cursory knowledge but intimate knowledge, the way
  a professor *professes*: publicly, with their name on it, open to peers.
- **Use** — the practice. Operated daily, bought over and over, the cadence
  of locking in and losing time into the object — the way musical
  instruments make repetition culturally honorable.
- **This** — the object. A specific item in the catalog, not a category.

So an entry is a review — a review in the fullest sense: **"An entry is a
love story, a historical tale, of an expert and the tools."** The story of
one man and his trainset, not a survey of all possible train gauges. Not
"grandma's favorite bowl" but *why* grandma loves her crockpot — the
iron-core ceramic glaze that lets her cook her best dishes — with the
recipe listed.

## 2. What the research found (the intellectual neighborhood)

- **Object biography.** Historians of material culture already do exactly
  this: they treat objects as having biographies and life cycles, and read
  a culture from how people used and cared for things. iusethis is that
  method applied to living memory — we are writing the primary sources that
  future historians of technology will wish existed. That's our elevator
  pitch to contributors.
- **["The Setup" / usesthis.com](https://usesthis.com/)** — the closest
  living ancestor: 15+ years of interviews asking people what they use.
  Its lesson: a fixed question format scales across hundreds of
  contributors, and its archives got mined as a research dataset
  ([usesthis-data](https://github.com/ats/usesthis-data)). Our difference:
  they ask *what*, we ask *why you love it and how you mastered it* — one
  object per article, at depth.
- **[IndieWeb blog carnivals](https://indieweb.org/IndieWeb_Carnival)** —
  a monthly themed prompt that people answer on their own sites, aggregated
  by a host. A proven, zero-cost recruiting engine for exactly the writers
  we want (people with personal sites who love their tools).
- **Standard contributor-recruiting practice** (blog-industry sources):
  publish contributor guidelines under that exact phrase so writers
  searching for openings find you; recruit by direct invitation from a list
  of writers you already admire; use community platforms where the niche
  already talks.

## 3. Ideas for using the entries (for review — adopt, adapt, or strike)

1. **The Archive framing.** Position the site as "a historical archive of
   use" — each article is testimony. Tagline candidates: *"Primary sources
   for the history of everyday tools."*
2. **The iusethis Carnival.** Quarterly themed call in the IndieWeb style
   ("the tool you've used longest", "the instrument you lose time in").
   Writers post on their own sites; we syndicate with permission into the
   catalog. Recruits collaborators without hiring anyone.
3. **Direct commissions.** Keep a standing list (issue label
   `invite-wishlist`) of people whose devotion to a tool is already visible
   — the person who's blogged about their mechanical keyboard for a decade,
   the org-mode lifer, the fountain-pen restorer. Invite them personally
   with one flattering, specific sentence about the object we want their
   story on.
4. **Interview fallback.** Not everyone writes. Offer a structured
   interview (the questions in §4's data block, plus "tell me about the
   day you got it") that an editor transcribes into the format. This is
   how The Setup scaled.
5. **Records as scouting.** The one-line register is the funnel: anyone
   whose record says "since 2009" gets a write-up invitation. Longevity of
   use is our editorial signal.
6. **Pairing with descendants.** Each article can carry a "still in use by"
   footer — future contributors who inherit or adopt the same object link
   their own stories, building the object's multi-owner biography over time.
7. **Entries as credentials.** An entry is a public certificate of mastery —
   authors cite their iusethis entries the way a professor cites
   publications. "Upgraded competencies" become linkable: a CV line that
   proves ten years of practice, not a claimed skill.

## 4. The article format ("the ledger format")

Long-form, magazine-style, **five images**, each image separating a section
and giving it context. Template: `article.html` (uses `assets/tokens.css`).

| # | Section | Carries | Image |
|---|---------|---------|-------|
| 0 | Title, standfirst, byline | The claim in one breath | 1 — the hero: the object in its place of use |
| — | **The Register** (mono data block) | in use since · hours logged · hours to fluency · expected remaining years · provenance · care ritual | — |
| 1 | **The Meeting** | How it entered your life; what it replaced | 2 — the object when it was new to you, or its arrival context |
| 2 | **The Practice** | The cadence: locking in, the repetition, losing time | 3 — hands on the object, mid-use |
| 3 | **The Expertise** | The tech analysis — the iron-core-glaze level of detail only years of use can teach | 4 — the detail shot: the mechanism, the wear pattern |
| 4 | **The Care and the Years** | Maintenance, lifecycle, what happens when it dies, who gets it next | 5 — the object today, honestly worn |
| 5 | **The Appendix** | What the object produces: the recipe, the score, the config file, the timetable | — |

Hard rules: first person throughout; the numbers in the Register are
required (they are what makes this an archive, not a blog); no affiliate
links ever; the author's expertise must show in at least one passage a
newcomer couldn't have written.

## 5. The color system (site-wide)

Trust colors of an opulent old bank — deep green, burnished gold, dark
mahogany, veined marble. Four complementing palettes, each with a light and
a dark theme, implemented in `assets/tokens.css`:

| Palette | Led by | Use for | Light bg / accent | Dark bg / accent |
|---------|--------|---------|-------------------|------------------|
| **Marble** (default) | ivory | reading, articles | `#f6f1e5` / `#175a43` | `#201b12` / `#4fa47e` |
| **Vault** | deep green | chrome, covers, home | `#edf3ee` / `#0f4d38` | `#0c1f18` / `#6fc79e` |
| **Coin** | gold | features, celebration | `#f7efd8` / `#8c6d1f` | `#241c09` / `#e0be4e` |
| **Teller** | mahogany | archive, history pages | `#f2eae2` / `#5c3a24` | `#1d130c` / `#c08a5f` |

Every palette carries the same `--gold` detail token so gold threads the
whole site. Type: Fraunces (display), Newsreader (body), IBM Plex Mono
(data — continuity with the register page).

**Open sub-question:** the register page currently wears the greenbar
printout look. Keep it as the "catalog room" inside the bank, or restyle
it onto Marble? (Proposer leans: keep greenbar for the register, bank
palettes everywhere else — the printout *is* the ledger.)

## 6. The logo and the © mark

`assets/logo.svg`: a **struck gold coin carrying all three elements** —
**I. / Use. / This.** stacked, in coin-relief ink, ringed the way a ©
circles its C — with the arrow-T's shaft breaking through the coin's rim
so the seal points at whatever it is affixed to. Beside it the wordmark
**I. Use. This.** — I in gold (the expert), Use in green (the practice),
This in mahogany (the object) — with the subtitle
**THE EXPERT · THE PRACTICE · THE OBJECT ↓** and the line
`© iusethis.org`. The SVG carries its own dark-theme colors.

**The arrow-T.** The T of *This* is drawn as a downward arrow: crossbar and
stem descending through the baseline into an arrowhead. The mark points at
whatever it is affixed to — that is the grammar of the logo. Which makes
the brand meta: put it on a device, a case, a sticker on a crockpot, and
the mark itself testifies *this is used*. The wordmark never needs a
photograph beside it; wherever it sits, the arrow supplies the object.

**Where the arrow lives.** The arrow-T belongs to the marks only — seal,
wordmark, Bearer's book. In running text, "This" stays plain text; there
is no JavaScript rewriting body copy. The one load action is inside the
logo SVG itself: the wordmark's arrow strikes downward into place once on
page load (pure CSS in the SVG, honors reduced-motion).

**The Bearer** (`assets/bearer.svg`). The second depiction: a graduate
figure holding the mark to their chest the way a diploma is held in the
commencement photo — *I got it, I worked for it, I use it, it got me a
job.* `/s`

The Bearer is posed in deliberate meta irony, and the `/s` is part of the
mark's caption: the Reddit sarcasm tag, born as a fake closing HTML tag
(see Know Your Meme,
[Fake HTML Tags](https://knowyourmeme.com/memes/fake-html-tags)) — a
fitting citation for a static-HTML archive. The joke is load-bearing: we
know exactly how proudly professing a crockpot reads, and we mean every
word anyway. Irony opens the door; sincerity furnishes the room.

The pose is the whole editorial stance in one image: ownership,
earned competency, the story told by the person who did the work, from
the doubled perspective of journalist and expert. The write-up *is* the
diploma — publishing an entry is the public certificate of an upgraded
competency. Uses: author badges beside bylines, the About page, the
carnival announcement, merch.

## 7. SOP additions (merged into CONTRIBUTING.md if this proposal passes)

- Write-ups follow the ledger format (§4); the Register data block is a
  merge requirement.
- New issue label `invite-wishlist`; anyone may nominate a writer+object.
- A quarterly carnival theme is chosen by whoever volunteers to host it
  (do-ocracy); syndication always by author permission, author retains
  copyright, CC BY-SA suggested for syndicated copies.
- All new pages use `assets/tokens.css`; no colors outside the token system.

## Sources

- https://usesthis.com/ and https://github.com/ats/usesthis-data
- https://indieweb.org/IndieWeb_Carnival and https://indieweb.org/blog_carnival
- https://www.blogtyrant.com/how-to-get-contributors-for-your-blog/
- https://wpforms.com/how-to-get-more-guest-post-submissions-on-your-wordpress-blog/
- https://www.chnm.gmu.edu/worldhistorysources/unpacking/objectsguide.pdf (object biography method)
- https://sk.sagepub.com/hnbk/edvol/hdbk_matculture/chpt/agency-biography-objects
