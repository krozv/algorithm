# 백트래킹
# 완전탐색 + 가지치기
# 가능성이 없는 경우의 수를 제거하는 기법

# combination의 경우

arr = [i for i in range(1, 4)]
path = [0] * 3

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때까지 반복
    if level == 3:
        print(path)
        return
    # 들어가기 전
    # 다음 재귀 호출
        # 다음에 갈 수 있는 곳들은 어디인가?
        # 이 문제에서는 1, 2, 3 세 가지 경우의 수가 존재
    for i in range(len(arr)):
        path[level] = arr[i]
        dfs(level+1)
    # 갔다와서 할 로직
    # path[level] = 1
    # dfs(level+1)
    # path[level] = 2
    # dfs(level+1)
    # path[level] = 3
    # dfs(level+1)

dfs(0)