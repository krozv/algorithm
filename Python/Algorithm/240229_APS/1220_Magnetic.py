# 1220 Magnetic
def get_cnt(col):
    cnt = 0
    # red 자성체를 체크
    is_red = False

    for row in range(N):
        # 1. red 발견
        if arr[row][col] == 1:
            is_red = True
        # 2. 이전에 red를 발견했고, 현재 blue 발견
        elif is_red and arr[row][col] == 2:
            is_red = False
            cnt += 1
    return cnt


import sys
sys.stdin = open('input.txt', 'r')
T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N):
        total += get_cnt(i)
    print(f'#{t} {total}')