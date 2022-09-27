import list_maker as lm
import random

def onep_dc(lst):
    n=len(lst)
    
    #defining a list containing the 'sample space'
    ss=[]
    for i in range(n):
        for j in range(lst[i]):
            ss.append(i+1)
    
    coup = []
    turns = 0
    while len(coup) != n:
        
        r=list(set(ss))
        if len(r)<n:
            turns = onep_dc(lst)
            break
        
        rand = random.choice(ss)
        ss.remove(rand)
        
        turns += 1
        if rand not in coup:
            coup.append(rand)
    
    return turns

def avg_turns(lst, itr):
    avg = 0
    for i in range(itr):
        avg += onep_dc(lst)
    return avg / itr

#l = lm.lst(20,50,150,5)
#print(int(avg_turns(l, 10000))+1)
'''    
import matplotlib.pyplot as plt

x=[i for i in range(21)]

y=[]

mx = 0; xmax = 0
xmaxl=[]

for i in range(len(x)):
    l = lm.lst(20,50,20*i,i)
    a = int(avg_turns(l,10000))+1
    if mx <= a:
        mx = a
    y.append(a)
    
for i in range(len(x)):
    if mx==y[i]:
        xmaxl.append(i)
    
plt.plot(x,y)
plt.savefig('1pdc_.png')

print(mx, xmaxl)
'''


# 1pdc_1 = 78, [7,8,9,10,11], [70,68]
# 1pdc_2 = 79, [8], [70,68]
# 1pdc_3 = 78, [7,8,9,10], [69,68]




# 20 different coupons
# 50 number of each coupon
# remove 20 number of coupons of i types