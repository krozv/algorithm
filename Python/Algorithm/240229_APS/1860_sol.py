def check():  # m초의 시간 동안 k 개의 붕어빵을 만들 수 있다.
    sold_bread = 0  # 현재까지 팔린 붕어빵의 개수 초기화

    for person in guests:
        made_bread = (person // M) * K  # 현재 만들어진 빵의 개수
        sold_bread += 1

        remain = made_bread - sold_bread

        if remain < 0:
            return "Impossible"

    return "Possible"


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    guests = list(map(int, input().split()))
    guests.sort()  # 오름차순 정렬
    result = check()
    print(f'#{tc} {result}')