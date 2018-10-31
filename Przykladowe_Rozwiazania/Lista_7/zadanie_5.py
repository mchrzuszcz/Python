#!/usr/bin/env python

import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help="Path to file", type=str, required=True)
    parser.add_argument('--mode', help="Mode how to read file, 0 - (default choice) read whole file, 1 - omit lines with # at the beginning, 2 - line numbering", choices=["0","1","2"], default=0, type=int)
    return parser.parse_args()


def read_file(file_name):
    content= []

    with open(file_name, "r") as f:
        for line in f:
            content.append(line)

    for i in range(len(content)):
        content[i] = content[i].replace("\n", "")

    return content


def parse_and_print(content, mode):
    if mode == "0":
        for line in content:
            print line
    elif mode == "1":
        for line in content:
            if not line.startswith("#"):
                print line
    elif mode == "2":
        for i, ele in enumerate(content):
            print "{}. {}".format(i+1,ele)


def main():
    arguments = arg_parser()
    content = read_file(arguments.file)
    parse_and_print(content, arguments.mode)


if __name__ == '__main__':
    main()