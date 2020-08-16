no_of_test_cases=int(input())
for _ in range(no_of_test_cases):
    n1=int(input())
    A=set(map(int,input().split()))
    n2=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))
    
