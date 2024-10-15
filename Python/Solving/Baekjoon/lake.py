# 3197. 백조의 호수
'''
두 마리의 백조
호수: R * C
호수는 차례대로 녹고, 매일 물과 접촉한 모든 빙판은 녹음
가로나 세로로 닿아있는 경우만
며칠이 지나야 백조가 만날 수 있는가?
함수 2개 필요
1. 얼음 녹이는 함수 bfs
2. 백조 만나는지 체크하는 함수 dfs
'''
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def melting_ice():
    # .이면 물 -> 상하좌우 visited에 체크
    global water, visited_ice, arr
    q = deque(water)
    water.clear()

    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0<=ni<R and 0<=nj<C and visited_ice[ni][nj] == 0 and arr[ni][nj] == 'X':
                visited_ice[ni][nj] = 1
                arr[ni][nj] = '.'
                water.append((ni, nj))
    return

# 이 부분 최적화해야 함
def is_arrived():
    global birds, queue, visited, arr
    q = deque(queue)
    queue.clear()
    # bfs
    while q:
        si, sj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
                if arr[ni][nj] == '.':
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                if (ni, nj) == birds[1]:
                    return True
                if arr[ni][nj] == 'X':
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
    return False


R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

# 백조 위치 파악 & 물 위치 파악
birds = []
water = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '.':
            water.append((i, j))
        if arr[i][j] == 'L':
            water.append((i, j))
            birds.append((i, j))
            arr[i][j] = '.'

flag = False
day = 0

visited = [[0] * C for _ in range(R)] # 백조 탐색 용
visited_ice = [[0] * C for _ in range(R)] # 얼음 용

queue = deque()
queue.append(birds[0])  # 첫 번째 백조 위치에서 시작
visited[birds[0][0]][birds[0][1]] = 1

while not flag:
    flag = is_arrived()
    if not flag:
        melting_ice()
        day += 1
print(day)
