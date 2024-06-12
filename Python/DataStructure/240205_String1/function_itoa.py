def itoa(a):
    s = ''
    while a > 0:
        s = chr(a%10+ord('0')) + s
        a //= 10
    return s


print(itoa(123))
print(type(itoa(123)))