class Recipe:
    def __init__(self, name):
        # 이름
        self.name = name

        # 내용
        self.contents = ''

        # 재료, 재료의 개수
        self.ingrediant = {}

        # 몇 인분
        self.people = 1

        # 영상 링크
        self.video = ''

    def set_contents(self):
        contents = input('레시피 내용을 입력하세요 : ')

        self.contents = '입력된 정보가 없습니다' if contents == '' else contents

    def set_people(self):
        people = input('몇 인분인지 입력하세요 : ')

        self.people = '1' if people == '' else people

    def set_video(self):
        video = input('레시피 영상 링크를 입력하세요 : ')

        self.video = '입력된 정보가 없습니다' if video == '' else video

    def set_ingrediant(self):
        while True:
            print('재료 입력이 끝나면 엔터를 누르세요.')
            ingrediant = input('재료를 입력하세요 : ')  # 입력 예시 : 감자 100

            if ingrediant == '':
                break

            ingrediant_name, ingrediant_gram = ingrediant.split()
            # 감자 200 split() -> '감자', '200'
            # 지함 = 지함이는 귀엽다 split() -> '지함이는', '귀엽다'

            self.ingrediant[ingrediant_name] = ingrediant_gram
            # '감자' : '100', '고구마' : '100'

    def __str__(self):
        return f'레시피 : {self.name}\n양 : {self.people}인분\n정보 : {self.contents}\n영상 링크 : {self.video}\n재료 : {self.ingrediant}'

    def set_recipe(self):
        self.set_contents()
        self.set_people()
        self.set_video()
        self.set_ingrediant()

# 카레 = Recipe('카레')
# 카레.set_recipe()
# print(카레)