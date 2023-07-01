#BOJ10798_세로읽기_B1
#https://www.acmicpc.net/problem/10798

#알파벳이 섞인 5개 입력 -> 세로로 읽어서 출력
#2차원배열로 읽어나가자

arr = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(arr[i]):
            print(arr[i][j], end='')