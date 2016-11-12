def j3():
    lst = [int(input()), int(input())]
    n = 0
    while True:
        if lst[n] > lst[n + 1]:
            k = lst[n] - lst[n + 1]
            lst.append(k)
            n += 1
        else:
            print(len(lst))
            break

j3()
