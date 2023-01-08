#BOJ4673_셀프넘버
#입력이 없는 경우 조건을 잘 보자
#
def self(num):
    self_num = num
    while num > 0:
        self_num += num%10 # 오른쪽 끝 숫자를 더함
        num //= 10 # 오른쪽 끝 숫자를 삭제
    return self_num
        
result = []
for i in list(range(1,10001)):
    result.append(self(i)) # 셀프 넘버를 저장
    #중복이 없는지 확인하는 로직(중요!)
    if i not in result:
        print(i)