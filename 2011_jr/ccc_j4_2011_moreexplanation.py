def j4():
    #create the array
    wellPlan = {}
    for col in range(-200, 201):
        for row in range(-1, -201, -1):
            wellPlan[(row,col)] = False

    #enter the spots
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

    #setting the start point
    ok = True #is it safe? 
    row = -1
    col = -5

    #do the drilling
    while ok and direction != 'q':
        vert = 0
        para = 0
        if direction == 'd': vert -= 1 #downwards
            
        elif direction == 'u': vert += 1 #upwards
            
        elif direction == 'l': para -= 1 #left
            
        elif direction == 'r': para += 1 #right
            

        while direction > 0:
            row += vert
            col += para
            if wellPlan[(row,col)]:
                ok = False
            else:
                wellPlan[(row,col)] = True
            distance -= 1

        if ok:
            print(col,row, "safe")
        else:
            print(col,row, "DANGER")

        #reset the instruction
        inst = input().split()
        direction = inst[0]
        distance = inst[1]

j4()

        
                    
            





    
    
