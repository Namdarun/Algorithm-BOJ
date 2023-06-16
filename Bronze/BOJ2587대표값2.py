#BOJ2587_대표값2_B2
#https://www.acmicpc.net/problem/2587

result = []
for i in range(5):
    result.append(int(input()))

result.sort()
#평균
print(int(sum(result)/5))
#중앙값
print(result[2])