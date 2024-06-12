# 5248. 그룹 나누기
def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    parents = [i for i in range(N+1)]
    arr = list(map(int, input().split()))
    for i in range(M):
        l, r = arr[i*2], arr[i*2+1]
        # 대표자 확인
        l = find_set(l)
        r = find_set(r)
        if l == r:
            continue
        # 작은 수 기준으로 합칠 것
        if l < r:
            parents[r] = l
        else:
            parents[l] = r

    ans = [0] * N
    for i in range(1, N+1):
        ans[i-1] = find_set(i)
    print(f'#{t} {len(set(ans))}')