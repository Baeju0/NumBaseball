import random

# 랜덤 숫자 생성
def ran() :
    num = random.sample(range(9),3)
    print(num)
    return num

# 정답 입력
def answe() :
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
        
    return answ

# 숫자 비교
def bi(answ, num) :
    st = 0
    ball = 0

    for x in range(3) :
        if answ[x] == num[x] :
            st += 1
            # print(f'{st}S')

    for x in range(3) :
        if answ[x] in num and answ[x] != num[x] :
            ball += 1

    while True :
        if st == 3 :
            print("ㅊㅊ")
            break
        
        else :
            print(f"{st}S",f"{ball}B")



    # return f"{st}S,",f"{ball}B"


# Answer = ran()
# sido = 0

# s = 0
# b = 0

# while True:
#     user = answe()
#     s, b = bi(user, Answer)

#     print(s,b)
#     sido += 1

#     if s == "3S":
#         break    

# print(f"ㅊㅊ{sido}번 시도함")
# break가 안 돼!

            # print(f'{st}S', f'{ball}B')
            # print(f'{ball}B')
        # else : # list 포함하지 않을 경우
        #     print('out!')
    
    
# while True :
#     user_guess = take_guess
#     if st == 3 :
#         print('ㅊㅊ')
#         break
#     else :
#         # ans
#         print(f'{st}S {ball}B')
#         break

# # if st == 3 :
# #     print('ㅊㅊ')

# git