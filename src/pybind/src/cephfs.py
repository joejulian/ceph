#!/bin/env python
import warnings
warnings.warn('"import ceph_cephfs" is deprecated. Please "import ceph.cephfs".',
        DeprecationWarning
        )
from ceph.cephfs import *
