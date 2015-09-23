#!/bin/bash
#
# Copyright (C) 2015 Red Hat <contact@redhat.com>
#
# Author: Loic Dachary <loic@dachary.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Library Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Public License for more details.
#
set -xe

base=${1:-/tmp/release}
codename=$(lsb_release -irs|awk '{print tolower($1) $2}')
releasedir=$base/$(lsb_release -si)/WORKDIR
rm -fr $releasedir
mkdir -p $releasedir
#
# remove all files not under git so they are not
# included in the distribution.
#
git clean -dxf
#
# git describe provides a version that is
# a) human readable
# b) is unique for each commit
# c) compares higher than any previous commit
# d) contains the short hash of the commit
#
vers=$(git describe --match "v*" | sed s/^v//)
sha1=$(git rev-parse HEAD)
arch=x86_64
base=ceph-rpm-$codename-$arch-basic
sha1_dir=$codename/$base/sha1/$sha1
#
# creating the distribution tarbal requires some configure
# options (otherwise parts of the source tree will be left out).
#
./autogen.sh
./configure --with-rocksdb --with-ocf \
    --with-nss --with-debug \
    --with-lttng --with-babeltrace
cp rpm/init-ceph.in-fedora.patch .
#
# use distdir= to set the name of the top level directory of the
# tarbal to match the desired version
#
make distdir=ceph-${vers%%-*} dist-bzip2
#
# create the packages without cephfs_java as configure is not built to
# check for fedora packaging
#
mkdir -p $sha1_dir
rpmbuild --without cephfs_java --define "_rpmdir $sha1_dir" \
    --define "_srcrpmdir $sha1_dir/SRPMS" -ta ceph-${vers%%-*}.tar.bz2
#
# Create a repository in a directory with a name structured
# as 
#
for repodir in $sha1_dir/{SRPMS,noarch,$arch}; do
    if [ -d $repodir ]; then 
        createrepo --basedir $repodir
    fi
done

echo $dvers > $sha1_dir/version
echo $sha1 > $sha1_dir/sha1
ref_dir=$codename/$base/ref
mkdir -p $ref_dir
git for-each-ref | grep $sha1 | while read sha1 type ref ; do
    base_ref=$(basename $ref)
    ln -sf $sha1_dir $ref_dir/$base_ref
done
