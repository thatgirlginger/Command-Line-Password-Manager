import sqlite3
import hashlib
import getpass

'''
functions for getting and initializing the master key password
'''

def hashmaster(password):
    h = hashlib.new("sha256")
    passw = password.encode('UTF-8')
    h.update(passw)
    return h.hexdigest()

def db_ify(service="master", password):
    user = getpass.getuser()
    hashedpass = hashmaster(passy)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO passwords (service_name, username, password) VALUES (?, ?, ?)', (service, user, encryptedpassword)
        )
    conn.commit()
    conn.close()

def check(service, password):
    passk = hashmaster(password)
    user = getpass.user()
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT password FROM passwords WHERE service_name = ? AND username = ?', (service, username)
    )
    result = cursor.fetchone()
    if result == None:
        return("incorrect system user. password manager must be used by the system creator")
    retrieved = ''.join(result)
    if retrieved == passk:
        return True
    else:
        return False
