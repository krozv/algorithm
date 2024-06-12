import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    time = [0] * N
    table = [0] * N
    for i in range(N):
        time[i] = int(input())
    cnt = 0
    for i in range(M):
        seat = table.index(0)
        # 비교하기
        other = [0] * N
        # 이진탐색 : min_other
        for i in range(N):
            other[i] = table[i] + time[i]
        if time[seat] > min(other):
            idx = other.index(min(other))
            table[idx] += time[idx]
        else:
            table[seat] = time[seat]
        ti = min(table)
        table = list(map(lambda x: x-min(table), table))
        cnt += ti

    print(f'#{t} {cnt + max(table)}')
