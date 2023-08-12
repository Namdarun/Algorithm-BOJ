#BOJ16435_스네이크_S5
#https://www.acmicpc.net/problem/16435

n , l = map(int, input().split())
input_li = list(map(int, input().split()))
# new_li = sorted(input_li)
input_li.sort()

# cnt = l 
# for i in new_li:
#     if cnt >= i:
#         cnt += 1

for i in range(n):
    if (l>= input_li[i]):
        l += 1
    else:
        break

# print(cnt)
print(l)