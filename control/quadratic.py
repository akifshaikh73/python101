# y = ax^2 + bx + c
a,b,c= 10 ,45,30

x=input("x=")
x=int(x) # Converting the string value from input into an integer

# Actual expression evaluation
y= a*x*x + b*x + c

# Converting the value of y to a string for concatenation
print(f"ax^2+bx+c={y}")

