def s3():
    times = int(input())
    for i in range(times):
        #create x,y plane:
        inst = input().split()
        m = int(inst[0])
        x = int(inst[1])
        y = int(inst[2])
        plane = {}
        for p in range(0, 5 ** m):
            for q in range(0, 5 ** m):
                plane[(p,q)] = False

        
        #set the coordinates
        #bottom line
        for p in range((5**(m-1)),(4*5**(m - 1))):
            for q in range(0,(5**(m-1))):
                plane[(p,q)] = True 

        """while m > 0:
        """

        if plane[(x,y)]:
            print('crystal')

        else:
            print('empty')

s3()

            
