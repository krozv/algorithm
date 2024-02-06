T = int(input())
for t in range(1, T+1):
    A = input()
    start = 0
    end = len(A)-1
    while start <= end:
        if A[start] != A[end]:
            break
        start += 1
        end -= 1
    print(f'#{t} {int(start > end)}')
