# 원재의 메모리 복구하기
# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    last = input()
    # print(len(last))
    N = len(last)
    first = '0' * N
    cnt = 0
    pre = 0
    for i in range(N-1, -1, -1):
        # print(int(last, 2) >> i & 1)
        if int(last, 2) >> i & 1:
            if not pre:
                cnt += 1
                pre = 1
        else:
            if pre:
                cnt += 1
                pre = 0
    print(f'#{t} {cnt}')