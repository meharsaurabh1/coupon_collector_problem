import list_maker as lm
import random

def np_dc_cus(lst, r):
    n=len(lst)
    
    #defining a list containing the 'sample space'
    ss=[]
    for i in range(n):
        for j in range(lst[i]):
            ss.append(i+1)
    
    coup = []
    turns = 0
    while len(coup) != n:
        
        var=list(set(ss))
        if len(var)<n:
            turns = np_dc_cus(lst, r)
            break
        
        rand = random.choice(ss)
        ss.remove(rand)
        
        turns += 1
        if rand not in coup:
            coup.append(rand)
        
        # for other people
        for i in range(r-1):
            a = random.choice(ss)
            ss.remove(a)
            
    return turns

def avg_turns(lst, r, itr):
    avg = 0
    for i in range(itr):
        avg += np_dc_cus(lst, r)
    return avg / itr

#l = lm.lst(20,50,150,5)
#print(int(avg_turns(l, 10000))+1)


'''    
import matplotlib.pyplot as plt

x=[i for i in range(21)]


for j in range(4):
    y=[]
    for i in range(len(x)):
        l = lm.lst(20,100,30*i,i)
        a = int(avg_turns(l, j*10, 1000))+1
        y.append(a)
        
    plt.plot(x,y)

plt.savefig('npdc_cus.png')
'''


# different plots for different r
# blue 0
# orange 10
# green 20
# red 30

# for each r
    # 20 different coupons
    # 100 number of each coupon
    # remove 30 number of coupons of i types