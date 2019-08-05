def solution(phone_book):

    # i를 비교대상으로 설정하고, j로 순회하면서 i와 j 비교
    for i in phone_book:
        for j in phone_book:

            # i, j가 같은 경우나 i의 길이가 j보다 길 경우 i가 j의 접두사가 될 수 없으므로 continue
            if (j == i) or (len(i) > len(j)):
                continue

            # i의 길이만큼이 j의 접두사부분에 존재하면 return false
            if j[0:len(i)] == i:
                return False

    return True





phone_book = ['12', '123', '1235', '567', '88']
answer = solution(phone_book)
print(answer)