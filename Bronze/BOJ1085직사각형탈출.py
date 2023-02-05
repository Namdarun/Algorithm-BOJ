#BOJ1085직사각형 탈출 
#https://www.acmicpc.net/problem/1085
#현수의 위치, 오른쪽 위 꼭짓점
x, y, w, h = map(int, input().split())
li = []
li.append(w-x)
li.append(h-y)
li.append(x)
li.append(y)
print(min(li))

