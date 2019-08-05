# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189


def bfs(graph, start):
    queue = [start]
    # 1번 인덱스가 1번 노드를 가리키기 위해서 distance 배열의 개수를 하나 더 늘려준다.
    distance = [0] * (len(graph) + 1)
    distance[0] = 1
    distance[1] = 1

    visited = [False] * (len(graph) + 1)
    visited[0] = True

    while(queue):
        n = queue.pop(0)

        # n 노드를 방문하지 않았으면 방문한다.
        if visited[n] == False:
            visited[n] = True
            temp = set(graph[n]) - set(queue)
            # temp 리스트는 n 노드와 인접한 노드들의 리스트이다.
            queue.extend(list(temp))

            # n 노드의 주변 노드를 순회하면서 주변 노드 중 방문하지 않은 노드의 distance 값을 입력해준다.
            for i in list(temp):
                if n == 1:
                    distance[i] = 1
                else:
                    if visited[i] != 0:
                        continue
                    else:
                        distance[i] = distance[n] + 1




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




n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
#edge = [[1,2]]
#edge = [[1,2], [1,3], [2,3],[2,5],[2,4],[3,6],[3,8],[3,5],[4,7],[6,8],[5,9],[2,9],[3,7],[1,7]]
#edge = [[1,2],[2,3],[3,5],[1,4],[4,5]]
#edge = [[1,2],[2,3],[3,4]]
answer = solution(n, edge)
print(answer)



# ============================================
# 풀이 2

'''
# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189


def bfs(graph, start):
    queue = [start]
    # 1번 인덱스가 1번 노드를 가리키기 위해서 distance 배열의 개수를 하나 더 늘려준다.
    distance = [0] * (len(graph) + 1)
    distance[0] = 0
    distance[1] = 0

    visited = [False] * (len(graph) + 1)
    visited[0] = True
    visited[1] = True

    while(queue):
        n = queue.pop(0)

        for i in graph[n]:
            # i 노드를 방문하지 않았으면 방문한다.
            if visited[i] == False:
                visited[i] = True
                # i 노드의 주변 노드를 방문하기 위해 queue 에 추가.
                queue.append(i)
                # n 노드와 i 노드가 연결되어 있으므로 (n 노드까지의 최소 거리 + 1) 이 i 노드 까지의 최소 거리이다.
                distance[i] = distance[n] + 1


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




n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
#edge = [[1,2]]
#edge = [[1,2], [1,3], [2,3],[2,5],[2,4],[3,6],[3,8],[3,5],[4,7],[6,8],[5,9],[2,9],[3,7],[1,7]]
#edge = [[1,2],[2,3],[3,5],[1,4],[4,5]]
#edge = [[1,2],[2,3],[3,4]]
answer = solution(n, edge)
print(answer)
'''