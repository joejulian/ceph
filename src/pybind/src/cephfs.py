#!/bin/env python

import warnings

warnings.warn('"import cephfs" is deprecated. Please "import ceph.cephfs".',
        DeprecationWarning
        )

from ceph.cephfs import *
