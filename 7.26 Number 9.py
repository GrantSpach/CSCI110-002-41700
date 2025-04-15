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
import math


def test(Did_Pass):
    linenum = sys._getframe(1).f_lineno
    if Did_Pass:
        msg = "test at line {0} ok.".format(linenum)
    else:
        msg = ("test at line {0} Failed.".format(linenum))
    print(msg)


def print_Trianglar_numbers(n):
    t = 0
    for v in range(n+1):
        t = t + v
        print(v, end ="     ")
        print(t)
    return(t)


print (print_Trianglar_numbers(8))