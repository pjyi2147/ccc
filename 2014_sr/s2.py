#assigning partners
with open('s2.in', 'r') as f:
    s = int(f.readline())
    firstlist = f.readline().split()
    secondlist = f.readline().split()
    dic = {}
    for i in range(s):
        dic[firstlist[i]] = i
    
    print(dic)
    correct = True
    for i in range(i):
        item = secondlist[i]
        key = dic[item]
        if firstlist[i] != secondlist[key]:
            correct = False

    if correct:
        print('good')

    else:
        print('bad')
        


