#BOJ17945_통학의신_B3
#https://www.acmicpc.net/problem/17945

#제곱근 구하기 
A, B = map(int, input().split())
#완전탐색 
for i in range(-1000, 1001):
    #방정식의 근은 항상 정수
    #B = -i**2-2Ai
    if i*(2*A-i) == B:
        #중복제거
        li = list(set([-i, -(2*A-i)]))

#오름차순으로 정렬
print(*sorted(li))