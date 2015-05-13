# Test here before installing, uses local version
import betools
from betools import CmdLine
import sys
# print(betools)

@CmdLine("n", "none")
def noArgument():
    """
    Call with no command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("s", "single", 1)
def singleArgument():
    """
    Call with 1 command-line argument
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("t", "two", 2)
def twoArguments():
    """
    Call with 2 command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("m", "many", "*")
def manyArguments():
    """
    Call with many command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("o", "oneormore", "+")
def oneOrMoreArguments():
    """
    Call one or more command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

if __name__ == '__main__': CmdLine.run()
