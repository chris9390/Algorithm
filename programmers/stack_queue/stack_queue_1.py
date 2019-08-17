# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):

    # return 될 인쇄 횟수.
    print_cnt = 0

    # 우선순위가 동일한 것을 구분하기 위해 리스트의 각 원소를 딕셔너리로 변경.
    # 이때 각 딕셔너리의 key는 인덱스, value는 기존 원소 값.
    new_pri = []
    for idx, i in enumerate(priorities):
        new_pri.append({idx : i})


    while(1):
        # 리스트의 제일 앞 원소 pop
        target_dict = new_pri.pop(0)
        target_val = list(target_dict.values())[0]

        # 비교할 target 원소보다 우선순위가 높은 문서가 존재할 경우 flag_a를 1로 set
        flag_a = 0
        for i in new_pri:
            # 비교할 target 원소보다 우선순위가 높은 문서가 존재할 경우 리스트의 뒤쪽에 붙임.
            if list(i.values())[0] > target_val:
                new_pri = new_pri + [target_dict]
                flag_a = 1
                break

        if flag_a == 1:
            continue
        # flag_a 가 0인 경우 즉, target 원소가 가장 큰 경우, location과 일치하면 print_cnt를 return.
        # location과 불일치하면 print_cnt(출력횟수)를 하나 증가시킴.
        else:
            letmesee = target_dict
            if list(letmesee.keys())[0] == location:
                return print_cnt + 1
            else:
                print_cnt += 1




priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = solution(priorities, location)
print(answer)