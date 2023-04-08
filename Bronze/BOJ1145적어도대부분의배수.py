#BOJ1145_적어도대부분의배수_B1
#https://www.acmicpc.net/problem/1145

li = list(map(int, input().split()))
li.sort()

for i in range(1, 1000001):
	cnt = 0
	for j in range(5):
		if i % li[j] == 0:
			cnt += 1
	if cnt >= 3:
		print(i)
		break