SETUP_PY=pyproject.toml
include Makefile.venv
include makefiles/*.mk


CODECOLOR = pelican/themes/smallweb/static/css/codecolor/bleak.css


dist: pelican pyproject.toml README.md LICENSE $(CODECOLOR)


.PHONY: test
test: | $(VENV)/tox $(CODECOLOR)
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
demo: | venv $(VENV)/markdown $(VENV)/pelican-neighbors $(CODECOLOR)
	$(VENV)/pelican $(DEMO_INPUT) -o $(DEMO_OUTPUT) -s $(DEMO_CONFIG) -vv -D


.PHONY: demo-server
demo-server: | venv
	$(VENV)/pelican --listen --port 8000 --bind 127.0.0.1 --output $(DEMO_OUTPUT)


pelican/themes/smallweb/static/css/codecolor/%.css: codecolor/%.py | venv
	mkdir -p $(dir $@)
	$(VENV)/python $< | tee $@


.PHONY: clean
clean:
	-$(RM) -r -v $(DEMO_OUTPUT)
