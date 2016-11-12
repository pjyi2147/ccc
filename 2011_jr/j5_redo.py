#ccc 2011 j5 redo
def Solution():
    N = int(input())
    ways = []
    for i in range(N+1):
        ways.append(1)
        
    for i in range(1,N):
        ways[int(input())] *= (ways[i] + 1)

    print(ways[N])
    





Solution()
