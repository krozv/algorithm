"""
L: 로봇이 왼쪽으로 90도 회전, 보는 방향 변경
R: 로봇이 오른쪽으로 90도 회전, 보는 방향 변경
A: 로봇이 바라보는 방향으로 두 칸 전진, 격자판 바깥 나갈 경우에는 명령 수행 X
같은 칸 두 번 방문X

1. 처음 로봇을 어떤 칸에 어떤 방향으로 두어야 함?
2. 어떤 명령어를 어떤 순서대로 입력?
3. 명령어 개수 최소화

condition
5<=H,W<=25
한 번 이상의 A명령. 로봇이 방문한 칸 수 최소 3개 이상
"""
import sys
sys.stdin = open('input.txt', 'r')

H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]

path = []
cnt = 0
for i in range(H):
    for j in range(W):
        if arr[i][j] == '#':
            arr[i][j] = 1
            cnt += 1
        else:
            arr[i][j] = 0

adj = [[] for _ in range(H*W+1)]
for i in range(H):
    for j in range(W):
        if arr[i][j]:
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni = i + d[0]
                nj = j + d[1]
                if 0<=ni<H and 0<=nj<W and arr[ni][nj]:
                    adj[i*W+j+1].append(ni*W+nj+1)

# 반복문으로 풀기
delta = [-W, +1, +W, -1]
button = '^>v<'
ans = ''
for i in range(1, H*W+1):
    if len(adj[i]) == 1:
        now = i
        dist = 1
        d = []
        command = ''
        visited = [0] * (H*W+1)
        while dist < cnt:
            visited[now] = 1
            for to in adj[now]:
                if not visited[to]:
                    dif = to - now
                    # 명령어 정하기
                    visited[to] = 1
                    if (to+dif) in adj[to] and not visited[to+dif]:
                        now = to + dif
                        dist += 2
                        direction = delta.index(dif)
                        if d and d[-1] != direction:
                            if (d[-1]+1)%4 == direction:
                                command += 'RA'
                            else:
                                command += 'LA'
                        else:
                            command += 'A'
                        d.append(direction)
                        break
        if not ans:
            start = i
            ans = command
            log = d
        else:
            if len(ans) > len(command):
                start = i
                ans = command
                log = d

a = (start-1) // W
b = (start-1)-(a*W)
print(a+1, b+1)
print(button[log[0]])
print(ans)



