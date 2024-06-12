# 공과 잡초
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    string = input()
    cnt = 0
    for i in range(len(string)):
        if string[i] == '(':
            cnt += 1
        elif string[i] == ')' and (i == 0 or string[i-1] != '('):
            cnt += 1
    print(f'#{t} {cnt}')