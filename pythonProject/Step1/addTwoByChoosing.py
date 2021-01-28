from itertools import permutations

def solution(numbers):
    answer = set([])
    result = list(permutations(numbers, 2))
    for arr in result:
        answer.add(sum(arr))

    return sorted(list(answer))