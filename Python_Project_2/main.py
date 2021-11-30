from T_ANBlist import T_ANBlist

def print_menu1():
    print()
    print('---------------')
    print('1. 회원가입 하기')
    print('2. 로그인 하기')
    print('3. 종료하기')
    print('---------------')

    num1 = input('\n메뉴를 선택하세요 | ')
    return num1

def print_menu2():
    print()
    print('---------------')
    print('1. 게시글 검색')
    print('2. 게시글 올리기')
    print('3. 모든 게시글 보기')
    print('4. 내 정보 보기')
    print('5. 로그아웃 하기')
    print('---------------')

    num2 = input('\n메뉴를 선택하세요 | ')
    return num2

def main():
    T_ANB = T_ANBlist()

    while True:
        num1 = print_menu1()

        if num1 == '1': # 회원가입 하기
            T_ANB.join_membership()
        elif num1 == '2': # 로그인 하기
            T_ANB.login()

            num2 = print_menu2()

            if num2 == '1':
                T_ANB.search_bulletin()  # 게시글 검색
                print_menu2()
            elif num2 == '2':
                T_ANB.upload_bulletin()  # 게시글 올리기
            elif num2 == '3':
                T_ANB.show_bulletin()  # 모든 게시글 보기
            elif num2 == '4':
                T_ANB.member_list()
            elif num2 == '5':
                break  # 로그아웃 하기
            else:
                print('1-5 사이의 숫자로 다시 입력해 주세요!')
            
        elif num1 == '3':
            # 종료하기
            break
        else:
            print('1-3 사이의 숫자로 다시 입력해 주세요!')

if __name__ == '__main__':
    main()