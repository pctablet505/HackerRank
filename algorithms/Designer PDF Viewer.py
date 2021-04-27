#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    letters = {}
    for i in range(26):
        letters[chr(ord('a') + i)] = h[i]
    w = [x for x in word]
    w.sort(key=(lambda x: letters[x]))
    return letters[w[-1]] * len(w)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
