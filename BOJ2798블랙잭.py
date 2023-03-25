# #BOJ2798_블랙잭_B2
# #https://www.acmicpc.net/problem/2798

# # N개의 숫자가 담겨있는 arr중 3개만 뽑은 조합인데, sort할 때 겹치면 안됨
# # 순열로 뽑고, 그걸 합들을 arr에 모두 담는다

# # 혹은 그냥 3개씩 뽑고 더한 값을 arr에 담고
# # m을 넘으면 버리고, m 안에 있으면 담아서 마지막값을 뽑는다.

# n, m= map(int, input().split())
# arr = sorted(map(int, input().split()))
# result = []

# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1,n):
#             if arr[i]+arr[j]+arr[k] > m:
#                 continue
#             else:
#                 result.append(arr[i]+arr[j]+arr[k])

# print(sorted(result)[-1])
    
from itertools import combinations

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

comb = combinations(arr, 3)
li = []
# max_num = 0
for c in comb:
    if sum(c) > m:
        continue
    else:
        li.append(sum(c))
        # max_num = sum(c)
        
# print(max_num)
print(sorted(li)[-1])

#왜 max_num은 494가 나오는가?