def check_input(inp, answer):
    global score
    iCycle = 0
    Still_guess = True
    while Still_guess and iCycle <= 2:
        if inp.lower() == answer.lower():
            print('Ответ верный')
            score = score + 1
            Still_guess = False
        else:
            if iCycle < 2:
                inp = input('Ответ неверный, попробуйте еще раз: ')
            iCycle = iCycle + 1
    if iCycle > 2:
        print('Верный ответ: ' + answer)
score = 0

print('Тест "Животные"')
input1 = input('Какой медведь живет за полярным кругом? ')
check_input(input1, 'белый медведь')
input2 = input('Какое сухопутное животное самое быстрое? ')
check_input(input2, 'гепард')
input3 = input('Какое животное самое большое? ')
check_input(input3, 'синий кит')
print('Вы набрали ' + str(score) + ' очков')
