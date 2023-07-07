#BOJ5073_삼각형과세변_B3
#https://www.acmicpc.net/problem/5073

while True:
    a,b,c = map(int, input().split())
    if a+b+c == 0:
        break

    arr = [a,b,c]
    # 삼각형의 조건
    if sum(arr) <= max(arr)*2:
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")