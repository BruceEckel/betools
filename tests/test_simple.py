# Test the local one, not the installed one:
import sys
sys.path.insert(0, "..")
import betools
from betools import CmdLine
# CmdLine appears to be global for all tests,
# so you can't use the same letter flag throughout
# the test suite (is this a py.test bug?)

@CmdLine("n", "none")
def test_noArgument():
    """
    Call with no command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("s", "single", 1)
def test_singleArgument():
    """
    Call with 1 command-line argument
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("d", "two", 2)
def test_twoArguments():
    """
    Call with 2 command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("m", "many", "*")
def test_manyArguments():
    """
    Call with many command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

@CmdLine("o", "oneormore", "+")
def test_oneOrMoreArguments():
    """
    Call one or more command-line arguments
    """
    print("args: {}".format(sys.argv[2:]))

def test_main():
    CmdLine.run()

if __name__ == '__main__':
    test_main()
