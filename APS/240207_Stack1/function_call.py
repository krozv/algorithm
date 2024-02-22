# function call
def f2(n):
    n *= 2
    print(n)


def f1(c, d):
    e = c + d
    f2(e)


a = 10
b = 20
c = a + b
f1(a, b)