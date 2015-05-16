# Test the local one, not the installed one:
import sys
sys.path.insert(0, "..")
from betools import CmdLine
# CmdLine appears to be global for all tests,
# so you can't use the same letter flag throughout
# the test suite (is this a py.test bug?)

@CmdLine("1", "option1")
def test_1():
    """
    Description of option1
    """
    print("option1")

@CmdLine("2", "option2")
def test_2():
    """
    Description of option2
    """
    print("option2")

@CmdLine("3", "option3")
def test_3():
    """
    Description of option3
    """
    print("option3")

@CmdLine("4")
def option4():
    """
    Use the function name as the word tag.
    """
    print("option4")

@CmdLine("5")
def option5():
    """
    Use the function name as the word tag.
    """
    print("option5")

@CmdLine("6")
def option6():
    """
    Use the function name as the word tag.
    """
    print("option6")

def test_main():
    CmdLine.run()

if __name__ == '__main__':
    test_main()
