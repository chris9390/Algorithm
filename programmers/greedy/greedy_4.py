# 구명보트
# https://www.welcomekakao.com/learn/courses/30/lessons/42885?language=python3

def solution(people, limit):
    answer = 0

    # 무거운 사람 순서로 정렬
    people.sort(reverse=True)

    front = 0
    rear = len(people) - 1

    while(1):

        # 무한 루프 탈출 조건
        if rear < front:
            break

        # 가장 무거운 사람과 가장 가벼운 사람이 같이 보트에 탔을때 limit을 초과하지 않는 경우
        if people[front] + people[rear] <= limit:
            front += 1
            rear -= 1
        # limit을 초과하면 무거운 사람만 타고 간다.
        else:
            front += 1

        answer += 1

    return answer



people = [10, 10, 20, 20, 20, 30, 40]
people = [70, 70, 10, 10]
people = [70, 50, 80, 50]
limit = 100
answer = solution(people, limit)
print(answer)