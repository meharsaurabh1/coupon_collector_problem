import list_maker as lm
import random

def np_dc_shop(lst, r):
    n=len(lst)
    
    #defining a list containing the 'sample space'
    ss=[]
    for i in range(n):
        for j in range(lst[i]):
            ss.append(i+1)
    
    coupons = []
    for i in range(r):
        l=[]
        coupons.append(l)

    mx=0
    turns = 0
    while mx<n:
        
        var=list(set(ss))
        if len(var)<n:
            turns = np_dc_shop(lst, r)
            break
        
        for i in range(r):
            rand = random.choice(ss)
            ss.remove(rand)
            if rand not in coupons[i]:
                coupons[i].append(rand)
        
        mx=0
        
        for i in range(len(coupons)):
            if mx < len(coupons[i]):
                mx = len(coupons[i])
        
        turns += 1
        
    return turns

def avg_turns(lst, r, itr):
    avg = 0
    for i in range(itr):
        avg += np_dc_shop(lst, r)
    return avg / itr

#l = lm.lst(20,50,150,5)
#print(int(avg_turns(l, 10000))+1)

    
import matplotlib.pyplot as plt

x=[i for i in range(21)]


for j in range(4):
    
    y=[]
    
    for i in range(len(x)):
        l = lm.lst(20,100,40*i,i)
        a = int(avg_turns(l, j*10 + 1, 500))+1
        y.append(a)
        
    plt.plot(x,y)
    
plt.savefig('npdc_shop.png')