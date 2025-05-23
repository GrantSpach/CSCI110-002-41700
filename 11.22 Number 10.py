#-------------------------------------------------------------------------------
# Name:        module2
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

def replace (s, old, new):

    first = s.split(old)
    glue = new
    glue = new.join(first)
    return glue

def test(did_pass):

    """  Print the result of a test.  """

    linenum = sys._getframe(1).f_lineno
    if did_pass:

        msg = "Test at line {0} Good.".format(linenum)
    else:

        msg = ("Test at line {0} Failed!!!.".format(linenum))

    print(msg)

def test_suite():

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite back. pain, spam, yum!")

test_suite()