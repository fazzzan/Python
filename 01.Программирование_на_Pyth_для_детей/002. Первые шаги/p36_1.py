def check_input(inp, answer):
    global score
    iCycle = 0
    iCycle_count = 2
    Still_guess = True
    if answer == 'да':
        iCycle_count = 1
    while Still_guess and iCycle <= iCycle_count:
        if inp.lower() == answer.lower():
            print('Ответ верный')
            score = score + 3 - iCycle
            Still_guess = False
        else:
            if iCycle < iCycle_count:
                inp = input('Ответ неверный, попробуйте еще раз: ')
            iCycle = iCycle + 1
    if iCycle > 2:
        print('Верный ответ: ' + answer)
score = 0

print('Тест "Животные"')
input0 = input('I. Какое из этих животных рыба? \n \
1) Кит\n 2) Дельфин\n 3) Акула\n 4) Кальмар\n \
Введите 1, 2, 3 или 4. ')
check_input(input0, '3')
input1 = input('II. Какой медведь живет за полярным кругом? \n \
1) Белый медведь\n 2) Черный медведь\n 3) Зубастый медведь\n 4) Мимимишный медведь\n \
Введите 1, 2, 3 или 4. ')
check_input(input1, '1')
input2 = input('III. Какое сухопутное животное самое быстрое? ')
check_input(input2, 'гепард')
input3 = input('IV. Какое животное самое большое? ')
check_input(input3, 'синий кит')
input4 = input('V. Мыши - это млекопитающие, да или нет? ')
check_input(input4, 'да')

print('Вы набрали ' + str(score) + ' очков')


