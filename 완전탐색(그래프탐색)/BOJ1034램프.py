#BOJ1034_램프_G4
#https://www.acmicpc.net/problem/1034

'''
알고리즘에 애드훅이란? 
= 복잡한 알고리즘 없이 구현만으로 풀이할 수 있는 문제
'''

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
#누르는 횟수 
k = int(input())

check = [0 for _ in range(n)]
#겹치는게 없으므로, 짝수홀수 체크
if k % 2 != 0:
    for i in range(n):
        #i의 모든 요소들
        zero_check = arr[i].count('0')
        if zero_check % 2 and zero_check <= k:
            for j in range(n):
                if arr[i] == arr[j]:
                    check[i] += 1

else:
    for i in range(n):
        #i의 모든 요소들
        zero_check = arr[i].count('0')
        if not zero_check % 2 and zero_check <= k:
            for j in range(n):
                if arr[i] == arr[j]:
                    check[i] += 1

# print(arr)
# print(check)
print(max(check))