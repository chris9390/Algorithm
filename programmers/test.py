import copy

def dfs(graph, start):
    visited = []
    stack = [start]

    while(stack):

        # 모든 곳을 한번씩 다 거치면 이동 경로 반환
        if set(graph.keys()) == set(visited):
            return visited

        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
        else:
            visited.append(n)

    return visited


'''
def dfs_recur(graph, start, visited):
    
    new_visited = copy.deepcopy(visited)
    new_visited.append(start)
    print(start)


    for i in graph[start]:
        if i not in new_visited:
            dfs_recur(graph, i, new_visited)
'''



graph = {1 : [2],
         2 : [3,4],
         3 : [1,5],
         4 : [2],
         5 : [3,4]}
start = 1
visited = dfs(graph, start)
#visited = []
#dfs_recur(graph, start, visited)
print(visited)
