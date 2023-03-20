# #BOJ2238_경매
import sys
input = sys.stdin.readline
u, n = map(int, input().split())
dic = dict()
result = []
#비교를 위해 딕셔너리 단위로 입력받기
for _ in range(n):
    s, p = input().split()
    p = int(p)
    #p가 
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
    result.append((s, p))

for i in range(n):
    result[i] = (result[i][0], result[i][1], dic[result[i][1]])
# #print(result)
# #[('Lew', 10, 1), ('CD', 5, 2), ('Fe', 5, 2), ('CD', 7, 1)]

#람다로 정렬해서 첫번째 순위 사람 뽑기
result = sorted(result, key = lambda result: (result[2], result[1]))
# print(result)
# [('CD', 7, 1), ('Lew', 10, 1), ('CD', 5, 2), ('Fe', 5, 2)]
print(result[0][0], result[0][1])
    