# 미로
"""
출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성
도착할 수 있으면 1, 아니면 0
주어진 미로 밖으로 나갈 수 없음
2에서 출발해서 3에 도착
1은 벽임. 0은 통로
"""
# 백트래킹 알고리즘으로 해결해야 함 + 재귀로도 풀 수 있음~~~ 확인해보세여~~~~
# 2에서 출발 -> 2의 좌표 = starting point
# 갈 수 있는 지점을 탐색 = 다음 값이 0 인지를 확인
    # 벽이거나 범위 밖이면 되돌아와야함 -> pop
"""
1. 출발점 탐색
2. 다음 경로 탐색
    탐색을 어떤 방향으로 할 것인가? 
    상하좌우 중 내가 지나온 길을 제외한 3방향 중 탐색해야함
    * 탐색한 칸은 searched_point에 집어넣음
    * searched_point에 없는 경우, 이동 가능!
    2-1. 탐색한 칸이 3인가? -> 도착 지점. 종료
    2-2. 탐색한 칸이 0인가? -> 이동. 해당 좌표 push
    2-3. 탐색한 칸이 1 또는 미로 밖인가? -> 후퇴. 해당 좌표 pop
"""
import sys
sys.stdin = open('input1.txt', 'r')


# 갈 수 있는 경로 탐색하는 함수
def search(coordi: [int], maze:[[int]]):
    """
    param loction: 탐색하는 위치. 현재 위치
    param maze: 미로 행렬
    """
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for k in range(4):
        ni = coordi[0] + di[k]
        nj = coordi[1] + dj[k]
        # 탐색한 칸이 0 또는 3인가? -> 이동
        if 0 <= ni < N and 0 <= nj < N:
            if maze[ni][nj] == 0 or maze[ni][nj] == 3:
                path = [ni, nj]
                maze[ni][nj] = 1
                return path


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    starting_point = []
    destination = []
    # 출발점, 도착점 탐색
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                starting_point = [i, j]
            if arr[i][j] == 3:
                destination = [i, j]

    stack = []
    stack += [starting_point]   # 지나간 경로 stack에 저장
    top = 0
    searched_point = []     # 이미 탐색한 칸은 searched_point로 체크

    while stack[top] != destination:
        possible = [search(stack[top], arr)]      # 이동 가능성 확인
        # 이동 가능하면 이동한다.
        if possible[0]:
            stack += possible
            searched_point += possible
            top += 1
        # 이동 불가하면 후진한다.
        else:
            stack.pop()
            top -= 1
        # 이동할 수 있는 좌표가 없을 경우 종료한다.
        if top == -1:
            print(f'#{t} 0')
            break
        # 목적지에 도달할 경우 종료한다.
        if destination == stack[top]:
            print(f'#{t} 1')
            break