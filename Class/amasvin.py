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
        super().__init__(self, name, price)
        self.pearl = 0

    def __str__(self):
        pass

# 사랑이 = Drink('밀크티', 2800)
# 사랑이.order()
# print(사랑이)

사랑이 = Coffee('카페모카', 3000)
사랑이.order()
print(사랑이)

사랑이 = Bubbletea('오레오쉐이크', 3900)
사랑이.order()
print(사랑이)