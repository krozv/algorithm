# 중위순회
"""
in_order 형식으로 특정 단어
트리: 완전 이진트리
"""
def in_order(T):
    if T:
        in_order(left[T])
        print(word[T], end='')
        in_order(right[T])

import sys
sys.stdin = open('input.txt', 'r')
T = 10
for t in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    word = [0] * (N+1)
    for _ in range(N):
        info = input()
        if info[-1].isdigit():
            node, char, *c = info.split()
            node = int(node)
            # 자식이 두 명일 경우
            if len(c) > 1:
                l, r = map(int, c)
                right[node] = r
                left[node] = l
                par[r] = node
                par[l] = node
            # 자식이 한 명일 경우:
            else:
                # print(c[0])
                l = int(c[0])
                left[node] = l
                par[l] = node
        else:
            node, char = info.split()
            node = int(node)
        word[node] = char
    print(f'#{t} ', end='')
    in_order(1)
    print()

