#BOJ2217_로프_S4
#https://www.acmicpc.net/problem/2217

#최댓값 찾기 

n = int(input())
lope = []
for i in range(n):
    lope.append(int(input()))

lope.sort(reverse=True)
result = []

# 각각의 개수만큼 얼마를 버틸 수 있는지를 리스트로 나열한다. 
for i in range(n):
    result.append(lope[i]*(i+1))

#그 중에 최댓값 도출 
print(max(result))