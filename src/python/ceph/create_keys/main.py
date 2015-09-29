#!/usr/bin/env python
import argparse
import logging

import ceph.create_keys

def parser():
    parser = argparse.ArgumentParser(
        description='Create Ceph client.admin key when ceph-mon is ready',
        )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true', default=None,
        help='be more verbose',
        )
    parser.add_argument(
        '--cluster',
        metavar='NAME',
        help='name of the cluster',
        )
    parser.add_argument(
        '--id', '-i',
        metavar='ID',
        help='id of a ceph-mon that is coming up',
        required=True,
        )
    parser.set_defaults(
        cluster='ceph',
        )
    parser.set_defaults(
        # we want to hold on to this, for later
        prog=parser.prog,
        )
    return parser


def run(argv=None, namespace=None):
    args = parser().parse_args(argv, namespace)

    if args.verbose:
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                            level=logging.DEBUG)

    try:
        ceph.create_keys.create(cluster=args.cluster, mon_id=args.id)
    except:
        raise

    return 0
