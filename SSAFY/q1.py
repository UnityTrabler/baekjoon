T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################
    #''' aaccb, abb
    #  이 부분에 여러분의 알고리즘 구현이 들어갑니다.    
    N = int(input())
    str = input()
    cnt = 0        
    flat = False
    for i in range(N):
        if (str[i] == 'a' or str[i] == 'b') and flat == True:
            cnt += 1
            continue
        elif str[i] == 'a' or str[i] == 'b':
            flat = True
        else : flat = False
    #'''
    #######################################################################################################

    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d" %test_case, "#%d" %cnt)
