def solution(people, limit):
    answer = 0

    front = 0
    rear = len(people) - 1

    people.sort(reverse=True)

    while(1):
        if front > rear:
            break

        if people[front] + people[rear] > limit:
            front += 1
        else:
            front += 1
            rear -= 1

        answer += 1


    return answer



people = [70, 50, 80, 50]
limit = 100
answer = solution(people, limit)
print(answer)