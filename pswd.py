import json, pprint,os
import random
import string
import pyinputplus as pyip
from datetime import datetime

# Will append the date to the password to know the date it was created
currentTime = datetime.today().strftime('%b %d %Y')


try:

    def pswd_gen():
        while True:
            try:
                pswd_length = int(input("Enter the length of the password or press 'Enter/0 to return to main menu' : "))
        
                if pswd_length == (""):
                    print('Nothing entered, returning to main menu')
                    main_menu()            

                elif pswd_length == int(0):
                    print('0 entered, returning to main menu')
                    main_menu()

                small_letters = string.ascii_uppercase
                caps = string.ascii_lowercase
                integers = string.digits
                symbols = string.punctuation

                combine = small_letters + caps + integers + symbols

                betapswd = random.sample(combine,pswd_length)
                global fullcred
                password = "".join(betapswd)
                fullcred = password #+ ":" + currentTime
            except ValueError as VE:
                main_menu()
            print(fullcred)
        #pswd_gen()

    def update_pswrd():

        while True:

            print('')
            print("What would you like to do in the dB?")
            print('')
            choice = pyip.inputMenu(["Delete", "Update", "Quit"], lettered = False, numbered = True)
            print('')
            
            if choice == "Quit":
                print('\nYou chose to quit...returning to main menu.\n')
                main_menu()

            if choice == "Delete":
                print('')
                print('You chose to delete an entry . ')
                print('')
                content_to_delete = input('Enter a saved credential to delete : ').lower().title()


        # this funcion handles the delete option
        # take one argument, then open the dictionary in read mode to load to memory
        # rest of code in this block carries out the chosen action if the entry is found, else informs that
        # no such entry found

                def delete_content(saved_key):
                    
                    try:
                        with open("pswd_db.json", 'r') as read_file:
                            data = json.load(read_file)
                    
                        if content_to_delete not in data.keys():
                            print('\nNo such entry found : {} '.format(content_to_delete))
                            pass

                        else:
                            if content_to_delete in data.keys():
                                del data[content_to_delete]
                                print('All entries of "{}" removed '.format(content_to_delete))
                                
                                
                            with open("pswd_db.json", 'w') as write_file:
                                json.dump(data,write_file)
                            
                    except RuntimeError as RE:
                        print('Credentials of {} removed . '.format(content_to_delete))

                delete_content(content_to_delete) 

            else:
                if choice == "Update":
                    print('')
                    print('You chose to update the dB. ')
                    print('')
                    content_to_update = input('Enter a saved credential to update : ').lower().title()
                    print('')
                    new_pswd = input("Enter the new password for {} : ".format(content_to_update))
                    fullcredupdate = new_pswd + ":" + currentTime


                    def update_content(content_to_update):

                        with open("pswd_db.json", "r") as read_file:
                            data = json.load(read_file)

                    
                        if content_to_update not in data.keys():
                            print('\nNo such entry found : {} '.format(content_to_update))
                            pass

                        else:

                            if content_to_update in data.keys():
                                data[content_to_update] = fullcredupdate

                                with open ("pswd_db.json", "w") as write_file:
                                    json.dump(data,write_file)

                                print("Password for '{}' has been updated . ".format(content_to_update))

                    update_content(content_to_update)

    def create_record():
        while True:

            with open ("pswd_db.json", "r") as read_file:
                pswd_records = json.load(read_file)

            print('')
            logInCred = input('Enter the LogIn/User Name : ').lower().title()

            if logInCred == "":
                print('Nothing entered, returning to main menu')
                main_menu()
            else:
                logInCred == logInCred
                logInPswrd = input('Enter a Password : ')
                fullcred = logInPswrd + ":" + currentTime

                data = {}    
                data[logInCred] = fullcred
                pprint.pprint(data)

                pswd_records.update(data)
                print('')
                print('Records updated')

            with open("pswd_db.json", "w") as write_file:
                json.dump(pswd_records, write_file)
                    
            #main_menu()


    def new_record(credential,passwd):
            with open ("pswd_db.json", 'r') as read_file:
                pswd_records = json.load(read_file)
        
    # created an empty dict, then assigned the variables that will be the key:value
    # credential:passwd respectively

            data = {}    
            data[credential] = passwd
            pprint.pprint(data)

            pswd_records.update(data)
            print('')
            print('Records updated')

            with open("pswd_db.json", "w") as write_file:
                json.dump(pswd_records, write_file)

            
    # called the 'update' method to update original json dict that has been loaded into pswd_records variable
    # then open the dictionary in write mode this time to dump the newly data into it
        
            pswd_records.update(data)
            print('')
            print('Records updated')

            with open("pswd_db.json", "w") as write_file:
                json.dump(pswd_records, write_file)


    def find_a_pswrd():
        
        while True:
        
            with open("pswd_db.json", "r") as readfile:
                pwdDb = json.load(readfile)

            print('')
            find_pwd = input("search for password of : ").lower().title()
            print('')
            

        # conditional block to tell if password already exist, if not further option to add    
            if find_pwd == '':
                print("Nothing entered, returning to main menu\n")
                main_menu()
                
            
            for k,v in pwdDb.items():   
                if k == find_pwd:
                    print("Match Found:\n" + os.linesep + k,':',v)
                    pass
            
            else:
                if find_pwd not in pwdDb:
                    print('Entry not found, would you like to save a new pswd?\n ')

                    response = pyip.inputMenu(["Yes","No"],lettered=False, numbered=True)
                    if response == "Yes":
                        create_record()

                    else:
                        main_menu()
                    print('')    
                    cred = input('Enter a name/key identifier: ').lower().title()
                    if cred == '':
                        print('nothing entered, exiting!')
                        quit()
                    print('')
                    print('Do you want to use the generated password?')
                    new_pswd = pyip.inputMenu(["yes","No"],numbered=True)

                    if new_pswd == "yes":
                        passwd = fullcred
                        new_record(cred,passwd)
                        main_menu()


                    if new_pswd == "No":
                        own_paswrd = input("Enter Password for " + cred + ": ")
                        new_record(cred,own_paswrd)

                #new_record(cred,passwd)

# the main menu of the program, every option in this block is linked to a function                
    while True:
        def main_menu():
            print('')
            print("What would you like to do: ")
            print('')
            options = pyip.inputMenu(["Generate a Password", "Retrieve a Password", "Store a Password", "Update/Delete a Password","Exit"],numbered=True)

            if options == "Generate a Password":
                pswd_gen()

            if options == "Retrieve a Password":
                find_a_pswrd()

            if options == "Store a Password":
                create_record()

            if options == "Update/Delete a Password":
                update_pswrd()

            if options == "Exit":
                print("Bye for now, take care !")
                quit()
        main_menu()

except KeyboardInterrupt as KI:
     print('\nInteruption detected')
     main_menu()
