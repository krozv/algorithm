# 연습 문제 - 상자 쌓기
N = int(input())    # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split()))
max_v = 0   # 가장 큰 낙차
for i in range(N-1):    # for i : 0 -> N-2, i 낙차를 구할 위치
    count = 0   # 오른쪽에 있는 더 낮은 높이
    for j in range(i+1, N):     # for j : i+1 -> N-1
        if arr[i] > arr[j]:
            count += 1
    if max_v < count:
        max_v = count
print(max_v)