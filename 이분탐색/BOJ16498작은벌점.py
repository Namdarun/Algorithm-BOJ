#BOJ16498_작은벌점_G5
#https://www.acmicpc.net/problem/16498

# A, B, C 크기의 정수 배열이 주어진다.
# 3개의 숫자 하나씩을 선택하여 가장 큰 수와 가장 작은 수의 차이를 계산한다.
# 가능한 모든 조합 중에서 가장 작은 차이를 출력한다.

#이진탐색
A, B, C = map(int, input().split())
arrA = sorted(list(map(int, input().split())))
arrB = sorted(list(map(int, input().split())))
arrC = sorted(list(map(int, input().split())))

