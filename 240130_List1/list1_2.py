# 최대 최소의 간격
T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    counts = [0] * N
    max_num = num_list[0]
    min_num = num_list[0]
    for num in num_list:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    max_count = 0
    min_count = 0
    for i in range(N):
        if max_num == num_list[i]:
            max_count += 1
        if min_num == num_list[i]:
            min_count += 1
    for i in range(N-1, -1, -1):
        if max_num == num_list[i]:
            max_distance = i
            break
    for i in range(N):
        if min_num == num_list[i]:
            min_distance = i
            break
    print(max_distance, min_distance)
    if (max_distance - min_distance) > 0:
        abs_distance = (max_distance - min_distance)
    else:
        abs_distance = (min_distance - max_distance)
    print(f'#{t+1} {abs_distance}')

