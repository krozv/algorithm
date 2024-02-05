s1 = list(input())
s2 = input()
s1[0] = 'd'     # 배열은 원소 변경 가능
print(s1)
print(s2[0])
s2[0] = 'a'     # 문자열은 원소 변경 불가능
print(s2)