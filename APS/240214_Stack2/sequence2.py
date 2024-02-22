# 순열 - 가지치기 有
def f(i, k, s):
    """
    i: 부분집합의 원소 개수
    k: 총 원소의 개수
    s: 구하고자 하는 합
    """
    global cnt      # 얼마나 함수가 호출되었는 지 알기 위한 변수
    global min_v    # 합의 최솟값
    cnt += 1
    if i==k:        # 부분집합의 개수 i가 k와 같아질 때 = 즉, 모든 요소를 가지고 있는 집합을 호출할 때 까지
        if min_v > s:   # 합이 최솟값인지 아닌지~~
            min_v = s
    elif s >= min_v:    # 합이 최솟값을 진작 넘으면 더 계산하지 않고, 그냥 return
        return
    else:
        for j in range(i, k):    # P[i] 자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]    # P[i] <-> P[j]
            f(i+1, k, s)               # i 개수를 증가(원소가 1개 더 많은) 함수
            P[i], P[j] = P[j], P[i]    # P[i] <-> P[j] 교환 전으로 원상복구


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]   # [0, 1, ..., N-1]
min_v = 100
cnt = 0
f(0, N, 15)
print(min_v, cnt)