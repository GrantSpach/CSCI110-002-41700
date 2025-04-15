#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      grant
#
# Created:     15/04/2025
# Copyright:   (c) grant 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def to_secs(Hours, Minutes, Seconds):
    return ((int(Hours) * 3600) + (int(Minutes) * 60) + (int(Seconds) * 1))

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

test_suite()