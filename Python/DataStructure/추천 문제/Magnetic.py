# Magnetic
"""
푸른색 -> N극으로
붉은색 -> S극으로
충돌하면 정지
교착상태 개수 반환
"""
import sys
sys.stdin = open('input (4).txt', 'r')
T = 1
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    test = True
    while test:
        print(arr)
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1:
                    print(i, j)
                    if i+1 > N-1:
                        # print('탈출')
                        arr[i][j] = 0
                        break
                    # 이동 가능
                    if arr[i+1][j] == 0:
                        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                    # 이동 불가능
                    else:
                        if arr[i+1][j] == 1:
                            arr[i][j] = 3
                        else:
                            arr[i][j] = 5
                # S극
                elif arr[i][j] == 2:
                    # 탈출
                    if i-1 < 0:
                        arr[i][j] = 0
                        break
                    # 이동 가능
                    if arr[i-1][j] == 0:
                        arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
                    # 이동 불가능
                    else:
                        if arr[i-1][j] == 2:
                            arr[i][j] = 4
                        else:
                            arr[i][j] = 5
        for i in range(N):
            if 1 not in arr[i] and i == N-1:
                test = False
    print(arr)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 5:
                cnt += 1
    print(cnt//2)