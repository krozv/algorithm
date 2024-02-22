# 4843. 특별한 정렬
'''
번갈아가면서 정렬할 것임
'''
import sys
sys.stdin = open('input2.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        # i가 짝수이면 최대값 찾기
        if not i % 2:
            max_idx = i
            for j in range(i+1, N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        # i가 홀수이면 최솟값 찾기
        else:
            min_idx = i
            for j in range(i+1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            # print(arr)
    print(f'#{t}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()