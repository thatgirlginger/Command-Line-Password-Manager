from cryptography.fernet import Fernet

def create_key():
    key=Fernet.generate_key()
    with open('key.key', 'wb') as keyfile:
        keyfile.write(key)

def load_key():
    return open('key.key', 'rb').read()

def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()
