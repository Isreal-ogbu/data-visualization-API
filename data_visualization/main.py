import numpy as np
import pandas as pd

file = open('text.txt')
for letters in file:
    line = letters.strip()
    if line.startswith('From:'):
        lin = line.split()
        if lin[1][0] == 'd':
            print(lin[1])
