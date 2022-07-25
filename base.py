import random

# 0~9까지의 세자리 숫자
# 숫자는 맞지만 위치가 다를 경우 볼
# 숫자와 위치가 맞을 경우 스트라이크
# 숫자와 위치가 다를 경우 아웃
# 숫자와 위치 전부 다 맞을 경우 홈런
# 총 9번의 기회

# print(random.randrange(0,1000))

# 랜덤 숫자 3자리 생성
res = []

for num in range(3) :
    a = random.randrange(0,9)
    while a in res :
        a = random.randrange(0,9)
    res.append(a)

# print(res)

# num = random.sample(range(0,999),1)
# num = str(num)
# print(num)

# for num in range() :
#     a = random.sample(range(0,999),1)
#     # res.append(a)
#     print(a)

base = 0

while True :
    try:
        ans = int(input('숫자 입력 : '))
        ans = str(ans)
        if len(ans) != 3:
            print('세자리를 입력해주세요')
            continue
        
    except :
        print("숫자를 입력해주세요!")
        continue
        
# an = []
# while True :
#     try:
#         ans = [list(map(int, input())) for a in range(3)]
#         ans = str(ans)
#         if len(ans) != 3:
#             print('세자리를 입력해주세요')
#             continue
        
#     except :
#         print("숫자를 입력해주세요!")
#         continue

# 예시용
    base += 1
    strike = 0
    ball = 0
    for i in range(3) :
        if ans[i] == num[i]:
            strike += 1
        if ans[i] == num[(i + 1) % 3] or ans[i] == num[(i+2) % 3] :
            ball += 1
        if strike == 0 and ball == 0: print('아웃')
        elif strike == 3:
            print('정답! %d번 시도하였습니다'%base)
            break
        else:
            print('%d스트라이크 %d볼 입니다'%(strike, ball))
            break
        

# input 입력, 결과값 for문으로 하나씩 출력
# h = str(input('입력:'))
# for z in h :
#     print(z)

# while True :
#     try:
#         b = int(input('숫자 입력 : '))
#         # print(b)
#         # for c in range(3):
#         if b == res[0]:
#             print("d")
#         break
#     except:
#         print("숫자를 입력")

 # for 변수 in 반복 범위 or 대상:
 # range()는 어떤 범위 내로 숫자를 만들어 주는 것,
 # 예로 range(10)을 하면 0이상 10미만의 숫자 생성
# for c in range(3):
    
# print(res)


# sample() 처럼 중복 없이 숫자 생성하는 함수도 있음
# x = random.sample(range(0,10),3)
# print(x)

# randint(a,b)0와 randrange(a,b)의 차이점
# randint는 a가 최소, b가 최대 범위
# randrange는 a가 최소, b-1이 최대 범위