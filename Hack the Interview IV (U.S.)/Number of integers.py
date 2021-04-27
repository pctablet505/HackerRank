dp = []
M = 100


def countInRangeUtil(position, count, tight, number):
    global K, M, dp
    if position == len(number):
        if count <= K:
            return 1
        return 0
    if dp[position][count][tight] != -1:
        return dp[position][count][tight]
    answer = 0
    limit = 9 if tight else number[position]
    for digit in range(limit + 1):
        currCount = count
        if digit != 0:
            currCount += 1
        currTight = tight
        if digit < number[position]:
            currTight = 1
        answer += countInRangeUtil(position + 1, currCount, currTight, number)
    dp[position][count][tight] = answer
    return dp[position][count][tight]


def countInRange(x):
    global dp, K, M
    number = []
    while x:
        number.append(x%10)
        x//=10
    number.reverse()
    dp = [[[-1, -1] for i in range(M)] for j in range(M)]
    return countInRangeUtil(0, 0, 0, number)




def fun(l, r, k):
    global K
    K = k
    c1 = countInRange(r) - countInRange(l - 1)
#   print(c1)
    K = k - 1
    c2 = countInRange(r) - countInRange(l - 1)
#    print(c2)
    return c1 - c2

l=int(input())
r=int(input())
k=int(input())
print(fun(l+1,r,k)%(10**9+7))
