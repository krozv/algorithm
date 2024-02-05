s1 = 'abc'
s2 = 'abc'
print(s1 == s2)     # True
print(s1 is s2)     # True

s3 = s1[:2] + 'c'
print(s1 == s3)     # True
print(s1 is s3)     # False