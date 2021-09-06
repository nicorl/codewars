s = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"

import statistics

def stat(strg):
    # https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python
    s = strg.split(", ")
    sgs = []
    for tiempo in s:
        t = tiempo.split("|")
        sgs.append(int(t[0])*3600 + int(t[1])*60 + int(t[2]))
    rngsgs = max(sgs) - min(sgs)
    meansgs = statistics.mean(sgs)
    mediansgs = statistics.median(sgs)
    
    return rngsgs, meansgs, mediansgs

print(stat(s))