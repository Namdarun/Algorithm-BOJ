#BOJ15649_N과M3
#https://www.acmicpc.net/submit/15651/54584976
##중복가능하게 n개 중 m개를 뽑음 
def nPm():
	if len(s) == M:
		print(*s)
		return
		# 중복가능
	for i in arr:
		s.append(i)
		nPm()
		s.pop()

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
s = []
nPm()