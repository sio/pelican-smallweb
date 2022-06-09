SETUP_PY=pyproject.toml
include makefiles/*.mk


dist: pelican pyproject.toml README.md LICENSE


.PHONY: test
test: | $(VENV)/tox
	$(VENV)/tox


DEMO_FLAVOR?=default
DEMO_INPUT=demo/
DEMO_OUTPUT=demo/html/$(DEMO_FLAVOR)
DEMO_CONFIG=demo/pelicanconf.py
SMALLWEB_ACCENT_default=
SMALLWEB_ACCENT_red=\#ff0000
SMALLWEB_ACCENT_blue=\#0000ff
export SMALLWEB_ACCENT=$(SMALLWEB_ACCENT_$(DEMO_FLAVOR))


.PHONY: demo
demo: | venv $(VENV)/markdown $(VENV)/pelican-neighbors
	$(VENV)/pelican $(DEMO_INPUT) -o $(DEMO_OUTPUT) -s $(DEMO_CONFIG) -vv -D


.PHONY: demo-server
demo-server: | venv
	$(VENV)/pelican --listen --port 8000 --bind 127.0.0.1 --output $(DEMO_OUTPUT)
