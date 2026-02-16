# Command-Line-Password-Manager
A simple python password manager for the command line

## to get started:

if not already installed in your directory, install sqlite3

```
pip install sqlite3
```

(this program also uses cryptography and getpass, which are part of the standard Python library)

navigate to the directory you want to use for your manager, then paste the following:

```
git clone https://github.com/thatgirlginger/Command-Line-Password-Manager
```
## initialize the application
now, run the initializing function. note that the service name goes in as "master" by default

```
$ python3 initialize.py
```
you should be prompted to enter a password. your console will not echo what you have typed, so be careful
(if you don't want to lock access to the whole thing, you could also initialize manually by opening a python shell and running the following commands. just make sure you go into manager.py and comment out or delete the first few lines):
```
>>>from initialize import create_database, create_key
>>>create_database()
>>>create_key()
```
(at any time, you can decide to password lock the manager if you didn't at first)
```
>>>from masterlock import db_ify
```

if you ran the whole file, not manually in the shell, the code will also create your encryption key. your password to get into the password and add/change/retrieve passwords is hashed, so this key does not decrypt it

## use it
once you've got everything initialized, run your manager with 

```
python3 manager.py
```
you'll be prompted to type an action: "newentry", "getuser", "getpassword", "update", "delete", "options", and "quit"
they're pretty self-explanatory. to retrieve a password, you'll have to enter the service and the username. if you try to update or delete, you'll need to enter the master password. it's set to a 'while true' so the whole thing will stay open until you want to close it



i made this to test out some of my burgeoning command line app, SQL, and security skills. i'm self-taught and coming from a humanities background, so please submit an issue if there's something glaringly wrong with it. i'm happy to have any input!
