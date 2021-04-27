import re

m = re.search(r'(\w(?!_))\1+', input())
print(m.group(1) if m else -1)
