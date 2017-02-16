import sys
import os
def Solution():
    f = open(os.path.join(sys.path[0], 's2.in'),'r')
    a = f.readline()
    lst = {}
    for i in range(int(a)):
        string = f.readline().split()
        x, y = string[0], string[1]
        lst[x] = y

    answer = ''
    binary = f.readline()
    while len(binary) > 0:
        for k, v in lst.items():
            if binary.startswith(v):
                answer += k
                binary = binary[len(v):]
                break
                
    print(answer)

Solution()
