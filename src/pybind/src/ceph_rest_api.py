#!/bin/env python

import warnings

warnings.warn('"import ceph_rest_api" is deprecated. Please "import ceph.rest.api".',
        DeprecationWarning
        )

from ceph.rest.api import *
