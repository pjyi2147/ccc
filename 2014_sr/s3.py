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
        while len(numlist) > 0:        #this only 0
            num = numlist.pop()

            if num == 1: 
                lake.append(num) 

            
            elif len(lake) > 0:

                if num == lake[-1]:
                    lake.append(num)
                
                while len(branch) > 0:
                    if branch[-1] == lake[-1]:
                        lake.append(branch.pop())

                    elif num != lake[-1]: 
                        branch.append(num)
                    
                    else: 
                        break
               
            else: 
                branch.append(num)

        while len(branch) > 0:
            if branch[-1] == lake[-1]:
                lake.append(branch.pop())
     

        if len(branch) != 0:
            fail = True
        
       
       

        
        if not fail:
            print('Y')

        else: 
            print('N')

