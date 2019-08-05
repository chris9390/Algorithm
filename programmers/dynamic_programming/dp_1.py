def solution(N, number):
    candidates = [[N]]

    for i in range(2, 9):
        lst = [int(str(N) * i)]

        for x_idx, j in enumerate(candidates):
            for x in j:

                # 중복되는 계산을 피하기 위한 탈출 조건
                if x_idx >= (len(candidates)+1) // 2:
                    break

                k = i - x_idx - 2
                for y in candidates[k]:

                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0:
                        lst.append(y // x)
                    if y != 0:
                        lst.append(x // y)

        candidates.append(lst)

        if number in set(lst):
            return i

    return -1

N = 5
number = 12
answer = solution(N, number)
print(answer)