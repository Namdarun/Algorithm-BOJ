#BOJ1924_2007년_B1
#https://www.acmicpc.net/problem/1924

result = 0
month = [31, 28, 31,30,31,30,31,31,30,31,30,31]
#몇번째인지 인덱스를 뽑아서 출력
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, input().split())

for i in range(x-1):
    #총 몇일인지 구함
    result += month[i]

#y까지 더해주고 7로 나누면 몇번째 날인지 정해짐
result = (result + y) % 7 
print(day[result])
