#!/usr/bin/env python

import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help="Path to file", type=str, required=True)
    parser.add_argument('--text', help="Text to be added to file", type=str, required=True)
    return parser.parse_args()

def write_to_file(content, filename):
    with open(filename, "a") as f:
        f.write("\n{}".format(content))

def main():
    arguments = arg_parser()
    write_to_file(arguments.text, arguments.file)

if __name__ == '__main__':
    main()