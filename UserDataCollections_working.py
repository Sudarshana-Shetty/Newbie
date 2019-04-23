from pymongo import MongoClient
from AllFunctions import SubClass
client = MongoClient()
db = client['UserDataDB'] # Creating new Data base 

subobj = SubClass(db)
           
print("---Welcome to User Data Collections Menu---")
print("Please select any one of the below option: ")
print("1. Inser user data")
print("2. Update existing data")
print("3. Delete existing record")
choice = int(input("Please enter your choice: ")) # Accepting input from user

if (choice == 1):
    uInput = subobj.userInput()
    print("You have entered the following details: \n", uInput)     
   
    result = subobj.findUser(db, uInput)
    
    if (result == 1):
        print("User already exist......")
        exit
    else:
        subobj.insertUser(db, uInput)
        subobj.displayAllUser(db)

if (choice == 2):
    uInput = {}
    print("Enter the name of the user which you want to update: ")
    uname = str(input("Enter User Name: "))
    uInput['Name'] = uname
    result = subobj.findUser(db, uInput)
    if (result != 1):
        print("User Does not exist......")
        exit
    else:
        subobj.displayOneUser(db, uInput)
        print("Please enter the new address: ")
        uaddress = str(input('Enter user address: '))
        uInput['Address'] = uaddress
        subobj.updateUser(db, uInput)
        subobj.displayAllUser(db)

if(choice == 3):
    uInput = {}
    print("Enter the name of the user which you want to delete: ")
    uname = str(input("Enter User Name: "))
    uInput['Name'] = uname
    result = subobj.findUser(db, uInput)
    if (result != 1):
        print("User Does not exist......")
        exit
    else:
        opt = str(input("Are you sure you want to delete the following user (Y/N):  \n"))
        subobj.displayOneUser(db, uInput)
        if(opt == 'Y' or opt == 'y'):
            subobj.deleteUser(db, uInput)
            subobj.displayAllUser(db)
        else:
            exit



    

