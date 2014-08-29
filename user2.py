#!/usr/bin/python

import os, crypt, sys
from datetime import date, timedelta
import logging
import argparse

logging.basicConfig(filename=sys.argv[0] + '.log', level=logging.DEBUG, 
	filemode='w')
 
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs='+', help="Creates a local Linux account")
parser.add_argument("-d", "--delete", nargs='+', help="Deletes a local Linux account")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
# adding required argument
parser.add_argument("-bar", required=True, help="Required argument")
args = parser.parse_args()

now = date.today()
end = now + timedelta(days=5)		#password expiration day is 5 days
expire = end.isoformat()
if not os.geteuid() == 0:
	logging.critical("Needs root privileges!")
	sys.exit("\nYou will need to be root to create/delete users, perhaps try sudo\n")
password = 'Password1'
encPassword = crypt.crypt(password, 'a1')

if args.verbose:
	logging.info("Verbosity turned on")
	print "Verbosity turned on"

if args.add:
	for user in args.add:
		logging.debug("Creating user: %s" % user) 
		os.system("useradd -m -p " + encPassword + " -e " + expire + ' ' + user)
if args.delete:
	for user in args.delete:
		logging.debug("Deleting user: %s" % user) 
		os.system("userdel -r " + user)
print "done"

