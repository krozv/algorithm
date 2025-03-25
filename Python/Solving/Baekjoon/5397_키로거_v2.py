import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

tc = int(input())
for t in range(tc):
    word = input().strip()
    left = deque()
    right = deque()

    for char in word:
        if char == '<':
            if left:
                right.appendleft(left.pop())
        elif char == '>':
            if right:
                left.append(right.popleft())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)

    result = ''.join(left) + ''.join(right)
    print(result)
