import sqlite3
from masterlock import *
import getpass
'''
initializing functions for the manager, run these in your project directory
'''
def create_database():
    connecting = sqlite3.connect('passwords.db')
    cursor = connecting.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER PRIMARY KEY,
        service_name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL)'''
    )
    connecting.commit()
    connecting.close()

create_database()
password = getpass.getpass()
db_ify(password)
