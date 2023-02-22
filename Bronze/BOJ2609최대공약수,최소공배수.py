#BOJ2609최대공약수, 최소공배수.py
#https://www.acmicpc.net/problem/2609

a, b = map(int, input().split())

def max_num(a, b):
    while b > 0:
        a, b = b, a% b
    return a
            

def min_num(a,b):
    return a*b // max_num(a,b)    

print(max_num(a,b))
print(min_num(a,b))

    