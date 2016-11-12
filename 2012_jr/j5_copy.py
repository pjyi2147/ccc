#ccc 2012 j5: A coin game copy

n = 0 #times that coin moved

class Node:
    def __init__(self, m, l):
        self.m = m
        self.level = l

def done(move): # finds out it is arranged as we want
    global n
    i = 0
    while i < n and move[i] == str(i+1):
        i += 1

    return i == n

#given a move, see if it is already in the tree
def inTree(t, m):
    for x in t:
        if x.m == m:
            return True

    return False

#creates a new move, given an oldmove and tow positions,
#p1 is the position to take from, p2 - add to(????)

def createNewMove(oldmove,p1,p2):
    global n
    newmove =[]
    for i in range(n):
        newmove.append(oldmove[i])

    newmove[p2] = newmove[p1][0:1] + newmove[p2]
    newmove[p1] = newmove[p1][1:]

    # don't allow the big guy to move left
    if p2 < p1 and newmove[p2][0:1] == str(n):
        return oldmove
    else:
        return newmove



def search(move):
    global n
    if done(move):
        return 0
    else:
        tree = []
        queue = 0
        tree.append(Node(move,0))
        while queue < len(tree):
            x = tree[queue]
            queue += 1
            for i in range(n):
                #move right
                if i < n - 1:
                    if len(x.m[i+1]) == 0 or x.m[i][0:1] < x.m[i+1][0:1]:
                        newmove = createNewMove(x.m, i, i+1)
                        if not inTree(tree, newmove):
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1

                elif i > 0:       
                    if len(x.m[i+1]) == 0 or x.m[i][0:1] < x.m[i+1][0:1]:
                        newmove = createNewMove(x.m, i, i+1)
                        if not inTree(tree, newmove):
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1
        
        return "IMPOSSIBLE"

n = int(input())
while n>0:
    m = input().split()
    print(search(m))
    n = int(input())
