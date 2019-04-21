class UserInput:
	print("---Welcome to User Data Collections Menu---")
	print("Please select any one of the below option: ")
	print("1. Inser user data")
	print("2. Update existing data")
	print("3. Delete existing record")
	# selection = int(input("Please enter your choice:"))
	selection = input("Please enter your choice: ")

	if (selection == 1):
		userInsert(Name, Address)

	if (selection == 2):
		userUpdate(Name, Address)

	if (selection == 3):
		userDelete(Name, Address)

class UserDataCollection:
	def __init__(self, name, address):
		self.name
		self.address

	def insertUser(self):
		
