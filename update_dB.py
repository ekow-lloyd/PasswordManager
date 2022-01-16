import json
import pyinputplus as pyip


while True:

    print('')
    print("What would you like to do in the dB? ")
    print('')
    choice = pyip.inputMenu(["Delete", "Update", "Quit"], lettered = False, numbered = True)
    print('')
    
    if choice == "Quit":
        print('\nYou chose to quit...Terminating session.\n')
        exit()

    if choice == "Delete":
        print('')
        print('You chose to delete an entry . ')
        print('')
        content_to_delete = input('Enter a saved credential to delete : ').lower().title()

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
            print('You chose to update the dB . ')
            print('')
            content_to_update = input('Enter a saved credential to update : ').lower().title()
            print('')
            new_pswd = input("Enter the new password for {} : ".format(content_to_update))

            def update_content(content_to_update):

                with open("pswd_db.json", "r") as read_file:
                    data = json.load(read_file)

               
                if content_to_update not in data.keys():
                    print('\nNo such entry found : {} '.format(content_to_update))
                    pass

                else:

                    if content_to_update in data.keys():
                        data[content_to_update] = new_pswd

                        with open ("pswd_db.json", "w") as write_file:
                            json.dump(data,write_file)

                        print("Password for '{}' has been updated . ".format(content_to_update))

            update_content(content_to_update)


