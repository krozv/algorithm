import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    table = [0] * N

    for i in range(N):
        table[i] = int(input())

    before_table = [0] * N
    print(before_table)
    for i in range(M):
        print(before_table)
        ending = before_table.index(min(before_table))
        for j in range(N):
            before_table[j] = before_table[j] - before_table[ending]
        print('최소시간 뺀 상태:', before_table)

        after_table = [0] * N
        for j in range(N):
            after_table[j] = before_table[j] + table[j]
        print('심사까지 걸리는 시간:', after_table)

        enter = after_table.index(min(after_table))
        for j in range(N):
            if j == enter:
                before_table[enter] = table[enter]
            else:
                before_table[j] -= table[enter]
        print(before_table)
        print('---------------')