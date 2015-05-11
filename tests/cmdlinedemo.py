from betools import CmdLine

@CmdLine("t", "option1")
def test1():
    """
    Description of option1
    """
    print("option1")

@CmdLine("u", "option2")
def test2():
    """
    Description of option2
    """
    print("option2")

@CmdLine("v", "option3")
def test3():
    """
    Description of option3
    """
    print("option3")


if __name__ == '__main__': CmdLine.run()

""" Output:
+>python cmdlinedemo.py
usage: cmdlinedemo.py [-h] [-t] [-u] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -t, --option1  Description of option1
  -u, --option2  Description of option2
  -v, --option3  Description of option3

C:\Users\Bruce\Dropbox\__TIJ4-ebook
+>python cmdlinedemo.py -u
option2

C:\Users\Bruce\Dropbox\__TIJ4-ebook
+>
"""
