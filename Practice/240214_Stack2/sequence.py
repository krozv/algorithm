# 순열
def f(i, k):
    if i==k:
        print(*P)
    else:
        for j in range(i, k):    # P[i] 자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]    # P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]    # P[i] <-> P[j] 교환 전으로 원상복구

N = 3
P = [1, 2, 3]
f(0, N)