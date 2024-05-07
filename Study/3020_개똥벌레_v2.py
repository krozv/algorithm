# 3020. 개똥벌레
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, H = map(int, input().split())
obstacle_up = [0]*(H+1)     # 석순
obstacle_down = [0]*(H+1)   # 종유석
obstacles = [int(input()) for _ in range(N)]
for idx, obstacle in enumerate(obstacles):
    # 석순일 경우
    if not idx % 2:
        obstacle_up[obstacle] += 1
    # 종유석일 경우
    else:
        obstacle_down[obstacle] += 1

target = N
cnt = 0

for h in range(H-1, 0, -1):     # 누적합을 구해서, 장애물 개수 count
    obstacle_up[h] += obstacle_up[h+1]
    obstacle_down[h] += obstacle_down[h+1]

result = [0]*(H+1)      # 석순과 종유석을 더한 장애물 개수
for h in range(1, H+1):
    result[h] = obstacle_up[h] + obstacle_down[H-h+1]
    if result[h] < target:
        target = result[h]
        cnt = 1
    elif result[h] == target:
        cnt += 1
print(target, cnt)


