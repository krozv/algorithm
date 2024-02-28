# 중복순열
path = []
def KFC(i):
    if i == 3:
        print(path)
        return

    for j in range(1, 7):
        path.append(j)
        KFC(i+1)
        path.pop()

KFC(0)