#ccc 2013 j5: Chance of winning
def Solution():
    fav = int(input()) - 1 #favorate team
    played = int(input()) #how many games?
    total = [0,0,0,0] #sum of numbers 
    #an 2D array that shows which games are played or not 
    whoplayed = [[0,1,1,1], [0,0,1,1],[0,0,0,1],[0,0,0,0]]
    #data input
    for i in range(played):
        game = list(map(int, input().split()))
        t1, t2, s1, s2 = game[0], game[1], game[2], game[3]
        whoplayed[t1-1][t2-1] = 0
        whoplayed[t2-1][t1-1] = 0
        if s1 > s2:
            total[(t1-1)] += 3
        elif s1 == s2:
            total[(t1-1)] += 1
            total[(t2-1)] += 1
        elif s1 < s2:
            total[(t2-1)] += 3

    #these numbers determine the numbers the game has played or not
    one = 1 #[0][1]
    two = 1 #[0][2]
    three = 1 # etc....
    four = 1
    five = 1
    six = 1
    final = 0 # the answer we are searching for 
    pt = [0,1,3]
    newtotal = [0,0,0,0]
    print(whoplayed)

    l = 0
    while l < 3:
        if whoplayed[0][1] == 0:
            one = 0 #as game one is already played
            l = 2 #to break the loop (why is it 2? the loop has to go 2 rounds at least)
        m = 0
        while m < 3:
            if whoplayed[0][2] == 0:
                two = 0 #etc
                m = 2 #break the loop
            p = 0
            while p < 0:
                if whoplayed[0][3] == 0:
                    three = 0
                    p = 2  #etc 

                q = 0 
                while q < 3:
                    if whoplayed[1][2] == 0:
                        four = 0
                        q = 2
                    r = 0
                    while r < 3:
                        if whoplayed[1][3] == 0:
                            five = 0
                            r = 2
                        s = 0
                        while s < 3:
                            if whoplayed[2][3] == 0:
                                six = 0
                                s = 2

                            print(l,m,p,q,r,s)
                            newtotal[0] = total[0] + pt[l*one] +pt[m*two] +pt[p*three]
                            newtotal[1] = total[1] + pt[(2-l)*one] + pt[q*four] + pt[r*five]
                            newtotal[2] = total[2] + pt[(2-m)*two] + pt[(2-q)*four] + pt[s*six]
                            newtotal[3] = total[3] + pt[(2-p)*three] + pt[(2-r)*five] + pt[(2-s)*six]
                            win = True
                            for i in range(4):
                                if newsum[fav] <= newsum[i] and fav != i:
                                    win = False

                            if win:
                                final += 1

                            s += 1
                        r += 1
                    q += 1
                p += 1
            m += 1
        l += 1

    print(final) 
                            
                            

                        
                        
    
    
        
    

Solution()
