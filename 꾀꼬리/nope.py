import sys
import json
print('환영합니다. 게임에 참여하시겠습니까? ')
D = int(input('1.네 2.아니요'))
if D == 1:
    print("자신의 정보를 확인해 보겠습니까?")
    C = int(input('1.네 2.아니요'))
    if C == 1:
            unit = { '체력': 5,  '마나': 2,  '가방': '없음',  '기술': '딱밤', '상태': '무기력',   '데미지': '1~7 dic'  }          
    print(ini)
        
if R == 2:

    a = input('이름을 입력해주세요 :')
    print(a,'님 환영합니다' )
    print(a ,"자신의 정보를 확인해 보겠습니까?")

    unit = { '체력': 5,  '마나': 2,  '가방': '없음',  '기술': '딱밤', '상태': '무기력',   '데미지': '1~7 dic'  }  

    f = int(input('1.네 2.아니요'))
    if f == 1:
        print("이름:" ,a)
        print(ini)
    if f == 2:
            
        print('장소를 이동중입니다')
        again = 'h'
        count = 1
        while again == 'h':

            print('야생의 돌덩이를 발견했습니다')
            print('싸우시겠습니까?')

            q = int(input('1.싸운다 2.도망친다'))

            if q == 1:
        
                try:
                    print('스킬 "딱밤" 를 사용하시겠습니까?')
                    u = int(input('1.사용한다 2.사용하지 않는다'))
                    import random
                    if u == 1:  
                        print('-' * 2)
                        print('주사위를 던집니다 : %d번째턴' % count)
                        me = random.randint(1, 4)
                        enemy = random.randint(1,2)
                        print('나 : %d' % me)
                        print('돌덩이 : %d' % enemy)

                        if me > enemy :
                            print('승리하셨군요')
                        else :
                            print('졌습니다')
                
                        count = count + 1
                        again = input('다시전투하려면 y를 입력해주세요')
                    else :

                        print('-' * 30)
                        print('주사위를 던집니다 : %d번째턴' % count)
                        me = random.randint(2, 6)
                        enemy = random.randint(1,3)
                        print('나 : %d' % me)
                        print('돌덩이 : %d' % enemy)

                        if me > enemy :     print('승리하였습니다')  
                        else :      
                               print('졌습니다')
                
                        count = count + 1
                        again = input('h를 입력해주세요')
                except :
                    print("에러가 발생하였습니다 종료합니다")
                    sys.exit()
            if B == 2:
                print('도주에 실패하였습니다. 사망하였습니다')
                again = input('h를 입력해주세요')
            else :
                print('잘못입력하셨습니다 종료합니다')
                sys.exit()
        

rin = 'h'
while rin == 'h':



          print('장소를 이동중입니다')  
          again = 'y'
          count = 1
          while again == 'y':
            print('야생의 돌덩이를 발견했습니다')
            print('싸우시겠습니까?')

            B = int(input('1.싸운다 2.도망친다'))

            if B == 1:
        
                try:
                    print('스킬 "딱밤" 를 사용하시겠습니까?')
                    C = int(input('1.사용한다 2.사용하지 않는다'))
                    import random
                    if C == 1:  
                        print('-' * 2)
                        print('주사위를 던집니다 : %d번째턴' % count)
                        me = random.randint(1, 4)
                        enemy = random.randint(1,2)
                        print('나 : %d' % me)
                        print('돌덩이 : %d' % enemy)

                        if me > enemy :
                            print('승리하셨군요')
                        else :
                            print('졌습니다')
                
                        count = count + 1
                        again = input('h를 입력해주세요')
                    else :

                        print('-' * 2)
                        print('주사위를 던집니다 : %d번째턴' % count)
                        me = random.randint(1, 4)
                        enemy = random.randint(1,2)
                        print('나 : %d' % me)
                        print('돌덩이 : %d' % enemy)

                        if me > enemy :
                            print('승리하였습니다')
                        else :
                            print('패배하였습니다')
                
                        count = count + 1
                        again = input('h를 입력해주세요')   
                except:
                    print("에러가 발생하였습니다 종료합니다")
                    sys.exit()
                    
            
            else :
                print('도주에 실패하였습니다. 사망하였습니다')
                again = input('다시전투하려면 y를 입력해주세요')
               
        
        

        
        

        
        


