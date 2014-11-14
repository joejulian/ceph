from setuptools import setup, find_packages
import os
from subprocess import Popen, PIPE
 
 
def call_git_describe():
    try:
        p = Popen(['git', 'describe', '--long'],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return line.strip()
 
    except:
        return None

def git_version():
    try:
        return re.sub(r'-',r'.', re.sub(r'([^-]*-g)',r'r\1', call_git_describe()))

    except:
        return None

def long_description():
    readme = os.path.join(os.path.dirname(__file__), 'README.md')
    return open(readme).read()

with open('requirements.txt') as f:
        required = f.read().splitlines()
setup(
    name = 'python-ceph',
    description = 'bindings to Ceph, the distributed file system',
    packages=find_packages(),
    author = 'Inktank',
    author_email = 'ceph-devel@vger.kernel.org',
    version = call_git_describe(),
    license = "LGPL2",
    zip_safe = False,
    keywords = "ceph, rest, bindings, api, cli",
    install_requires=required,
    long_description = long_description(),
    url = "https://github.com/ceph/ceph",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Topic :: System :: Filesystems',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules = ['ceph_argparse', 'cephfs', 'rados', 'rbd'], 
    scripts = ['ceph-create-keys', 'ceph-disk', 'ceph-rest-api', 'ceph'],
)

