from collections import OrderedDict
dictionary=OrderedDict()
for _ in range(int(input())):
    inp=input()
    dictionary[inp]=dictionary.get(inp,0)+1
print(len(dictionary))
for items in dictionary:
    print(dictionary.get(items),end=' ')
