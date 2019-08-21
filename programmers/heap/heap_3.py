# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer = 0
    summ = 0
    heap = []
    length = len(jobs)


    # 우선 작업 시작 시간 기준으로 정렬
    jobs = sorted(jobs, key=lambda x : x[0])


    current_time = 0
    while(1):
        # jobs 리스트가 비면 무한루프 빠져 나온다.
        if len(jobs) == 0:
            break

        # 작업 중에 현재 시간 이전에 시작한 작업이 있으면 heap에 넣어준다.
        while(jobs[0][0] <= current_time):
            heapq.heappush(heap, (jobs[0][1], jobs[0]))
            # 넣어준 작업은 jobs 리스트에서 제거.
            jobs.pop(0)
            if len(jobs) == 0:
                break

        # 처리해줄 작업이 heap에 없다면 current_time을 1 늘려준다.
        if len(heap) == 0:
            current_time += 1
            continue

        # 현재 시간 까지 작업 소요 시간이 가장 작은 작업 추출.
        job = heapq.heappop(heap)[1]
        # 작업 시작시간이 current_time 이전에 있는지 아닌지에 따라 계산 방식이 달라진다.
        if job[0] < current_time:
            summ += (current_time-job[0]+job[1])
        elif job[0] == current_time:
            summ += job[1]

        # current_time 을 작업 소요 시간만큼 늦춰준다.
        current_time += job[1]


    # current_time 이후에 남은 작업이 없게되면 heap 이 빌때까지 작업 소요시간이 작은 순서로 꺼내준다.
    while(len(heap)!=0):
        job = heapq.heappop(heap)[1]
        if job[0] < current_time:
            summ += (current_time-job[0]+job[1])
        elif job[0] == current_time:
            summ += job[1]
        current_time += job[1]


    answer = summ // length
    return answer




#jobs = [[0, 3], [1, 9], [2, 6]]
#jobs = [[0,10], [2,2]]
#jobs = [[0,10], [6,2]]
#jobs = [[0,2], [0,4]]
#jobs = [[1,2], [4,3]]
#jobs = [[0,9],[0,4],[0,5],[0,7],[0,3]]
jobs = [[0, 3], [1, 9], [2, 6], [4, 3]]
answer = solution(jobs)
print(answer)