'''
3
1 2 3
4 5 6
7 8 9
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0]*N for _ in range(N)]
arr3 = [[0]*N]*N    # 2차원 배열 이렇게 만들지 마세여
print(arr3)     # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
arr3[0][0] = 1
print(arr3)     # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        function(array[i][j])