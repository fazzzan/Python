# ТЗ

![](../_picturres/image_20250325175901.png)

ТГ-бот может общаться с другими
1. Общаться с чатом GPT
2. Генерить сообщения в Tinder
3. Помощник при переписке в Tinder

# Открываем шаблон проекта

Закрываем старый проект

![](../_picturres/image_20250325180332.png)

Открываем новый

![](../_picturres/image_20250325180438.png)

Можно задать интерпретатор
![](../_picturres/image_20250325180700.png)

# Установка через интерпретатор библиотек

![](../_picturres/image_20250325181252.png)
```
pip install python-telegram-bot
```
Если установка была проделана правильно, то все подчеркивания красным - уйдут. Следующая команда для установки библиотеки OpenAI

```
pip install openai
```

![](../_picturres/image_20250325185603.png)

# Первый запуск

Все с ошибками, так как еще не получен Бот-токен

![](../_picturres/image_20250325185759.png)
![](../_picturres/image_20250325185832.png)

# Регистрация бота в ТГ

Через botfather

![](../_picturres/image_20250325190119.png)

```
/newbot
...
TD_AI_bot_abc
...
TD_AI_bot_abc_bot
...
You will find it at t.me/TD_AI_bot_abc_bot. 
...
Use this token to access the HTTP API:
7655264179:AAE1LTOG7pDmaphBpFCmRE32rCF-uavuyxY
Keep your token secure and store it safely, it can be used by anyone to control your bot.
```

![](../_picturres/image_20250325190533.png)

ТГ-токен - замена пары логин/пасс для ТГ

![](../_picturres/image_20250325190652.png)
![](../_picturres/image_20250325190727.png)

# Второй запуск

Уже без ошибок

![](../_picturres/image_20250325190820.png)

И мы можем уже зайти в этого бота и посмотреть что с ним:

![](../_picturres/image_20250325191015.png)

Можно нажать кнопку START, ничего не произойдет, написанного кода - нет
Добавим код, теперь печать любого слова в ТГ вызовет ответное приветствие

![](../_picturres/image_20250325191814.png)

```
Важно! Слова async и await обязательно использовать, т.к. библиотека python-telegram-bot полностью асинхронная. Поэтому мы должны тоже писать асинхронные функции – и использовать ключевое слово async перед объявлением наших функций. Перед вызовом же асинхронной функции нужно обязательно писать ключевое слово await.  
```

![](../_picturres/image_20250325192103.png)

![](../_picturres/image_20250325192412.png)

## MD в ТГ

![](../_picturres/image_20250325192533.png)

## Вывод в чат доп. информации
### Фото

![](../_picturres/image_20250325193024.png)
 ![](../_picturres/image_20250325193137.png)
### Кнопки

![](../_picturres/image_20250325193526.png)
![](../_picturres/image_20250325193624.png)

Чтобы при нажатии на кнопки что-то происходило - надо добавить хэндлер
 ![](../_picturres/image_20250325194040.png)

### START

![](../_picturres/image_20250325194919.png)

![](../_picturres/image_20250325195559.png)

Исправляем ошибку

![](../_picturres/image_20250325195827.png)
![](../_picturres/image_20250325200016.png)

![](../_picturres/image_20250325200151.png)

![](../_picturres/image_20250325200325.png)
