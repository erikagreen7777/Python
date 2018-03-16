#!/usr/bin/python

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
    return sorted(string)