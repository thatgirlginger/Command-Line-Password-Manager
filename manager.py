from management import *
from encryption import *
from managermanagement import *
import sys
import getpass


'''
the app to run in your command line
'''

serviceentry = getpass.getpass(prompt='service?')
passwordentry = getpass.getpass(prompt='password?')
string = check(serviceentry, passwordentry)
if not string == None:
    pass
else:
    print("incorrect password")
    sys.exit()


while True:
    a = input("action?")
    match a:
        case "newentry":
            service = input("service?")
            user = input("username?")
            passw = input("password?")
            add_password(service, user, passw)
            print("password added")
        case "getuser":
            service = input("service?")
            username = retrieve_user(service)
            print(username)
        case "getpassword":
            service = input("service?")
            user = input("username?")
            password = retrieve_password(service, user)
            print(password)
        case "updatepassword":
            service = input("service?")
            user = input("username?")
            newp = input("new password?")
            update(service, user, newp)
        case "deleteentry":
            service = input("service?")
            user = input("username?")
            password = input("password?")
            delete(service, user, password)
        case "options":
            print("newentry, getuser, getpassword, updatepassword, deletentry")
        case "quit":
            sys.exit()
