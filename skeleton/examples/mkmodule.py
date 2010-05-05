#!/usr/bin/env python
"""
Basic script to create an empty python package containing one module
"""
from skeleton import Skeleton, Var


class BasicModule(Skeleton):
    """
    Create an empty module with its etup script and a README file.
    """
    src = 'basic-module'
    vars = [
        Var('ModuleName'),
        Var('Author'),
        Var('AuthorEmail'),
        ]


def main():
    """Basic command line bootstrap for the BasicModule Skeleton"""
    BasicModule.cmd()

if __name__ == '__main__':
    main()
