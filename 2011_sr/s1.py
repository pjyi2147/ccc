#Senior s1 problem written in python
def s1():
    N = int(input())
    t = 0
    s = 0
    for i in range(N):
        string = input()
        for i in string:
            if i == "t" or i == "T": t += 1
            elif i == "s" or i == "S": s += 1

    if t > s:
        print("English")
    else:
        print("French")




s1()
