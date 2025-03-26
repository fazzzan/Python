import random
import string 

terms = ['print', 'input', 'module', 'webbrowser', 'random', 'random.choice', \
         'random.randrange', 'string.punctuation', 'range', 'join', \
         'len', 'replace', 'reversed', 'lower', 'upper', 'break', 'for', \
         'if..elif..else', 'while', 'int', 'float']

descr = ['вывод на экран', 'считывание данных', 'блоки кода', 'модуль отвечающий за открытие странички', 'модуль произвольных символов', 'выбор произвольного символа', \
         'выбор произвольного числа', 'строковые спецсимволы', 'диапазон чисел', 'соединение подстрок', \
         'длина', 'замена', 'обратный вывод', 'нижний регистр', 'верхний регистр', 'выход из цикла', 'цикл в диапазоне', \
         'ветвление кода', 'цикл до выполнения условия', 'преобразование в целое число', 'преобразование в вещественное число']

done = ['-', '-', '-', '-', '-', '-', \
         '-', '-', '-', '-', \
         '-', '-', '-', '-', '-', '-', '-', \
         '-', '-', '-', '-']

heart_symbol = u'\u2764'

def start_game():
    global lives
    global secret_term
    global secret_len
    global string
    global winner
    winner = False
    string = []
    lives = 9
    secret_term = random.choice(terms)
    ind1 = terms.index(secret_term) - 1
    if '-' in done: 
        while done[ind1] == '+':
            secret_term = random.choice(terms)
            ind1 = terms.index(secret_term) - 1
    else:
        abc = input('Повторение окончено, закругляемся')
        winner = True
        lives = 0
    secret_len = len(secret_term)
#    string = ''
    index = 0
    while index < secret_len:
        string.append('?')
        index = index + 1

#    for counter in range(secret_len):
#        string = string + '?'


def update_string(letter, word, string):
    index = 0
    string1 = ''
    while index < secret_len:
        if letter == word[index]:
#            string1 = string1 + letter            
            string[index] = letter
#        else:
#            string1 = string1 + string[index]
        index = index + 1
#    print('letter ' + string1)
    return string

def check_lives():
    global lives
    global secret_term
    global secret_len
    global string
    global winner
    global unknown_letters
    unknown_letters = len(secret_term)
    while lives > 0:
        if unknown_letters > 0:
            print(string)
            print('Осталось жизней: ' + heart_symbol * lives)
            ind = terms.index(secret_term)
            print('Термин имеет отношение к ' + descr[ind])
            letter_in_secret = input('Угадайте букву или слово целиком: ')
#        print(letter_in_secret + ' - ' + secret_term)
            print(letter_in_secret)
            if letter_in_secret == '':
                print('Это неспортивно, снимаю 1 жизнь')
                lives = lives - 1
            elif letter_in_secret == secret_term:
                print('Вы угадали термин: ' + secret_term)
                ind = terms.index(secret_term)
                done[ind] = '+'
                print(done)
                break
            elif letter_in_secret in secret_term:
                # передаем на проверку букву, термин, строку ???????
                string = update_string(letter_in_secret, secret_term, string)
                aaa = secret_term.count(letter_in_secret)
                while aaa > 0:
                    unknown_letters = unknown_letters - 1
                    aaa = aaa - 1
#                print(str(unknown_letters))
            else:
                print('Неправильно, -1 жизнь потеряна')
                lives = lives - 1
        else:
            print('Вы угадали термин: ' + secret_term)
            ind = terms.index(secret_term)
            done[ind] = '+'
            print(done)
            break

oncemore = input('Практикуем термины y/n[y]?')
if oncemore == '':
    oncemore = 'y'
while oncemore == 'y':
    start_game()
    print(lives)
    check_lives()
    print(oncemore)
    oncemore = input('Практикуем дальше y/n[y]?')
    if oncemore == '':
        oncemore = 'y'
        print(oncemore)

if oncemore == 'n':
    print('Повторение не окончено, но закругляемся')
    winner = True
