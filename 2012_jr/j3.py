#2012 ccc j3 Icon Scaling
def Solution():
    n = int(input())
    for i in range(n):
        print('*'*n +'x'*n + '*'*n)
    for i in range(n):
        print(' '*n +'x'*n*2)
    for i in range(n):
        print('*'*n +' '*n+'*'*n)



Solution()
