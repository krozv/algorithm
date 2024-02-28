def test(i):
    if i == 3:
        return
    test(i+1)
    test(i+1)
    print(i)

test(0)