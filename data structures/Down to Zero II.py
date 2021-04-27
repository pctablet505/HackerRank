N = int(input())
Q = []
for _ in range(N):
    Q.append(int(input()))

M = max(Q) + 1
nums = [-1] * M
nums[0] = 0
nums[1] = 1
nums[2] = 2
nums[3] = 3
for i in range(M):
    if nums[i] == -1 or nums[i] > (nums[i - 1] + 1):
        nums[i] = nums[i - 1] + 1
    for j in range(1, i + 1):
        if j * i >= M:
            break
        if nums[j * i] == -1 or (nums[i] + 1) < nums[j * i]:
            nums[j * i] = nums[i] + 1
for x in Q:
    print(nums[x])
