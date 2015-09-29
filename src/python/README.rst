python-ceph
===========

python-ceph are the python tools that support ceph

Home page : https://pypi.python.org/pypi/python-ceph

Hacking
=======

* Get the code : git clone https://git.ceph.com/ceph.git
* Run the unit tests : tox
* Run the integration tests (requires docker) : tox -e integration
* Check the documentation : rst2html < README.rst > /tmp/a.html
* Prepare a new version

 - version=1.0.0 ; perl -pi -e "s/^version.*/version='$version',/" setup.py ; do python setup.py sdist ; amend=$(git log -1 --oneline | grep --quiet "version $version" && echo --amend) ; git commit $amend -m "version $version" setup.py ; git tag -a -f -m "version $version" $version ; done

* Publish a new version

 - python setup.py sdist upload --sign
 - git push ; git push --tags

* pypi maintenance

 - python setup.py register # if the project does not yet exist
 - trim old versions at https://pypi.python.org/pypi/ceph-detect-init
