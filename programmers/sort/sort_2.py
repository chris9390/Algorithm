from functools import cmp_to_key

def compare(a, b):
    if a+b < b+a:
        return 1
    elif a+b > b+a:
        return -1
    else:
        return 0


def solution(numbers):

    numbers = list(map(str, numbers))

    a = sorted(numbers, key=cmp_to_key(compare))

    answer = ''.join(a)

    if int(answer) == 0:
        return '0'

    return answer

numbers = [6, 10, 2]
answer = solution(numbers)
print(answer)