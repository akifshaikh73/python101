counter = int(input("counter="))

while(counter > 0):
    # While block
    print("While loop")
    menuitem=input("Option (only valid integers):")
    # Check if the menuitem is a valid integer  - data validation
    if(menuitem.isdigit()):
        menuitem = int(menuitem)
        # If statements
        if(menuitem == 1) :
            ### if block
            print("Option one selected")
            print("-----")
        elif (menuitem == 2):
            # elif block
            print("Option two selected")
        elif (menuitem == 3):
            print("Option three selected")
        else:
            # default else
            print("No valid option selected")
            #counter = counter-1    
    else:
        # If the input is invalid
        print("Option should be a valid integer")    
    # While loop     
    counter = counter-1    



