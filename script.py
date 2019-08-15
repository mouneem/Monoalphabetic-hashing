#-*- coding: utf-8 -*-
import random

import csv
w_dict = []
with open('dict.csv', "rt") as f:
    reader = csv.reader(f)
    w_dict = list(reader)
alpha = list("abcdefghijklmnopqrstuvwxyz")


t = "dk. afr dkl. rwklstb, gy fwdztk ygwk, hkoxtm rkoxt, ctkt hkgwr mg lab miam mitb ctkt htkytemsb fgkdas, miafq bgw xtkb dwei. mitb ctkt mit salm htghst bgw’r tvhtem mg zt ofxgsxtr of afbmiofu lmkafut gk dblmtkogwl, zteawlt mitb pwlm rorf’m igsr comi lwei fgfltflt."

#t = "dk. afr dkl. rwklstb, gy fwdztk ygwk, hkoxtm rkoxt, ctkt hkgwr mg lab miam mitb ctkt htkytemsb fgkdas"
#list of alphabet with known keys
to_ignore = "dka\'"
#the knowm keys
map_of_ignored = "m\'"

solutions = []
keys = []
scores = []
alpha = list("abcdefghijklmnopqrstuvwxyz")
for j in range(1000):
    alpha2 = random.sample(alpha,26)
    keys.append(alpha2)
    new_string = ""
    for c in t:
        if not c in to_ignore and c in alpha2:
            index = alpha2.index(c)
            new_c = alpha[index]
            new_string += new_c
        #char to ignore (alredy known key)
        elif c in to_ignore:
            index = to_ignore.index(c)
            new_c = map_of_ignored[index]
            new_string += new_c
        #keep the same
        else:
            new_string += c
    solutions.append(new_string)
    wds = new_string.split()
    count = 0
    for w in wds:
        if [w] in w_dict:
            count+=1
    scores.append(count)

for s in range(len(scores)):
    #the random encoding with at least N english word
    if scores[s] > 29:
        print(scores[s],solutions[s])
