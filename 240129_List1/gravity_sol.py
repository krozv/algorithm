"""
9
7 4 2 0 0 6 0 7 0
"""

N = int(input()) #상자가 쌓여있는 가로 길이
arr = list(map(int,input().split())) #상자 세로 길이

max_count = 0 #가장 큰 낙차

for i in range(N-1):
    count = 0 # 오른쪽에 있는 더 낮은 높이의 개수
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            count +=1
    if count > max_count :
        max_count = count
print(max_count)