# 라면공장
# https://programmers.co.kr/learn/courses/30/lessons/42629

import heapq

def solution(stock, dates, supplies, k):

    answer = 0
    h = []
    date_idx = 0

    while(1):

        # 현 시점 stock 남은 계산
        if date_idx == 0:
            stock -= dates[date_idx]
        elif date_idx >= len(dates):
            stock -= (k - dates[date_idx - 1])
        else:
            stock -= (dates[date_idx] - dates[date_idx - 1])


        # 공급 후보군에 추가.
        try:
            heapq.heappush(h, (-supplies[date_idx], supplies[date_idx]))
        except:
            pass


        if date_idx < len(dates) - 1:
            # 다음 공급일까지 못 버팀. 공급 받아야 하는 상황.
            if dates[date_idx+1] - dates[date_idx] > stock:
                stock += heapq.heappop(h)[1]
                answer += 1
        # 마지막 공급일 이라면
        else:
            # 현 시점 부터 k 일후 까지 못 버팀. 공급 받아야 하는 상황.
            if k - dates[date_idx] > stock:
                stock += heapq.heappop(h)[1]
                answer += 1

            # 마지막 공급일 이후 공급이 더 필요했다면 공급해준다.
            while(stock < k - dates[date_idx]):
                stock += heapq.heappop(h)[1]
                answer += 1

            break

        date_idx += 1



    '''
    for i in range(0, k):

        # 밀가루를 더 공급 받을 필요가 없다면 바로 return
        if k - i <= stock:
            return answer


        if date_idx < len(dates):
            if i == dates[date_idx]:
                # heapq 는 최소힙밖에 지원되지 않기 때문에 최대힙으로 사용하려면 이런식으로 편법을 써야한다.
                # heap 에 넣어두는 행동은 공급 받았다는게 아니라 가능한 후보군에 넣어 놓는 것이다.
                heapq.heappush(h, (-supplies[date_idx], supplies[date_idx]))
                date_idx += 1

        # 공급 받아야 하는 상황.
        if stock == 0:
            # heap 에 들어있는 후보군 중 가장 큰 밀가루 공급량 선택. (max heap)
            stock += heapq.heappop(h)[1]
            answer += 1

        # 하루가 지날때마다 밀가루 1톤씩 사용.
        stock -= 1
    '''

    return answer



'''
stock = 10
dates = [5, 10]
supplies = [1, 100]
k = 110
'''

'''
stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30
'''


stock = 4
dates = [1,2,3,4]
supplies = [10, 40, 30, 20]
k = 100

answer = solution(stock, dates, supplies, k)
print(answer)