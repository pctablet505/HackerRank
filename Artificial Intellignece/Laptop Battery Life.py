#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    timeCharged = float(input())
    print(min(2 * timeCharged, 8.00))
