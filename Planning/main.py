from GooDSlist import GooDSlist

def print_menu():
    print('1. 상품 검색')
    print('2. 판매할 상품 올리기')
    print('3. 인기 상품 보여주기')
    print('4. 올라온 상품 전체 보여주기')
    print('5. 종료하기')

    num = input('메뉴를 선택하세요 : ')
    return num

def main():
    KNY_GooDS = GooDSlist()

    while True:
        num = print_menu()

        if num == '1':
            # 상품 검색
            KNY_GooDS.search_product()
        elif num == '2':
            # 판매할 상품 올리기
            pass
        elif num == '3':
            # 인기 상품 보여주기
            pass
        elif num == '4':
            # 올라온 상품 전체 보여주기
            pass
        elif num == '5':
            # 종료하기
            break
        else:
            print('1-5 사이의 숫자로 다시 입력해주세요')

if __name__ == '__main__':
    main()