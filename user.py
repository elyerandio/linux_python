#!/usr/bin/python

import os, crypt, sys
from datetime import date, timedelta
import logging

logging.basicConfig(filename=sys.argv[0] + 'log', level=logging.DEBUG, 
	filemode='w')
 
if len(sys.argv) == 1:
	logging.critical("Needs root privileges!")
	sys.exit("\nYou need to specify the username to create!\n")
	
logging.debug("Number of arguments: %d" % len(sys.argv))
logging.debug("Arguments: %s" % sys.argv)

now = date.today()
end = now + timedelta(days=5)		#password expiration day is 5 days
expire = end.isoformat()
if not os.geteuid() == 0:
	sys.exit("\nYou will need to be root to create users, perhaps try sudo\n")
password = 'Password1'
encPassword = crypt.crypt(password, 'a1')
for user in sys.argv[1:]:
	logging.debug("Creating user: %s" % user) 
	os.system("useradd -m -p " + encPassword + " -e " + expire + ' ' + user)
print "done"
