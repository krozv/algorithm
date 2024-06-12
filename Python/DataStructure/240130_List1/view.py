import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        count = 0
        min_j = 255
        for j in range(i-2, i+3):
            if arr[i] > arr[j]:
                count = arr[i] - arr[j]
                if min_j > count:
                    min_j = count
            elif arr[i] <= arr[j] and (i != j):
                min_j = 0
                break

        total += min_j
    print(f'#{tc} {total}')
