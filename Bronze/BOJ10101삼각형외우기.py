#BOJ10101_삼각형외우기_B4
#https://www.acmicpc.net/problem/10101

# 단순구현 

a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:              
    print("Equilateral")
elif a + b + c == 180:           
    if a == b or b == c or c == a: 
        print("Isosceles")
    else:                       
        print("Scalene")
else:                           
    print("Error")