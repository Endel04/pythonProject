# for dan in range(2, 9 + 1):
#     for i in range(1, 9 + 1):
#         print(f'{dan} x {i} = {dan * i}')
#     print()
#
# for dan in range(2, 9 + 1):
#     for i in range(1, 9 + 1):
#         print(f'{dan} x {i} 8 {dan * i}')
#     print()
#     if dan == 7:
#         break
#
# for dan in range(2, 9 + 1):
#     for i in range(1, 9 + 1):
#         #   if i == 2 or i == 4 or i == 6 or i == 8:
#         if i % 2 == 0:
#             continue
#         print(f'{dan} x {i} 8 {dan * i}')
#     print()

def solution(num):
    cnt = 0



    for i in range(1, num + 1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            cnt += 1
        if i // 10 % 10 == 3 or i // 10 % 10 == 6 or i // 10 % 10 == 9:
            cnt += 1
        if i // 100 % 10 == 3 or i // 100 % 10 == 6 or i // 100 % 10 == 9:
            cnt += 1

    return cnt


number = 31
answer = solution(number)
print(answer)

# arr = 'abcdefg'
#
# print(arr[len(arr)])
# print(arr[3])
# print(arr[6])
# print(arr[0])
# print(arr[-1])