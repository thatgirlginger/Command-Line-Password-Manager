from management import *
from masterlock import *
import sys
import getpass


'''
the app to run in your command line
'''

pentry = getpass.getpass()
pcheck = check(pentry)
if pcheck == True:
    pass
else:
    print("incorrect")
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
            pentry = check(getpass.getpass())
            if pentry == True:
                update(service, user, newp)
            else:
                print("update failed")
        case "deleteentry":
            service = input("service?")
            user = input("username?")
            password = input("password?")
            pentry = check(getpass.getpass())
            if pentry == True:
                delete(service, user, password)
            else:
                print("not deleted")
        case "options":
            print("newentry, getuser, getpassword, updatepassword, deletentry")
        case "quit":
            sys.exit()
