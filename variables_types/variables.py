# Example of Swapping two variable
# Incorrect way of swapping

a=25
b=36
# Before swapping
print(a,b)
a=b
b=a
# After  swapping
print(a,b)

print("------------------------")
# Correct way of swapping
# Initializing the variables
a=25
b=36
# Before swapping
print(a,b)
temp=a
a=b
b=temp
# After  swapping
print(a,b)


print("------------------------")
# Shortcut way  of swapping using pythons syntax
# Initializing the variables
a=25
b=36
# Before swapping
print(a,b)
a,b = b,a
# After  swapping
print(a,b)
