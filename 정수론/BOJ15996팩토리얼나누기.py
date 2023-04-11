#BOJ15996_팩토리얼나누기_S3
#https://www.acmicpc.net/problem/15996

# 음이 아닌 정수 n과 소수a -> n!을 a의k제곱으로 나누었을 때
# 나머지가 0이 되는 최대의 음이 아닌 정수 k를 구해라

import sys
input = sys.stdin.readline 

n, a = map(int, input().split())

# nn = 1
# for i in range(1, n+1):
#     nn *= i
#     result = 1
#     for j in range(1, n+1):
#         if nn%a**j == 0:
#             if result < j:
#                 result = j

# print(result)

#에라토스테네스의 체
result = 0
#nn = 2부터 시작해서 제곱해나감
#5보다 작거나 같은 동안 result에 n을 nn으로 나눴을 때 발생하는 몫을 더해줌(특정수의 배수)
nn = a
while nn <= n:
    # print(nn)
    result += n // nn
    nn *= a
    # print('뭔데' ,nn)

print(result)