# 혁진이의 프로그램 검증
"""
6>--v.
.^--_@
"""
def preproceesing(i, j):
    # 범위 밖일 경우 전처리
    if i == -1:
        i = R - 1
    elif i == R:
        i = 0
    elif j == -1:
        j = C - 1
    elif j == C:
        j = 0
    return i, j


def test(i, j, m, d, c):
    if c:
        return True
    delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    if 0 > i or i >= R or 0 > j or j >= C:
        i, j =preproceesing(i, j)

    key = f'{i}{j}{m}{d}'
    if key in visited:
        return False
    else:
        visited.append(key)

    # 범위 내일 경우
    if arr[i][j] == '<':
        d = 0
        c = test(i+delta[d][0], j+delta[d][1], m, d, c)
    elif arr[i][j] == '>':
        # print('right')
        d = 1
        # print(i + delta[d][0], j + delta[d][1])
        c = test(i + delta[d][0], j + delta[d][1], m, d, c)
    elif arr[i][j] == '^':
        d = 2
        c = test(i + delta[d][0], j + delta[d][1], m, d, c)
    elif arr[i][j] == 'v':
        d = 3
        c = test(i + delta[d][0], j + delta[d][1], m, d, c)
    elif arr[i][j] == '_':
        # print('test')
        if m == 0:
            d = 1
        else:
            d = 0
        c = test(i + delta[d][0], j + delta[d][1], m, d, c)
    elif arr[i][j] == '|':
        if m == 0:
            d = 3
        else:
            d = 3
        c = test(i + delta[d][0], j + delta[d][1], m, d, c)
    elif arr[i][j] == '?':
        d = 0
        x = i + delta[d][0]
        y = j + delta[d][1]
        c = test(x, y, m, d, c)
        if not c:
            d = 1
            x = i + delta[d][0]
            y = j + delta[d][1]
            c = test(x, y, m, d, c)
            if not c:
                d = 2
                x = i + delta[d][0]
                y = j + delta[d][1]
                c = test(x, y, m, d, c)
                if not c:
                    d = 3
                    x = i + delta[d][0]
                    y = j + delta[d][1]
                    c = test(x, y, m, d, c)
    elif arr[i][j] == '.':
        c = test(i + delta[d][0], j + delta[d][1], m, d, c)
    elif arr[i][j] == '@':
        return True
    elif arr[i][j] == '+':
        if m == 15:
            c = test(i + delta[d][0], j + delta[d][1], 0, d, c)
        else:
            c = test(i + delta[d][0], j + delta[d][1], m+1, d, c)
    elif arr[i][j] == '-':
        # print('minus')
        if m == 0:
            c = test(i + delta[d][0], j + delta[d][1], 15, d, c)
        else:
            c = test(i + delta[d][0], j + delta[d][1], m-1, d, c)
        # return
    elif arr[i][j].isdigit():
        c = test(i + delta[d][0], j + delta[d][1], int(arr[i][j]), d, c)

    if c:
        return True
    else:
        return False




import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]
    c = True
    for r in range(R):
        if '@' in arr[r]:
            c = True
        if not c and '@' not in arr[r] and r == R-1:
            c = False
    # print(arr)
    cnt = 1
    for rx in range(R):
        for ry in range(C):
            if arr[rx][ry] == '?':
                cnt += 1
    # print(cnt, c)
    visited = []
    # print(visited)
    if c:
        k = test(0, 0, 0, 1, False)
        print(t, k)
    else:
        print(t, c)

