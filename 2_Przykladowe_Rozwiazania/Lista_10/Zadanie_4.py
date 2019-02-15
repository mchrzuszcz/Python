#!/usr/bin/env python

import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tekst', help="Tekst do zliczenia samoglosek", type=str, required=True)
    return parser.parse_args()

def licz_samogloski(tekst):
    tekst = tekst.lower()
    ilosc_samoglosek = 0
    ilosc_samoglosek += tekst.count("a")
    ilosc_samoglosek += tekst.count("e")
    ilosc_samoglosek += tekst.count("i")
    ilosc_samoglosek += tekst.count("o")
    ilosc_samoglosek += tekst.count("u")
    ilosc_samoglosek += tekst.count("y")
    return ilosc_samoglosek

def main():
    arguments = arg_parser()
    ilosc_samoglosek = licz_samogloski(arguments.tekst)
    print "Ilosc samoglosek w podanym tekscie wynosi: {}".format(ilosc_samoglosek)

if __name__ == '__main__':
    main()