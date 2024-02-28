import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    time = [0] * N
    table = [0] * N
    for i in range(N):
        time[i] = int(input())
    print('time', time)
    cnt = 0
    for i in range(M):
        while True:
            if 0 in table:
                seat = table.index(0)
                print(table)
                # 비교하기
                other = [0] * N
                for i in range(N):
                    other[i] = table[i] + time[i]
                print('other', other)

                if time[seat] > min(other):
                    idx = other.index(min(other))
                    table[idx] += time[idx]
                    print('here')
                else:
                    table[seat] = time[seat]
                break
            table = list(map(lambda x: x-1, table))
            cnt += 1
            print(table)

    print(f'#{t} {cnt + max(table)}')
