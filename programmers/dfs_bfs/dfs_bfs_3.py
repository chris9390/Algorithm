# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

import copy

def cipher_check(a, b):
    check = 0

    for i in range(0, len(a)):
        if a[i] != b[i]:
            check += 1

    if check == 1:
        return True


    return False


def dfs_recur(graph, start_node, target, visited, possible):
    temp = copy.deepcopy(visited)
    temp.append(start_node)

    if start_node == target:
        possible.append(temp)
        return

    for i in graph[start_node]:
        if i not in temp:
            dfs_recur(graph, i, target, temp, possible)





def solution(begin, target, words):
    graph = {}

    if target not in words:
        return 0



    for i in words:
        graph[i] = []
        for j in words:
            check = 0
            if i == j:
                continue
            else:
                # 1글자만 다른지 체크
                if cipher_check(i, j) == True:
                    graph[i].append(j)


    lst = []
    for i in graph:
        if cipher_check(begin, i) == True:
            visited = []
            possible = []
            dfs_recur(graph, i, target, visited, possible)

            print(possible)
            if not possible:
                lst.append(-1)
            else:
                #lst.append(len(min(possible)))
                lst.append(min(list(map(len, possible))))


    # 모든 시작점에서의 dfs 결과가 -1 이라면 target 을 도출하지 못하는 경우이다.
    if set(lst) == {-1}:
        return 0
    # lst 가 비어있는 경우는 begin에서 graph의 각 노드로 이동이 불가능한 경우이다.
    elif not lst:
        return 0
    else:
        if -1 in lst:
            lst.remove(-1)
        return min(lst)






begin = 'coa'
target = 'cog'
#words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
#words = ['hot', 'hut', 'lut', 'lot', 'log', 'cog']
#words = ['hot', 'hot', 'hog', 'cog']
words = ['cua', 'cot', 'cog']

answer = solution(begin, target, words)
print(answer)