import sys
sys.stdin = open('input.txt', 'r')
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    price = price[::-1]
    earn = 0
    i = 0
    saleprice = price[0]
    while True:
        if i == N:
            break
        if saleprice >= price[i]:
            earn += saleprice - price[i]
        elif saleprice < price[i]:
            saleprice = price[i]
        i += 1
    print(f'#{tc} {earn}')