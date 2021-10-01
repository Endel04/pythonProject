import random

# 정답 정하기 : 0~9 사이의 숫자 세개 뽑고 잇기
def make_answer():
    num = random.sample(range(0, 9 + 1), 3)
    return str(num[0]) + str(num[1]) + str(num[2])

def check(guess, answer):
    strike = 0
    ball = 0

    # 숫자 하나 꺼내서 정답에 있고 자리가 같으면 strike += 1
    # 숫자 하나 꺼내서 정답에 있고 자리가 다르면 bal += 1

    # for i in range(3):
    #     if guess[i] == answer[i]:
    #         strike += 1
    #     elif guess[i] in answer:
    #         ball += 1

    for i, g in enumerate(guess):
        for j, a in enumerate(answer):
            if g == a:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    return strike, ball

if __name__ == '__main__':
    answer = make_answer()
    print(answer)  # 1 0
    strike, ball = check("832", "934")
    print(strike, ball)
    strike, ball = check("431", "934")
    print(strike, ball)  # 1 1
    strike, ball = check("934", "934")
    print(strike, ball)  # 3 0