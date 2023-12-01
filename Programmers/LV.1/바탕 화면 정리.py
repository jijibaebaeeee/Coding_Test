def solution(wallpaper):
    min_x = 50
    max_x = 0
    tmp_y = []
    for i in range(len(wallpaper)):
        tmp_x = []
        if '#' not in wallpaper[i]:
                # result.append('')
                continue
        else:
            tmp_y.append(i)
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                tmp_x.append(j)

        # x좌표 최대,최소 계산        
        tmp_min_x = tmp_x[0]
        tmp_max_x = max(tmp_x)
        if tmp_min_x < min_x:
            min_x = tmp_min_x
        if tmp_max_x > max_x:
            max_x = tmp_max_x
    # y좌표 최대,최소 계산
    min_y = min(tmp_y)
    max_y = max(tmp_y)

    answer = [min_y, min_x, max_y+1,max_x+1]

    return answer

# [".#...", "..#..#", "...#."]
# 이러한 리스트내의 문자열을 보고
# 하나의 문자열이 끝나면 카운트를하고
# .도 카운트하며 #이 있으면 그 수를 저장을해서 숫자로 변환된 새로운 리스트를 만든다.
# 스크롤하는 하는 가장 최적의 방법은 (세로,가로)가 기준이라고 했으므로
# 세로 <= 리스트 내의 문자열의 개수
# 가로 <= 문자열 내의 # 위치.

# 세로에서 가장 작은 것을 return하여 출력의 첫 번째 리스트 원소로
# 가로에서 가장 작은 것으 return하여 출력의 두 번째 리스트 원소로
# 세로에서 가장 큰 것을 return하여 출력의 세 번째 리스트 원소로
# 가로에서도 가장 큰 것을 return하면 출력의 네 번째 리스트 원소로

#하면 될 듯하다. 시간초과만 나오지 말아라 ㅠㅠ