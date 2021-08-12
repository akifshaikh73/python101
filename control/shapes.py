'''
def line():
    print("---------------------------")
'''

'''
def line(size):
    c = '-'
    line = c*size
    print(line)
'''

def line(size,c='-'):
    line = c*size
    print(line)


def rectangle(width,height,c='-'):
    line=c*width # generated -------
    h=0
    while (h <= height):
        print(line)
        h=h+1

line(10)
line(100,'o')
line(100,'*')
rectangle(40,10,'*')

'''
print()
rectangle(40,20)
rectangle(100,25)
'''
