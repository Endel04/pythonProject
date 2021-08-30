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

def get_compliment(word):
    if '연어' in word:
        return 'しゃけ | 긍정, 동의, 답변'
    elif '가다랑어포' in word:
        return 'おかか | 부정, 항의, 저지'
    elif '명란젓' in word:
        return 'めんたいこ | 기합, 부름, 자신감'
    elif '참치마요' in word:
        return 'ツナマヨ | 제안, 대답, 찬동'
    elif '연어알' in word:
        return 'イクラ | 어이없음'
    elif '연어알젓' in word:
        return 'すじこ | 웃음, 의견, 기막힘'
    elif '다시마' in word:
        return 'コンブ | 거부, 응답, 인사, 위험'
    elif '갓나물' in word:
        return 'たかな | 괜찮아'
    elif '참치' in word:
        return 'ツナ | 불편, 호소'

result = get_compliment('연어 덮밥 먹으러 갈래?')
print(result)