from Bullentin_list import Bullentin_list

def print_menu():
    print('---------------')
    print('1. 회원가입 하기')
    print('2. 로그인 하기')
    print('3. 종료하기')
    print('---------------')

    num = input('\n메뉴를 선택하세요 | ')
    return num

def main():
    T_ANB = Bullentin_list()

    while True:
        num = print_menu()

        if num == '1': # 회원가입 하기

            question1 = input('회원가입을 하시겠습니까? (1 : yes, 1 이외의 숫자 : no) | ')

            if question1 == '1':
                T_ANB.join_membership()
            else:
                return

        elif num == '2': # 로그인 하기
            question2 = input('로그인을 하시겠습니까? (1 : yes, 1 이외의 숫자 : no) | ')

            if question2 == 1:
                T_ANB.login()
            else:
                return
            
        elif num == '3':
            # 종료하기
            break
        else:
            print('1-3 사이의 숫자로 다시 입력해주세요')

if __name__ == '__main__':
    main()