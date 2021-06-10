from GooDS import GooDS

class GooDSlist:
    def __init__(self):
        self.GooDS_list = []

    def add_product(self):
        # 판매할 상품 이미지 삽입
        image = input('상품 이미지를 삽입하세요 : ')
        new_image = GooDS(image)
        
        # 판매할 상품명 입력
        name = input('상품 이름을 입력하세요 : ')
        new_product = GooDS(name)

        # 판매할 상품 카테고리 선택
        category = input('상품의 카테고리를 선택하세요 : ')
        new_category = GooDS(category)

        # 판매자가 살고 있는 지역 입력
        area = input('판매자의 거주지를 입력하세요 : ')
        new_area = GooDS(area)

        # 판매할 상품의 상태 선택
        state = input('상품의 상태를 선택하세요 : ')
        new_state = GooDS(state)

        # 판매할 상품 교환 가능, 불가능 선택
        exchange = input('상품의 상태를 선택하세요 : ')
        new_exchange = GooDS(exchange)

        # 판매할 상품의 가격 입력
        price = input('상품의 상태를 선택하세요 : ')
        new_price = GooDS(price)

        # 판매할 상품 설명 입력
        explain = input('상품의 상태를 선택하세요 : ')
        new_explain = GooDS(explain)

        # 판매할 상품 태그 입력
        tag = input('상품의 상태를 선택하세요 : ')
        new_tag = GooDS(tag)

    def set_product(self):
        self.add_product()

    def search_product(self):
        # 찾은 상품
        searched_product = []

        # 상품 이름 입력받기
        name = input('상품이 이름을 입력하세요 : ')

        # 상품의 이름이 검색한 이름과 같은지 확인
        for product in self.GooDS_list:
            if name = product.name:
                print(product)
                searched_product.append(product)

    def __str__(self):
        pass