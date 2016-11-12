#ccc 2011 j3 redo
def Solution():
    lst = []
    for i in range(2):
        lst.append(int(input()))

    n = 0
    while lst[n+1] < lst[n]:
        lst.append(lst[n] - lst[n+1])
        n += 1

    print(len(lst))

    
Solution()
