CACHEDIR=~/.cache/today.txt/

install:
	install -d $(CACHEDIR)
	install -m 0644 template.txt $(CACHEDIR)
	install -m 0644 default.txt $(CACHEDIR)
	install today ~/bin/
	install -m 0644 today.service ~/.config/systemd/user/

.PHONY: install
