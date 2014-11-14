#!/bin/env python

import warnings

warnings.warn('"import ceph_argparse" is deprecated. Please "import ceph.argparse".',
        DeprecationWarning
        )

from ceph.argparse import *
