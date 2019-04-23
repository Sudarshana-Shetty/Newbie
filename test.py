from pymongo import MongoClient
client = MongoClient()
print("Connsction Established:", client)

db = client['test-database']
print("DB Created successfully!!", db)

courses = db.courses
print("Collections or Table created: ", courses)
'''
# Insert a single record
course1 = {
	'author': 'Balaji',
	'course': 'MongoDB',
	'price': 100,
	'rating': 5
}

result = courses.insert_one(course1)

if result.acknowledged:
	print('Course added: the course id ', str(result.inserted_id))
	
# Insert multiple records

arr_course1 = [{
	'author': 'Harsha',
	'course': 'MongoDB',
	'price': 100,
	'rating': 5
}, 
{
	'author': 'Sudarshan',
	'course': 'MongoDB',
	'price': 100,
	'rating': 5
	}
]

results = courses.insert_many(arr_course1)

for object_id in results.inserted_ids:
	print('Course added: the course id ', str(object_id)) '''

# Retriving all the data from mongo
courses = courses.find()

for course1 in courses:
	print(course1)
	# pprint.pprint(course1)

# Filter results 
courses = courses.find({
	'author': 'Balaji'
	})

for course1 in courses:
	print(course1)

# Filter results multiple condition

courses = courses.find({
	'author': 'Balaji',
	'price':{
		'$gt': 10
	}
	})

for course1 in courses:
	print("Multi condition filter:", course1)