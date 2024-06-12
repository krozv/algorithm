# 파스칼의 삼각형
def pascal(N):  # N은 행 개수
    if N == 1:
        print(1)
        return 1
    arr = [0] * N
    pre_arr = pascal(N-1)
    arr[0] = 1
    arr[N - 1] = 1
    for i in range(1, N-1):
        arr[i] = pre_arr[i-1] + pre_arr[i]
    print(*arr)
    return arr


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t}')
    pascal(N)