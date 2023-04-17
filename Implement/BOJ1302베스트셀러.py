
n = int(input())
dict = {}
for i in range(n):
    book = input()
    #책이 저장되어있지 않으면
    if book not in dict:
        dict[book] = 1
    #책이 저장되어 있으면 1추가
    else:
        dict[book] += 1

count= []
check=max(dict.values())
for i in dict:
    if check==dict[i]:
        count.append(i)

count.sort()
print(count[0])