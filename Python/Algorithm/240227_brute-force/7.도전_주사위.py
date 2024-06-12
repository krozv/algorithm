# 주사위
path = []


# 중복순열 함수
def dice1(i):
    # depth를 결정함
    if i == N:
        print(path)
        return
    # branch를 결정함
    for j in range(1, 7):
        path.append(j)
        dice1(i+1)
        path.pop()


# 순열 함수
def dice2(i):
    if i == 3:
        print(path)
        return

    for j in range(1, 7):
        if used[j]: continue
        used[j] = 1
        path.append(j)
        dice2(i+1)
        path.pop()
        used[j] = 0


N, T = map(int, input().split())
if T == 1:
    dice1(0)
else:
    used = [0] * 7
    dice2(0)