#BOJ15649_N과M1
#https://www.acmicpc.net/problem/15649
#중복없이 n개 중 m개를 뽑음 
def nPm():
	if len(s) == M:
		print(*s)
		return
	# 중복없이 
	for i in arr:
		if i in s:
			continue
		else:
			s.append(i)
			nPm()
			s.pop()

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
s = []
nPm()