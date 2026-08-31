# iusethis.org

A register of software actually in use — a single static page styled as a
continuous-form greenbar printout, served by GitHub Pages at
[iusethis.org](https://iusethis.org).

MIT License © 2026 Paul Richeson <paulr@sdf.org>

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

`index.html` renders the array as numbered records. No build step.

## Deploying to GitHub Pages

1. Create a GitHub repository (e.g. `iusethis.org`) and push this repo to it.
   Update the `USERNAME` placeholder in `projects.js` to the real repo URL.
2. In the repo: **Settings → Pages**, set Source to **Deploy from a branch**,
   branch `main`, folder `/ (root)`. The `CNAME` file in this repo tells Pages
   the site's custom domain is `iusethis.org`.

## DNS setup

At the DNS provider for `iusethis.org`:

### 1. Verify the domain (TXT record)

In GitHub: **profile Settings → Pages → Add a domain** → enter `iusethis.org`.
GitHub shows a TXT record to create, shaped like:

| Type | Name                                | Value                    |
|------|-------------------------------------|--------------------------|
| TXT  | `_github-pages-challenge-USERNAME`  | *(code GitHub displays)* |

Create it, wait for propagation (check with
`dig TXT _github-pages-challenge-USERNAME.iusethis.org +short`), then click
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
| CNAME | `www` | `USERNAME.github.io.` |

### 3. Enable HTTPS

Back in the repo's **Settings → Pages**, confirm the custom domain shows
`iusethis.org` with a green check, then tick **Enforce HTTPS** (available once
the certificate is issued, usually within an hour of DNS propagating).

## Local preview

```sh
python3 -m http.server 8000
# → http://localhost:8000
```
