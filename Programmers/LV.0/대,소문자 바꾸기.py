str = input()
s = ""
while True:
    if len(str) < 1 and len(str) > 20:
        continue
    else:
        for i in range(len(str)):
            if str[i] >= 'A' and str[i] <= 'Z':
                s += chr(ord(str[i]) + 32)
            elif str[i] >= 'a' and str[i] <= 'z':
                s += chr(ord(str[i]) - 32)
        break 
print(s)

#다른 사람의 풀이 1
str = input()
str1=""
for s in str :
    if s.islower() :
        str1+=s.upper() 
    else :
        str1+=s.lower() 
print(str1)

#다른 사람의 풀이 2
str = input().swapcase()
