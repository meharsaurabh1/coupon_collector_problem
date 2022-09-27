#from coupon_collector_simulation import avg_sim

#defining a function to easily make a list to input in next function

#....n is the number of different coupons
#....max_c is the initial number of coupons of each type
#....t_err is the total error in number of coupons
#....t is the number of type of coupons to be affected

def lst(n,max_c,t_err,t):

    l=[int(max_c) for x in range(n)]

    if t>0:    
        err=t_err/t
        
        #t=x denotse k/x less coupons of x type
        for i in range(t):
            l[-1-i]-=int(err)

    return l

#coupon_collector_simulation.avg_sim([10,10,10],10)