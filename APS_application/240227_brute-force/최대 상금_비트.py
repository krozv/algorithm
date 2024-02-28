def f(k, N):
    global max_v
    if k == N:
        money = int(''.join(card))
        if max_v < money:
            max_v = money
    else:
        for i in range(len(card)):
            for j in range(i + 1, len(card)):
                card[i], card[j] = card[j], card[i]
                m = int(''.join(card))  # memo에서 같은 교환횟수에 같은 값이 나온적이 있으면 생략
                # 숫자 m이 k번째 교환할때 출현했는 지를 확인
                if memo[m] & (1 << k) == 0:
                    memo[m] |= 1 << k
                    f(k + 1, N)
                card[i], card[j] = card[j], card[i]


T = int(input())
for tc in range(1, T + 1):
    num, N = input().split()
    card = list(num)
    N = int(N)
    max_v = 0
    memo = [0] * (10 ** len(card))
    f(0, N)
    print(f'#{tc} {max_v}')