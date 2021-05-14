def solution(price, grade):
    if 100 <= price <= 100000:
        if grade == "S":
            sale_price = price - price * 0.15
            return sale_price
        elif grade == "G":
            sale_price = price - price * 0.1
            return sale_price
        elif grade == "V":
            sale_price = price - price * 0.05
            return sale_price
        else:
            return "올바른 회원 등급을 입력해주세요"
    else:
        return "100 이상 100,000 이하의 가격을 입력해주세요"

result = solution(5200, "G")
print(result) # 4680.0
result = solution(2500, "S")
print(result) #2125
result = solution(96900, "V")
print(result) #92055