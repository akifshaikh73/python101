courses = ['aws','python','java']

students =[]

studentname ='--'
classlimit = 5



while (studentname != '' and len(students) < classlimit ):
    studentname=input("Name:")
    if(studentname != ''):
        students.append(studentname)
    #print(sorted(students))

students.sort()

#print(f"The final list is {students}")
i=0
for s in students:
    print(f"The name is {s}")
    i=i+1

