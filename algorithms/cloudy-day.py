#!/bin/python3

import bisect
from collections import defaultdict
def maximumPeople(p, x, y, r):
    
    pi = defaultdict(int)
    clouds = set()
    for i in range(len(x)):
        pi[x[i]] += p[i]
    for i in range(len(y)):
        clouds.add(range(y[i] - r[i], y[i] + r[i] + 1))
    clouds = list(clouds)
    cities = sorted(list(pi))
    
    
    
    n=len(cities)
    
    cities_clouds=[0 for i in range(n+1)]
    
    for y in clouds:
        i = bisect.bisect_left(cities, y.start)
        j = bisect.bisect_left(cities, y.stop)
        
        if i >= j:
            continue
        if (j == len(cities) - 1 and cities[j] >= y.stop):
            j -= 1
        if cities[i] < y.start:
            i += 1
        j-=1
        
        
        cities_clouds[i]+=1
        cities_clouds[j+1]-=1
    temp=[0 for i in range(n)]
    for i in range(n):
        if i==0:
            temp[i]=cities_clouds[i]
        else:
            temp[i]=temp[i-1]+cities_clouds[i]        
    cities_clouds=temp
    
    
    single_clouded=[]
    for i in range(n):
        if cities_clouds[i]==1:
            single_clouded.append(cities[i])
    
    single_clouded.sort()
    if single_clouded:
        sum_single_clouded = [pi[single_clouded[0]]]
        for i in range(1, len(single_clouded)):
            sum_single_clouded.append(sum_single_clouded[-1] + pi[single_clouded[i]])
    
    def getSum_(i, j):
        if i == 0:
            return sum_single_clouded[j]
        return sum_single_clouded[j] - sum_single_clouded[i - 1]

    M = 0
    for y in clouds:
        m = 0
        

        i = bisect.bisect_left(single_clouded, y.start)
        j = bisect.bisect_left(single_clouded, y.stop)
        if i >= j:
            continue

        if j == len(single_clouded):
            j -= 1
        elif single_clouded[j] >= y.stop:
            j -= 1
        
        m += getSum_(i, j)
        '''
        for z in single_clouded[i:j]:
            #if z in y:
                m+=pi[z]
                '''
        M = max(m, M)
    
    for i in range(n):
        if cities_clouds[i]==0:
            M += pi[cities[i]]
            pass
    return M


