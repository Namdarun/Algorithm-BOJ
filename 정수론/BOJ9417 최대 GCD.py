#BOJ9417_최대GCD_S4
#https://www.acmicpc.net/problem/9417

import sys
input = sys.stdin.readline

#유클리드 호제법을 통한 최대공약수 구하기
def GCD(a, b):
    while b >0:
        a, b = b, a%b
    return a

n= int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    nums_length = len(nums)
    max_num = 1

    for i in range(nums_length -1) :   
        for j in range(i+1, nums_length):
            result = GCD(nums[i], nums[j])

            #최댓값 구하기 
            if result > max_num:
                max_num = result
    
    print(max_num)