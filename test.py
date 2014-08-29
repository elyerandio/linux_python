#!/usr/bin/python
import getpass
import crypt

u = raw_input('User name: ')
p = getpass.getpass('Password: ')

print "User = %s" % u
print "Pwd = %s" % p

