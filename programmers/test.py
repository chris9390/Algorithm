import copy
from operator import eq

answer = 100000
alphabet = [i for i in range(26)]
def DFS(arr,visit, name, value, i):
    global answer
    global alphabet
    if(eq(name, arr)):
        answer = value-1 if value-1 < answer else answer
        return

    if(i == -1):
        i = len(name)-1
    if(i == len(name)):
        i = 0
    if (visit[i] > 1):
        return
    visit2 = copy.deepcopy(visit)
    visit2[i] += 1
    arr2 = copy.deepcopy(arr)
    mid_val = abs(ord(name[i]) - ord(arr2[i]))
    if(arr2[i] == name[i]):
        DFS(arr2,visit2, name, value + 1, i + 1)
        DFS(arr2,visit2, name, value + 1, i - 1)
    else:
        arr2[i] = name[i]
        DFS(arr2,visit2, name, value + alphabet[mid_val] + 1, i + 1)
        DFS(arr2,visit2, name, value + alphabet[mid_val] + 1, i - 1)

def solution(name):
    global answer
    global alphabet
    k = 2
    for i in range(14,len(alphabet)):
        alphabet[i] = 14-k
        k += 1
    arr = ['A' for i in range(len(name))]
    name2 = []
    visit = [0 for i in range(len(name))]
    for i in range(len(name)):
        name2.append(name[i])
    DFS(arr,visit,name2,0,0)
    return answer



name = 'ABAAAABB'
answer = solution(name)
print(answer)