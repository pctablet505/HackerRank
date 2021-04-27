marksheet = []
for _ in range(0, int(input())):
    name = input()
    score = float(input())
    marksheet.append([name, score])

second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([name for name, marks in sorted(marksheet) if marks == second_lowest]))
