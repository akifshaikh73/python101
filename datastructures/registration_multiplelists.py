courses = ('aws',  'java', 'python')

students=['ahmed','muhammad','ali','fatima','ayesha']
semails=['a@gmail.com','m@yahoo.com','ali@yahoo.com','f@gmail.com','ayesha@yahoo.com']
coursesenrolled=['aws','aws','java','python','python']

listofstudents=[
    {'name':'ahmed','email':'a@gmail.com','course':'aws','address':'123 main'},
    {'name':'muhammad','email':'m@yahoo.com','course':'aws','address':'12 finley'},
    {'name':'ali','email':'ali@yahoo.com','course':'java','address':'15 lawler ave'},
]


numofstudents=len(students)

#print(f"A total of {len(courses)} are offered:")
#for course in courses:
#    print(course)

print("name,email,course,address")

for student in listofstudents:
    #print(f"student {student['name']} with the email id {student['email']} is enrolled in {student['course']} and lives at {student['address']}")
    print(f"{student['name']} , {student['email']} , {student['course']} , {student['address']}")


#for i in range(numofstudents):
#    print(f"student {students[i]} with the email id {semails[i]} is enrolled in {coursesenrolled[i]}")

