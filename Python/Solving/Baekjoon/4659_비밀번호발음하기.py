# 4659. 비밀번호 발음하기
"""
발음이 가능한 패스워드 만들기
패스워드의 품질 평가
1. 모음(a,e,i,o,u)중 1 포함
2. 모음 3개 혹은 자음 3개가 연속으로 오면 안된다
3. 같은 글자 연속 금지. ee와 oo 허용
품질 평가.
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

vowel_list = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input().split()[0]
    # end point check
    if password == 'end':
        break
    # password 품질 평가
    check = True
    conso = 0 # 자음
    vowel = 0 # 모음
    prev = password[0]
    cnt = 0
    for idx, char in enumerate(password):
        # 연속 글자 확인
        if idx and prev == char and prev != 'e' and prev != 'o':
            check = False
            break
        # char가 모음인 경우
        if char in vowel_list:
            vowel += 1
            if idx and prev in vowel_list:
                cnt += 1
            else:
                cnt = 0
        # char가 자음인 경우
        else:
            conso += 1
            if idx and prev not in vowel_list:
                cnt += 1
            else:
                cnt = 0
        prev = char
        # 3번 연속 여부 확인
        if cnt == 2:
            check = False
            break
        # check 확인
        if not check:
            break
    # 모음 포함 확인
    if not vowel:
        check = False
    if check:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
