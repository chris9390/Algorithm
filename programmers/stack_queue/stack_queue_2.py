# 탑
# https://programmers.co.kr/learn/courses/30/lessons/42588

def solution(heights):
    answer = []
    stack = []
    for h_idx, height in enumerate(heights):
        if h_idx == 0:
            stack.append([(h_idx, height)])
            answer.append(0)
        else:
            stack_idx = len(stack)-1
            while(1):
                if stack_idx == -1:
                    stack[-1].append((h_idx, height))
                    answer.append(0)
                    break

                if height >= stack[stack_idx][-1][1]:
                    if len(stack) == 1:
                        stack[stack_idx].append((h_idx, height))
                        answer.append(0)
                        break
                    stack_idx -= 1
                elif height < stack[stack_idx][-1][1]:
                    answer.append(stack[stack_idx][-1][0] + 1)
                    # 스택이 존재하면 끼워넣고
                    try:
                        stack[stack_idx + 1].append((h_idx,height))
                    # 없으면 새로 만든다.
                    except:
                        stack.append([(h_idx, height)])
                    break






    return answer


heights = [5,4,3,2,1]
answer = solution(heights)
print(answer)