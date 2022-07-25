import random

# 랜덤 숫자 생성
num = random.sample(range(9),3)
print(num)

st = 0
ball = 0

while st == 3 :
# 정답 입력
    answ = []
    while len(answ) < 3:
        try :
            ans = int(input(f"{len(answ) +1}번째 숫자를 입력하세요 :"))

            if ans < 0 or ans > 9:
                print("한 자리수로 입력")
            elif ans in answ:
                print("중복, 다시")
            else:
                answ.append(ans)
        except : 
            print('숫자만 입력')


# 랜덤 숫자와 정답 비교
# for x in range(3):
#         if answ[x] == num[x] :
#             print(f'{x}회')


    for x in range(3) :
        if answ[x] == num[x] :
            st += 1
            # print(f'{st}S')

    for x in range(3) :
        if answ[x] in num and answ[x] != num[x] :
            ball += 1
            # print(f'{st}S', f'{ball}B')
            # print(f'{ball}B')
        # else : # list 포함하지 않을 경우
        #     print('out!')
    print('ㅊㅊ')
    break

# while True :
#     if st == 3 :
#         print('ㅊㅊ')
#     # else :
#     #     print(f'{st}S {ball}B')
#         break
# # if st == 3 :
# #     print('ㅊㅊ')