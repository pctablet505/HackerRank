import math
mean, std_dev=map(float,input().split())
x1=float(input())
x2,x3=map(float,input().split())
def F(x,mean,std_dev):
   return 0.5*(1+math.erf((x-mean)/(std_dev*2**0.5)))
print(F(x1,mean,std_dev))
print(F(x3,mean,std_dev)-F(x2,mean,std_dev))
