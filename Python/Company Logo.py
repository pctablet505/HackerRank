#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, namedtuple



if __name__ == '__main__':
    s = input()
    l=Counter(sorted(s)).most_common(3)
    for x in l:
        print(*x)
