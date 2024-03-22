import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 출발점의 경우 이동거리 저장하기!
    visited = [[0] * N for _ in range(N)]
    max_dis = 0
    room = N * N
    for i in range(N):
        for j in range(N):
            # 백트래킹
            # 최대 이동거리만큼 이동 못하는 경우 가지치기
            if arr[i][j] > N*N - max_dis:
                continue
            # 이동
            if not visited[i][j]:
                y, x = i, j
                dis = 1
                while not visited[y][x]:

                    visited[y][x] = 1
                    for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        ny = y + d[0]
                        nx = x + d[1]
                        # 출발 조건
                        if 0 <= ny < N and 0 <= nx < N and (arr[y][x] + 1 == arr[ny][nx]):
                            # 이미 이동한 전적이 있는 방임: 굳이 이동안하고, 최대이동거리와 방 번호 update 한 후 break
                            if visited[ny][nx]:
                                dis += visited[ny][nx]
                                break
                            # 처음 이동하는 방임: 이동
                            else:
                                y, x = ny, nx
                                dis += 1
                                break
                    else:
                        break
                visited[i][j] = dis
                # max_dis가 업데이트 된 경우, room번호 업데이트
                if max_dis < dis:
                    max_dis = dis
                    room = arr[i][j]
                # max_dis == dis인 경우: room번호 업데이트
                if max_dis == dis:
                    room = min(room, arr[i][j])

    print(f'#{t} {room} {max_dis}')