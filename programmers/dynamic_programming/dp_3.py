def solution(triangle):

    for i in range(1, len(triangle)):

        # 현재 라인의 양쪽 끝 원소는 이전 라인의 양쪽 끝 원소를 더해주면 된다.
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]

        for cur_idx, cur_each in enumerate(triangle[i]):

            # 처음과 끝은 이미 계산 끝나서 따로 처리 필요하지 않다.
            if cur_idx == 0 or cur_idx == len(triangle[i]) - 1:
                continue

            # 이전 라인의 양쪽 원소중 큰 값을 더해가면서 누적 계산해준다.
            triangle[i][cur_idx] += max(triangle[i-1][cur_idx - 1], triangle[i-1][cur_idx])


    # 누적 계산된 배열에서 최대값 찾기
    max_val = 0
    for i in triangle:
        if max(i) > max_val:
            max_val = max(i)

    return max_val


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
answer = solution(triangle)
print(answer)