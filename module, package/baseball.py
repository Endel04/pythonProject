from baseball_game_Engine import make_answer, check

answer = make_answer()

while True: # 무한 반복
    # 숫자 묻기
    guess = input('숫자 세자리를 입력해주세요 : ')

    # 숫자인지 아닌지 확인하기
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자 세자리를 입력하세요 : ')
        continue

    if len(guess) != len(answer):
        raise InvalidLengthError('정답의 길이와 다른 숫자를 입력했습니다.')

    # strike, ball 판정하기
    strike, ball = check(guess, answer)

    # 출력하기
    print(f'{guess}\tstrike : {strike}\tball : {ball}')

    # 정답과 숫자가 같다면 끝내기
    if answer == guess:
        print('삐빅 정답입니다!')
        break