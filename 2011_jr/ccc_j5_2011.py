def j5():
    N = int(input()) # the number of person
    ways = [1,1,1,1,1,1,1] #As the maximum number of the person is 6
    for i in range(1, N):
        y = int(input())
        ways[y] *= (1+ways[i]) #deleting the number i(1) + ways to delete numbers under i(ways[i])
        
    print(ways[N]) # the answer

j5()
