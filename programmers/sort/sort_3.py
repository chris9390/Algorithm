# H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    h_list = []
    h = 0
    while(1):
        up = 0

        for i in citations:
            if i >= h:
                up += 1

        if up < h:
            break

        if up >= h:
            h_list.append(h)

        h += 1

    return max(h_list)

citations = [3, 0, 6, 1, 5]
citations = [22,42]
answer = solution(citations)
print(answer)