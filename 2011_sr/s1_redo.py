#ccc 2011 s1 redo
def Solution():
    file = open("s1.in", 'r')
    T = 0
    S = 0
    for i in range(int(file.readline())):
        string = file.readline().lower()
        T += string.count('t')
        S += string.count('s')
    if T > S:
        print("English")
    if T <= S:
        print("French")
        




Solution()
