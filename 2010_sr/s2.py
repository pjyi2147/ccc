def Solution():
    f = open('S2.in' ,'r')
    a = f.readline()
    lst = {}
    for i in range(int(a)):
        string = f.readline().split()
        x, y = string[0], string[1]
        lst[x:y]

    print(lst)

    
Solution()
