import json
import pprint
import pyinputplus as pyip
from datetime import datetime, timedelta

# this block opens the dict in read mode to query it

def new_record(credential,passwd):
        with open ("pswd_db.json", 'r') as read_file:
            pswd_records = json.load(read_file)
     
 
 # created an empty dict, then assigned the variables that will be the key:value
 # credential:passwd respectively

        data = {}    
        data[credential] = passwd
        pprint.pprint(data)

        
# called the 'update' method to update original json dict that has been loaded into pswd_records variable
# then open the dictionary in write mode this time to dump the newly data into it
      
        pswd_records.update(data)
        print('')
        print('Records updated')

        with open("pswd_db.json", "w") as write_file:
            json.dump(pswd_records, write_file)

# using the while true helps keep the program running till terminated by user
# dictionary is opened again in read mode in order to load the key:values into memory for query
# user input is then required

while True: 

    with open("pswd_db.json", "r") as readfile:
        pwdDb = json.load(readfile)

    print('')
    find_pwd = input("search for password of : ").lower().title()
    print('')
    

# conditional block to tell if password already exist, if not further option to add    
    if find_pwd == '':
        print("Nothing entered, exiting program\n")
        quit()

    for k,v in pwdDb.items():   
        if k == find_pwd:
            print(k,':',v)
    
    else:
        if find_pwd not in pwdDb:
            print('Entry not found, would you like to save a new pswd?\n ')

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
