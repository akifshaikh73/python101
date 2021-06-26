# Linear

def linear(x,m=10,c=5):
    m=10
    c=5
    x = int(x)
    y = m*x + c
    return y



#x = input("x=")
#y = linear(x)
#print(y)

for x in range(10):
    y=linear(x)
    #draw(x,y)
    print(f'x,y=',x,y)
