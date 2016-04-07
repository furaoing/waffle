# -*- coding: utf-8 -*-

from waffle import system
import pandas as pd
import re

rel_path = "corpos"
abs_path = system.create_abs_path(rel_path)
my_files = system.listdir_powered(abs_path)

my_texts = list()
for my_file in my_files:
    content = system.f_read(my_file)
    my_texts.append(content)

volume = len(my_texts)

s = pd.Series(my_texts)
s1 = s.str.findall("(是)")
s2 = s.str.findall("(人)")

s3 = s[s.str.contains("是") & s.str.contains("人")]

c1 = s1.apply(lambda x: len(x))
c2 = s2.apply(lambda x: len(x))
c3 = len(s3)

c1 = c1[c1 > 0]
c2 = c2[c2 > 0]

c1 = len(c1)
c2 = len(c2)

p1 = c1/volume*100
p2 = c2/volume*100
p3 = c3/volume*100

p12 = p3/p2 * 100
print("The percentage of 是 occurs in string is: %s" % str(p1))
print("The percentage of 是 occurs in string is: %s" % str(p2))
print("The percentage of 是 and 人 occurs in string is: %s" % str(p3))

print("The percentage of 是/人 occurs in string is: %s" % str(p12))