def j4():
    # creating original well plan
    wellPlan = {}
    for row in range(-1,-201,-1):
        for col in range(-200,201):
            wellPlan[(row,col)] = False

    wellPlan[(-1,0)] = True
    wellPlan[(-2,0)] = True
    wellPlan[(-3,0)] = True
    wellPlan[(-3,1)] = True
    wellPlan[(-3,2)] = True
    wellPlan[(-3,3)] = True
    wellPlan[(-4,3)] = True
    wellPlan[(-5,3)] = True
    wellPlan[(-5,4)] = True
    wellPlan[(-5,5)] = True
    wellPlan[(-4,5)] = True
    wellPlan[(-3,5)] = True
    wellPlan[(-3,6)] = True
    wellPlan[(-3,7)] = True
    wellPlan[(-4,7)] = True
    wellPlan[(-5,7)] = True
    wellPlan[(-6,7)] = True
    wellPlan[(-7,7)] = True
    wellPlan[(-7,6)] = True
    wellPlan[(-7,5)] = True
    wellPlan[(-7,4)] = True
    wellPlan[(-7,3)] = True
    wellPlan[(-7,2)] = True
    wellPlan[(-7,1)] = True
    wellPlan[(-7,0)] = True
    wellPlan[(-7,-1)] = True
    wellPlan[(-6,-1)] = True
    wellPlan[(-5,-1)] = True
    
    #read instruction
    inst = input().split()
    direction = inst[0]
    distance = int(inst[1])
    ok = True
    row = -5 
    col = -1

    #do the drilling
    while ok and direction != 'q':
        dr = 0 # moving upside & downside
        dc = 0 # moving sideways
        if direction == "l":
            dc = -1
        elif direction == "r":
            dc = 1
        elif direction == "u":
            dr = 1
        elif direction == "d":
            dr = -1

        while distance > 0:
            row += dr
            col += dc
            if wellPlan[(row, col)]:
                ok = False
            else:
                wellPlan[(row, col)] = True
            distance -= 1

        if ok:
            print(col,row, "safe")
            
        else:
            print(col,row, "DANGER")
            break
        
        inst=input().split() # getting the new line
        direction = inst[0]
        distance = int(inst[1])

j4()




                
