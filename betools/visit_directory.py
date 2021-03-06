"""
Visits a directory and automatically returns
to original directory when you're done.
"""
__all__ = ['visitDir']

from contextlib import contextmanager
import os

@contextmanager
def visitDir(d):
    d = str(d)
    old = os.getcwd()
    os.chdir(d)
    yield d
    os.chdir(old)


