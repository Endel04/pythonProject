# 1)

letters = 'python'
print(letters[0] + " " + letters[2])

# 2)

license_plate = "24가 2210"
print(license_plate[-4:])

# 3)

phone_number = '010-1111-2222'

# 문자열을 다 찾은 다음 '-'를 ''로 대체
phone_number = phone_number.replace('-', ' ')
print(phone_number)

# result = ''
#
# for x in phone_number:
#     if x == '-':
#         result += x
#     else:
#         result += ' '
#
# print(result)

# 4)

url = "http://sharebook.kr"
print(url[-2:])

# 5)

t1 = 'python'
t2 = 'java'

print((t1 + ' ' + t2 + ' ') * 4)

# 6)

상장주식수 = '5,969,782,550'
a = 상장주식수.replace(',', ' ')
print(int(a))

# 7)

ticker = "btc_krw"
ticker = ticker.replace('_', ' ')
print(ticker)