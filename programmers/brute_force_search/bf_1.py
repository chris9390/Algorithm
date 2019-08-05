def solution(answers):

    man_1 = [1,2,3,4,5]
    man_2 = [2,1,2,3,2,4,2,5]
    man_3 = [3,3,1,1,2,2,4,4,5,5]

    man_1_cnt = 0
    man_2_cnt = 0
    man_3_cnt = 0


    for idx, i in enumerate(answers):
        if i == man_1[idx % len(man_1)]:
            man_1_cnt += 1

        if i == man_2[idx % len(man_2)]:
            man_2_cnt += 1

        if i == man_3[idx % len(man_3)]:
            man_3_cnt += 1

    '''
    if man_1_cnt == man_2_cnt and man_2_cnt == man_3_cnt:
        return [1,2,3]

    if man_1_cnt == man_2_cnt and man_1_cnt > man_3_cnt:
        return [1,2]

    if man_2_cnt == man_3_cnt and man_2_cnt > man_1_cnt:
        return [2,3]

    if man_1_cnt == man_3_cnt and man_1_cnt > man_2_cnt:
        return [1,3]

    if max(man_1_cnt, man_2_cnt, man_3_cnt) == man_1_cnt:
        return [1]

    if max(man_1_cnt, man_2_cnt, man_3_cnt) == man_2_cnt:
        return [2]

    if max(man_1_cnt, man_2_cnt, man_3_cnt) == man_3_cnt:
        return [3]
    '''

    max_cnt = max(man_1_cnt, man_2_cnt, man_3_cnt)

    ret = []

    if max_cnt == man_1_cnt:
        ret.append(1)
    if max_cnt == man_2_cnt:
        ret.append(2)
    if max_cnt == man_3_cnt:
        ret.append(3)

    return ret


answers = [1,3,2,4,2]
answers = solution(answers)
print(answers)