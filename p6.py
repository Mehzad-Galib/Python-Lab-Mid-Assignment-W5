def dp(l1, l2):
    def p(ll1, ll2, n):
        return ll1[n] * ll2[n]  # 1*4 2*5 3*6
    r = 0  # 0 + 4 + 10 + 18
    for i in range(len(l1)):  # 0 to 3, so 3 times
        r += p(l1, l2, i)
    return r


print(dp([1, 2, 3], [4, 5, 6]))
