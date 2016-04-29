# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:23:52 2015

@author: Taikor
"""
import os
import time
import codecs
import json
import sys
import logging


def listdir_powered(folder):
    files = os.listdir(folder)
    myfiles = list()

    for file in files:
        myfiles.append(os.path.join(folder, file))
    myfiles = sorted(myfiles)
    return myfiles


def f_read(_file, readlines=False, strip_option=True):
    strip_option_enum = (True, False)
    readlines_enum = (True, False)

    if strip_option not in strip_option_enum:
        logging.warning("Wrong Argument Given: strip_option")
        raise Exception
    if readlines not in readlines_enum:
        logging.warning("Wrong Argument Given: readlines")
        raise Exception
    # check if a illegal argument was given

    if not readlines:
        with codecs.open(_file, "r", encoding="utf8") as f:
            s = f.read()
            return s
    else:
        with codecs.open(_file, "r", encoding="utf8") as f:
            s = f.readlines()

            if strip_option:
                for i in range(len(s)):
                    s[i] = s[i].strip("\n")
                    s[i] = s[i].strip("\r")
                    s[i] = s[i].strip(" ")
                    s[i] = s[i].strip("\t")
            return s


def f_read_generator(_file, strip_option=True):
    strip_option_enum = (True, False)
    if strip_option not in strip_option_enum:
        logging.warning("Wrong Argument Given: strip_option")
        raise Exception
    f = codecs.open(_file, "r", encoding="utf8")
    while True:
        yield f.readline()


def f_write(_file, content, mode="w"):
    with codecs.open(_file, mode, encoding="utf8") as f:
        f.write(content)
    return 0


def json_read(_file):
    json_str = f_read(_file)
    json_obj = json.loads(json_str)
    return json_obj


def json_write(_file, json_obj):
    json_str = json.dumps(json_obj, ensure_ascii=False)
    f_write(_file, json_str)
    return 0


class Timer(object):
    def __init__(self):
        self.start_time = time.time()
        self.end_time = 0

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def end(self):
        self.end_time = time.time()
        return self.t_elapsed()

    def t_elapsed(self):
        return self.end_time - self.start_time


def get_entry_pth():
    tmp = sys.path[0]
    if sys.path[0] == "":
        return os.getcwd()
    else:
        return tmp


def get_entry_pth_parent():
    entry_pth = get_entry_pth()
    return os.path.dirname(entry_pth)


def get_entry_pth_basename():
    entry_pth = get_entry_pth()
    return os.path.basename(entry_pth)


def extend_pythonpath():
    try:
        package_path = get_entry_pth_parent()
        sys.path.append(package_path)
        return True
    except Exception:
        raise Exception


def create_abs_path(relative_pth):
    base_path = get_entry_pth()
    abs_path = os.path.join(base_path, relative_pth)
    return abs_path


if __name__ == "__main__":
    path = r"C:\Users\roy\Desktop\abc.txt"
    print(f_read(path, readlines=True))
