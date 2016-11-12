#ccc 2011 j2 redo
def Solution():
    h = int(input())
    t = int(input())
    
    for i in range(1,t+1):
        A = (-6*i**4)+(h*i**3)+2*i**2+i
        if A <= 0:
            print("The balloon first touches ground at hour\n%d" % i)
            break
        elif i == t:
            print("The balloon does not touch ground in the given time")

Solution() 
