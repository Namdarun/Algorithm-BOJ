#BOJ14225_부분수열의합_S1
#https://www.acmicpc.net/problem/14225

# 수열이 주어졌을 때 합으로 나올 수 없는 가장 작은 값

def check(arr):
    # 가능한 합을 저장하는 집합
    possible = set()  
    for num in arr:
        #현재 숫자로 가능한 새로운 합
        new_sums = {num}  
        for prev_sum in possible:
            # 이전 합에 현재 숫자를 더한 값을 추가
            new_sums.add(prev_sum + num)  
        # 가능한 합에 새로운 합을 추가
        possible.update(new_sums)  
    # 1부터 시작하여 가능한 합 중 최솟값을 찾음
    smallest = 1
    while smallest in possible:
        smallest += 1
    return smallest

n = int(input())
arr = list(map(int, input().split()))

answer = check(arr)
print(answer)