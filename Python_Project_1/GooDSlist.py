from GooDS import GooDS

class GooDSlist:
    def __init__(self):
        self.GooDS_list = []
        self.init_product()

    def add_product(self):
        # 추가할 상품 이름 입력
        name = input('상품의 이름을 입력하세요 : ')

        # 상품 추가
        new_product = GooDS(name)
        new_product.set_product()

        # 굿즈 리스트에 생성한 상품 추가하기
        self.GooDS_list.append(new_product)

    def show_product(self):
        # 모든 상품 보여주기
        for index, product in enumerate(self.GooDS_list):
            print(f'{index + 1}')
            print(product)

    def search_product(self):
        # 찾은 상품
        searched_product = []

        # 상품 이름 입력받기
        name = input('상품의 이름을 입력하세요 : ')

        # 상품의 이름이 검색한 이름과 같은지 확인
        for product in self.GooDS_list:
            if name == product.name:  # 같으면 상품 보여주기
                searched_product.append(product)
                print(product)

        if len(searched_product) == 0:   # 검색한 상품이 없으면
            # 상품 추가할지 물어보기
            answer = input('찾으시는 상품이 없습니다. 상품을 추가하시겠습니까? (1 : yes, 1 이외의 숫자 : no) : ')

            if answer == '1':   # 1을 입력했을 때
                # 상품 추가하기
                self.set_product()
            else:   # 1이 아닌 다른 숫자를 입력했을 때
                return

    def set_product(self):
        self.add_product()

    def show_popular(self):
        popular_list = []

        GooDS_list = sorted(self.GooDS_list, key=lambda product:product.favor, reverse=True)

        for index, product in enumerate(GooDS_list[:3]):
            popular_list.append(product)
            print(f'{index + 1}')
            print(product)

    def init_product(self):
        스티커 = GooDS('스티커')
        스티커.image = 'sticker_01.jpg'   # []
        스티커.category = '스티커'   # ''
        스티커.area = '서울특별시 은평구 증산동'   # ''
        스티커.state = '새상품'   # ''
        스티커.exchange = '교환불가'   # ''
        스티커.price = 3000   # 0
        스티커.explain = '그냥 사가주세요 제발'   # ''
        스티커.tag = '#귀멸의칼날', '#스티커'   # []
        스티커.favor = 8   # 0

        self.GooDS_list.append(스티커)
        
        도무송 = GooDS('도무송')
        도무송.image = 'sticker_02.jpg'
        도무송.category = '스티커'
        도무송.area = '서울특별시 은평구 갈현동'
        도무송.state = '새상품'
        도무송.exchange = '교환불가'
        도무송.price = 1000
        도무송.explain = '도무송 1set : 1000원'
        도무송.tag = '#귀멸의칼날', '#도무송'
        도무송.favor = 14

        self.GooDS_list.append(도무송)

        포스터 = GooDS('포스터')
        포스터.image = 'poster_01.jpg'
        포스터.category = '포스터'
        포스터.area = '서울특별시 관악구 신림동'
        포스터.state = '중고상품'
        포스터.exchange = '교환불가'
        포스터.price = 12000
        포스터.explain = '무한열차 포스터 장당 12000원에 팔아요'
        포스터.tag = '#귀멸의칼날', '#무한열차', '#포스터', '#렌고쿠'
        포스터.favor = 19

        self.GooDS_list.append(포스터)  

        도장 = GooDS('도장')
        도장.image = 'stamp_01.jpg'
        도장.category = '도장'
        도장.area = '서울특별시 서대문구 북가좌동'
        도장.state = '새상품'
        도장.exchange = '교환불가'
        도장.price = 6000
        도장.explain = 'ㅇㅇ님 도장 6000원에 판매합니다'
        도장.tag = '#귀멸의칼날', '#도장', '#비공굿'
        도장.favor = 28

        self.GooDS_list.append(도장)

        포카 = GooDS('포카')
        포카.image = 'photocard_01.jpg'
        포카.category = '포토카드'
        포카.area = '서울특별시 용산구 한강로동'
        포카.state = '중고상품'
        포카.exchange = '교환불가'
        포카.price = 800
        포카.explain = '포토카드 장당 800원'
        포카.tag = '#귀멸의칼날', '#포토카드'
        포카.favor = 24

        self.GooDS_list.append(포카)

    def __str__(self):
        pass