def solution(numbers):
    answer_set = set()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer_set.add(numbers[i] + numbers[j])
    answer = list(answer_set)
    answer.sort()
    return answer

a1 = [2, 1, 3, 4, 1]
print(solution(a1))
a2 = [5, 0, 2, 7]
print(solution(a2))