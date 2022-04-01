#!/usr/bin/python3
"""
Demonstrate the use of recursion to execute a search through the local filesystem
"""
import argparse
import os
from os import path


def search(filename, fullpath) -> bool:
    print("searching in: " + fullpath)
    if filename in fullpath:
        print("Found: ", fullpath)
        return True

    if path.isfile(fullpath):
        return False

    for file in os.listdir(fullpath):
        return search(filename, path.join(fullpath, file))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('pattern')
    args = parser.parse_args()
    search(args.pattern, args.path)


if __name__ == '__main__':
    main()
