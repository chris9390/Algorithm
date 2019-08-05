# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

cnt = 0

def f(a, i, j, sum, target, left, right):

    global cnt

    # 왼쪽으로 가면 -
    if left == 1:
        sum += a[i][j]
    # 오른쪽으로 가면 +
    elif right == 1:
        sum -= a[i][j]

    # 트리의 끝까지 도착하면 탈출
    if i == len(a)-1:
        if sum == target:
            cnt += 1
        return


    f(a, i+1, j * 2, sum, target, 1, 0)
    f(a, i+1, j * 2 + 1, sum, target, 0, 1)



def solution(numbers, target):

    a = [[0]]

    for idx, i in enumerate(numbers):
        a.append([i] * pow(2,(idx+1)))

    sum = 0
    f(a, 0, 0, sum, target, 0, 0)

    return cnt




numbers = [1, 1, 1, 1, 1]
target = 3

answer = solution(numbers, target)
print(answer)


# 또 다른 풀이
'''
import copy

cnt = 0

def dfs(numbers, target, idx):
    global cnt

    if idx == len(numbers):
        if sum(numbers) == target:
            cnt += 1
            return
        return

    # deepcopy를 하지 않으면 기다리던 dfs 함수 안의 numbers 배열이 모두 변해버린다.
    temp = copy.deepcopy(numbers)
    temp[idx] *= 1
    #numbers[idx] *= 1
    dfs(temp, target, idx+1)
    print(temp)

    temp = copy.deepcopy(numbers)
    temp[idx] *= -1
    #numbers[idx] *= -1
    dfs(temp, target, idx+1)
    print(temp)

def solution(numbers, target):

    dfs(numbers, target, 0)
    return cnt


numbers = [1,2,3]
target = -6

answer = solution(numbers, target)
print(answer)
'''