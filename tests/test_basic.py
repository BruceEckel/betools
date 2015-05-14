# Test the local one, not the installed one:
import sys
sys.path.insert(0, "..")
from betools import CmdLine, visitDir
# Is there a way to verify we're getting the local version?
# How does py.test validate output?

# CmdLine appears to be global for all tests,
# so you can't use the same letter flag throughout
# the test suite (is this a py.test bug?)

@CmdLine("t", "test")
def test_basic():
    """
    Testing CmdLine
    """
    print("basic")

def test_main():
    sys.argv.append("-t")
    CmdLine.run()

if __name__ == '__main__':
    test_main()
