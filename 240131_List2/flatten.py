# Flatten
# 이유 모르겠음
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for t in range(T):

    dump = int(input())
    box_list = list(map(int, input().split()))

    # dump 시작
    for i in range(dump+1):
        max_box = box_list[0]
        min_box = box_list[0]
        max_index = 0
        min_index = 0
        substraction = 0
        # 최고점과 최저점 탐색
        for j in range(100):
            if max_box < box_list[j]:
                max_box = box_list[j]
                max_index = j
            if min_box > box_list[j]:
                min_box = box_list[j]
                min_index = j
        subtraction = box_list[max_index] - box_list[min_index]
        box_list[max_index] -= 1
        box_list[min_index] += 1
    print(f'#{t+1} {subtraction}')
