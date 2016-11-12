#ccc j4
def Solution():
    mi = int(input())
    lst = []
    for i in range(int(input())):
        lst.append(int(input()))

    lst2 = []
        
    while len(lst) > 0:
        lst2.append(min(lst))
        lst.remove(min(lst))
        print(lst)
        
        if sum(lst2) > mi:
            lst2.remove(max(lst2))
            
                
        elif len(lst) == 0:
            break
        

    print(len(lst2))
    

Solution()
