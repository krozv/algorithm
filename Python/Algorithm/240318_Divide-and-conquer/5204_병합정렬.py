"""
병합 정렬을 이용해 오름차순 정렬
병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 출력
"""
# 리스트를 2분할
def merge_sort(m):
    # print(m)
    if len(m) == 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    # 분할
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

# 분할한 리스트 병합
def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = [0] * (len(right)+len(left))
    i = j = 0
    # left, right 존재
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            result[i+j] = right[j]
            j += 1
    # left 원소만 남은 경우
    while i < len(left):
        result[i+j] = left[i]
        i += 1
    # right 원소만 남은 경우
    while j < len(right):
        result[i+j] = right[j]
        j += 1
    return result

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{t} {result[N//2]} {cnt}')
