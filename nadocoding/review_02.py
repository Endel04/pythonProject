# # 1)
# def n_sum(n):
#     n = str(n)
#     # 123 // 100 : 1
#     # 123 // 10 : 2
#     # 123 // 1 : 3
#
# result = n_sum(10)
# print(result)   #1
# result = n_sum(331)
# print(result)   #7
# result = n_sum(408)
# print(result)   #12
# result = n_sum(1000000000)
# print(result)   #-1

# 문제 2번
def get_subway_fare(km):
    if km < 10:
        return 720
    elif 10 <= km <50:
        result = (int((km-10)/5))*100+720
        return result
    elif 50 < km:
        result = ((int((km-50)/8)+1)*100) + (int(40/5*100)) + 720
        return result

fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(61)
print(fare)

# 문제 3번
print(" ")
def get_three_six_nine(i):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
        return "짝" * cnt
    else:
        return i

result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)