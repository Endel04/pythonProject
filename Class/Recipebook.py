from Recipe import Recipe

class RecipeBook:
    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

    def add_recipe(self):
        # 추가할 레시피 이름 입력
        name = input('레시피의 이름을 입력하세요 : ')

        # 중복 체크
        for recipe in self.recipe_list:
            if name == recipe.name:  # 중복되는 레시피가 있으면 중복이라고 표기
                print('이미 존재하는 레시피입니다.')
                return  # 빠져 나오기

        # 중복되는 레시피가 없으면 추가
        # 레시피 생성
        new_recipe = Recipe(name)
        new_recipe.set_recipe()

        # 레시피 리스트에 생성한 레시피 추가하기
        self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1}')
            print(recipe)

    def search_recipe(self):
        # 찾은 레시피
        searched_recipe = []

        # 레시피 이름 입력받기
        name = input('원하는 레시피를 검색하세요 : ')

        # 레시피의 이름이 검색한 이름과 같은지 확인
        for recipe in self.recipe_list:
            if name == recipe.name:  # 같으면 레시피 보여주기
                print(recipe)
                searched_recipe.append(recipe)

        if len(searched_recipe) == 0:  # 검색한 레시피가 없으면
            # 추가할지 물어보기
            answer = input('찾는 레시피가 없습니다. 레시피를 추가하시겠습니까? 1 : yes, 1 이외의 숫자 : no')

            if answer == 1:   # 1을 입력했을 때
                # 레시피 추가하기
                self.add_recipe()
            else:   # 1이 아닌 다른 숫자를 입력했을 때
                return

    # 재료로 메뉴 검색하기
    def search_ingrediant(self):
        # 빈 set 생성
        all_ingrediant = set()

        # 레시피북의 레시피 재료 set에 넣기
        for recipe in self.recipe_list:
            for ingrediant in recipe.ingrediant:
                all_ingrediant.add(ingrediant)

        # 모든 재료 보여주기
        for index, ingrediant in enumerate(all_ingrediant):
            print(f'{index + 1}, {ingrediant}')

        # 찾을 재료 이름 검색하기
        search_num = int(input('사용할 재료를 입력하세요 : '))
        search_ingrediant = list(all_ingrediant)[search_num-1]

        # 입력한 재료가 포함되는 레시피 모두 보여주기
        for recipe in self.recipe_list:
            # 입력한 재료가 포함되면
            if search_ingrediant in recipe.ingrediant:
                # 레시피 모두 보여주기
                print(recipe)
                
    def init_recipe(self):
        떡볶이 = Recipe('떡볶이')
        떡볶이.people = 2   # 1
        떡볶이.video = 'youtube.com'   # ''
        떡볶이.ingrediant = {'물': '100', '떡': '100', '고추장': '100'}   # {}
        
        self.recipe_list.append(떡볶이)

        카레 = Recipe('카레')
        카레.ingrediant = {'카레가루': '150', '감자': '100', '당근': '100'}

        self.recipe_list.append(카레)
        
        파스타 = Recipe('파스타')
        파스타.contents = '맛있게 만드세요!'
        파스타.ingrediant = {'면': '100', '소스': '200'}

        self.recipe_list.append(파스타)

    def __str__(self):
        pass