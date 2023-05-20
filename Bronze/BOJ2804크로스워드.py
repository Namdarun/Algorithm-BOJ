#BOJ2804_크로스워드_B1
#https://www.acmicpc.net/problem/2804

a, b = input().split()
n, m = len(a), len(b)

word = [['.']*n for _ in range(m)]

for i in range(n):
    check = False
    for j in range(m):
        if a[i] == b[j]:
            row = j
            col = i
            check = True
            break
        if check == True:
            break

#가로로 들어갈 문자
for i in range(n):
    word[row][i] = a[i]

#세로로 들어갈 문자 
for i in range(m):
    word[i][col] = b[i]

for i in range(m):
    print(''.join(word[i]))