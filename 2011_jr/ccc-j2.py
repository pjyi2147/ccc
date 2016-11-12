def j2():
    h, M = int(input()), int(input())
    for t in range(1, M + 1):
        eq = -6 * (t**4)+ h * t**3 + 2 * t**2 + t
        if eq <= 0:
            print("The balloon first touches ground at hour:\n",t)
            break
        elif t == M:
            print("The balloon does not touch ground in the given time.")
            break

j2()        
    
