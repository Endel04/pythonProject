from baseball_game_Engine import make_answer, check
from custom_error import InvalidLengthError

def save_history(answer, count, name):
    with open('baseball_history.txt', 'a', encoding='utf-8') as f:
        f.write(f'{answer}:{count}:{name}\n')

def load_history():
    count_name = {}

    with open('baseball_history.txt', 'r', encoding='utf-8') as f:
        print('-----history-----')

        while True:
            line = f.readline()
            if line == '':
                break
            print(line.rstrip())
            line = line.rstrip()  # answer:count:name
            data = line.split(':')  # data[0]: answer, data[1]: count, data[2]: name
            count_name[data[1]] = data[2]  # {3: 'name'}

        # Top3
        count_name = sorted(count_name.items())
        return count_name[:3]

answer = make_answer()
print(answer)
count = 0

while True: # 무한 반복
    # 숫자 묻기
    guess = input('숫자 세자리를 입력해주세요 (t : history, top3) : ')
    
    # t를 입력하면 Top3 불러오기
    if guess == 't':
        top3 = load_history()
        print(top3)
        continue

    # 숫자인지 아닌지 확인하기
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자 세자리를 입력하세요 : ')
        continue

    if len(guess) != len(answer):
        # raise InvalidLengthError('정답의 길이와 다른 숫자를 입력했습니다.')
        print(f'정답의 길이와 다른 숫자를 입력했습니다. {len(answer)} 문자')
        continue

    # strike, ball 판정하기
    strike, ball = check(guess, answer)
    count += 1

    # 출력하기
    print(f'{guess}\tstrike : {strike}\tball : {ball}\t{count} try')

    # 정답과 숫자가 같다면 끝내기
    if answer == guess:
        print('삐빅 정답입니다!')
        # 정답과 시도횟수 저장하기
        name = input('이름 : ')
        save_history(answer, count, name)
        
        # Top3 불러오기
        top3 = load_history()
        print(top3)
        break