name=input("Student's name=")
age=input("age=")
age=int(age)

# Variable needs to be initialized before it can be used
parentsname = ''

# If block
if(age < 17): # It could be True or False
    # These statements will run only if age is less than 17
    parentsname=input("Father's name=")
    print(f"fathers name={parentsname}")

# These statements will run regardless of the value of age
print(f"Registered student,{name.title()}, is {age} years old")

if (parentsname) : # Not equal to , its the opposite of equal to 
    # Print the name only if it is not empty
    print(f"Fathers name is {parentsname.title()}")
else: # Else block
    print(f"{name} is an adult")    
    print("----")


print("****")



