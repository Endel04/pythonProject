# 가운데 글자 가져오기
def solution(s):
    # 문자열의 갯수가 홀수일 때 한 개만 반환
    # 5개일 때 -> idx : 2 / 7개일 때 -> idx : 3 / 9개일 때 -> idx : 4
    if len(s) % 2 == 1:
        return s[len(s) // 2]

    # 문자열의 갯수가 짝수일 때 두 개를 반환
    # 4개일 때 idx : 1,2 / 6개일 때 idx : 2,3 / 8개일 때 idx : 3,4
    else:
        return s[len(s)//2-1] + s[len(s)//2]

s1 = "abcde"
print(solution(s1))  # c
s2 = "qwer"
print(solution(s2))  # we