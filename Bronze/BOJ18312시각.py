#BOJ18312_시각_B2
#https://www.acmicpc.net/problem/18312

n, k = map(int, input().split())
k = str(k)
cnt = 0

for i in range(0, n+1):
    if i < 10:
        i = '0'+str(i)
    for j in range(0, 60):
        if j < 10:
            j = '0'+str(j)
        for l in range(0, 60):
            if l < 10:
                l = '0'+str(l)
            if k in (str(i) + str(j) + str(l)):
                cnt += 1

# print(type(i)) #str
# print(type(j)) #int
# print(type(l)) #int
print(cnt)