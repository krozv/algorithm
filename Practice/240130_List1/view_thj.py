import sys
sys.stdin = open('input.txt', 'r')
#stdin 표준 입력
#콘솔과 연결되어 있는 표준 입력임
#이걸 파일에 있는 걸로 바꿔!
T = 10
for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))

    sum_good = 0
    for i in range(2, N-2):
        max_height = 0
        for j in [i-2, i-1, i+1, i+2]:
            if max_height < height[j]:
                max_height = height[j]
        if max_height < height[i]:
            sum_good += height[i] - max_height

    print(f'#{tc} {sum_good}')