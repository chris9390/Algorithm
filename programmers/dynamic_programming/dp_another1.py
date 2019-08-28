# 가장 큰 정사각형 찾기
# https://www.welcomekakao.com/learn/courses/30/lessons/12905

def solution(board):

    # 모든 리스트가 0 으로 구성될 때는 0 return
    flag = 0
    for i in board:
        if set(i) == {0}:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        return 0



    for i in range(1, len(board)):
        for j in range(1, len(board[0])):

            # (i,j) 가 1일때 왼쪽, 왼쪽위, 위쪽이 모두 1 이상이라면 최소값에 1을 더한게 (i,j) 의 값이다.
            if board[i][j] == 1:
                minimum = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                if minimum >= 1:
                    board[i][j] = minimum + 1


    maximum = 1
    for i in board:
        if max(i) > maximum:
            maximum = max(i)

    return maximum * maximum



#board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[0,1,1,1],[1,1,0,1],[1,1,1,0],[0,0,1,0]]
#board = [[0,1],[1,1]]
answer = solution(board)
print(answer)