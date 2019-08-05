def solution(N):

    a = 1
    b = 1
    fibo_list = [1, 1]

    for i in range(0, N-2):
        c = a + b
        fibo_list.append(c)

        a = b
        b = c

    return (fibo_list[N-1] + fibo_list[N-2]) * 2 + (fibo_list[N-2] + fibo_list[N-3]) * 2


N = 6
answer = solution(N)
print(answer)