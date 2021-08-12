# Function definition
def printline(length,character='-'):
    #dash='-' # Hardcode
    print(character*length)

printline(100,'o')
printline(100,'_')
printline(25)

# Invoking
counter = 4
while (counter > 0):
    printline(100,'*')
    printline(50,'o')
    counter=counter-1

