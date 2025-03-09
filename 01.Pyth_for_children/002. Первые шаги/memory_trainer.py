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

print('Тест на знание команд')
input0 = input('I. Как импортировать модуль? ')
check_input(input0, 'import')
input1 = input('II. Какая команда отвечает за вывод на экран? ')
check_input(input1, 'print')
input2 = input('II. Какая команда отвечает за ввод данных пользователя? ')
check_input(input2, 'input')
input3 = input('III. Создать список <list> и наполнить его значениями: 1, 2, one, two ? ')
check_input(input3, "list = ['1', '2', 'one', 'two']")
input4 = input('IV. Какое животное самое большое? ')
check_input(input4, 'синий кит')
input5 = input('V. Мыши - это млекопитающие, да или нет? ')
check_input(input5, 'да')

print('Вы набрали ' + str(score) + ' очков')


