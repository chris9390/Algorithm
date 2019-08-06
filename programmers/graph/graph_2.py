# 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

def dfs(graph, start):
    visited = []
    stack = [start]

    while(stack):
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])

    return visited



def solution(n, results):
    answer = 0
    di_graph = {}
    win = {}
    lose = {}

    for i in range(1, n+1):
        di_graph[i] = []
        win[i] = []
        lose[i] = []

    for i in results:
        win[i[0]].append(i[1])
        lose[i[1]].append(i[0])

    for i in win:
        v = dfs(win, i)
        v.remove(i)
        win[i].extend(v)
        win[i] = list(set(win[i]))

    for i in lose:
        v = dfs(lose, i)
        v.remove(i)
        lose[i].extend(v)
        lose[i] = list(set(lose[i]))


    # 여기까지 그래프 제작


    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1


    return answer



#n = 5
#results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

n = 6
results = [[1,2],[3,2],[4,2],[2,5],[5,6]]
answer = solution(n, results)
print(answer)