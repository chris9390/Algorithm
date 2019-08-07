# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
import copy

def solution(n, lost, reserve):

    # 가장 for 문을 돌때 remove 메소드가 lost 배열에 영향을 미치기 때문에 
    temp = copy.deepcopy(lost)


    # 여벌의 체육복을 가져온 학생이 도난당하는 경우
    for i in temp:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)


    temp = copy.deepcopy(lost)


    for i in temp:

        # 앞 번호 학생이 여벌 체육복 있으면
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)

        # 뒷 번호 학생이 여벌 체육복 있으면
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)


    return n - len(lost)



n = 5
lost = [2,4]
reserve = [1,3,5]


answer = solution(n,lost,reserve)
print(answer)