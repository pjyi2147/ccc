#ccc 2011 j4 redo
def Solution():
    #make the dictionary
    array = {}
    for x in range(-200,201):
        for y in range(-1,-201,-1):
            array[(x,y)] = False

    array[(0,-1)] = True
    array[(0,-2)] = True
    array[(0,-3)] = True
    array[(1,-3)] = True
    array[(2,-3)] = True
    array[(3,-3)] = True
    array[(3,-4)] = True
    array[(3,-5)] = True
    array[(4,-5)] = True
    array[(5,-5)] = True
    array[(5,-4)] = True
    array[(5,-3)] = True
    array[(6,-3)] = True
    array[(7,-3)] = True
    array[(7,-4)] = True
    array[(7,-5)] = True
    array[(7,-6)] = True
    array[(7,-7)] = True
    array[(6,-7)] = True
    array[(5,-7)] = True
    array[(4,-7)] = True
    array[(3,-7)] = True
    array[(2,-7)] = True
    array[(1,-7)] = True
    array[(0,-7)] = True
    array[(-1,-7)] = True
    array[(-1,-6)] = True
    array[(-1,-5)] = True

    

    kk = input().split()
    dire = kk[0]
    depth = int(kk[1])
    x = -1
    y = -5
    danger = False
    while dire != 'q' and depth > 0 and danger == False:    
        for i in range(depth):
            if dire == 'l':
                x -= 1
                if array[(x,y)] == True:
                    danger = True
                    
            if dire == 'r':
                x += 1
                if array[(x,y)]:
                    danger = True

            if dire == 'u':
                y += 1
                if array[(x,y)]:
                    danger = True

            if dire == 'd':
                y -= 1
                if array[(x,y)]:
                    danger = True

        if danger:
            print(x,y,'DANGER')
        else:
            print(x,y, 'safe')

        kk = input().split()
        dire = kk[0]
        depth = int(kk[1])

    
Solution()
