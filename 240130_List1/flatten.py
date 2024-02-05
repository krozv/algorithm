# flatten
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for t in range(T):
    dump = int(input())
    box_list = list(map(int, input().split()))
    # print(box_list)
    for _ in range(1, dump+1):
        flattening = True
        max_box = box_list[0]
        min_box = box_list[0]
        max_index = 0
        min_index = 0
        for i in range(100):
            if max_box < box_list[i]:
                max_box = box_list[i]
                max_index = i
            if min_box > box_list[i]:
                min_box = box_list[i]
                min_index = i
        subtraction = box_list[max_index] - box_list[min_index]
        box_list[max_index] -= 1
        box_list[min_index] += 1
        if (box_list[max_index] - box_list[min_index]) <= 1:
            flattening = False
            break
    if flattening:
        print(f'#{t+1} {subtraction}')
    else:
        print(f'#{t+1} {box_list[max_index] - box_list[min_index]}')
