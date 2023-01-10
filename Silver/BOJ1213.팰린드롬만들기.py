#BOJ1213_팰린드롬만들기 
#홀수인 알파벳의 숫자가 2개 이상이면 펠린드롬이 될 수 없다.
#펠린드롬이 될 수 없는 케이스를 거르고 그 후 되는걸 앞 / 가운데 / 뒤(앞의 [::-1]) 붙여서 결과를 낸다
import collections
import sys
input = sys.stdin.readline

word = input().rstrip()
check_word = collections.Counter(word)
count = 0
result = ''
mid = ''
for k, v in list(check_word.items()):
    if v % 2 == 1: #홀수라면
        count += 1
        mid = k #중간에 들어갈 값으로 저장
        if count >= 2: #홀수가 2개이상이면 팰린드롬이 될 수 없다!!
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()): #정렬을 통해 사전순으로 for문을 돌게함
    result += (k * (v // 2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눠줌

print(result + mid + result[::-1]) # 앞+중간+뒤 를 더해 문자열 출력
