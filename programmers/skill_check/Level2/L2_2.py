
# idx 에서 어느 방향으로 가야 서로 다른 문자가 더 빨리 나오는지 알려주는 함수.
def which_way_to_go(init, name, idx):
    l_check = []
    r_check = []

    temp_idx = idx
    # go right
    temp_idx = (temp_idx + 1) % len(name)
    for _ in range(len(name)):
        if init[temp_idx] != name[temp_idx]:
            r_check.append(1)
        else:
            r_check.append(0)
        temp_idx = (temp_idx + 1) % len(name)


    temp_idx = idx
    # go left
    if temp_idx == 0:
        temp_idx = len(name) - 1
    else:
        temp_idx -= 1
    for _ in range(len(name)):
        if init[temp_idx] != name[temp_idx]:
            l_check.append(1)
        else:
            l_check.append(0)

        if temp_idx == 0:
            temp_idx = len(name) - 1
        else:
            temp_idx -= 1

    # 서로 다른 문자가 나올 때 까지 양쪽 방향으로 가는 횟수가 동일한 경우.
    if l_check.index(1) == r_check.index(1):
        if l_check < r_check:
            return 'go_left'
        else:
            return 'go_right'
    elif l_check > r_check:
        return 'go_left'
    elif l_check < r_check:
        return 'go_right'



def solution(name):
    answer = 0

    init = 'A' * len(name)
    idx = 0

    while(1):
        # init을 name으로 바꿀 것이다.
        if name == init:
            break

        if init[idx] != name[idx]:
            if ord(name[idx]) <= ord('M'):
                answer += (ord(name[idx]) - ord('A'))
            elif ord(name[idx]) >= ord('N'):
                answer += (ord('Z') - ord(name[idx]) + 1)

            temp = list(init)
            temp[idx] = name[idx]
            init = ''.join(temp)

            if name == init:
                break


        which_way = which_way_to_go(init, name, idx)
        if which_way == 'go_left':
            if idx == 0:
                idx = len(name)-1
            else:
                idx -= 1
        elif which_way == 'go_right':
            idx = (idx + 1) % len(name)
        answer += 1




    return answer



name = 'ABAAABB'
answer = solution(name)
print(answer)