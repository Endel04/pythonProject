class Drink:
    _CUPS = ('레귤러', '점보')   # 레귤러
    _ICES = ('0%', '50%', '100%', '150%')   # 100%
    _SUGARS = ('0%', '50%', '100%', '150%') # 100%

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0    # 레귤러   Drink._CUPS[self.cup]
        self.ice = 2    # 100%    Drink._ICES[self.ice]
        self.sugar = 2  # 100%    Drink._SUGARS[self.sugar]

    def set_cup(self):
        # 컵 종류 보여주기
        for index, cup in enumerate(Drink._CUPS):
            print(f'{index + 1}: {cup}')
            
        # 컵 선택하기
        cup = input('컵사이즈를 선택하세요 : ')

        # 컵 self에 넣기
        if cup == '':
            self.cup = 0
        else:
            self.cup = int(cup) - 1

        if self.cup == 1:   # 점보일 때 +500원
            self.price += 500


    def set_ice(self):
        # 얼음량 보여주기
        for index, ice in enumerate(Drink._ICES):
            print(f'{index + 1} : {ice}')

        # 얼음량 선택하기
        ice = input('얼음량을 선택하세요 : ')

        # if ice == '':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1

        self.ice = 2 if ice == '' else int(ice) - 1

        # self.ice 설정하기

    def set_sugar(self):
        # 당도 보여주기
        for index, sugar in enumerate(Drink._SUGARS):
            print(f'{index + 1} : {sugar}')

        # 당도 선택하기
        sugar = input('설탕량을 선택하세요 : ')

        # if sugar == '':
        #     self.sugar = 2
        # else:
        #     self.sugar = int(sugar) - 1

        self.sugar = 2 if sugar == '' else int(sugar) - 1

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'이름 : {self.name}\t가격 : {self.price}원\t컵사이즈 : {Drink._CUPS[self.cup]}\t얼음량 : {Drink._ICES[self.ice]}\t당도 : {Drink._SUGARS[self.sugar]}'


class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _PEARLS = ('타피오카', '화이트', '알로에', '젤리')
    
    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0

    def set_pearl(self):
        # 펄 종류 보여주기
        for index, pearl in enumerate(Bubbletea._PEARLS):
            print(f'{index + 1} : {pearl}')

        # 펄 선택하기
        pearl = input('펄의 종류를 선택하세요 : ')

        # self.pearl에 넣기
        self.pearl = 0 if pearl == '' else int(pearl) - 1

    def order(self):
        # 부모 클래스의 order() 호출하기
        super().order()

        # set_pearl() 호출하기
        self.set_pearl()

    def __str__(self):
        # 부모 클래스의 __str__() (이름, 가격, 컵사이즈, 얼음량, 당도), 펄
        result = super().__str__()
        return result + f'\t펄 종류 : {Bubbletea._PEARLS[self.pearl]}'

class Order:
    def __init__(self):
        # self.menu : 매장에 있는 음료수 전체
        self.menu = []

        # init.menu()
        self.init_menu()

        # self.order_menu : 내가 고른 메뉴
        self.order_menu = []

    def init_menu(self):
        사랑이 = Coffee('카페모카', 2500)
        나 = Bubbletea('오레오 쉐이크', 3900)
        에스더 = Bubbletea('타로 밀크티', 3300)
        
        self.menu.append(사랑이)
        self.menu.append(나)
        self.menu.append(에스더)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1} : {drink.name}\t{drink.price}원')

    def sum_price(self):
        # self.order_menu를 하나씩 꺼내 그 Drink의 가격의 합계를 리턴
        sum_value = 0

        for drink in self.order_menu:
            sum_value += drink.price
        return sum_value

    def order_drink(self):
        # 메뉴 보여주기
        while True:
            self.show_menu()

            # 메뉴 선택하기
            drink = input('메뉴를 선택하세요 : ')
            drink = int(drink) - 1
            new_drink = self.menu[drink]

            # 옵션 선택하기
            new_drink.order()

            # self.order_menu에 추가하기
            self.order_menu.append(new_drink)

            # 더 주문하시겠어요? (처음으로 돌아가서 반복)
            is_add = input('더 주문하시겠습니까? (n : 종료) : ')

            if is_add == 'n':
                break

        # 주문 내역 보여주기
        print(self)

    def __str__(self):
        # 주문 내역 보여주기
        s = '-' * 20 + '주문 내역' + '-' * 20 + '\n'

        # 주문한 음료 목록 보여주기
        for drink in self.order_menu:
            s += str(drink) + '\n'

        # 총 합계 가격 보여주기
        s += f'총 금액 : {self.sum_price()}원'

        return s

# 사랑이 = Drink('밀크티', 2800)
# 사랑이.order()
# print(사랑이)

# 사랑이 = Coffee('카페모카', 3000)
# 사랑이.order()
# print(사랑이)

# 사랑이 = Bubbletea('오레오 쉐이크', 3900)
# 사랑이.order()
# print(사랑이)

# 나 = Bubbletea('오레오 쉐이크', 3900)
# 나.order()
# print(나)

order = Order()
order.order_drink()