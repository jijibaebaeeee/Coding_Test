def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer



#다른 사람의 풀이

def solution_1(number):
    from itertools import combinations
    cnt = 0
    for i in combinations(number, 3):
        if sum(i) == 0 :
            cnt += 1
    return cnt