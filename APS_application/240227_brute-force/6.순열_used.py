# 순열 구현 - 중요함
path = []
used = [False, False, False]


def KFC(x):
    if x == 2:
        print(path)
        return

    for i in range(3):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        KFC(x + 1)
        path.pop()
        used[i] = False


KFC(0)
