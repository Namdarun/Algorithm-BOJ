#BOJ3040_백설공주와일곱난장이_B2
#https://www.acmicpc.net/problem/3040

arr = [0]*9
for i in range(0, 9):
    arr[i] = int(input())

for i in range(9):
    for j in range(i+1, 9):
        if sum(arr)-arr[i]-arr[j] == 100:
            x, y = i, j
            break

arr.pop(x)
arr.pop(y-1)
for i in arr:
    print(i)