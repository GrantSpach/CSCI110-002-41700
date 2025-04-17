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



def myreadposint ():

    data = input("Please enter your int: ")

    try:
        data = int(data)

        if data <= 0:
            my_errors = ValueError("> {0} < is not an interger ".format(data))

            raise my_errors

        elif data >= 1:
            print("> {0} < is a positive interger ".format(data))

    except ValueError:

        print("> {0} < is not an interger ".format(data))

myreadposint()




