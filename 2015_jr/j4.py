dic = {}
for i in range(int(input())):
    string = input().split()
    order = string[0]
    person = string[1]

    if order is "R":                    #received a message!
        if person in dic:               #friend is already in the dic!
            dic[person][1] = False

        else:                           #he was not in the list
            dic[person] = [0, False]    #add him in the list

        for k, v in dic.items(): 
            if not v[1]:
                v[0] += 1         
            
    elif order is "S":                  #I sent a message!
        dic[person][1] = True           #he needs to be closed! 
        
        for k, v in dic.items():
            if not v[1]:
                v[0] +=1
    
    else:
        tick = string[1]

        for k, v in dic.items():
            if not v[1]:
                v[0] = v[0] + int(tick)-1 

    print(dic)

for k, v in dic.items():
    if v[1] is False:
        print(k, -1)
    
    else:
        print(k, v[0])

