DESTDIR ?= /
EXTRA_DIST = setup.py src ceph ceph_argparse.py ceph-create-keys ceph-disk \
			 cephfs.py ceph-rest-api ceph_rest_api.py rados.py rbd.py

# assemble Python script with global version variables
# NB: depends on format of ceph_ver.h
#
#ceph: ceph.in ./ceph_ver.h Makefile
#	rm -f $@ $@.tmp
#	echo "#!/usr/bin/env python" >$@.tmp
#	grep "#define CEPH_GIT_NICE_VER" ./ceph_ver.h | \
#		sed -e 's/#define \(.*VER\) /\1=/' >>$@.tmp
#	grep "#define CEPH_GIT_VER" ./ceph_ver.h | \
#	  sed -e 's/#define \(.*VER\) /\1=/' -e 's/=\(.*\)$$/="\1"/' >>$@.tmp
#	cat $(srcdir)/$@.in >>$@.tmp
#	chmod a+x $@.tmp
#	chmod a-w $@.tmp
#	mv $@.tmp $@

all:

all-local:
	$(PYTHON) setup.py build

install-exec-hook:
	$(PYTHON) setup.py install --root=$(DESTDIR) --prefix=$(PY_PREFIX) $(PYTHON_SETUPUTIL_ARGS)

clean: clean-local

clean-local:

check-local: all
