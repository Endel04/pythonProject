answer = make_answer()
print(answer)

while True: # 무한 반복
    # 숫자 묻기
    guess = input('숫자 세자리를 입력해주세요 : ')

    # strike, ball 판정하기
    strike, ball = check(guess, answer)

    # 출력하기
    print(f'{guess}\tstrike : {strike}\tball : {ball}')

    # 정답과 숫자가 같다면 끝내기
    if answer == guess:
        print('삐빅 정답입니다!')
        break