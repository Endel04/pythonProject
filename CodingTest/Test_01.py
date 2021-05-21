# 1)
# def solution(price, grade): # price : 원가, grade : 회원등급
#     sale_price = 0
#     if grade == "S":
#         sale_price = price * 0.05
#     elif grade == "G":
#         sale_price = price * 0.1
#     elif grade == "V":
#         sale_price = price * 0.15
#     return price - sale_price
#
# result = solution(2500, "V")
# print(result) # 2125
# result = solution(5000, "S")
# print(result) # 4750


# 2)
# def solution(month, day):
#     month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     total = 0
#     for i in range(month-1):
#         total += month_list[i]
#     total +=
#     return total - 1

# 3)
# arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
# count = [0] * 4
#
# for x in arr:
#     count[x] += 1
#
# print(f'1의 개수 : {count[1]}')
# print(f'2의 개수 : {count[2]}')
# print(f'3의 개수 : {count[3]}')
#
# counter = [0, 2, 3, 5]
#
# def get_maximum(arr):
#     maximum = 0
#     for x in arr:
#         if x > maximum:
#             maximum = x
#         return maximum
#
# def get_minimum(arr):
#     value = 0
#     for x in arr:
#         if x < value and x != 0:
#             value = x
#         minimum = value
#     return value
#
# a = get_minimum(counter)
# print(a)

# 4)
# def solution(arr):
#     left = 0
#     right = len(arr) - 1
#
#     # todo : @@@ 빈칸 채우기
#     while left < len(arr)/2:
#         # arr[left]와 arr[right]의 값을 서로 바꿈
#         arr[left], arr[right] = arr[right], arr[left]
#
#         left += 1
#         right -= 1
#     return arr
#
# # The following is code to output testcase.
# arr = [1, 4, 2, 3]
# ret = solution(arr)
#
# # Press Run button to receive output.
# print("Solution: return value of the function is ", ret, ".")


# 5)
# 숫자를 입력하고 입력받은 숫자가 몇 번 박수를 치는지 알아보자

# 방법1 : 사람이 생각하는 방법
a = 31
문자열 = str(a)

count = 0
while a:
    if a % 10 in [3, 6, 9]:
        count += 1
    a = a // 10

print(count)

# 6)
# def solution(scores):
#     count = 0
#     for s in scores:
#         if 650 <= s < 800:
#             count += 1
#     return count
#
# # The following is code to output testcase. The code below is correct and you shall correct solution function.
# scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
# ret = solution(scores)
#
# # Press Run button to receive output.
# print("Solution: return value of the function is", ret, ".")

# 7)
# def solution(sentence):
#     str = ''
#     for c in sentence:
#         if c != '.' and c != ' ':
#             str += c
#     size = len(str)
#     for i in range(size // 2):
#         if str[i] != str[size - 1 - i]:
#             return False
#     return True
#
# # The following is code to output testcase. The code below is correct and you shall correct solution function.
# sentence1 = "never odd or even."
# ret1 = solution(sentence1)
#
# # Press Run button to receive output.
# print("Solution: return value of the function is", ret, ".")