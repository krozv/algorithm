# 회문1
import sys
sys.stdin = open('input (11).txt', 'r')
T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    palindrome = 0
    for i in range(8):
        for j in range(8-N+1):
            str1 = ''
            str2 = ''
            for k in range(N):
                str1 += arr[i][j+k]
                str2 += arr[j+k][i]
            if str1 == str1[::-1]:
                palindrome += 1
            if str2 == str2[::-1]:
                palindrome += 1
    print(f'#{t} {palindrome}')