import sqlite3
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
