# snail number
'''
1부터 N*N까지 시계방향
N크기의 달팽이 구하기~~!
1 <= N <= 10
'''
T =int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(range(1, N**2+1))
    snail = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    initial = [0, 0]
    s = 0
    while True:
        for i in range(N**2):
            snail[initial[0]][initial[1]] = arr[i]
            if 0 <= initial[0] + di[s] < N and 0 <= initial[1] + dj[s] < N:
                if snail[initial[0]+di[s]][initial[1]+dj[s]] == 0:
                    initial[0] = di[s] + initial[0]
                    initial[1] = dj[s] + initial[1]
                else:
                    s = (s + 1) % 4
                    initial[0] = di[s] + initial[0]
                    initial[1] = dj[s] + initial[1]
            else:
                s = (s + 1) % 4
                initial[0] = di[s] + initial[0]
                initial[1] = dj[s] + initial[1]
        break
    print(f'#{t}')
    for row in snail:
        print(*row)
