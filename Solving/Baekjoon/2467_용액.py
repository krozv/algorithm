# 2467. 용액
"""
합이 < 0 경우: start+1
합이 > 0 경우: end -1
"""
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 초기값 설정
start, end = 0, N-1
min_dif = abs(arr[start] + arr[end])
a, b = arr[start], arr[end]
while start < end:
    target = arr[start] + arr[end]
    if abs(min_dif) > abs(target):
        min_dif = abs(target)
        a, b = arr[start], arr[end]
    if target == 0:
        break
    elif target < 0:
        start += 1
    elif target > 0:
        end -= 1
print(a, b)