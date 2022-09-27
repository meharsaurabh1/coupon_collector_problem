import random
from matplotlib import pyplot as plt

def simulate(n):
    l=[];count=0
    while(len(l)<n):
        count=count+1
        k=random.randint(1,n)
        if k not in l:
            l.append(k)
    return count

def avrg(n,a):
    av=0
    for i in range(a):
        av=av+simulate(n)
    avg=av/a
    return avg
'''

x = [x + 1 for x in range(1,100)]
y = []
for i in range(len(x)):
    y.append(avrg(x[i],1000))
y1=x.copy()
    
    
plt.plot(x,y)
plt.plot(x,y1)
plt.show()
'''
'''
turns = constant * (n log(n))

constant = 1.1851666114768928
'''



# varied n for (1,100)
# iterations = 1000