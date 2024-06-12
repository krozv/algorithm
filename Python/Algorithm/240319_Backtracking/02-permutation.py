# 백트래킹
# 완전탐색 + 가지치기
# 가능성이 없는 경우의 수를 제거하는 기법

# permutation의 경우

arr = [i for i in range(1, 4)]
path = [0] * 3


def dfs(level):
    if level == 3:
        print(path)

    for i in range(len(arr)):
        # 여기는 못가! 가지치기
        # 갈 수 없는 경우를 활용하는 것이 코드가 깔끔함
        # 갈 수 없을 때 continue
        if arr[i] in path:
            continue

        path[level] = arr[i]
        dfs(level + 1)

        # 갔다와서 할 로직
        # 기존 방문을 초기화
        path[level] = 0


dfs(0)