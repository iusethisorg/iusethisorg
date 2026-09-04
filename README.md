# iusethis.org

A register of software actually in use — a single static page styled as a
continuous-form greenbar printout, served by GitHub Pages at
[iusethis.org](https://iusethis.org).

MIT License © 2026 Paul Richeson

## Adding a project

Edit `projects.js` and add an object to the `PROJECTS` array:

```js
{
  name:   "my-tool",                 // required
  desc:   "What it does, one line.", // required
  url:    "https://…",               // optional
  since:  "2021",                    // optional
  status: "in use",                  // optional: "in use" (default) or "dormant"
  lang:   "Go",                      // optional
  tags:   ["cli", "daily"],          // optional
}
```

`index.html` renders the array as numbered records — no build step for
records.

## Writing an article (the text-blog pipeline)

Articles are plain text files in `articles/` — front matter plus a tiny
markup (paragraphs, `## sections`, `![caption](src)` figures, `>` pull
quotes, numbered lists). The Makefile does all the important targets:

```sh
make new SLUG=my-object   # scaffold an article in the ledger format
make build                # render writeups/*.html + articles.js (the
                          # manifest the front-page ledger gallery reads)
make check                # strict build — what CI runs
make serve                # build + preview at http://localhost:8000
make clean                # remove generated files
```

Set `status: published` (the Register front-matter fields become
mandatory) and the article gets a page and a "published" card in the
front-page gallery; `status: forthcoming` shows a claimable card.
Generated files are never committed — the GitHub Action
(`.github/workflows/pages.yml`) runs `make check` on every push to
`main` and deploys the result to Pages.

## Fork this — please

The whole site is MIT (code) — forking is not just permitted, it's the
point: take the repo, empty `articles/` and `projects.js`, and run your
own register of use. Keep the `LICENSE` file and its copyright line and
you're fully compliant; a link back to iusethis.org is appreciated,
never required. Write-ups are the authors' own (CC BY-SA proposed —
see proposal 003).

## Deploying to GitHub Pages

1. The repo lives at `iusethisorg/iusethisorg` (an org account, not a
   personal one, so governance handoff never requires migrating the repo —
   see `docs/GOVERNANCE.md`).
2. In the repo: **Settings → Pages**, set Source to **GitHub Actions**.
   The workflow builds (`make check`) and deploys on each push to `main`.
   The `CNAME` file tells Pages the custom domain is `iusethis.org`.

## DNS setup

At the DNS provider for `iusethis.org`:

### 1. Verify the domain (TXT record)

In GitHub: **profile Settings → Pages → Add a domain** → enter `iusethis.org`.
GitHub shows a TXT record to create, shaped like:

| Type | Name                                | Value                    |
|------|-------------------------------------|--------------------------|
| TXT  | `_github-pages-challenge-iusethis`  | *(code GitHub displays)* |

Create it, wait for propagation (check with
`dig TXT _github-pages-challenge-iusethis.iusethis.org +short`), then click
**Verify**. This proves domain ownership and prevents takeover if the Pages
site is ever disabled.

### 2. Point the apex at GitHub Pages (A/AAAA records)

| Type | Name | Value               |
|------|------|---------------------|
| A    | `@`  | `185.199.108.153`   |
| A    | `@`  | `185.199.109.153`   |
| A    | `@`  | `185.199.110.153`   |
| A    | `@`  | `185.199.111.153`   |
| AAAA | `@`  | `2606:50c0:8000::153` |
| AAAA | `@`  | `2606:50c0:8001::153` |
| AAAA | `@`  | `2606:50c0:8002::153` |
| AAAA | `@`  | `2606:50c0:8003::153` |

Optionally add `www`:

| Type  | Name  | Value                 |
|-------|-------|-----------------------|
| CNAME | `www` | `iusethisorg.github.io.` |

### 3. Enable HTTPS

Back in the repo's **Settings → Pages**, confirm the custom domain shows
`iusethis.org` with a green check, then tick **Enforce HTTPS** (available once
the certificate is issued, usually within an hour of DNS propagating).

## Local preview

```sh
python3 -m http.server 8000
# → http://localhost:8000
```
