#BOJ1780_색종이의개수_py
#https://zidarn87.tistory.com/385

#분할정복
#종이가 다 같은 종이가 될 때까지 9개로 자른 후 -1, 0, 1의 개수 파악

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

num_m = 0 
num_z = 0
num_p = 0

#재귀를 위한 dfs 함수 설정
def dfs(x, y, n):
    global num_m, num_p, num_z

    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if (paper[i][j] != check):
                #다르면 분할정복 재귀 돌림
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return
            
    #하나의 색으로 구성되는 경우 그 값으 1 더해준다
    if check == -1:
        num_m += 1
    elif check == 0:
        num_z += 1
    else:
        num_p +=1

#1, 1이 아님에 주의
dfs(0, 0, n)
print(num_m)    
print(num_z)
print(num_p)