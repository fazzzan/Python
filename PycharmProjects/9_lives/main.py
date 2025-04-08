import random
from random import choice

from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *



# тут будем писать наш код :)
heart_symbol = u'\u2764'

# основной обработчик
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

# обработчик нажатия кнопки
async def hello_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()

# Пригласительный текст главного меню из файла main.txt
async def start(update, context):
    dialog.mode = "main"
    # текст главного меню из файла main.txt
    text = load_message("main")
    await send_text(update, context, text)
    await show_main_menu(update, context, {
        "start ": "Главное меню бота",
        "show ": "Показать изучаемые термины",
        "game ": "Игра в угадай термин"
    })

# пролистываем изучаемые термины через дефис
async def show(update, context):
    dialog.mode = "show"
    # Пригласительный текст из messages
    text = load_message("show")
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    # пролистывание терминов
    while dialog.len > 0:
        # Отправка текста в ТГ
        await send_text(update, context, terms[dialog.len-1] + " - " + descr[dialog.len-1])
        dialog.len -= 1

async def show_dialog(update, context):
    text = update.message.text
    await send_text(update, context, text)

    # надо придумать как оптимизировать показ данных из массива, чтобы он повторялись по алгоритму "Интервальные повторения"
    # конкретная формула: Y=2X+1, где Y означает день, когда информация начнет забываться, а X — день последнего повторения.
    # Таким образом, если вы выучили информацию, например, неделю назад, то повторить ее вам нужно будет через 8 дней.
async def game(update, context):
    dialog.mode = "game"
    text = load_message("game")
    await send_text(update, context, text)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)

    dialog.term_choice = random.choice([e for e in range(dialog.len) if e not in dialog.ind_choice])
    dialog.ind_choice.append(dialog.term_choice)
#    dialog.term_choice = random.randrange(1, dialog.len)

    dialog.secret_term = terms[dialog.term_choice]
    dialog.secret_len = len(dialog.secret_term)
    await send_text(update, context, "Длина термина: " + str(dialog.secret_len))
    secret_index = 0
    dialog.string = []
    while secret_index < dialog.secret_len:
        dialog.string.append('?')
        secret_index += 1

    await send_text(update, context, "термин связан с понятием: " + descr[dialog.term_choice])
    await send_text(update, context, "термин зашифрован: " + str("".join(dialog.string)))

async def game_dialog(update, context):
    dialog.mode = "game"
    text = update.message.text.lower()
#    await send_text(update, context, str("".join(dialog.string)))
    dialog.string1 = update_string(text, dialog.secret_term, dialog.string)
    if dialog.string1 != dialog.secret_term:
        await send_text(update, context, dialog.string1)
        dialog.string = dialog.string1
    else:
        await send_text(update, context, "Термин угадан, поздравляю, повторили " + str(len(dialog.ind_choice)) + " из " + str(dialog.len))
        await send_photo(update, context, dialog.string1)
        if len(dialog.ind_choice) < dialog.len:
            await send_text_buttons(update, context, "Еще раз?", {
                "game_start": "да",
                "game_stop": "нет"
            })
        else:
            await send_text(update, context, "Коллега, вы повторили все термины, приятно было поиграть.")
#        await game_button(update, context)
#    secret_index = 0
#    dialog.string = []
#    while secret_index < dialog.secret_len:
#        dialog.string.append(dialog.string1[secret_index])
#        secret_index += 1

async def game_button (update, context):
    query = update.callback_query.data
    await update.callback_query.answer()
    if query == "game_start":
        query_date = "да"
        await game(update, context)
    elif query == "game_stop":
        query_date = "нет"
        await send_text(update, context, "Нет - так нет. Приятно было поиграть.")


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
dialog.ind_choice = []

# Подключаемся к чату
app = ApplicationBuilder().token("7655264179:AAE1LTOG7pDmaphBpFCmRE32rCF-uavuyxY").build()
# Обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show", show))
app.add_handler(CommandHandler("game", game))

# Обработчик текстов, которые пишутся в чат
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

# Обработчик нажатий на кнопки с шаблоном передаваемых значений в виде регулярки
app.add_handler(CallbackQueryHandler(game_button, pattern="^game_.*"))

# Обработчик нажатий на остальные кнопки
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()

