import sys
sys.stdin = open('GNS_test_input.txt', 'r')
T = int(input())
for _ in range(T):
    tc, N = input().split()
    N_list = input().split()
    counts = [0]*10 #다른 행성의 0~9를 세는 리스트
    language = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in N_list:
        for j in range(10):
            if i == language[j]:
                counts[j] += 1
                break
    print(tc)
    for i in range(10):
        print(f'{language[i]} '*counts[i], end=' ')
    print()
