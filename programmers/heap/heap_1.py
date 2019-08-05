import heapq

def solution(scoville, K):

    # 섞는 횟수
    mix_cnt = 0

    # scoville 배열을 최소 힙에 맞게 정렬해줍니다.
    heapq.heapify(scoville)

    while(1):
        # 탈출 조건
        # 배열의 첫번째 원소. 즉, 가장 작은 값이 K 보다 크면 무한 루프를 빠져나오게 됩니다.
        if scoville[0] >= K:
            return mix_cnt

        # 제한 사항
        if len(scoville) <= 1:
            return -1

        # 스코빌 지수가 가장 낮은 두 가지를 pop
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        temp = a + 2 * b
        # 계산 후 다시 push
        heapq.heappush(scoville, temp)

        mix_cnt += 1


scoville = [1, 2, 3, 9, 10, 12]
K = 7

answer = solution(scoville, K)
print(answer)