# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):


    # 큰 숫자부터 내려가면서 해당 숫자 앞에 k 보다 작은 개수의 숫자가 있다면 전부 제거
    for i in range(9, -1, -1):
        try:
            num_location = number.index(str(i))
            if num_location == 0:
                continue
        except:
            continue

        if max(number[0:num_location]) < str(i) and num_location <= k:
            number = number[num_location:]
            k -= num_location

    if k == 0:
        return number


    # 숫자가 작아졌다 커지는 부분이 있으면 제거
    i = 0
    while(1):
        if i == len(number)-1:
            break

        if k == 0:
            return number

        if i == 0 or i == len(number) - 1:
            i += 1
            continue

        #if number[i-1] > number[i] and number[i] < number[i+1]:
        if number[i] < number[i+1]:
            number = number[0:i] + number[i+1:]
            i -= 2
            k -= 1

        i += 1


    if k == 0:
        return number



    # 최종 단계. 작은 수부터 지워 나간다.
    while(k != 0):
        minimum = min(number)
        idx = number.index(minimum)
        number = number[0:idx] + number[idx+1:]
        k -= 1

    return number





if __name__ == '__main__':
    number = '321321'
    k = 2
    answer = solution(number, k)
    print(answer)