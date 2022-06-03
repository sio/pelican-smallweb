include makefiles/*.mk


dist: pelican setup.cfg pyproject.toml README.md LICENSE $(FONTS)


THEME=pelican/themes/smallweb
FONTS=$(THEME)/static/css/fonts.css

fonts: $(FONTS)
$(FONTS): fonts.py fonts.toml | venv $(VENV)/toml
	$(VENV)/python fonts.py $(THEME)
