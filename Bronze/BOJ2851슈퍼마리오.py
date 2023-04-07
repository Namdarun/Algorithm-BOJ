#BOJ2851_슈퍼마리오_B1
#https://www.acmicpc.net/problem/2851

result = 0
total = 0

for i in range(10):
    #10개의 값을 차례대로 입력받는데,
    total += int(input())
    #total은 누적하면서 값들 더해나가고,
    #100에서 result 뺀 값과 비교했을 때 절대값이 더 높으면 그 값이 100과 가까운 최댓값
    if 100-result >= abs(100-total):
        # print({result})
        # print([total])
        result = total
        
print(result)