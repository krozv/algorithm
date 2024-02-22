# 전기버스
T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    count = [K] * (M+1)
    for i in range(1, M+1):
        count[i] = count[i] + count[i-1]
    for i in range(M+1):
        if count[i] >= N:
            charge = i
            break
    distance = [0] * (M-1)
    for i in range(M-1):
        distance[i] = data[i+1] - data[i]
    for i in range(M-1):
        if distance[i] > K:
            print(f'#{t+1} 0')
            break
    else:
        print(f'#{t+1} {charge}')