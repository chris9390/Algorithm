# 예산
# https://programmers.co.kr/learn/courses/30/lessons/43237


def solution(budgets, M):

    # 예외처리 1
    # 각 도시의 예산 합이 M 보다 작은 경우
    if sum(budgets) <= M:
        return max(budgets)

    # 예외처리 2
    # 각 도시의 예산이 너무 큰 경우
    if min(budgets) * len(budgets) > M:
        return M // len(budgets)


    minimum = min(budgets)
    maximum = max(budgets)
    center = (minimum + maximum) // 2

    while(maximum - minimum > 1):
        total = 0
        for i in budgets:
            if i < center:
                total += i
            else:
                total += center

        if total > M:
            maximum = center
            center = (minimum + maximum) // 2
        else:
            minimum = center
            center = (minimum + maximum) // 2

    return center



budgets = [120, 110, 140, 150]
M = 485
answer = solution(budgets, M)
print(answer)