class GooDS:
    def __init__(self, name):
        # 상품 사진
        self.image = []

        # 상품 이름
        self.name = name

        # 카테고리
        self.category = ''

        # 판매자 거주 지역
        self.area = ''

        # 상품 상태 (1. 중고상품 2. 새상품)
        self.state = ''

        # 교환 (1. 교환불가 2. 교환가능)
        self.exchange = ''

        # 가격
        self.price = 0

        # 상품 설명
        self.explain = ''

        # 태그
        self.tag = []
        
        # 찜(좋아요)
        self.favor = 0

    def set_image(self):
        image = input('상품의 이미지를 삽입하세요 : ')

        self.image = '삽입된 이미지가 없습니다' if image == '' else image

    def set_category(self):
        category = input('상품의 카테고리를 선택하세요 : ')

        self.category = '상품의 카테고리를 선택해주세요' if category == '' else category

    def set_area(self):
        area = input('판매자의 거주지를 입력하세요 : ')

        self.area = '판매자의 거주지를 입력해주세요' if area == '' else area

    def set_state(self):
        state = input('상품의 상태를 입력하세요 (1. 중고상품 2. 새상품) : ' )

        self.state = '상품의 상태를 입력해주세요' if state == '' else state

    def set_exchange(self):
        exchange = input('상품의 교환 가능 여부를 입력하세요 (1. 교환불가 2. 교환가능) : ')

        self.exchange = '상품의 교환 가능 여부를 입력해주세요' if exchange == '' else exchange

    def set_price(self):
        price = input('상품의 가격을 입력하세요 : ')

        self.price = '가격을 설정해주세요' if price == '' else price

    def set_explain(self):
        explain = input('상품의 설명을 입력하세요 : ')

        self.explain = '상품의 설명을 입력해주세요' if explain == '' else explain

    def set_tag(self):
        tag = input('상품의 태그를 입력하세요 : ')

        self.tag = '상품의 태그를 입력해주세요' if tag == '' else tag

    def set_product(self):
        self.set_image()
        self.set_category()
        self.set_area()
        self.set_state()
        self.set_exchange()
        self.set_price()
        self.set_explain()
        self.set_tag()

    def __str__(self):
        return f'이름 : {self.name}\n이미지 : {self.image}\n카테고리 : {self.category}\n판매자 거주 지역 : {self.area}\n상태 : {self.state}\n교환 : {self.exchange}\n가격 : {self.price}\n설명 : {self.explain}\n태그 : {self.tag}\n찜 : {self.favor}'