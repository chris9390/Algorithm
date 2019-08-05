def solution(array, commands):
    answer = []
    temp = []

    for i in commands:
        temp = array[i[0]-1 : i[1]]
        temp.sort()
        answer.append(temp[i[2]-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2,5,3], [4,4,1], [1,7,3]]
answer = solution(array, commands)
print(answer)