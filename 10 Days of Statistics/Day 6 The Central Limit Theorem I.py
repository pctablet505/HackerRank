import math
wt_max=int(input())
no_box=int(input())
mean=int(input())
std_dev=int(input())
u_=mean*no_box
s_=std_dev*no_box**0.5
def F(x,mean,std_dev):
   return 0.5*(1+math.erf((x-mean)/(std_dev*2**0.5)))
print(round(F(wt_max,u_,s_),4))
