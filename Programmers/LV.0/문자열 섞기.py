# #길이가 같은 두 문자열 str1과 str2가 주어집니다.
# #두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

def soultion(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

a = soultion('abc', 'def')
print(a)

# #다른 사람의 풀이1        (zip 내장함수를 for문에 사용할 수 있다.)
def soultion_1(str1,str2):
    res = ''
    for s1,s2 in zip(str1, str2):
        res += s1+s2

    return res

#다른 사람의 풀이2
def solution_2(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]

    return answer

a = solution_2('acb','asd')
print(a)