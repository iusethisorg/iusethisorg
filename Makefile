# iusethis.org — all the important targets.
# The Makefile is the interface; CI calls the same targets you do.

PYTHON ?= python3
PORT   ?= 8000

.PHONY: all build check serve new clean help

all: build

## build: render writeups/*.html and articles.js from articles/*.md
build:
	$(PYTHON) tools/build.py

## check: build strictly — fail on any warning (CI uses this)
check:
	$(PYTHON) tools/build.py 2>&1 | tee /dev/stderr | { ! grep -q '^warning:'; }

## serve: build, then preview at http://localhost:$(PORT)
serve: build
	$(PYTHON) -m http.server $(PORT)

## new: scaffold an article — make new SLUG=my-object
new:
	@test -n "$(SLUG)" || { echo "usage: make new SLUG=my-object"; exit 1; }
	@test ! -e articles/$(SLUG).md || { echo "articles/$(SLUG).md exists"; exit 1; }
	@printf -- '---\ntitle: \nstandfirst: \nauthor: \nstatus: forthcoming\nobject: \nsince: \nhours_logged: \nhours_to_fluency: \nexpected_remaining: \nprovenance: \ncare_ritual: \n---\n\n![the hero — the object in its place of use](placeholder:the hero)\n\n## The Meeting\n\nHow it entered your life.\n\n![the arrival](placeholder:the arrival)\n\n## The Practice\n\nThe cadence of locking in.\n\n> The single sentence that carries the love.\n\n![mid-use](placeholder:the practice)\n\n## The Expertise\n\nWhat only years of use can teach.\n\n![the detail](placeholder:the detail)\n\n## The Care and the Years\n\nMaintenance, lifecycle, succession.\n\n![today, honestly worn](placeholder:today)\n\n## Appendix - What It Makes\n\n1. The recipe, the score, the config.\n' > articles/$(SLUG).md
	@echo "created articles/$(SLUG).md — set status: published when the Register is filled"

## clean: remove generated files
clean:
	rm -f articles.js writeups/*.html

## help: list targets
help:
	@grep -E '^## ' Makefile | sed 's/^## /  make /'
