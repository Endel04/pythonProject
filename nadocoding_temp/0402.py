# 3-2)
phone_number1 = '010-2540-5357'
phone_number2 = '010 7584 1367'
phone_number3 = '01073201685'

phone_number = phone_number1

result = phone_number.replace('-', '').replace(' ', '')
print(result)

# 2-1)
student_number = '2400'
n = int(student_number[1])

majors = ['소프트과', '소프트과', '웹솔과', '웹솔과', '디자인과', '디자인과']

if 1 <= n <= 6:
    print(f"{n}반 {majors[n-1]}")
else:
    print("잘못 입력했습니다.")

# 2-2)
def get_major(student_number):
    majors = ['소', '소', '솔', '솔', '디', '디']
    grade = student_number[0]
    classroom = int(student_number[1])
    return grade, majors[classroom-1]

grade, major = get_major('2100')
print(major, grade)

# 2-3)
def average(*numbers):
    cnt = 0
    sum_value = 0
    for number in numbers:
        sum_value += number
        cnt += 1
    return sum_value/cnt
#   return sum(numbers)/len(numbers)

print(average(10, 20, 30))
print(average(4, 23))

# 2-4)
def get_bmi(height, weight):
    height = height * 0.01

    bmi = weight / height ** 2

    return round(bmi, 1)

bmi = get_bmi(170, 58)
print(bmi)

if bmi < 18.5:
    print("저체중입니다.")
elif 18.5 <= bmi < 23.0:
    print("정상입니다.")
elif 23.0 <= bmi < 25.0:
    print("과제충입니다.")
elif bmi >= 25:
    print("비만입니다.")