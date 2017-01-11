# the Geneva confection
# basic file input
with open('s3.in', 'r') as f:
    for i in range(int(f.readline())):
        # this list is listed backwards
        numlist = []      
        k = int( f.readline())
        if k < 4:
            print('Y')
            for i in range(k):
               f.readline()
            continue 

        for i in range(k):
            numlist.append(int(f.readline())) 
        
        branch = []
        lake = []
        # logic start here 
        fail = False
        while numlist:        #this only 0
            num = numlist.pop()

            if num == 1: 
                lake.append(numlist.pop()) 

            
            elif lake:

                if num != 1 and num == lake[-1]:
                    lake.append(numlist.pop())

                elif num != 1 and num != lake[-1]: 
                    branch.append(numlist.pop())

                elif branch and branch[-1] == lake[-1]:
                    lake.append(branch.pop())

            else: 
                branch.append(num)
            
        if len(branch) != 0:
            fail = True

            
        if fail:
            print('Y')

        else: 
            print('N')

