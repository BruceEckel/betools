"""
Decorator adds a new command-line option and manages argparse.
For class-based decorators, see:
http://www.artima.com/weblogs/viewpost.jsp?thread=240845
"""
__all__ = ['CmdLine']

import argparse
import __main__ as main

class CmdLine:
    if main.__doc__:
        parser = argparse.ArgumentParser(description = main.__doc__.strip())
    else:
        parser = argparse.ArgumentParser()
    commands = dict()
    letterflags = set()

    def __init__(self, letterFlag=None, wordFlag=None, num_args=None):
        self.wordFlag = wordFlag
        self.letterFlag = letterFlag
        assert letterFlag not in CmdLine.letterflags, \
            "Duplicate command argument letter flags"
        if letterFlag:
            CmdLine.letterflags.add(letterFlag)
        self.num_args = num_args

    def __call__(self, func):
        if not self.wordFlag:
            self.wordFlag = func.__name__

        args = ["--" + self.wordFlag]
        if self.letterFlag:
            args = ["-" + self.letterFlag] + args # Order is important

        kwargs = { "help" : func.__doc__ }
        if self.num_args:
            kwargs["nargs"] = self.num_args
        else:
            kwargs["action"] = 'store_true'

        CmdLine.parser.add_argument(*args, **kwargs)
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
