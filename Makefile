# MAKEFILE OF ALMOHAWELL
# GPL2 LICENSE
# MOSAAB ALZOUBI
# 1434 - 12 - 2
# ALMASA PROJECT
########################

prefix = /usr

all:
	@echo "Select one of install or uninstall to continue"

install:
	mkdir -p $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell/Package
	mkdir -p $(DESTDIR)$(prefix)/share/man/man1
	mkdir -p $(DESTDIR)$(prefix)/bin
	install -m 0755 almohawell $(DESTDIR)$(prefix)/bin
	install -m 0644 Package.pm $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell
	install -m 0644 Rpm.pm $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell/Package
	install -m 0644 Deb.pm $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell/Package
	install -m 0644 Lsb.pm $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell/Package
	install -m 0644 Pkg.pm $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell/Package
	install -m 0644 Slp.pm  $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell/Package
	install -m 0644 Tgz.pm $(DESTDIR)$(prefix)/lib/Almohawell/Almohawell/Package
	install -m 0644 almohawell.1.gz $(DESTDIR)$(prefix)/share/man/man1

uninstall:
	rm -rf $(DESTDIR)$(prefix)/lib/Almohawell
	rm $(DESTDIR)$(prefix)/bin/almohawell

