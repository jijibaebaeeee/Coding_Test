def solution(line):
    answer, tmp = [], []
    n = len(line)
    
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    
    for i in range(n):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            if (a*d == b*c):  continue
            
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                tmp.append([x,y])    # 확인함
                x_max, y_max = max(x, x_max), max(y, y_max)
                x_min, y_min = min(x, x_min), min(y, y_min)
    
    width = x_max - x_min + 1
    height = y_max - y_min + 1
    coord = [['.'] * width for _ in range(height)]  #[['.']] 괄호가 두 개임
    
    for x_star, y_star in tmp:
        p_x = x_star + abs(x_min) if x_min < 0 else x_star - x_min
        p_y = y_star + abs(y_min) if y_min < 0 else y_star - y_min
        coord[p_y][p_x] = '*'

    for result in coord: answer.append(''.join(result))
        
    return answer[::-1]