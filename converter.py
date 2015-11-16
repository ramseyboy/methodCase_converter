#!/usr/bin/env python3

__author__ = 'walkerhannan'

import fileinput
import re
import sys

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')
sub_between_re = re.compile(r'void (.+?)\(\)', re.DOTALL)


def read_file():
    for line in fileinput.input(inplace=True):
        camel_case_methods = sub_between_re.findall(line)
        if len(camel_case_methods) > 0:
            new_sig = "{0} {1}{2}".format('void', convert(camel_case_methods[0]), '()')
            sys.stdout.write(sub_between_re.sub(new_sig, line))
        else:
            sys.stdout.write(line)
    sys.stdout.write("\n")


def convert(method):
    s1 = first_cap_re.sub(r'\1_\2', method)
    return all_cap_re.sub(r'\1_\2', s1).lower()


if __name__ == '__main__':
    read_file()
