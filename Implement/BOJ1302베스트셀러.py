#BOJ1302_베스트셀러_S4
#https://www.acmicpc.net/problem/1302
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
#책 개수에서 가장 큰 숫자
check=max(dict.values())
for i in dict:
    #딕셔너리를 순회하면서, 숫자가 똑같은 dict의 key값을 count리스트에 추가
    if check==dict[i]:
        count.append(i)

#리스트를 sort하고 맨 앞에 있는 걸 출력
count.sort()
print(count[0])