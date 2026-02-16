import sqlite3
import os
import hashlib
import sys
import getpass

def hashmaster(password):
    h = hashlib.new("sha256")
    passw = password.encode('UTF-8')
    h.update(passw)
    return h.hexdigest()

def db_ify(passy, service="master2", user="eatpant"):
    encryptedpassword = hashmaster(passy)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO passwords (service_name, username, password) VALUES (?, ?, ?)', (service, user, encryptedpassword)
        )
    conn.commit()
    conn.close()

def check(service, password):
    passk = hashmaster(password)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT password FROM passwords WHERE service_name = ?', ([service])
    )
    result = cursor.fetchone()
    retrieved = ''.join(result)
    if retrieved == passk:
        return("onward")
    else:
        return None