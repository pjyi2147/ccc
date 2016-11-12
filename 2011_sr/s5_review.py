#ccc 2011 s5 switch review for myself
def Solution():
    INF = 1000000

    #file input
    file = open('s5.1.in','r')
    K = int(file.readline())
    #making groups
    lights = []
    for i in range(0,K):
        lights.append(int((file.readline()))) 

    group = []
    N = 0
    group.append([0,0])

    for i in range(0,K):
        if lights[i] == 1:
            if group[N][1] == 0:
                group[N][0] = i
                group[N][1] = i
            group[N][1] += 1
        
        elif group[N][1] != 0:
            group.append([0,0])
            N += 1

    if group[N][1] == 0:
        group.pop()
        N -= 1
        
    N +=1
    #the algorithm starts!
    minimumSwitch = []
    for i in range(0,N+1):
        minimumSwitch.append(0)

    for i in range(N-1,-1,-1):
        minimumSwitch[i] = INF
        num1s = 0
        j = i
        while j < N and ((group[j][1] - group[i][0]) <= 7):
            num1s = num1s + group[j][1] - group[j][0]
            leng = max(4, group[j][1] - group[i][0])
            t = leng - num1s

            #for spans 6,7 there are some sequences that are not possible to delete all of them as a block
            if leng == 6 and lights[group[i][0] + 2] == 1 and lights[group[i][0] + 3] == 1:
                t = INF

            elif leng == 7 and lights[group[i][0] + 3] == 1:
                t = INF

            minimumSwitch[i] = min(minimumSwitch[i], t + minimumSwitch[j+1])
            j += 1
            print(i,j,minimumSwitch)

            
    print(minimumSwitch[0])


    

Solution()
