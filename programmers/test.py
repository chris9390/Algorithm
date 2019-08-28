def solution(board):

    x_len = len(board[0])
    y_len = len(board)

    flag = 0
    for i in board:
        if set(i) == {0}:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        return 0


    maximum = 1
    for i in range(0, y_len):
        for j in range(0, x_len):

            if board[i][j] == 1:

                # 확인해볼 정사각형 한변의 길이
                for n in range(2, min(x_len, y_len)+1):

                    # 기준점부터 가로 길이가 x_len 을 넘어가면 안됨.
                    if j + n > x_len:
                        break

                    ok_flag = 0
                    temp = 0

                    while(temp != n):
                        # 기준점부터 세로 길이가 y_len 을 넘어가면 안됨.
                        if i+temp >= y_len:
                            ok_flag = 0
                            break

                        if 0 not in board[i+temp][j:j+n]:
                            ok_flag = 1
                        else:
                            ok_flag = 0
                            break
                        temp += 1

                    if ok_flag == 1:
                        if maximum < n * n:
                            maximum = n * n

    return maximum



board = 	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board =  [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
board = [[0,0,1,1],[1,1,1,1]]
board = [[1,1,1],[1,1,1],[1,0,1]]
board = [[0,1,1,0,0,1,1,1], [0,1,1,0,0,1,1,1], [0,0,0,0,0,1,1,1]]
board = [[0,0],[0,1]]
board = [[1,1],[1,1],[1,0],[0,1]]
board = [[0,1,1,1], [1,1,1,1]]
answer = solution(board)
print(answer)