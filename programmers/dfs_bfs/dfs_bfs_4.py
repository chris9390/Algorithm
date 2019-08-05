# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164
import copy

'''
def dfs(graph, start):
    visited = []
    stack = [start]

    while(stack):
        # 모든 경로를 거치면 반환
        if set(graph.keys()) == set(visited):
            return visited

        n = tuple(stack.pop())

        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
'''



# dfs 재귀적 방법으로 구현. 가능한 모든 경로를 탐색하기 위해.
def dfs_recur(graph, start, visited, possible):
    new_visited = copy.deepcopy(visited)
    new_visited.append(start)

    # 모든 경로를 탐색했다면 return
    if set(graph.keys()) == set(new_visited):
        possible.append(new_visited)
        return

    for i in graph[start]:
        if tuple(i) not in new_visited:
            dfs_recur(graph, tuple(i), new_visited, possible)



def solution(tickets):

    # 방향 그래프
    di_graph = {}

    # 그래프 제작
    # 딕셔너리의 키는 리스트가 될 수 없기 때문에 tuple 로 바꿔줬다.
    for idx_i, i in enumerate(tickets):
        # 딕셔너리의 키에 입력할 때 인덱스 번호도 같이 저장하자. 중복 항공편을 구분하기 위해서.
        i.append(idx_i)
        di_graph[tuple(i)] = []
        for j in tickets:
            if i == j:
                continue
            else:
                if i[1] == j[0]:
                    di_graph[tuple(i)].append(j)
    # 그래프 제작



    lst = []
    for i in di_graph:
        # 항상 ICN 공항에서 출발한다.
        if i[0] == 'ICN':
            visited = []
            # 가능한 모든 경로를 저장하기 위한 리스트
            possible = []
            dfs_recur(di_graph, i, visited, possible)
            lst.append(possible)


    # 항공편 도착과 시작을 이어주는 과정 ( [ICN, JFK], [JFK, COO] -> ICN JFK COO )
    final = []
    for i in lst:
        for j in i:
            temp = []
            for idx_k, k in enumerate(j):
                temp.append(k[0])
                if idx_k == len(j)-1:
                    temp.append(k[1])
            final.append(temp)



    # 여러개가 가능하면 알파벳 순서가 더 빠른 것 선택
    return min(final)





#tickets = [['ICN', 'SFO'],['ICN', 'ATL'],['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
#tickets = [['ICN', 'BOO'],['ICN', 'COO'],['COO', 'DOO'],['DOO','COO'],['BOO', 'DOO'],['DOO','BOO'],['BOO','ICN'],['COO','BOO']]
#tickets = [['ICN', 'COO'], ['ICN', 'BOO'], ['COO', 'ICN']]
tickets = [['ICN', 'COO'], ['ICN','COO'],['COO','ICN']]
answer = solution(tickets)
print(answer)