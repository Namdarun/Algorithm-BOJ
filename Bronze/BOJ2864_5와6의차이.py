#BOJ2864_5와6의차이_B2
#https://www.acmicpc.net/problem/2864

a, b = input().split() #str로 입력

min_num = int(a.replace('6', '5')) + int(b.replace('6', '5')) #replace함수
max_num = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(min_num, max_num)