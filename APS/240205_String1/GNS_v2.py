# GNS
'''
숫자 체계가 다름
다른 숫자 체계로 sort
'''
import sys
sys.stdin = open('GNS_test_input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    tc, N = map(int, input().lstrip('#').split())
    arr = list(input().split())
    number = list(range(0, 10))
    string = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 변환하기 쉽게 dictionary에 key-value 형태로 저장
    str_to_num = dict(zip(string, number))      # 문자열을 숫자로
    num_to_str = dict(zip(number, string))      # 숫자를 문자열로
    # counting sort로 정렬
    new_arr = [0] * N
    cnt = [0] * 10
    for i in range(N):
        new_arr[i] = str_to_num[arr[i]]
        cnt[new_arr[i]] += 1
    print(f'#{tc}')
    for i in range(10):
        print(f'{num_to_str[i]} ' * cnt[i], end=' ')
    print()