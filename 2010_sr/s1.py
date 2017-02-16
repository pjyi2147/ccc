#problem s1: computer purchase
import os
import sys
with open(os.path.join(sys.path[0], 's1.in'), 'r') as f:    
    dic = {}
    n = f.readline()
    for i in range(int(n)):
        lst = f.readline().split()
        name, r, s, d = lst[0], int(lst[1]), int(lst[2]), int(lst[3])
        value = 2*r + 3*s + d
        dic[name] = value

    if len(dic) == 1:
        print(max(dic, key=dic.get))

    else:
        big = max(dic, key=dic.get)
        print(big)
        dic.pop(big)
        print(max(dic, key=dic.get))
