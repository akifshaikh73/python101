import matplotlib.pyplot as plt

def linear(x):
    m = 20
    c = 50
    y=x*m +c
    return y

def quadratic(x):
    a = 12
    b = 55
    c = 54
    y=x*x*a +b*x*x +c*x + 45
    return y


counter = 0
yvalues =[]
xvalues = []
while (counter < 10):
    xvalues.append(counter)
    y=quadratic(counter)
    #y=linear(counter)
    yvalues.append(y)
    counter=counter+1

squares = [1, 4, 9, 16, 25]
fig,ax = plt.subplots()
ax.plot(xvalues,yvalues)

plt.show()
