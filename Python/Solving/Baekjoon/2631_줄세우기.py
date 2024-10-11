'''
3 7 5 2 6 1 4
1 2 2 1 3 1 1
i) i번째 데이터의 값을 기준으로 앞에 데이터의 값과 dp 값 비교하여 dp 생성
ii) 가장 큰 값

'''

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

# arr[i]번째 숫자를 dp 배열을 만들어서 저장
child = 0
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        # dp 배열에 값 저장
        if arr[j] < arr[i]:
            if dp[j] >= dp[i]:
                dp[i] = dp[i] + 1
    child = max(dp)
print(n - child)