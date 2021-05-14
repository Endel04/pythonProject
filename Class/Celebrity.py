class Celebrity:
    def __init__(self, name):
        # 이름
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    # def info(self):
    #     print(f'이름 : {self.name}\t소속사 : {self.entertainment}')

    def __str__(self):
        return f'이름 : {self.name}\t소속사 : {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)  # Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마 : {self.drama}'

class Singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)  # self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t노래 : {self.song}'

IU = Celebrity('IU')    # new Celebrity() in java
# IU.set_name('이지은')
IU.set_entertainment('이담')
# IU.info()
# print(IU.name, IU.entertainment)
print(IU)   # 클래스의 __str__() 호출

남주혁 = Celebrity('남주혁')
# 남주혁.set_name('남주혁')
남주혁.set_entertainment('숲')
# 남주혁.info()
# print(남주혁.name, 남주혁.entertainment)
print(남주혁)

이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)

태현 = Singer('태현', 'Your Light')
태현.set_entertainment('하이브')
print(태현)

연준 = Singer('연준', 'Wishlist')
연준.set_entertainment('하이브')
print(연준)

투모로우바이투게더 = []
투모로우바이투게더.append(태현)
투모로우바이투게더.append(연준)
# print(투모로우바이투게더)

for member in 투모로우바이투게더:    # member : 태현의 객체, 연준의 객체
    print(member)

# for member in range(len(투모로우바이투게더)):    # member : 0, 1
#     print(투모로우바이투게더[member])