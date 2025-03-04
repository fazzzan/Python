Age_min = 8
Age_max = 50
Rost_min = 1.4
Rost_max = 1.9
Age = input('Сколько тебе лет? ')

if ((int(Age) < 8) or (int(Age) > 50)):
    print('Не проходишь по возрасту')    
else:
    Rost = input('Введи свой рост ')
    if ((float(Rost) >= 1.4) and (float(Rost) <= 1.9)):
        print('Катись с богом, проходишь')
    else:
        print('Не проходишь по росту')
        
