#!/bin/env python

import subprocess
import tempfile
import errno
import logging
from time import sleep

try:
    import simplejson
except:
    import json

QUORUM_STATES = ['leader', 'peon']

def wait_for_quorum(mon_id, cluster='ceph'):
    while True:
        p = subprocess.Popen(
            args=[
                'ceph',
                '--cluster={cluster}'.format(cluster=cluster),
                '--admin-daemon=/var/run/ceph/{cluster}-mon.{mon_id}.asok'.format(
                    cluster=cluster,
                    mon_id=mon_id,
                    ),
                'mon_status',
                ],
            stdout=subprocess.PIPE,
            )
        out = p.stdout.read()
        returncode = p.wait()
        if returncode != 0:
            logging.info('ceph-mon admin socket not ready yet.')
            sleep(1)
            continue

        if out == '':
            logging.info('ceph-mon admin socket returned no data')
            sleep(1)
            continue

        try:
            data = json.loads(out)
        except:
            logging.info('failed to parse json %s', out)
            sys.exit(errno.EINVAL)

        state = data['state']
        if state not in QUORUM_STATES:
            logging.info('ceph-mon is not in quorum: %r', state)
            sleep(1)
            continue

        break


def create_client_admin_key(mon_id, cluster='ceph'):
    path = '/etc/ceph/{cluster}.client.admin.keyring'.format(
        cluster=cluster,
        )
    if os.path.exists(path):
        logging.info('Key exists already: %s', path)
        return
    pathdir = os.path.dirname(path)
    if not os.path.exists(pathdir):
        os.makedirs(pathdir)
    while True:
        try:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                tmp = f.name
                logging.info('Talking to monitor...')
                returncode = subprocess.call(
                    args=[
                        'ceph',
                        '--cluster={cluster}'.format(cluster=cluster),
                        '--name=mon.',
                        '--keyring=/var/lib/ceph/mon/{cluster}-{mon_id}/keyring'.format(
                            cluster=cluster,
                            mon_id=mon_id,
                            ),
                        'auth',
                        'get-or-create',
                        'client.admin',
                        'mon', 'allow *',
                        'osd', 'allow *',
                        'mds', 'allow',
                        ],
                    stdout=f,
                    )
            if returncode != 0:
                if returncode == errno.EPERM or returncode == errno.EACCES:
                    logging.info('Cannot get or create admin key, permission denied')
                    sys.exit(returncode)
                else:
                    logging.info('Cannot get or create admin key')
                    sleep(1)
                    continue

            os.rename(tmp, path)
            break
        finally:
            try:
                os.unlink(tmp)
            except OSError as e:
                if e.errno == errno.ENOENT:
                    pass
                else:
                    raise


def bootstrap_key(type_, cluster='ceph'):
    path = '/var/lib/ceph/bootstrap-{type}/{cluster}.keyring'.format(
        type=type_,
        cluster=cluster,
        )
    if os.path.exists(path):
        logging.info('Key exists already: %s', path)
        return

    args = [
        'ceph',
        '--cluster={cluster}'.format(cluster=cluster),
        'auth',
        'get-or-create',
        'client.bootstrap-{type}'.format(type=type_),
        'mon',
        'allow profile bootstrap-{type}'.format(type=type_),
        ]

    pathdir = os.path.dirname(path)
    if not os.path.exists(pathdir):
        os.makedirs(pathdir)

    while True:
        try:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                tmp = f.name
                logging.info('Talking to monitor...')
                returncode = subprocess.call(
                    args=args,
                    stdout=f,
                    )
            if returncode != 0:
                if returncode == errno.EPERM or returncode == errno.EACCES:
                    logging.info('Cannot get or create bootstrap key for %s, permission denied', type_)
                    break
                else:
                    logging.info('Cannot get or create bootstrap key for %s', type_)
                    sleep(1)
                    continue

            os.rename(tmp, path)
            break
        finally:
            try:
                os.unlink(tmp)
            except OSError as e:
                if e.errno == errno.ENOENT:
                    pass
                else:
                    raise
