#!/bin/env python

import warnings

warnings.warn('"import rbd" is deprecated. Please "import ceph.rbd".',
        DeprecationWarning
        )

from ceph.rbd import *
