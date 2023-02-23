#S1_BOJ14888_연산자 끼워넣기
#https://www.acmicpc.net/problem/14888
#순열활용 - 1352ms / pypy만 통과

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
operator = '+' * oper[0] + '-' * oper[1] + '*' * oper[2] + '/' * oper[3]
# 조합가능한, 합이 n-1개인 연산자들의 모든 순열 조합
# print(operator)
operator_perm = permutations(operator, n-1)

#최댓값 
max_result = -1e9
#최솟값
min_result = 1e9
for i in operator_perm:
    # result에 연산해주면서 값들을 구해나간다.
    result = num[0]
    for j in range(1, n):
        if i[j-1] == '+':
            result += num[j]
        elif i[j-1] == '-':
            result -= num[j]
        elif i[j-1] == '*':
            result *= num[j]
        elif i[j-1] == '/':
            # 직전의 값이 -일땐 유지성을 위해 두 번 곱해준다
            if result < 0 and num[j] > 0: 
                result = -1*(result*(-1) // num[j])
            # 그 외는 몫만 남기기
            else:
                result //= num[j]
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)




#재귀의 활용 
# import sys
# input = sys.stdin.readline

# N = int(input())

# nums = list(map(int, input().split()))
# a, b, c, d = map(int, input().split())
# max_ans = -1e9
# min_ans = 1e9

# def solution(num, idx, add, sub, mul, div):
#     global max_ans, min_ans
#     if idx == N:
#         max_ans = max(max_ans, num)
#         min_ans = min(min_ans, num)
#         return 
    
#     if add > 0:
#         solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
#     if sub > 0:
#         solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
#     if mul > 0:
#         solution(num * nums[idx], idx + 1, add, sub , mul -1, div)
#     if div > 0:
#         solution(int(num / nums[idx]), idx + 1, add, sub, mul, div -1)

# solution(nums[0], 1, a, b, c, d)
# print(max_ans)
# print(min_ans)