class SubClass:
    def __init__(self, db):
        self.db = db
    
    def userInput(self):
        userInput = {}
        uname = str(input("Enter User Name: "))
        uaddress = str(input('Enter user address: '))
        userInput['Name'] = uname
        userInput['Address'] = uaddress
        return userInput
                    
    def findUser(self, db, uInput):
        uCollections = db.UserCollections.find({'Name': uInput['Name']})
        for uInput in uCollections:
            print(uInput)
            return 1 

    def displayOneUser(self, db, uInput):
        uCollections = db.UserCollections.find({'Name': uInput['Name']})
        for uInput in uCollections:
            print(uInput)
            return uInput

    def insertUser(self, db, uInput):
        result = db.UserCollections.insert_one(uInput)
        if (result.acknowledged):
            print('User successfully added!!!\n \nUser Object ID is: ', str(result.inserted_id)) #Printing user object id

    def displayAllUser(self, db):
        print('--------- Users Available in UserDataDB ---------\n')
        uCollections = db.UserCollections.find()
        for allrecord in uCollections:
            print(allrecord)

    def updateUser(self, db, uInput):
        db.UserCollections.update(
            {
                'Name': uInput['Name']
            },
            {
                '$set':{
                    'Address': uInput['Address']
                }

            }, multi = False
            )
        uCollections = db.UserCollections.find({'Name': uInput['Name']})
        for uInput in uCollections:
            print('Record updated successfully!!', uInput)

    def deleteUser(self, db, uInput):
        db.UserCollections.delete_one({
            'name': uInput['Name']
        })
        print('!!!-----Record Deleted----!!!', uInput)