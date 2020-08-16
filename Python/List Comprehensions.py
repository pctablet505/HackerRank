if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

def function(x,y,z,n):
    results=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k)!=n:
                    result=results.append([i,j,k])
                
    print(results)
function(x,y,z,n)


