#Senier s2 question of 2011 written in python
def Solution():
    N = int(input())
    ans, s_ans = [], []
    ans_cor = 0
    for i in range(N):
        ans.append(input())

    for r in range(N):
        s_ans.append(input())

    for i in range(N):
        if ans[i] == s_ans[i]:
            ans_cor += 1

    print(ans_cor)

Solution()
