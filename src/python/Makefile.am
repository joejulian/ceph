#
# Copyright (C) 2015 SUSE LINUX GmbH
# Copyright (C) 2015 <contact@redhat.com>
#
# Author: Owen Synge <osynge@suse.com>
# Author: Loic Dachary <loic@dachary.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see `<http://www.gnu.org/licenses/>`.
#
check_SCRIPTS += python/run-tox.sh

EXTRA_DIST += \
	python/AUTHORS.rst \
	python/Makefile.am \
	python/MANIFEST.in \
	python/README.rst \
	python/requirements.txt \
	python/run-tox.sh \
	python/setup.py \
	python/test-requirements.txt \
	python/tests/test_all.py \
	python/tox.ini

all-local::
	cd $(srcdir)/python ; python setup.py build

clean-local::
	cd $(srcdir)/python ; python setup.py clean ; rm -fr wheelhouse .tox build .coverage *.egg-info

install-data-local::
	cd $(srcdir)/python ; \
	if test "$(DESTDIR)" ; then \
		if lsb_release -si | grep --quiet 'Ubuntu\|Debian\|Devuan' ; then \
			options=--install-layout=deb ; \
		else \
			options=--prefix=/usr ; \
		fi ; \
		root="--root=$(DESTDIR)" ; \
	fi ; \
	python setup.py install $$root $$options
