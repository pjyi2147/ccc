#ccc 2011 s5 switch copy of the answer from unofficial answers
#it is very fine unable to understand it at the first time!
#read over 10 times aloud then maybe.... you would understand it!



INF = 1000000 #just a very big number

#make group
K = int(input()) #how many numbers there are
lights = []  #sequence
for i in range(0,K):
    lights.append(int(input()))
group = [] 
N = 0 #number of groups
group.append([0,0])

for i in range(0,K):
    if lights[i] == 1: #if there is 1 in the sequence 
        if group[N][1] == 0:  #if it is a new group
            group[N][0] = i
            group[N][1] = i
        group[N][1] += 1
    elif group[N][1] != 0:
        N += 1                 #there is one more group
        group.append([0,0])

if group[N][1] == 0: #delete empty groups
    N = N - 1
    group.pop()

print(group) #for test

N = N + 1 #compensation for not adding 1 at the first time (as first item in list is treated 0)
minimumSwitches = []
for i in range(0,N+1):
    minimumSwitches.append(0) # add 0 as many as N+1 (because it needs a 0 value behind the first value that is calculated)



for i in range(N-1, -1, -1):
    minimumSwitches[i] = INF #to use min() function
    numOnes = 0
    j = i #it needs another variable to iterate 2 groups
    while j < N and ((group[j][1] - group[i][0]) <= 7): #adding two groups into one group, however number should not exceed 7
        numOnes = numOnes + group[j][1] - group[j][0] #numOnes = how many 1's there are in the group        
        len = max(4, group[j][1] - group[i][0])  #the length of the big chunk of the group that has to be turned off
        t = len - numOnes #number of lights that can be turned on 

        #for spans of 6 and 7 there are certain configuration that cannot be cleared as a block

        if len == 6 and lights[group[i][0] + 2] == 1 and lights[group[i][0] + 3] == 1:
            t = INF
        elif len == 7 and lights[group[i][0] + 3] == 1:
            t = INF

        minimumSwitches[i] = min(minimumSwitches[i], t + minimumSwitches[j+1])   #1st one = original one & 2nd one as new calculated one


        print(i,j,minimumSwitches)
        
        j = j + 1 #to iterate 2 groups

print(minimumSwitches[0])


