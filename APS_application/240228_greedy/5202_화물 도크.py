# 5202. 화물 도크
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))
    # print(time)
    time.sort(key=lambda x: x[1])
    # print(time)
    s = 0
    cnt = 0
    for start, end in time:
        if start >= s:
            cnt += 1
            s = end
    print(f'#{t} {cnt}')
