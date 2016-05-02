# -*- coding: utf-8 -*-

import random
import pandas as pd

dice_score = (1, 2, 3, 4, 5, 6)

exp1 = []
exp2 = []
outcomes = []

for _ in range(10000):
    exp1.append(random.choice(dice_score))
    exp2.append(random.choice(dice_score))

for i in range(10000):
    outcomes.append(str(exp1[i])+str(exp2[i]))

series = pd.Series(outcomes)

series = set(series)
print(series)
print(len(series))
