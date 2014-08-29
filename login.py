#!/usr/bin/python

import crypt, getpass, pwd
import sys, csv

def login():
	username = raw_input('Python login: ')
	try:
		cryptedpasswd = pwd.getpwnam(username)[1]
	except KeyError:
		print "Username not valid!"
		sys.exit(1)

	if cryptedpasswd:
		if cryptedpasswd == 'x' or cryptedpasswd == '*':
			# get encrypted password from shadow file
			cryptedpasswd = get_shadow_pwd(username)
			#raise NotImplementedError(
			#	"Sorry, currently no support for shadow password")
		cleartext = getpass.getpass("Password: ")
		return crypt.crypt(cleartext, cryptedpasswd) == cryptedpasswd
	else:
		return 0 

def get_shadow_pwd(username):
	'''
	Retrieves the username's encrypted password from
	the shadow file in the current directory
	'''
	csv_file = csv.DictReader(open('shadow','rb'), delimiter=':')
	for line in csv_file:
		if username == line['username']:
			return line['password']
	return None

if __name__ == '__main__':
	if login() == 1:
		print "Login successful!"
	else:
		print "Login failed!"
