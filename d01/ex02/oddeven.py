#!/usr/bin/python
# import sys


while True:
    try:
        num = raw_input("Enter a number: ")
    except EOFError:
        print "^D"
        break
    try:
        number = int(num)
    except ValueError:
        print "\'%s\' is not a number" % num
    else:
        check = number%2
        if check == 0:
            print "The number %d is even" % int(number)
        elif check == 1:
            print "The number %d is odd" % int(number)
