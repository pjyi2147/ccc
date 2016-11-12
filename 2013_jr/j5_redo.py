#ccc 2013 j5
def Solution():
    team = int(input()) - 1
    played = int(input())
    total = [0,0,0,0]
    whoplayed = [[0,1,1,1],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
    for i in range(played):
        game = list(map(int, input().split()))
        t1,t2,s1,s2 = game[0]-1, game[1]-1, game[2], game[3]
        whoplayed[t1][t2] = 0
        whoplayed[t2][t1] = 0
        if s1 > s2:
            total[t1] += 3
        if s1 == s2:
            total[t1] += 1
            total[t2] += 1
        if s1 < s2:
            total[t2] += 3


    one = 1     #[0][1] is played?
    two = 1     #[0][2] "
    three = 1   #[0][3] "
    four = 1    #[1][2] "
    five = 1    #[1][3] "
    six = 1     #[2][3] "
    ways = 0
    newtotal = [0,0,0,0]
    pt = [0,1,3]

    u = 0
    while u < 3:
        if whoplayed[0][1] == 0:
            one = 0
            u = 3
        v = 0
        while v < 3:
            if whoplayed[0][2] == 0:
                two = 0
                v = 3
            w = 0
            while w < 3:
                if whoplayed[0][3] == 0:
                    three = 0
                    w = 3
                x = 0
                while x < 3:
                    if whoplayed[1][2] == 0:
                        four = 0
                        x = 3
                    y = 0
                    while y < 3:
                        if whoplayed[1][3] == 0:
                            five = 0
                            y = 3
                        z = 0
                        while z < 3:
                            if whoplayed[2][3] == 0:
                                six = 0
                                z = 3

                            newtotal[0] = total[0] + pt[u*one] + pt[v*two] + pt[w*three]
                            newtotal[1] = total[1] + pt[(2-u)*one] + pt[x*four] + pt[y*five]
                            newtotal[2] = total[2] + pt[(2-v)*two] + pt[(2-x)*four] + pt[z * six]
                            newtotal[3] = total[3] + pt[(2-w)*three] + pt[(2-y)*five] + pt[(2-z)*six]
                            win = True
                            for i in range(4):
                                if newtotal[team] <= newtotal[i] and team != i:
                                    win = False

                            if win:
                                ways += 1
                            
                            z += 1
                        y += 1
                    x += 1
                w += 1
            v += 1
        u += 1

    print(ways)

Solution()

    
