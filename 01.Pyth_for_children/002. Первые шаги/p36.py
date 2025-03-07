iCount = 0
iCycle = 0

print('Тест "Животные"')
input1 = input('Какой медведь живет за полярным кругом? ')
while iCycle <= 1:    
    if input1 == 'белый':
        print('Ответ верный')
        iCycle = 4
        iCount = iCount + 1
        # print(str(iCycle))
    elif input1 == 'белый медведь':
        print('Ответ верный')
        iCycle = 4
        iCount = iCount + 1
        # print(str(iCycle))
    else:
        input1 = input('Ответ неверный, попробуйте еще раз: ')
        iCycle = iCycle + 1
        iCount = iCount + 0
        # print(str(iCycle))
# print('Вы набрали ' + str(iCount) + ' очков')
iCycle = 0
input2 = input('Какое сухопутное животное самое быстрое? ')
while iCycle <= 1:    
    if input2 == 'гепард':
        print('Ответ верный')
        iCycle = 4
        iCount = iCount + 1
        # print(str(iCycle))
    else:
        input2 = input('Ответ неверный, попробуйте еще раз: ')
        iCycle = iCycle + 1
        iCount = iCount + 0
        # print(str(iCycle))
# print('Вы набрали ' + str(iCount) + ' очков')    
iCycle = 0
input3 = input('Какое животное самое большое? ')
while iCycle <= 1:
    if input3 == 'синий кит':
        print('Ответ верный')
        iCycle = 4
        iCount = iCount + 1
        # print(str(iCycle))
    else:
        input3 = input('Ответ неверный, попробуйте еще раз: ')
        iCycle = iCycle + 1
        iCount = iCount + 0
        # print(str(iCycle))
        
print('Вы набрали ' + str(iCount) + ' очков')
        
