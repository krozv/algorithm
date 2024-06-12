# 4828. min max


T = int(input())
for t in range(T):
    input()
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    min_num = num_list[0]
    for num in num_list:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    print(f'#{t+1} {max_num - min_num}')

