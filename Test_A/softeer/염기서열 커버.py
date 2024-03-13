N, M = map(int, input().split())
lst = [0] * M
for _ in range(N):
    s = list(input())
    for i in range(s):
        if s[i] != '.' and lst[i] == 0:
            lst[i] = s[i]
        elif s[i] != '.' and lst[i] != 0:
            