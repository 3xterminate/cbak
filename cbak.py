#!/usr/bin/env python3
# cbak.py v2.0
import argparse
import glob
import os
import shutil
import sys


# print filename without absolut path
def print_name(b, b2):
    b, b2 = os.path.basename(b), os.path.basename(b2)
    print(b, "->", b2)


# create bak
def bak(file):
    for b in file:
        ext = os.path.splitext(b)[1]
        try:
            if ext == ".bak":
                b2 = os.path.splitext(b)[0]
                os.rename(b, b2)
            else:
                b2 = b + ".bak"
                shutil.copyfile(b, b2)
            print_name(b, b2)
        except Exception as e:
            print(e)


# list all .baks in folder
def listall(folder):
    folder = os.path.abspath(folder) + "/"
    dist = glob.glob(folder + "*.bak")

    for b in dist:
        b = os.path.basename(b)
        print(b)


# remove all .baks in folder
def clear(folder):
    folder = os.path.abspath(folder) + "/"
    dist = glob.glob(folder + "*.bak")
    for b in dist:
        try:
            os.remove(b)
            b = os.path.basename(b)
            print("Deleted:", b)
        except Exception as e:
            print(e)
            sys.exit(1)


# unbackup all .baks in folder
def unbackup(folder):
    folder = os.path.abspath(folder) + "/"
    dist = glob.glob(folder + "*.bak")
    for b in dist:
        ext = os.path.splitext(b)[1]
        try:
            if ext == ".bak":
                b2 = os.path.splitext(b)[0]
                os.rename(b, b2)
            print_name(b, b2)
        except Exception as e:
            print(e)


parser = argparse.ArgumentParser(
    description="Fast and easy backup creation tool.")
parser.add_argument("-f", "--file", nargs="+", help="File to backup")
parser.add_argument(
    "-c",
    "--clear",
    metavar="FOLDER",
    nargs="?",
    const=".",
    help="delete all backups in folder")
parser.add_argument(
    "-u",
    "--unbackup",
    metavar="FOLDER",
    nargs="?",
    const=".",
    help="unbackup all backups in folder")
parser.add_argument(
    "-l",
    "--list",
    metavar="FOLDER",
    nargs="?",
    const=".",
    help="list all backups in folder")
args = parser.parse_args()

if args.list:
    listall(args.list)
elif args.clear:
    clear(args.clear)
elif args.unbackup:
    unbackup(args.unbackup)
elif args.file:
    bak(args.file)
else:
    parser.print_help()
