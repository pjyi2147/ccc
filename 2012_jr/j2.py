#2012 ccc j2
def Solution():
    lst = []
    for i in range(4):
        lst.append(int(input()))
        

    if lst[0] < lst[1] and lst[1] < lst[2] and lst[2] < lst[3]:
        print("Fish Rising")

    elif lst[0] > lst[1] and lst[1] > lst[2] and lst[2] > lst[3]:
        print("Fish Diving")

    elif lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3]:
        print("Constant Depth")

    else:
        print("No fish")
                   

Solution()
