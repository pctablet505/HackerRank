import math
mean, std_dev=map(float,input().split())
x1=float(input())
x2=float(input())
def F(x,mean,std_dev):
   return 0.5*(1+math.erf((x-mean)/(std_dev*2**0.5)))
print(round(100*(1-F(x1,mean,std_dev)),2))
print(round(100*(1-F(x2,mean,std_dev)),2))
print(round(100*F(x2,mean,std_dev),2))

'''    15.87

    84.13

    15.87'''
