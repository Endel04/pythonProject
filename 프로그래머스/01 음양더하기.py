def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # 참인 경우 양수이기 때문에 더하기
        if signs[i]:
            answer += absolutes[i]
        # 거짓인 경우 음수이기 때문에 빼기
        else:
            answer -= absolutes[i]
    return answer

if __name__ == '__main__':
    a = [4, 7, 12]
    s = [True, False, True]
    print(solution(a, s))