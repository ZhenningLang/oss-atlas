.PHONY: lint cards health health-backfill upstream-snapshot upstream-check test install-hooks help

help:
	@echo "oss-atlas make targets:"
	@echo "  make lint           run the index linter (tools/lint.py)"
	@echo "  make cards          regenerate ALL health radar SVGs from frontmatter (offline)"
	@echo "  make health PAGE=…  (re)score one page via GitHub/registry APIs and write its health: block"
	@echo "                      e.g. make health PAGE=categories/python-tooling/memory-analyzer.md"
	@echo "  make health-backfill ARGS='--limit 5'  dry-run/apply/resume Phase 1 health backfill"
	@echo "  make upstream-snapshot PAGE=…  refresh cheap GitHub upstream snapshot for one page"
	@echo "  make upstream-check PAGE=…  compare stored upstream snapshot with GitHub without writing"
	@echo "  make test           run stdlib tool tests"
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
	python3 tools/health_card.py "$(PAGE)" "$(basename $(PAGE)).zh.md"

health-backfill:
	python3 tools/health_backfill.py $(ARGS)

upstream-snapshot:
	@test -n "$(PAGE)" || { echo "usage: make upstream-snapshot PAGE=categories/<cat>/<slug>.md"; exit 2; }
	python3 tools/upstream_snapshot.py --page "$(PAGE)" --apply --yes

upstream-check:
	@test -n "$(PAGE)" || { echo "usage: make upstream-check PAGE=categories/<cat>/<slug>.md"; exit 2; }
	python3 tools/upstream_snapshot.py --page "$(PAGE)" --check

test:
	python3 -m unittest tools/test_health_backfill.py tools/test_lint.py tools/test_upstream_snapshot.py

install-hooks:
	git config core.hooksPath scripts/hooks
	chmod +x scripts/hooks/pre-commit
	@echo "installed: core.hooksPath -> scripts/hooks (pre-commit active)"
