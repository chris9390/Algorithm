def solution(brown, red):

    # red 가 1인 경우, brown이 둘러싸면 [3,3] 일 수 밖에 없다.
    if red == 1:
        return [3,3]

    for i in range(1, red // 2 + 1):

        # i 가 red 의 약수이면
        if red % i == 0:
            r_height = i
            r_width = red // i

            if 2 * (r_height + r_width) + 4 == brown:
                return [r_width + 2, r_height + 2]



brown = 24
red = 24
answer = solution(brown, red)
print(answer)