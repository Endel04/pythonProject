class Icecream:
    def __init__(self, name):   # 생성자 : 주로 변수 초기화
        self.name = name

    def set_explanation(self, explanation):
        self.explanation = explanation

    def __str__(self, name):    # 객체를 알아보기 쉽게 문자열로 리턴, 주로 print()에서 호출함
        return f'이름 : {self.name}'

아이스홈런볼 = Icecream('아이스홈런볼')
# 아이스홈런볼.set_explanation('초콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 쏙쏙!')

레인보우샤베트 = Icecream('레인보우샤베트')

블랙소르베 = Icecream('블랙소르베')

엄마는외계인 = Icecream('엄마는외계인')

class Order:
    _CATEGORIES = ('싱글레귤러', '더블레귤러', '파인트', '쿼터')
    _PRICES = (3200, 6200, 8200, 15000)

    def __init__(self):
        # 종류 : 콘, 파인트, ...
        self.set_cateries()
        
        # 메뉴
        self.menu = []
        self.init_menu()

        # 주문한 메뉴
        self.order_menu = []

    def __str__(self):
        pass

    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):
            print(index + 1, category)
        category_num = input('종류를 골라주세요 : ')
        self.category = int(category_num)

    def init_menu(self):
        self.menu.append(Icecream('레인보우샤베트'))
        self.menu.append(Icecream('블랙소르베'))
        self.menu.append(Icecream('엄마는외계인'))

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index + 1}. {icecream}')

    def order(self):
        self.show_menu()    # 아이스크림 보여주기

        for _ in range(self.category):  # 종류에 따라 반복함
            # 메뉴 선택
            icecream = input('아이스크림을 골라주세요 : ')
            icecream = int(icecream)

            # 주문한 메뉴에 추가
            self.order_menu.append(self.menu[icecream - 1])

        # 종류 출력하기
        print('-' * 10 + '주문 내역입니다' + '-' * 10)
        print(Order._CATEGORIES[self.category - 1])
        print(str(Order._PRICES[self.category - 1]) + '원')

        # 주문한 아이스크림 출력하기
        for icecream in self.order_menu:
            print(icecream)

order = Order()
order.order()
