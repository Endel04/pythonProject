import math, random, datetime

# 1)
# 핸드폰 요금이 62421원이 나왔다. 100원 미만은 절사한다고 했을 때 62400원 청구.
# 59827원일 경우, 실제 청구 금액은?

bill = 62421
bill = 59827
print(bill//100*100)
print(bill - bill % 100)
print(math.floor(bill/100)*100)
print(int(bill/100)*100)

print()

# 2)
# 평가 계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나와서 90점 부여.
# 56점은 몇 점을 부여할까?

score = 93
print(round(score/10)*10)
print(round(score, -1))
print(math.floor(score * 0.1) * 10)

print()

# 3)
# 로또 복권 자동 생성기를 만든다면? (로또 복권 : 1~45 사이의 번호 중 랜덤으로 6개 뽑기)

print(random.sample(range(1, 45 + 1), 6))

print()

# 4)
# 1~9 숫자 중 중복되지 않은 숫자 세자리를 뽑는 방법은? (185 : o, 212 : x)

number = random.sample(range(1, 9 + 1), 3)
print(number[0] * 100 + number[1] * 10 + number[2])
print(str(number[0]) + str(number[1]) + str(number[2]))
print("".join(str(num) for num in number))
print("".join(map(str, number)))

print()

# 5)
# 내가 태어난 날로부터 며칠이 지났을까?

birthday = datetime.datetime(2004, 5, 18)
now = datetime.datetime.now()
print(now - birthday)

print()

# 6)
# 올해 크리스마스까지 며칠이 남았을까?

christmas = datetime.datetime(2021, 12, 25)
now = datetime.datetime.now()
print(christmas - now)

print()

# 7)
# 내 생일이 며칠 남았을까?

my_birthday = datetime.datetime(2022, 5, 18)
now = datetime.datetime.now()

if my_birthday < now:
    my_birthday = my_birthday.replace(year=2022)

print(my_birthday - now)

print()

# 8)
# 랜덤하게 번호로 자리를 배치하는 방법은?

# 마지막 번호 묻기
last_number = input('마지막 번호를 입력해주세요 : ')

# 1에서 마지막 번호까지 숫자 리스트 만들기
list_class = list(range(1, int(last_number) + 1))
print(list_class)

# 반복
while True:
    # 빼야 할 번호 묻기
    exclude_number = input('뺄 번호를 입력하세요 (Enter | 종료) : ')

    # 뺐으면 반복 끝내기
    if exclude_number == '':
        break

    # 번호 빼기
    list_class.remove(int(exclude_number))
    print(list_class)

# 섞기
random.shuffle(list_class)

# 출력하기
print('자리\t학생 번호')
for i, num in enumerate(list_class):
    print(f'{i+1}\t{num}')

print()