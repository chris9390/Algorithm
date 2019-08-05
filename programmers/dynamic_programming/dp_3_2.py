def tri(triangle, i, j, memo):
    if len(triangle) - 1 == i:
        return triangle[i][j]

    if (i, j) in memo:
        return memo[(i, j)]

    a = tri(triangle, i + 1, j, memo)
    b = tri(triangle, i + 1, j + 1, memo)
    hap = max(a, b) + triangle[i][j]

    memo[(i, j)] = hap

    return hap


def solution(triangle):
    answer = 0
    i = 0
    j = 0

    # memo 는 dictionary
    memo = {}
    answer = tri(triangle, i, j, memo)

    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
answer = solution(triangle)
print(answer)