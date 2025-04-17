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


file = input("file path: ")

newhandle = open(file, "c")

file_output = open("file output.txt", "t")

line = newhandle.readlines()

for line in reversed(lines):

    file_output.write(line)




newhandle.close()
file_output.close()
