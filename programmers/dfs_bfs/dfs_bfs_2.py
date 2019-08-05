# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def dfs(graph, start_node):
    visited = []
    # DFS는 stack을 사용해서 표현할 수 있다.
    stack = [start_node]

    while(stack):
        n = stack.pop()

        # vertex n을 방문하지 않았으면 방문하자.
        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])

    return visited



def solution(n, computers):
    graph = {}

    # 그래프 그리기
    for idx_i, i in enumerate(computers):
        graph[idx_i] = []
        for idx_j, j in enumerate(i):

            if idx_i == idx_j:
                continue
            else:
                # i와 j가 연결되어 있으면
                if j == 1:
                    graph[idx_i].append(idx_j)

    # 그래프 그리기

    # ==========================================


    # 그래프의 각 노드에서 dfs 를 하면서 중복되지 않는 경로들 체크
    possible_nets = []
    for i in graph:
        visited = dfs(graph, i)
        if set(visited) in possible_nets:
            continue
        else:
            possible_nets.append(set(visited))

    print(possible_nets)

    return len(possible_nets)




n = 3
computer = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
answer = solution(n, computer)
print(answer)