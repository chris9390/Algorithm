def solution(baseball):
    answer = 0

    for i in range(123, 1000):

        # 비교할 대상 (정답 후보)
        a = list(str(i))
        a_set = set(list(map(int, a)))

        # flag 가 False가 되면 정답이 아니다.
        flag = True

        # 세 자리가 다 달라야한다.
        if len(a_set) != 3:
            continue

        # 0 이 포함되면 안된다.
        if '0' in a:
            continue

        for j in baseball:

            # 주어진 예시 숫자. a가 정답이 맞는지 비교.
            b = list(str(j[0]))

            strike = 0
            ball = 0

            # 각 3자리 비교하며 strike, ball 개수 체크
            for k in range(0, 3):
                if a[k] == b[k]:
                    strike += 1

                if (a[k] != b[k]) and (a[k] in b):
                    ball += 1

            # strike, ball 개수가 일치하지 않는 경우 flag는 False
            if strike != j[1] or ball != j[2]:
                flag = False
                break


        if flag == False:
            continue
        elif flag == True:
            answer += 1

    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
answer = solution(baseball)
print(answer)