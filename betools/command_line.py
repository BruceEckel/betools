"""
Decorator adds a new command-line option and manages argparse.
For class-based decorators, see:
http://www.artima.com/weblogs/viewpost.jsp?thread=240845
"""
__all__ = ['CmdLine']

import argparse
import __main__ as main

class CmdLine:

    parser = argparse.ArgumentParser(description = main.__doc__)
    commands = dict()
    letterflags = set()

    def __init__(self, letterFlag, wordFlag=None, num_args=None):
        self.wordFlag = wordFlag
        self.letterFlag = letterFlag
        self.num_args = num_args
        assert letterFlag not in CmdLine.letterflags, \
            "Duplicate command argument letter flags"
        CmdLine.letterflags.add(letterFlag)

    def __call__(self, func):
        if not self.wordFlag:
            self.wordFlag = func.__name__
        if self.num_args:
            CmdLine.parser.add_argument(
                "-" + self.letterFlag,
                "--" + self.wordFlag,
                nargs=self.num_args,
                help=func.__doc__
            )
        else:
            CmdLine.parser.add_argument(
                "-" + self.letterFlag,
                "--" + self.wordFlag,
                action='store_true',
                help=func.__doc__
            )
        CmdLine.commands[self.wordFlag] = func
        return func # No wrapping needed

    @staticmethod
    def run():
        show_help = True
        args = vars(CmdLine.parser.parse_args())
        for wordFlag, func in CmdLine.commands.items():
            if args[wordFlag]:
                func()
                show_help = False
        if show_help:
            CmdLine.parser.print_help()
