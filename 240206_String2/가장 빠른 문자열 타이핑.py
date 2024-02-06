# 가장 빠른 문자열 타이핑
"""
문자열 A를 타이핑
B는 단축키 같은 느낌
"""
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    string, key = input().split()
    idx = 0
    new_string = ''
    while len(key) + idx <= len(string):
        for i in range(len(key)):
            if string[idx + i] != key[i]:
                idx += 1
                same = False
                break
            else:
                same = True
        if same:
            new_string += '0'
            idx += len(key)
        else:
            new_string += string[idx-1]
    new_string += string[idx:]
    print(f'#{tc} {len(new_string)}')
