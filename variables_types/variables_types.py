# Variables and Types

fname=input("First Name:")

lname=input("Last Name:")

hnumber=input("House Number:")

street=input("Street:")
print("----------------------------------")
#print("Assalam o alaium \n"+fname.capitalize()+' '+lname.capitalize()+"\nYou live at "+hnumber+' '+street.capitalize())

print(f"Assalam o alaium \n{fname.capitalize()} {lname.capitalize()} \nYou live at {hnumber} {street.capitalize()}")

# Printing the original variables , to show that they have not changed - Strings are *immutable*
print(fname,lname,street)


