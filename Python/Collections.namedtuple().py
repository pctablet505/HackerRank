from collections import namedtuple

n = int(input())
avg = 0
Student = namedtuple('Student', input().split())
for _ in range(n):
    temp = Student._make(input().split())
    avg += int(temp.MARKS)
print(avg / n)
