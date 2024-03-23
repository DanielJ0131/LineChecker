"""Line count program to count the number of codelines in a file"""

import os
import sys


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python linecount.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"{filename} does not exist.")
        sys.exit(1)
    else:
        count = linecount(filename)
        print(f"{filename} has {count} lines.")


def linecount(filename):
    """Count the number of lines in a file"""
    count = 0
    with open(filename, "r", encoding="utf-8") as infile:
        for _ in infile:
            count += 1
    return count


if __name__ == "__main__":
    main()
