# 집합
'''
비어있는 공집합 S
add x
remove x
check x
toggle x
all S를 변경
empty S를 공집합으로
'''
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    calc = input().strip('\n').split(' ')
    # calc 길이에 따라 나누기
    # all, empty
    if len(calc) == 1:
        if 'all' == calc[0]:
            S = set(range(1, 21))
        if 'empty' == calc[0]:
            S = set()
    # add, remove, check, toggle
    else:
        num = int(calc[1])
        if 'add' == calc[0]:
            S.add(num)
        if 'remove' == calc[0]:
            if S.issuperset({num}):
                S.remove(num)
        if 'check' == calc[0]:
            print(int(S.issuperset({num})))
        if 'toggle' == calc[0]:
            if S.issuperset({num}):
                S.remove(num)
            else:
                S.add(num)
