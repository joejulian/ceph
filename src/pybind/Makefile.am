EXTRA_DIST += pybind/MANIFEST.in \
	      pybind/Makefile.am \
	      pybind/README.md \
	      pybind/ceph \
	      pybind/ceph-create-keys \
	      pybind/ceph-disk \
	      pybind/ceph-rest-api \
	      pybind/requirements.txt \
	      pybind/setup.py \
	      pybind/src/ceph \
	      pybind/src/ceph/__init__.py \
	      pybind/src/ceph/argparse.py \
	      pybind/src/ceph/cephfs.py \
	      pybind/src/ceph/rados.py \
	      pybind/src/ceph/rbd.py \
	      pybind/src/ceph/rest \
	      pybind/src/ceph/rest/__init__.py \
	      pybind/src/ceph/rest/api.py \
	      pybind/src/ceph_argparse.py \
	      pybind/src/ceph_rest_api.py \
	      pybind/src/cephfs.py \
	      pybind/src/rados.py \
	      pybind/src/rbd.py


all-local:
	cd $(srcdir)/pybind ; \
	$(PYTHON) setup.py build

install-data-local:
	cd $(srcdir)/pybind ; \
	if test "$(DESTDIR)" ; then \
		if lsb_release -si | grep --quiet 'Ubuntu\|Debian\|Devuan' ; then \
	    		options=--install-layout=deb ; \
		else \
			options=--prefix=/usr ; \
		fi ; \
		root="--root=$(DESTDIR)" ; \
	fi ; \
	$(PYTHON) setup.py install --root=$(DESTDIR) $$root $$options

clean-local:
	cd $(srcdir)/pybind ; \
	$(PYTHON) setup.py clean ; \
	rm -fr build wheelhouse .tox .coverage
