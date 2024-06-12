# 파이프 옮기기 1
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
bfs(0, 0, 0)
print(cnt)