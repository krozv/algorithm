# 활주로 건설

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    H = 0

    for i in range(N):
        h1 = arr[i][0]
        d = 0
        max_h = 0
        for j in range(N):
            if max_h < arr[i][j]:
                max_h = arr[i][j]
            # 높이의 변화가 있을 경우
            if h1 != arr[i][j]:
                # 경사로 설치 가능 여부 판단
                # 높이가 높아졌을 때
                if h1 < arr[i][j]:
                    H = arr[i][j] - h1
                    # 경사로 설치 가능
                    if d >= H * X:
                        d = 1
                        h1 = arr[i][j]
                    # 경사로 설치 불가능
                    else:
                        break
                # 높이가 낮아졌을 때
                elif h1 > arr[i][j]:
                    H = h1 - arr[i][j]
                    # 최고높이에서 낮아진 게 아닐 때
                    if h1 != max_h:
                        # 경사로 설치 가능
                        if d >= H * X:
                            h1 = arr[i][j]
                            d = 1
                        # 경사로 설치 불가능
                        else:
                            break
                    # 최고높이에서 낮아질 때
                    else:
                        d = 1
                        h1 = arr[i][j]
            # 높이의 변화가 없을 경우
            else:
                d += 1
        else:
            # 마지막 칸에서 확인
            if d >= H * X:
                cnt += 1
    # print(cnt)

    for j in range(N):
        h1 = arr[0][j]
        d = 0
        max_h = 0
        print(f'{j}열 확인중')
        for i in range(N):
            if max_h < arr[i][j]:
                max_h = arr[i][j]
            # 높이의 변화가 있을 경우
            if h1 != arr[i][j]:
                # 경사로 설치 가능 여부 판단
                # 높이가 높아졌을 때
                if h1 < arr[i][j]:
                    H = arr[i][j] - h1
                    # 경사로 설치 가능
                    if d >= H * X:
                        d = 1
                        h1 = arr[i][j]
                    # 경사로 설치 불가능
                    else:
                        break
                # 높이가 낮아졌을 때
                elif h1 > arr[i][j]:
                    H = h1 - arr[i][j]
                    # 마지막 칸에서 확인
                    if i == N-1:
                        d = 1
                        if d >= H * X:
                            pass
                        else:
                            break
                    else:
                        # 최고높이에서 낮아진 게 아닐 때
                        if h1 != max_h:
                            # 경사로 설치 가능
                            if d >= H * X:
                                h1 = arr[i][j]
                                d = 1
                            # 경사로 설치 불가능
                            else:
                                break
                        # 최고높이에서 낮아질 때
                        else:
                            d = 1
                            h1 = arr[i][j]
            # 높이의 변화가 없을 경우
            else:
                d += 1
        else:
            print(f'{j} 가능')
            cnt += 1
    print(f'#{t} {cnt}')

