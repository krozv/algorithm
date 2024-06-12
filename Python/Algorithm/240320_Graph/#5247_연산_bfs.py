def f(N):
    global min_cnt
    q = deque()
    q.append(N)
    visited[N] = 1
    while q:
        num = q.popleft()
        if num == M:
            return
        if 0 < num+1 <= 1e6 and visited[num+1] == 0:
            visited[num+1] = visited[num]+1
            q.append(num+1)
        if 0 < num-1 <= 1e6 and visited[num-1] == 0:
            visited[num-1] = visited[num]+1
            q.append(num-1)
        if num < M and 0 < num*2 <= 1e6 and visited[num*2] == 0:
            visited[num*2] = visited[num]+1
            q.append(num*2)
        if 0 < num-10 <= 1e6 and visited[num-10] == 0:
            visited[num-10] = visited[num]+1
            q.append(num-10)
    return -1


from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    min_cnt = 1000000
    f(N)
    print(f'#{t} {visited[M]-1}')