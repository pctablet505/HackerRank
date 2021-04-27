from collections import Counter

number_of_shoes = int(input())
available_shoes_size = Counter(list(map(int, input().split())))
num_customers = int(input())
sale = 0

for x in range(num_customers):
    size, price = (map(int, input().split()))
    if available_shoes_size[size]:
        sale += price
        available_shoes_size[size] -= 1

print((sale))
