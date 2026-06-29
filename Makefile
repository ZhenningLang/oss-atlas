.PHONY: lint cards health install-hooks help

help:
	@echo "oss-atlas make targets:"
	@echo "  make lint           run the index linter (tools/lint.py)"
	@echo "  make cards          regenerate ALL health radar SVGs from frontmatter (offline)"
	@echo "  make health PAGE=…  (re)score one page via GitHub/registry APIs and write its health: block"
	@echo "                      e.g. make health PAGE=categories/python-tooling/memory-analyzer.md"
	@echo "  make install-hooks  point git at scripts/hooks (offline pre-commit: refresh cards + lint)"

lint:
	python3 tools/lint.py

cards:
	python3 tools/health_card.py --all

# Network step (GitHub + package registries via the already-authenticated gh CLI).
# Scores the page, writes the health: block to BOTH siblings, then regenerates its card.
health:
	@test -n "$(PAGE)" || { echo "usage: make health PAGE=categories/<cat>/<slug>.md"; exit 2; }
	python3 tools/health.py --page "$(PAGE)" --write
	python3 tools/health_card.py "$(PAGE)"

install-hooks:
	git config core.hooksPath scripts/hooks
	chmod +x scripts/hooks/pre-commit
	@echo "installed: core.hooksPath -> scripts/hooks (pre-commit active)"
