import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    num, change = input().split()
    num_list = list(map(int, list(num)))
    change = int(change)
    max_num = num_list[0]

    for ch in range(change):
        max_index = ch
        for n in num_list[ch:]:
            if max_num < n:
                max_num = n
        for n in num_list[ch:]:
            if n == max_num:
                break
            max_index += 1
        num_list[ch], num_list[max_index] = max_num, num_list[ch]
    num_list = ''.join(list(map(str, num_list)))

    print(f'#{t+1} {num_list}')