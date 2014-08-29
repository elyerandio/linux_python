#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs="+", help="Creates a local Linux account")
parser.add_argument("-d", "--delete", nargs="+", help="Deletes a local Linux account")
args = parser.parse_args()

if args.add:
	for u in args.add:
		print "Creating user: " + u

if args.delete:
	for u in args.delete:
		print "Deleting user: " + u
