#BOJ1541_잃어버린 괄호
sik = input().split('-')
# print(sik)

arr = []

#입력값을 돌며
for i in sik:
    hap = 0
    #덧셈을 하기 위해 +를 기준으로 나눔
    hapsik = i.split('+')
    for j in hapsik:
        hap += int(j)
        
    #연산결과들을 arr에 저장
    arr.append(hap)
    
#식의 제일 처음은 숫자, 0번째 값에서 나머지값을 뺌
result = arr[0]
for i in range(1, len(arr)):
    result -= arr[i]
    
print(result)