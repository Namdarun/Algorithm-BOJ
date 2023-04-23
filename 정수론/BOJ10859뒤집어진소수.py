#BOJ10859_뒤집어진소수_S2
#https://www.acmicpc.net/problem/10859

#0,2,5,8은 그대로
# 1은 왼쪽으로 옮겨짐
# 6은 9, 9는 6
# 3,4,7은 숫자가 아님 

import math

#소수판정 
def is_prime(num):
    if num == 1:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return True
    return False

#숫자인지 판정 -3,4,7
def check(s):
    num = int(s)
    while num > 0:
        if num % 10 in (3, 4, 7):
            return False
        num //= 10
    return True

#180도 돌리기 
def change(s):
    num = int(s)
    result = 0
    while num > 0:
        if num % 10 == 6:
            result = result * 10 + 9
        elif num % 10 == 9:
            result = result * 10 + 6
        else:
            result = result * 10 + num % 10
        num //= 10
    return result

n = int(input())
if is_prime(n):
    print("no")
else:
    if not check(str(n)):
        print("no")
    else:
        after = change(str(n))
        if is_prime(after):
            print("no")
        else:
            print("yes")