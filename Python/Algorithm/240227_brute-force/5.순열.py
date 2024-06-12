# 중복순열
path = []

def KFC(x):
    if x == 2:
        print(path)
        return

    for i in range(3):
        path.append(i)
        KFC(x+1)
        path.pop()
KFC(0)