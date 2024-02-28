# 무한 재귀호출
def KFC(i):
    if i == 6:
        return
    print(i)
    KFC(i+1)
    print(i)

n = 0
KFC(0)
print('end')