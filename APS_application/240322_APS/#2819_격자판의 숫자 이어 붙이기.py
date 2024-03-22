# 2819. 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open('input.txt', 'r')


def dfs(y, x, path):
    # 기저조건: 7자리면 끝
    if len(path) == 7:
        result.add(path)
        return
    for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        ny = y + d[0]
        nx = x + d[1]
        if 0<=ny<4 and 0<=nx<4:
            dfs(ny, nx, path+maps[ny][nx])


T = int(input())

for t in range(1, T+1):
    # 격자판 저장
    maps = [input().split() for _ in range(4)]
    # 중복을 제거하기 위해 set 사용
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{t} {len(result)}')
