#BOJ10039_평균점수_B4
#https://www.acmicpc.net/problem/10039

result = 0

for i in range(5):
    rank = int(input())

    if rank <= 40:
        rank = 40

    result += rank

print(result // 5)