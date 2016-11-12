#ccc 2011 s2 redo
def Solution():
    file = open("s2.in", 'r')
    answer = []
    score = 0
    n = int(file.readline())
    for i in range(n*2):
        answer.append(str(file.readline()))

    print(answer)

    for i in range(n):
        if answer[i] == answer[i+3]:
            score += 1

    print(score)
    file.close()


Solution()
