# 3020. 개똥벌레
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, H = map(int, input().split())
lst = [0]*(H+1)
obstacles = [int(input()) for _ in range(N)]
for idx, obstacle in enumerate(obstacles):
    # 석순
    if not idx % 2:
        for i in range(1, obstacle+1):
            lst[i] += 1
    # 종유석
    else:
        for i in range(H, H-obstacle, -1):
            lst[i] += 1
lst = lst[1:]
lst.sort()
print(lst[0], lst.count(lst[0]))