# 7576. 토마토
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)