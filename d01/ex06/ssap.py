#!/usr/bin/python
import sys


def ft_split(string):
    array = string.split(" ")
    j = 0
    for i in range(0, len(array)):
        if array[i] != '':
            j += 1

    string = [None] * j
    j = 0
    for i in range(0, len(array)):
        if array[i] != '':
            string[j] = array[i]
            i += 1
            j += 1
    return (string)
#
#
def main():
    if len(sys.argv) > 1:
        array = ' '.join(sys.argv[1:])
        new = ft_split(array)
        print ("\n".join(sorted(new)))



if __name__ == "__main__":
    main()
