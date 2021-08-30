# 3-1)

# id_number = "040518"
#
# print(id_number[0:2]) # print(id_number[:2])
# print(id_number[2:6])
# print(int(id_number[0:2]) * int(id_number[2:6]))

# 3-2)
# phone_number01 = "02-305-0518"
#
# print(phone_number01[:2])
# print(phone_number01[-4:])
#
# phone_number02 = "032-305-0518"
#
# print(phone_number02[:3])
# print(phone_number02[-4:])



# 2-1)
# 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'

# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

# student_number = "2800"
# major = int(student_number[1:2])
#
# if major < 0 and major >= 7:
#     print("잘못 입력했습니다.")
# else:
#     if major == 1 and major == 2:
#         print(major + "반 뉴미디어소프트웨어과")
#     elif major == 3 and major == 4:
#         print(major + "반 뉴미디어웹솔루션과")
#     elif major == 5 and major == 6:
#         print(major + "반 뉴미디어디자인과")

# 2-2)
# 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기

# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2

# def get_major(major, grade):
#
# grade, major = get_major('2100')
# print(major, grade)

# 2-3)
# 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기

# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

# def average(n1, n2, n3, n4, n5):
#
#
# print(average(10, 20, 30))
# print(average(4, 23))

# 2-4)
# 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만

# bmi = get_bmi(176, 69)
# print(bmi) #22.3

# def get_bmi(height, weight):
#     height = height * 0.01
#
#     bmi = round(weight / (height * height), 1)
#
#     print(bmi)
#
#    if bmi < 18.5:
#        print("저체중입니다.")
#    elif 18.5 <= bmi < 23.0:
#        print("보통입니다.")
#    elif 23.0 <= bmi < 25.0:
#        print("과제충입니다.")
#    elif bmi >= 25:
#        print("비만입니다.")
#
# bmi = get_bmi(176, 69)

# 3-1)
'''n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면,
각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''

# def n_sum(num):
#     num = str(num)
#     sum = 0
#
#     if len(num) >= 10:
#         return -1
#
#     for digit in num:       #num: '408' digit: '4' '0' '8'
#         sum = sum + int(digit)
#     return sum
#
# result = n_sum(10)
# print(result)   #1
# result = n_sum(331)
# print(result)   #7
# result = n_sum(408)
# print(result)   #12
# result = n_sum(1000000000)
# print(result)   #-1

print()

# 3-2)
'''
get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.

* 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''

# def get_subway_fare(km):
#     if km < 10:
#         return 720
#     elif 10 <= km <= 50:
#         rkm = int(km-10)
#         #result = (int((km-10)/5)+1)*100+720
#         if rkm % 5 == 0:
#             result = (rkm//5) * 100 + 720
#         else:
#             result = ((rkm//5) + 1) * 100 + 720
#         return result
#     elif 50 < km:
#         rkm = int(km-50)
#         if rkm % 8 == 0:
#             result = (rkm // 8) * 100 + (int(40/5*100)) + 720
#         else:
#             result = ((rkm // 8) + 1) * 100 + (int(40/5*100)) + 720
#         #result = (int((km-50)/8)*100) + (int(40/5*100)) + 720
#         return result
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(20)
# print(fare)        #920
# fare = get_subway_fare(27)
# print(fare)        #1120
# fare = get_subway_fare(57)
# print(fare)         #1620
# fare = get_subway_fare(58)
# print(fare)         #1620
# fare = get_subway_fare(59)
# print(fare)         #1720
# fare = get_subway_fare(67)
# print(fare)         #1820

print()

# 3-3)
'''
get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
* 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''

# def get_three_six_nine(i):
#     # if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#     cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
#     if cnt == 0:
#         return i
#     else :
#         return "짝" * cnt
#     # else:
#     #     return i
#
# result = get_three_six_nine(1)
# print(result)   #1
# result = get_three_six_nine(3)
# print(result)   #짝
# result = get_three_six_nine(16)
# print(result)   #짝
# result = get_three_six_nine(31)
# print(result)   #짝
# result = get_three_six_nine(36)
# print(result)   #짝짝

print()

# 3-4)
'''
get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result)  # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result)  # 으무!
'''

# def get_compliment(word):
#     if '고구마' in word:
#         return "왓쇼이!"
#     elif '맛있는' in word:
#         return "우마이!"
#     elif '놀랄 만한' in word:
#         return "요모야..!"
#     elif '황당한' in word:
#         return "요모야..!"
#     else:
#         return "으무! " + word
#
# result = get_compliment('고구마 밥')
# print(result)  # 왓쇼이!
# result = get_compliment('맛있는 라멘')
# print(result)  # 우마이!
# result = get_compliment('황당한 일')
# print(result)  # 요모야..!
# result = get_compliment('재밌구나!')
# print(result)  # 으무!

print()

# 4-1)
# 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.

# def is_prime(num):
#     if num < 2:
#         return "소수 아님"
#     elif num == 2:
#         return "소수"
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 return "소수 아님"
#             return "소수"
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님

print()

# 4-2)
# def get_compliment(word):
#     if '고구마' in word:
#         return "왓쇼이!"
#     elif '맛있는' in word:
#         return "우마이!"
#     elif '놀랄 만한' in word:
#         return "요모야..!"
#     elif '황당한' in word:
#         return "요모야..!"
#     else:
#         return "으무!"
#
# result = get_compliment('고구마 밥')
# print(result)  # 왓쇼이!
# result = get_compliment('맛있는 라멘')
# print(result)  # 우마이!
# result = get_compliment('황당한 일')
# print(result)  # 요모야..!
# result = get_compliment('재밌구나!')
# print(result)  # 으무!

print()

'''
Quiz5-1. 모듈이란?

함수나 변수 또는 클래스 들을 모아 놓은 파일

Quiz5-2. 패키지란?   

모듈을 디렉토리 형식으로 구조화 한 것

Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요

import theater_module as p학번
p학번.price(1)

Quiz5-4. __all__의 역할은?

해당 디렉토리에서 import * 할 경우 이곳에 정의된 모듈만 import 된다

Quiz5-5. 지금 파이썬 파일을 직접 실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?

if __name__ == "__main__"

Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
< 가 > 

trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()

from travel import vietnam
< 나 > 

trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel.vietnam import VietnamPackage
< 다 > 

trip_to = VietnamPackage()
trip_to.detail()

'''