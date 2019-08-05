# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189


def bfs(graph, start):
    visited = []
    queue = [start]
    distance = [0] * (len(graph) + 1)
    distance[0] = 1
    distance[1] = 1


    while(queue):
        n = queue.pop(0)

        # distance 배열이 다 채워지면 탈출
        if 0 not in set(distance):
            break


        if n not in visited:

            if n == start:
                for i in graph[n]:
                    distance[i] = 1
            else:
                for i in graph[n]:
                    if distance[i] != 0:
                        continue
                    else:
                        if distance[i] != 0:
                            if distance[i] > distance[n] + 1:
                                distance[i] = distance[n] + 1
                        elif distance[i] == 0:
                            distance[i] = distance[n] + 1

            visited.append(n)
            queue.extend(graph[n])



    return distance



def solution(n, edge):

    graph = {}

    # 그래프 키 초기화
    for i in range(1, n+1):
        graph[i] = []


    # 그래프 제작
    for i in edge:
        # 중복 방지를 위한 if 문
        if i[1] not in graph[i[0]]:
            graph[i[0]].append(i[1])

        # 중복 방지를 위한 if 문
        if i[0] not in graph[i[1]]:
            graph[i[1]].append(i[0])


    distance = bfs(graph, 1)    
    maximum = max(distance)
    return distance.count(maximum)

    # ==============================================================================

    distance = [0] * (len(graph) + 1)
    is_already_checked = [0] * len(distance)
    is_already_checked[0] = 1
    is_already_checked[1] = 1

    for i in graph:

        if i == 1:
            for j in graph[i]:
                distance[j] = 1
                is_already_checked[j] = 1
        else:
            for j in graph[i]:
                if is_already_checked[j] == 1:
                    if distance[j] > distance[i] + 1:
                        distance[j] = distance[i] + 1
                else:
                    distance[j] = distance[i] + 1
                    is_already_checked[j] = 1


    maximum = max(distance)
    return distance.count(maximum)



n = 5
#edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
#edge = [[1,2]]
#edge = [[1,2], [1,3], [2,3],[2,5],[2,4],[3,6],[3,8],[3,5],[4,7],[6,8],[5,9],[2,9],[3,7],[1,7]]
edge = [[1,2],[2,3],[3,5],[1,4],[4,5]]
answer = solution(n, edge)
print(answer)