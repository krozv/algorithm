# 이진탐색 그냥 외우자..
def f(i, a, N):
    if i > N:
        return 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    f(1, 0, N)
    print(f'#{t} {tree[1]} {tree[N//2]}')