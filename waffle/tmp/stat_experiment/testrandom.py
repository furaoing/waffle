# -*- coding: utf-8 -*-


import random
import pandas as pd

my_list = []

for _ in range(100000):
    my_list.append(random.random())

rans = pd.Series(my_list)

rans.plot()
