#BOJ9461_파도반수열_S3
#https://www.acmicpc.net/problem/9461

# 전형적인 dp문제
#시간초과버전
# import sys
# input = sys.stdin.readline

# def tran(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n == 3:
#         return 1
#     else:
#         return tran(n-2)+tran(n-3)

# test = int(input())
# for i in range(test):
#     n = int(input())
#     print(tran(n)) 


#통과버전

import sys
input = sys.stdin.readline

n = int(input())
arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11,101):
    arr.append(arr[i-2]+arr[i-3])

for _ in range(n):
    check = int(input())
    print(arr[check])