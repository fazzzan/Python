import random
from random import choice

from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *



# тут будем писать наш код :)
heart_symbol = u'\u2764'

async def hello(update, context):
    if dialog.mode == "show":
        await show_dialog(update,context)
    if dialog.mode == "game":
        await game_dialog(update,context)
    else:
        # Отправка текста в ТГ
        await send_text(update, context, "*Привет*")
        await send_text(update, context, "_Как дела?_")
        await send_text(update, context, "Вы написали: " + update.message.text)

async def hello_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()

async def start(update, context):
    dialog.mode = "main"
    # Пригласительный текст из messages
    text = load_message("main")
    await send_text(update, context, text)
    await show_main_menu(update, context, {
        "start ": "главное меню бота",
        "show ": "Показать изучаемые термины",
        "game ": "игра в угадай термин"
    })

async def show(update, context):
    dialog.mode = "show"
    # Пригласительный текст из messages
    text = load_message("show")
    await send_text(update, context, text)

    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    while dialog.len > 0:
        # Отправка текста в ТГ
        await send_text(update, context, terms[dialog.len-1] + " - " + descr[dialog.len-1])
        dialog.len -= 1

async def show_dialog(update, context):
    text = update.message.text
    await send_text(update, context, text)

async def game(update, context):
    dialog.mode = "game"
    text = load_message("game")
    await send_text(update, context, text)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    dialog.term_choice = random.randrange(1, dialog.len)
    dialog.secret_term = terms[dialog.term_choice]
    dialog.secret_len = len(dialog.secret_term)
    await send_text(update, context, "Длина слова: " + str(dialog.secret_len))
    secret_index = 0
    dialog.string = []
    while secret_index < dialog.secret_len:
        dialog.string.append('?')
        secret_index += 1

    await send_text(update, context, "термин связан с понятием: " + descr[dialog.term_choice])
    await send_text(update, context, "термин зашифрован: " + str("".join(dialog.string)))

async def game_dialog(update, context):
    text = update.message.text.lower()
#    await send_text(update, context, str("".join(dialog.string)))
    dialog.string1 = update_string(text, dialog.secret_term, dialog.string)
    if dialog.string1 != dialog.secret_term:
        await send_text(update, context, dialog.string1)
        dialog.string = dialog.string1
    else:
        await send_text(update, context, "Оператор угадан, поздравляю")
        await send_photo(update, context, dialog.string1)
        await start(update, context)
#    secret_index = 0
#    dialog.string = []
#    while secret_index < dialog.secret_len:
#        dialog.string.append(dialog.string1[secret_index])
#        secret_index += 1



def update_string(letter, word, string):
    index = 0
    string1 = []
    secret_len = len(word)
    if letter != word:
        while index < secret_len:
            if string[index] != '?':
                string1.append(string[index])
            else:
                if word[index] == letter:
                    string1.append(letter)
                else:
                    string1.append(string[index])
            index += 1
    else:
        string1.append(letter)
#    print('letter ' + string1)
    return str("".join(string1))

dialog = Dialog()
dialog.mode = None
dialog.len = 0
dialog.term_choice = 0
dialog.secret_term = None
dialog.secret_len = 0
dialog.index = 0
dialog.string = []
dialog.string1 = []

# Подключаемся к чату
app = ApplicationBuilder().token("7655264179:AAE1LTOG7pDmaphBpFCmRE32rCF-uavuyxY").build()
# Обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show", show))
app.add_handler(CommandHandler("game", game))

# Обработчик текстов, которые пишутся в чат
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

# Обработчик нажатий на кнопки с шаблоном передаваемых значений в виде регулярки
# app.add_handler(CallbackQueryHandler(show_button, pattern = '^show_.*'))

# Обработчик нажатий на остальные кнопки
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()

