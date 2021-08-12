def positional_args(*argv):  
    print(type(argv))
    for arg in argv:  
        print (arg) 
def kw_positional_args(**argv):  
    print(type(argv))
    for arg in argv:  
        print (argv[arg]) 
positional_args ('Hello', 'Welcome', 'to', 'GITAM')  
kw_positional_args (first="akif", last= 'Shaikh', age=40)  