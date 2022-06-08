dist: pelican pyproject.toml README.md LICENSE
include makefiles/*.mk


test: | $(VENV)/tox
	$(VENV)/tox
