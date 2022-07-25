# import random

# # 0~9까지의 세자리 숫자
# # 숫자는 맞지만 위치가 다를 경우 볼
# # 숫자와 위치가 맞을 경우 스트라이크
# # 숫자와 위치가 다를 경우 아웃
# # 숫자와 위치 전부 다 맞을 경우 홈런
# # 총 9번의 기회

# # 랜덤 숫자 3자리
# # res = []
# # for numb in range(3) :
# #     a = random.randrange(0,9)
# #     while a in res :
# #         a = random.randrange(0,9)
# #     res.append(a)

# # print(res)


# num = random.sample(range(9),3)

# print(num)


# # ans = input('숫자 입력(,으로 구분) :').split(',')
# # ans = int(input('숫자 입력:'))
# # an = list(map(str, range(ans)))


# answ = []

# # for i in range(3) :
# #     answ.append(int(input('숫자 입력:')))

# while len(answ) < 3:
#     try :
#         ans = int(input(f"{len(answ) +1}번째 숫자를 입력하세요 :"))

#         if ans < 0 or ans > 9:
#             print("한 자리수로 입력")
#         elif ans in answ:
#             print("중복, 다시")
#         else:
#             answ.append(ans)
#     except : 
#         print('숫자만 입력')

# # if 조건1:
# #     이 문장
# # elif 조건2:
# #     저 문장
# # else:
# #     그 문장
# # 다음 문장

# # i = 0
# # if answ[i] == num[i] :

#  # range()는 어떤 범위 내로 숫자를 만들어 주는 것, 예로 range(10)을 하면 0이상 10미만의 숫자 생성
#  # for x in range(10)는 0~9까지의 숫자들을 순서대로 x에 하나씩 넣는다!
#  # x는 임의의 값이며 원하는 이름으로 지정 가능
#     for x in range(3):
#         if answ[x] == num[x] :
#             print(f'{x}회')
    
# # 만약 정답의 첫번째 값[0] == 입력한 첫번째 값[0]이 같다면, 1str
# # 다음 조건 실행, 입력값[1] == 정답의 첫번째 값[0]부터 비교

# # 만약 정답의 첫번째 값[0] !== 입력한 첫번째 값[0]이 다르다면, 다음 정답[1]비교
# # 만약 정답의 두,세번째 값[1][2] == 입력한 첫번째 값[0]이 같다면, 1ball

# # 만약 정답의 모든 배열[0],[1],[2]의 값 중 입력한 첫번째 값[0]이 일치하는 게 없을 시 out

# # 만약 정답의 모든 배열[0],[1],[2]이 일치할 시, homer


# # ans = input('입력:')
# # answ.append(ans)
# print(answ)

# # try 예외처리
# # try:
# #     num = int(input("숫자입력"))
# #     if num >= 10
# #         raise ValueError
# # except ValueError:
#     # print("에러! 10이상의 값을 입력하셨습니다.")




# # if 조건문 2 (참고)

# # elif (이거 아냐!? 그럼 이건 어때??)
# # 앞의 조건이 참이 아닌 경우 다른 조건을 다시 한번 확인하기 위한 용도

# # if, elif, elif, elif, else 
# # 만약 ~ 라면(if) / 아니라고? 그럼 이건 어때?(elif) * 3 / 그렇지 않다면!(else)
# # else는 생략 가능!

# # if 조건1:
# #     이 문장
# # elif 조건2:
# #     저 문장
# # else:
# #     그 문장
# # 다음 문장

# # if -> True -> '이 문장' 실행 -> 다음 문장
# # if -> False -> elif -> True -> '저 문장' 실행 -> 다음 문장
# # elif -> False -> '그 문장' 실행 -> 다음 문장

# # ex)
# # today = '월요일'
# # if today == '일요일':
# #     print('게임 한 판')
# # elif today == '토요일':
# #     print('폰 5분만')
# # else:
# #     print('물 한 잔')
# # print('공부 시작!')

# # if와 else 사이에 elif 조건은 얼마든지 추가 가능!