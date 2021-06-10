from Recipebook import RecipeBook

def print_menu():
    print('1. 레시피 검색')
    print('2. 레시피 추가하기')
    print('3. 재료 검색하기')
    print('4. 전체 레시피 보여주기')
    print('5. 종료하기')

    num = input('메뉴를 선택하세요 : ')
    return num

def main():
    recipebook_204 = RecipeBook()

    while True:
        num = print_menu()

        if num == '1':
            # 레시피 검색
            recipebook_204.search_recipe()
        elif num == '2':
            # 레시피 추가하기
            recipebook_204.add_recipe()
        elif num == '3':
            # 재료 검색하기
            recipebook_204.search_ingrediant()
        elif num == '4':
            # 전체 레시피 보여주기
            recipebook_204.show_recipe()
        elif num == '5':
            # 종료하기
            break
        else:
            print('1-5 사이의 숫자로 다시 입력해주세요')

if __name__ == '__main__':
    main()