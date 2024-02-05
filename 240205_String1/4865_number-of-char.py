# 4865. 글자수
'''
문자열 str1에 포함된 글자가 str2에 몇 개씩 있는 지 찾고
그 중 가장 많은 글자의 개수를 출력
딕셔너리 이용 가능
'''
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T+1):
    N = list(input())
    M = list(input())
    char_dict = {}
    for char in N:
        char_dict[char] = 0
    for char in M:
        if char in char_dict:
            char_dict[char] += 1
    max_char = 0
    for value in char_dict.values():
        if max_char < value:
            max_char = value
    print(f'#{t} {max_char}')