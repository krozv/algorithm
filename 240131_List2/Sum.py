# Sum
'''
10개의 테스트 케이스
배열 크기 100 * 100
최댓값 구하세여
'''
import sys
sys.stdin = open('input4.txt', 'r')
for _ in range(10):
    t = int(input())
    arr = [0] * 100
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    max_sum = 0
    # 초기화 위치 유의
    cross_sum_1 = 0
    cross_sum_2 = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        # indentation 유의
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum
        cross_sum_1 += arr[i][i]
        cross_sum_2 += arr[i][99-i]
    # indentation 유의
    if max_sum < cross_sum_1:
        max_sum = cross_sum_1
    if max_sum < cross_sum_2:
        max_sum = cross_sum_2
    print(f'#{t} {max_sum}')
