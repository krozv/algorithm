T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0  # 맨 앞을 최솟값으로 지정
    max_idx = 0

    for i in range(N):
        if arr[min_idx] > arr[i]: # 지금까지의 최솟값보다 arr[i]가 더 작으면
            min_idx = i
        if arr[max_idx] <= arr[i]: # >=면 같은게 나오면 이동. >면 처음 그 위치
            max_idx = i

    ans = abs(max_idx - min_idx)
    print(f'#{t+1} {ans}')