#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os


def process_path():
    return []


def process_single_file(file_path, rep_str):
    try:
        file = open(file_path, mode='r')
        result = ""
        tab_count = 0
        raw_lines = file.readlines()
        for line in raw_lines:
            tab_count += line.count("\t")
            line = line.replace("\t", rep_str)
            result += line
        file.close()
        os.rename(path, path + ".old")
        print("replaced %d tab(s)" % tab_count)
        new_file = open(path, mode='w')
        new_file.write(result)
        new_file.close()
    except FileNotFoundError:
        print("File not found: %s" % path)
    except Exception as e:
        print("error appeared: %s" % e)


def get_replace_str(count=0):
    try:
        if count <= 0:
            space_num = int(input("how many spaces will one tab be replaced with: "))
        else:
            space_num = count
        rep_str = ""
        for i in range(space_num):
            rep_str += " "
    except Exception as e:
        print("input illegal:%s" % e)
        print("use default(4 spaces)")
        rep_str = "    "
    return rep_str


if __name__ == "__main__":
    arg2 = ""
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if len(sys.argv) > 2:
            arg2 = sys.argv[2]
    else:
        print("argument not found")
        path = input("input file path: ")
    paths = process_path()
    try:
        arg2_val = int(arg2)
    except ValueError as e:
        arg2_val = 0
        print("argument 2 illegal")
    process_single_file(path, get_replace_str(arg2_val))
