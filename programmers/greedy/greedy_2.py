# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

import copy

# 현재 idx 에서 어느 방향으로 가는 것이 효율적인지 구하는 함수.
def which_way(name_temp, name, idx):
    left_result = []
    right_result = []

    nt_l = copy.deepcopy(name_temp)
    n_l = copy.deepcopy(name)

    nt_r = copy.deepcopy(name_temp)
    n_r = copy.deepcopy(name)

    right_cnt = 0
    left_cnt = 0
    idx_temp = idx
    # 왼쪽, 오른쪽 중 다른 문자를 더 빨리 만나는 방향으로 이동
    while(name_temp[idx_temp] == name[idx_temp]):
        right_cnt += 1

        if idx_temp == len(name) - 1:
            idx_temp = 0
        else:
            idx_temp += 1

    idx_temp = idx
    while(name_temp[idx_temp] == name[idx_temp]):
        left_cnt += 1

        if idx_temp == 0:
            idx_temp = len(name) - 1
        else:
            idx_temp -= 1


    if left_cnt < right_cnt:
        return 'go_left'
    elif left_cnt > right_cnt:
        return 'go_right'

    # 이동 거리가 같다면 그중 더 효율적인 방향으로 이동
    elif left_cnt == right_cnt:
        idx_r = idx
        # right way result
        while(nt_r != n_r):
            if nt_r[idx_r] != n_r[idx_r]:
                right_result.append(1)
                nt_r = list(nt_r)
                nt_r[idx_r] = n_r[idx_r]
                nt_r = ''.join(nt_r)
            else:
                right_result.append(0)

            # idx inc
            if idx_r == len(n_r)-1:
                idx_r = 0
            else:
                idx_r += 1


        idx_l = idx
        # left way result
        while(nt_l != n_l):
            if nt_l[idx_l] != n_l[idx_l]:
                left_result.append(1)
                nt_l = list(nt_l)
                nt_l[idx_l] = n_l[idx_l]
                nt_l = ''.join(nt_l)
            else:
                left_result.append(0)

            # idx inc
            if idx_l == 0:
                idx_l = len(n_l) -1
            else:
                idx_l -= 1

        if left_result > right_result:
            return 'go_right'
        else:
            return 'go_left'


def solution(name):
    answer = 0

    # 우리는 name_temp 를 name 으로 바꿀때 이동한 조이스틱 횟수를 구할 것이다.
    name_temp = 'A' * len(name)

    idx = 0
    while(name_temp != name):

        if name_temp[idx] != name[idx]:
            # A ~ M 는 위로 조이스틱 올리는게 최소 이동
            if ord(name[idx]) <= ord('M'):
                answer += (ord(name[idx]) - ord(name_temp[idx]))
            # N ~ Z 는 아래로 조이스틱 내리는게 최소 이동
            else:
                answer += (ord('Z') - ord(name[idx]) + 1)

            # temp 의 idx 위치 문자 변경
            name_temp = list(name_temp)
            name_temp[idx] = name[idx]
            name_temp = ''.join(name_temp)


        if name_temp == name:
            break


        if which_way(name_temp, name, idx) == 'go_right':
            if idx == len(name) - 1:
                idx = 0
            else:
                idx += 1
        elif which_way(name_temp, name, idx) == 'go_left':
            if idx == 0:
                idx = len(name) - 1
            else:
                idx -= 1



        # 조이스틱 좌우 이동.
        answer += 1



    return answer


name = 'ABAAAABB'
answer = solution(name)
print(answer)