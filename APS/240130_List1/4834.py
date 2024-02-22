# 4834

T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int, list(input())))
    counts = [0] * 10
    for num in num_list:
        counts[num] += 1
    max_num = counts[0]
    for i in range(10):
        if max_num <= counts[i]:
            max_num = counts[i]
            number = i
    print(f'#{t+1} {number} {max_num}')