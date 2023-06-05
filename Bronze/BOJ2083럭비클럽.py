#BOJ2083_럭비클럽_B4
#https://www.acmicpc.net/problem/2083

#단순구현문제 

while True:
    name, age, weight = input().split()
    if '#' in name:
        break
    if int(age) > 17 or int(weight) >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")