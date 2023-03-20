#BOJ1094_막대기
#https://www.acmicpc.net/problem/1094

X = int(input())
count = 0
N = 64
while X > 0:
	if N > X:
		N = N // 2
	else:
		count += 1
		X -= N
print(count)