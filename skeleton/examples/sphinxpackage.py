"""
Skeleton to create a project with sphinx support.
"""

from __future__ import with_statement

import logging
import os

from skeleton import Skeleton, Var
from skeleton.examples.basicpackage import BasicPackage
from skeleton.utils import get_loggger

_LOG = get_loggger(__name__)


class SphinxPackage(Skeleton):
    """Create a new package package with sphinx setup.
    includes features from basicpackage:
    Create a new package package (with namespace support) with the setup.py,
    README.rst and MANIFEST.in files already setup.

    Require the following variables:

    - project_name;
    - package_name;
    - author;
    - author_email;
    - license;
    - and short_description.


    """

    src = 'sphinx-package'
    variables = [
        Var('project_name'),
        Var('package_name'),
        Var('author'),
        Var('author_email'),
        Var('license'),
        Var('short_description')
        ]
    required_skeletons = [
        BasicPackage,
        ]


def main(argv=None):
    """Bootstrap SphinxPackage."""
    SphinxPackage.cmd(argv)

if __name__ == '__main__':
    main()
