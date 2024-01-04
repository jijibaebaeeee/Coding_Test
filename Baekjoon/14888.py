import itertools
from functools import reduce
import sys
import time



def insert_operation(length, input_num, input_oper):

    ops = {"0":(lambda x,y: x+y), "1":(lambda x,y: x-y), "2":(lambda x,y: x*y), "3":(lambda x, y: int(x / y) if x >= 0 else int(-(-x / y)))}
    oper_permutation = []
    result = []
    list(oper_permutation.extend(
        [str(index)] * value) for index, value in enumerate(input_oper) if value > 0)
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]
    for i in permutation:
        result.append(reduce(lambda x,y: ops[i.pop()](x,y) , input_num))
    
    max_result = max(result)
    min_result = min(result)

    # print(str(max(result))+"\n"+str(min(result)))
    return max_result, min_result
    

n = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))

a, b = insert_operation(n, numbers, operator)
print(a)
print(b)