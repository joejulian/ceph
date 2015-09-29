#!/usr/bin/env python

from ceph.mon import *

def create(mon_id, cluster='ceph'):
    try:
        wait_for_quorum(cluster=cluster, mon_id=mon_id)
        create_client_admin_key(cluster=cluster, mon_id=mon_id)

        bootstrap_key(
            cluster=cluster,
            type_='osd',
            )
        bootstrap_key(
            cluster=cluster,
            type_='rgw',
            )
        bootstrap_key(
            cluster=cluster,
            type_='mds',
            )
    except:
        raise
