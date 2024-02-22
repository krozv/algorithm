# Baby_gin

T = int(input())
N = 10
for t in range(T):
    count = [0] * 10
    num_list = list(map(int, list(input())))
    a = 0
    tri = 0
    for num in num_list:
        count[num] += 1
    for i in range(N):
        tri += count[i] // 3
        count[i] %= 3
    for i in range(1, N-2):
        while True:
            if count[i] >= 1 and count[i + 1] >= 1 and count[i + 2] >= 1:
                count[i] -= 1
                count[i + 1] -= 1
                count[i + 2] -= 1
                a += 1
            else:
                break
    if tri + a >= 2:
        print(f'#{t+1} Baby Gin')
    else:
        print(f'#{t+1} Lose')