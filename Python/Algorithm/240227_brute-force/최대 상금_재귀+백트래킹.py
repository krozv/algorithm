# 최대 상금 외우기
def dfs(x):
    global max_cost
    if x == c:  # c번 교환
        max_cost = max(max_cost, int("".join(map(str, nums))))  # 최댓값 비교
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            nums[i], nums[j] = nums[j], nums[i]  # 자리 바꾸기

            chk = int("".join(map(str, nums)))
            if (x, chk) not in path:  # 가지치기 (지나간 자리가 아니면)
                dfs(x + 1)  # x+=1
                path.append((x, chk))  # 흔적 남기기

            nums[i], nums[j] = nums[j], nums[i]  # 초기화


T = int(input())
for tc in range(1, T + 1):
    tmp, c = input().split()
    c = int(c)
    N = len(tmp)
    nums = []  # 순열 리스트 초기화
    path = []  # 흔적 리스트 초기화
    max_cost = 0  # 최댓값 초기화
    for i in tmp:
        nums.append(i)
    dfs(0)
    print(f'#{tc} {max_cost}')