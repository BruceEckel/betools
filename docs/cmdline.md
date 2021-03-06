## @CmdLine

Makes it trivial to use argparse. Just add the decorator to
functions that you want to publish as command-line arguments.

### Usage

```Python
#: tests/demo_cmdline.py
from betools import CmdLine

@CmdLine("1", "word_tag")
def option_one():
    """
    Description of first option
    """
    print("option_one")

@CmdLine("f")
def fn_name_as_word_tag():
    """
    With no explicit word_tag, uses
    the function name as the word_tag.
    """
    print("second option")

@CmdLine("o", num_args=1)
def one_arg():
    """
    Takes a single command-line argument
    """
    print("one_arg " + sys.argv[2])

@CmdLine("t", num_args=2)
def two_args():
    """
    Takes two command-line arguments
    """
    print("two_args " + sys.argv[2] + " " + sys.argv[3])

# num_args='+', '*' not yet supported
# Passing command-line args as function args might also be good

if __name__ == '__main__':
    CmdLine.run()

output = """
usage: demo_cmdline.py [-h] [-1] [-f] [-o ONE_ARG] [-t TWO_ARGS TWO_ARGS]

optional arguments:
  -h, --help            show this help message and exit
  -1, --word_tag        Description of first option
  -f, --fn_name_as_word_tag
                        With no explicit word_tag, uses the function name as
                        the word_tag.
  -o ONE_ARG, --one_arg ONE_ARG
                        Takes a single command-line argument
  -t TWO_ARGS TWO_ARGS, --two_args TWO_ARGS TWO_ARGS
                        Takes two command-line arguments
"""
```
