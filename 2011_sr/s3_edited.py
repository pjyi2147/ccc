#python answer for ccc_s3_2011
def Solution():

    def MaxheightatX(m, x):
        power = 5 ** (m - 1)
        location = x // power
        blocks = 0
        if m >= 1:
            if location == 0 or location == 4:
                blocks = blocks
            elif location == 1 or location == 3:
                blocks = blocks + power + MaxheightatX(m-1, x % power)
            elif location == 2:
                blocks = blocks + 2 * power + MaxheightatX(m-1, x % power)
                
        return blocks

    lst= list(map(int, input().split()))
    times = lst[0]
    for i in range(times):
        #create x,y plane:
        m = int(lst[1 + 3*i])
        x = int(lst[2 + 3*i])
        y = int(lst[3 + 3*i])
        if y < MaxheightatX(m,x):
            print('crystal')
        else:
            print('empty')



Solution()
