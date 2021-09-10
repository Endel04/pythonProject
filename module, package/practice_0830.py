import math, random, datetime

# 1)
# 핸드폰 요금이 62421원이 나왔다. 100원 미만은 절사한다고 했을 때 62400원 청구.
# 59827원일 경우, 실제 청구 금액은?

price = 59827
print('1번 문제 : ', price - price % 100)

print()

# 2)
# 평가 계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나와서 90점 부여.
# 56점은 몇 점을 부여할까?

score = 56
print('2번 문제 : ', math.floor(score * 0.1) * 10)

print()

# 3)
# 로또 복권 자동 생성기를 만든다면? (로또 복권 : 1~45 사이의 번호 중 랜덤으로 6개 뽑기)

number = random.sample(range(1, 45), 6)
print('3번 문제 : ', number)

print()

# 4)
# 1~9 숫자 중 중복되지 않은 숫자 세자리를 뽑는 방법은? (185 : o, 212 : x)

number = random.sample(range(1, 9), 3)
# print('4번 문제 : ', number[0]*100 + number[1]*10 + number[2])
print('4번 문제 : ', str(number[0]) + str(number[1]) + str(number[2]))

print()

# 5)
# 내가 태어난 날로부터 며칠이 지났을까?

now = datetime.datetime.now()
birthday = datetime.datetime(2004, 5, 18)
print('5번 문제 : ', now - birthday)   # 2021.08.30 기준 6313일

print()

# 6)
# 올해 크리스마스까지 며칠이 남았을까?

now = datetime.datetime.now()
christmas = datetime.datetime(2021, 12, 25)
print('6번 문제 : ', christmas - now)  # 2021.8.30 기준 116일

print()

# 7)
# 내 생일이 며칠 남았을까?

now = datetime.datetime.now()
birthday = datetime.datetime(2022, 5, 18)
print('7번 문제 : ', birthday - now)   # 2021.8.30 기준 260일

print()

# 8)
# 랜덤하게 번호로 자리를 배치하는 방법은?

x = int(4)
y = int(5)

print('↓ 8번 문제 ↓')
print()

c = [int(a) for a in range(1, x*y+1)]
for i in range(y):
    for j in range(x):
        d = random.choice(c)
        if len(str(d)) == 1:
            print("0" + str(d), end=" ")
        else:
            print(str(d), end=" ")
        c.remove(d)
    print("")

print()

# 제적(전출, 자퇴) 인원이 있다면?

x = int(4)
y = int(5)

print('↓ 8-a번 문제 ↓')
print()

c = [int(a) for a in range(1, x*y+1)]
for i in range(y):
    for j in range(x):
        d = random.choice(c)
        if len(str(d)) == 1:
            print("0" + str(d), end=" ")
        else:
            print(str(d), end=" ")
        c.remove(d)
    print("")