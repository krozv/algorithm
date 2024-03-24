import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = float(input())
    ans = ''
    for i in range(1, 13):
        if N == 0:
            break
        if N >= 2**(-i):
            N -= 2**(-i)
            ans += '1'
        else:
            ans += '0'
    print(f'#{t}', end=' ')
    if N == 0:
        print(ans)
    else:
        print('overflow')