def solution(participant, completion):

    # 방법 1. 딕셔너리
    '''
    dict = {}
    for i in participant:
        try:
            dict[i] += 1
        except:
            dict[i] = 1


    for i in completion:
        dict[i] -= 1

    for i in dict:
        if dict[i] == 1:
            return i
    '''


    # 방법 2. 정렬
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if i == len(completion):
            return participant[-1]
        if participant[i] != completion[i]:
            return i


    return participant[0]



participant = ['marina', 'josipa', 'nikola', 'vinko', 'fillipa']
completion = ['josipa', 'fillipa', 'marina', 'nikola']
answer = solution(participant, completion)
print(answer)