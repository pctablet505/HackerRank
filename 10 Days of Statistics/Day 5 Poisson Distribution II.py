la,lb=map(float,(input().split()))
ECa=160+40*la*(la+1)
ECb=128+40*lb*(lb+1)
print(round(ECa,3),round(ECb,3),sep='\n')
