import argparse
import os

parser = argparse.ArgumentParser('run the linux command in python')
parser.add_argument('commands', nargs='+', help='the command to be run')
args =  parser.parse_args()
os.system(' '.join(args.commands))
