#!/usr/bin/python
import sys
import re

def main():
    if len(sys.argv) > 1:
        if sys.argv[1]:
            matchObject = re.sub(r'(\t+| +)', ' ', sys.argv[1])
            print matchObject
    else:
        print "\n"


if __name__ == "__main__":
    main()