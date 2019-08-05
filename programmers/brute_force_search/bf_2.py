from itertools import permutations

'''
# 에라토스테네스의 체
n = 9999999
numbers = [False, False] + [True] * (n-1)
primes = []

for i in range(2, n+1):
    if numbers[i] == True:
        primes.append(i)
        for j in range(2 * i, n+1, i):
            numbers[j] = False
# primes에 소수 집합 저장..
'''

def is_prime(num):
    if num <= 1:
        return False

    if num == 2 or num == 3:
        return True

    for i in range(2, num //2 + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    temp = []
    num_list = list(numbers)

    for i in range(1, len(num_list) + 1):
        num_permuts = permutations(num_list, i)

        for j in num_permuts:
            joined_str = ''.join(j)
            joined_int = int(joined_str)
            if joined_int in temp:
                continue
            temp.append(joined_int)



    num_permuts = temp
    for i in num_permuts:
        if is_prime(i) == True:
            answer += 1
        '''
        if i in primes:
            answer += 1
        '''
    return answer


numbers = '011'
answers = solution(numbers)
print(answers)