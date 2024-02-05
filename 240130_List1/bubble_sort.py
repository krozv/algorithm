# Bubble Sort
# 오름차순
N = 6
arr = [7, 2, 5, 3, 1, 4]
for i in range(N-1, 0, -1):     # for i : N-1 -> 1, 정렬할 구간의 마지막 인덱스
    for j in range(i):      # for j : 0 -> i-1, 비교할 두 원소 중 왼쪽의 인덱스
        if arr[j] > arr[j+1]:       # 오름차순
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# 내림차순
for i in range(N-1, 0, -1):     # for i : N-1 -> 1, 정렬할 구간의 마지막 인덱스
    for j in range(i):      # for j : 0 -> i-1, 비교할 두 원소 중 왼쪽의 인덱스
        if arr[j] < arr[j+1]:       # 내림차순
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)