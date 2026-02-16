import sqlite3
from cryptography.fernet import Fernet
from database import *
from encryption import *

def add_password(service, username, password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    key = load_key()
    encryptedpass = encrypt_password(password, key)
    cursor.execute('INSERT INTO passwords (service_name, username, password) VALUES (?, ?, ?)', (service, username, encryptedpass))
    conn.commit()
    conn.close()

def retrieve_user(service):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM passwords WHERE service_name = ?', [service])
    result = cursor.fetchone()
    conn.close()
    return result

def retrieve_password(service, username):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    key = load_key()
    cursor.execute('SELECT password FROM passwords WHERE service_name = ? AND username = ?', (service, username))
    result = cursor.fetchone()
    conn.close()
    if result:
        return decrypt_password(result[0], key)
    else:
        return None
    
def update(service, username, new_password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    key = load_key()
    encrypted_password = encrypt_password(new_password, key)
    cursor.execute('UPDATE passwords SET password = ? WHERE service_name = ? AND username = ?', (encrypted_password, service, username))
    conn.commit()
    conn.close()

def delete(service, username, password):
    check = retrieve_password(service, username)
    if check == password:
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM passwords WHERE service_name = ? AND username = ?', (service, username))
        conn.commit()
        conn.close()
        print("successful")
    elif check != password:
        print("password failed, delete not executed")
