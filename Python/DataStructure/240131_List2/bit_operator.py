N = 3
arr = [1, 2, 3]

for i in range(1<<N):
    for j in range(N):
        if i & (1<<j):
            print(arr[j], end=' ')
        print()