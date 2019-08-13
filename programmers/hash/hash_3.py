# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1

    # 옷 종류 끼리 classify 사전에 분류
    classify = {}
    for i in clothes:
        try:
            classify[i[1]].append(i[0])
        except:
            classify[i[1]] = [i[0]]


    # 각 옷 종류별로 안입는 경우까지 포함하여 곱해준다.
    for i in classify:
        answer *= (len(classify[i])+1)


    # 옷을 다 벗은 경우는 제외시킨다.
    return answer - 1


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
answer = solution(clothes)
print(answer)