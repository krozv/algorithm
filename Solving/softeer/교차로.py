import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque
N = int(input())
arr = [deque() for _ in range(4)]
for i in range(N):
    t, w = input().split()
    arr[ord(w)-65].append((int(t), i))
print(arr)
