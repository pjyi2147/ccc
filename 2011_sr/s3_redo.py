#ccc 2011 s3 redo
def Solution():
    file = open('s3.in','r')
    def MaxheightatX(m,x):
        power = 5**(m-1)
        location = x // power
        height = 0
        if m >= 0:
            if location == 0 or location == 4:
                height = height
            elif location == 1 or location == 3:
                height = height + power + MaxheightatX(m-1, x%power)
            elif location == 2:
                height = height + power * 2 + MaxheightatX(m-1, x%power)
        return height
            
    for i in range(int(file.readline())):
        line = list(map(int, file.readline().split()))
        m, x, y = line[0],line[1],line[2]
        print(m,x,y)
        if y < MaxheightatX(m,x):
            print('crystal')

        else:
            print('empty')

    file.close()
Solution()

        
