# -*- coding: utf-8 -*-

db={}

def create_user() :
	print "please input your username"
	username = raw_input ("username:")
	if username in db :
		print "sorry username is already excite ! please input again !"
	else :
		print "please input your password"
		password = raw_input ("password:")
		db[username]=password
def old_user() :
	print "please input your username"
	username = raw_input ("username:")
	if username not in db :
		print "sorry username is not excite ! please input again !"
	else :
		print "please input your password"
		password = raw_input ("password:")
		if db.get(username)==password:
			print "welcome to xizhilang"
		else :
			print "sorry your login is incorrect"
CMDs={'o':old_user,'n':create_user}
def login_user():
	print "please input n/o/q"	
	while True:
         choice = raw_input ("choice:").lower()
         if choice == 'q':break
         if choice not in 'noq' :
             print "try again"
             continue
         CMDs[choice]()
if __name__ =='__main__':
	login_user()
			

	