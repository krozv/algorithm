# 활주로 건설
"""
6<=N<=20
경사로 조건
    높이 = 1
    2<=X<=4
지형 높이 1<=H<=6
경사로 겹치기 불가, 세우기 불가
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(N, X)
    cnt = 0
    '''
    for i in range(N):
        print(f'{i}열 탐색중')
        h1 = arr[i][0]
        d = 0
        for j in range(N):
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
                        print(i, '가능1')
                    # 경사로 설치 불가능
                    else:
                        print(i, '불가능1')
                        break
                # 높이가 낮아졌을 때
                elif h1 > arr[i][j]:
                    H = h1 - arr[i][j]
                    # 마지막 칸에서 확인
                    if j == N - 1:
                        d = 1
                        if d >= H * X:
                            print(i, '가능2')
                        # 경사로 설치 불가능
                        else:
                            print(i, '불가능2')
                            break
                    # 최고높이에서 낮아진 게 아닐 때
                    if h1 != max(arr[i]):
                        # 경사로 설치 가능
                        if d >= H * X:
                            h1 = arr[i][j]
                            d = 1
                            print(i, '가능3')
                        # 경사로 설치 불가능
                        else:
                            print(i, '불가능3')
                            break
                    # 최고높이에서 낮아질 때
                    else:
                        d = 1
                        h1 = arr[i][j]
            # 높이의 변화가 없을 경우
            else:
                d += 1
        else:
            cnt += 1
            print(i, '가능')
    '''
    H = 0
    for j in range(N):
        print(f'{j}열 탐색중')
        h1 = arr[0][j]
        d = 0
        max_h = 0
        for i in range(N):
            print(arr[i][j])
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
                        print(j, '가능1')
                    # 경사로 설치 불가능
                    else:
                        print(j, '불가능1')
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
                            print(j, '가능3')
                        # 경사로 설치 불가능
                        else:
                            print(j, '불가능3')
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
            print(d)
            if d >= H * X:
                cnt += 1
                print(j, '가능')
            # 경사로 설치 불가능
            else:
                print(j, '불가능2')
    print(cnt)

