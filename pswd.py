import json
import pprint
import pyinputplus as pyip
from datetime import datetime, timedelta

# creating the database

""" with open("pswd_db.json", 'w') as writeFile:
    json.dump(dataDb,writeFile) """

def new_record(credential,passwd):
        with open ("pswd_db.json", 'r') as read_file:
            pswd_records = json.load(read_file)
     
        data = {}    
        data[credential] = passwd
        pprint.pprint(data)

        update = pswd_records.update(data)
        print('')
        print('Records updated')

        with open("pswd_db.json", "w") as write_file:
            json.dump(pswd_records, write_file)

while True: 

    with open("pswd_db.json", "r") as readfile:
        pwdDb = json.load(readfile)

    print('')
    find_pwd = input("search for password of : ").lower().title()
    print('')
    
    if find_pwd == '':
        print("Nothing entered, exiting program")
        print('')
        quit()

    for k,v in pwdDb.items():   
        if k == find_pwd:
            print(k,':',v)
    
    else:
        if find_pwd not in pwdDb:
            print('Entry not found, would you like to save a new pswd? ')
            print('')

            response = pyip.inputMenu(["Yes","No"],lettered=False, numbered=True)
            if response == "Yes":
                pass

            else:
                continue

            cred = input('Enter a name/key identifier: ').lower().title()
            if cred == '':
                print('nothing entered, exiting!')
                quit()

            passwd = input('Enter the password to store: ')
            if passwd == "":
                print('nothing entered, exiting!')
                quit()


            new_record(cred,passwd)
