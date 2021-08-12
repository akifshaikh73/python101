def printline(length,character='-'):
    #dash='-' # Hardcode
    print(character*length)

# y=mx+c

def linear(x):
    m = 10
    c = 0
    y=x*m +c
    return y

def quadratic(x):
    a = 2
    b = 3
    c = 4
    y=x*x*a +b*x +c
    return y

x=17
linearresponse = linear(x)
print(linearresponse)
print(quadratic(x))

counter = 8
while (counter > 0):
    y=quadratic(counter)
    printline(y,'_')
    counter=counter-1

