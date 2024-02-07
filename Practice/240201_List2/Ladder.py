# ladder
'''
어느 사다리는 고르면 X 표시에 도착?
2에 도착하려면 어떤 출발점에서 시작해야할까?
'''
import sys
sys.stdin = open('input_ladder.txt', 'r')
T = 10
for t in range(1, T+1):
    N = int(input())
    ladder = [0]*100
    # 사다리에 숫자 집어넣었음
    for i in range(100):
        # print(i)
        ladder[i] = list(map(int, input().split()))
    # 2의 위치를 찾을 것
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                break
    # 출발점 = 2의 위치
    coord = [i, j]
    # di, dj 행렬 형성
    di = [0, 0, -1]
    dj = [1, -1, 0]
    # 왼쪽, 오른쪽이 1일 경우 해당 방향으로 움직임
    s = 2
    while coord[0] != 0:
        # 왼쪽이 1이면 계속 왼쪽, 그러다가 0만나면 방향 전환
        coord[0] = coord[0]+di[s]
        coord[1] = coord[1]+dj[s]
        # 범위 벗어나지 않았는 지 확인
        if (0 > coord[0] or 100 <= coord[1]) and (0 > coord[0] or 100 <= coord[1]):
            # print(coord)
            coord[0] -= di[s]
            coord[1] -= dj[s]
            s = (s + 1) % 3
            continue
        # 막혔어!
        if ladder[coord[0]][coord[1]] != 1:
            coord[0] -= di[s]
            coord[1] -= dj[s]
            s = (s + 1) % 3

        else:
            ladder[coord[0]][coord[1]] = 0
            if s == 2:
                s = (s + 1) % 3
    print(f'#{N} {coord[1]}')
        # if s == 2:
        #     # 좌우탐색 해야 함
        #     if ladder[coord[0]+di[0]][coord[1]+dj[0]] == 1:
        #         s = 0
        #         coord[0] += di[s]
        #         coord[1] += dj[s]
        #
        #     elif ladder[coord[0]+di[1]][coord[1]+dj[1]] == 1:
        #         s = 1
        #         coord[0] += di[s]
        #         coord[1] += dj[s]
        # elif s != 2:
        #     s = 2
        #     coord[0] += di[s]
        #     coord[1] += dj[s]
        #     s = (s + 1) % 3

        # 범위 맞고, 값이 1이야!
        # 오른쪽부터
        # if (0<=coord[0]+di[0]<100 and 0<=coord[1]+dj[0]<100) and ladder[coord[0]+di[0]][coord[1]+dj[0]] == 1:
        #     s = 0
        #     coord[0] = coord[0]+di[s]
        #     coord[1] = coord[1]+dj[s]
        # elif
        # if (0<=coord[0]+di[1]<100 and 0<=coord[1]+dj[1]<100) and ladder[coord[0]+di[1]][coord[1]+dj[1]] == 1:
        #     s = 1
        #     coord[0] = coord[0] + di[s]
        #     coord[1] = coord[1] + dj[s]
        #
        # else:
        #     s = 2
        #     coord[0] = coord[0] + di[s]
        #     coord[1] = coord[1] + dj[s]
        # else:
        #     s = 2
        #     coord[0] = coord[0] + di[s]
        #     coord[1] = coord[1] + dj[s]




        # 오른쪽이 1이면 계속 오른쪽, 그러다가 0만나면 방향 전환
        # 왼쪽과 오른쪽이 둘 다 1이 아닐 경우 위로
        # if ladder[coord[0]+di[0]][coord[1]+dj[0]] == 1:
        #     coord[0] += di[0]
        #     coord[1] += dj[0]
        # elif ladder[coord[0]+di[1]][coord[1]+dj[1]] == 1:
        #     coord[0] += di[1]
        #     coord[1] += dj[1]
        # else:
        #     coord[0] += di[2]
        #     coord[1] += dj[2]
        # print(coord)
    # 아니면 무조건 위로 직진
    # 도착한 곳의 위치 출력
    # print(coord)