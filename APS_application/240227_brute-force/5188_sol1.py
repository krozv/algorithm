# 최소합
def f(i, j, ss):
    global min_ss
    if min_ss < ss:
        return
    if i == n or j == n:
        return
    ss += arr[i][j]
    if i == n - 1 and j == n - 1:
        if min_ss > ss:
            min_ss = ss
        return
    f(i, j + 1, ss)
    f(i + 1, j, ss)


T = int(input())
for case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    min_ss = 10 * 2 * n
    f(0, 0, 0)

    print(f'#{case}', min_ss)