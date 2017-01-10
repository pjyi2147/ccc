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
        print(numlist) 
        # logic start here 
        
       


