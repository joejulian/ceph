#!/bin/env python
import warnings
warnings.warn('"import ceph_rados" is deprecated. Please "import ceph.rados".',
        DeprecationWarning
        )
from ceph.rados import *
