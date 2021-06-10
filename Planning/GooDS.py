class GooDS:
    def __init__(self, image, name, state, price, exchange):
        # 상품 사진
        self.image = []

        # 상품 이름
        self.name = name

        # 카테고리
        self.category = []

        # 판매자 거주 지역
        self.area = {}

        # 상품 상태 (1. 중고상품 2. 새상품)
        self.state = state

        # 교환 (1. 교환불가 2. 교환가능)
        self.exchange = exchange

        # 가격
        self.price = price

        # 상품 설명
        self.explain = ''

        # 태그
        self.tag = {}
        
        # 찜(좋아요)
        self.favor = []

    def set_total(self):
        pass

    def set_popular(self):
        pass

    def __str__(self):
        pass