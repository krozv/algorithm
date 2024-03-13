import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    answer = 0
    n, m = map(int, input().split())

    times = [int(input()) for _ in range(n)]
    left, right = 1, max(times) * m

    while left <= right:
        mid = (left+right) // 2
        people = sum([mid//time for time in times])

        if people >= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(f'#{t} {answer}')