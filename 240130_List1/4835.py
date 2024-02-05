# 4835. 구간합

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = 0
    for num in num_list[:M]:
        max_sum += num
        min_sum += num
    for i in range(N-M+1):
        total = 0
        for num in num_list[i:i+M]:
            total += num
        if max_sum < total:
            max_sum = total
        if min_sum > total:
            min_sum = total
    print(f'#{t+1} {max_sum - min_sum}')