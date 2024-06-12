# 전기버스
T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # distance: 충전기가 위치한 정류장 사이의 거리를 배열로 만들 예정
    distance = [0] * (M+2)
    distance[0] = K     # 출발 위치에서 갈 수 있는 거리 = K
    distance[1] = charge[0]     # 처음 충전기가 위치한 정류장
    distance[-1] = N - charge[-1]   # 종점까지의 거리
    
    # 충전기가 위치한 정류장 사이의 거리를 distance에 저장
    for i in range(2, M+1):
        distance[i] = charge[i-1] - charge[i-2]

    count = 0
    drivable = True

    # 버스 출발~!
    for i in range(1, M+1):
        # 버스의 이동거리만큼 뺍니다.
        distance[i] = distance[i-1] - distance[i]

        # 충전필요함 -> 충전
        if distance[i] < distance[i+1]:
            distance[i] = K
            count += 1 # 충전 횟수 증가

            # 충전 못함
            if distance[i] < distance[i+1]:
                drivable = False
                break
    if drivable:
        print(f'#{t + 1} {count}')
    else:
        print(f'#{t + 1} 0')
