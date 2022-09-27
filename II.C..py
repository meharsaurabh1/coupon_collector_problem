import random    
import matplotlib.pyplot as plt
import ccs_akela

def r_people_same_coupon_individual(l,r):
    n=len(l)
    
    #defining a list containing the 'sample space'
    k=[]
    for i in range(n):
        for j in range(l[i]):
            k.append(i+1)
            
    # making list for one person
    coup = []
    maal = []

    turn = 0;ind=0
    
    while(len(coup)!=n):
        rn=random.choice(k)
        k.remove(rn)
        if ind%r==0:
            turn += 1
            maal.append(rn)
            if rn not in coup:
                coup.append(rn)
        ind += 1
        
    return turn
#aa,bb=(r_people_same_coupon_individual(l_maker(20), 100))

"""a = no of iterations"""

def avg_turns(l, a, r):
    av=0
    for i in range(a):
        av = av + r_people_same_coupon_individual(l,r)
    avg = av/a
    return avg

def l_maker(n):
    l = []
    for i in range(n):
        l.append(500)
    return(l)
    

'''

x = [x + 1 for x in range(30)]

y = []
for i in range(len(x)):
    y.append(avg_turns(l_maker(i+1),(i+1)*10, 30))

y1 = []
for i in range(len(x)):
    y1.append(ccs_akela.avrg(x[i],1000))
    
plt.plot(x,y)
plt.plot(x,y1)

plt.savefig('1pnc_r_vs_akela.png')
#y3 = [ccs_akela.avrg(20,1000) for i in range(len(x))]

y4=x.copy()

y2 = []
for i in range(len(x)):
    y2.append(avg_turns(l_maker(20), 100, x[i]))
    
plt.plot(x, y4)
plt.plot(x, y)
plt.savefig('1pnc_r.png')

'''

# r(people) {constant} = 30
# coupons[1,30] vs turns

# compared above with akela

# coupons {constant} = 20
# r(people)[1,30] vs turns