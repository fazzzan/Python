import random
from random import choice

from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *



# тут будем писать наш код :)
heart_symbol = u'\u2764'

# основной обработчик
async def hello(update, context):
    if dialog.mode == "show" or dialog.mode == "show1_3" or dialog.mode == "show1_5" or dialog.mode == "show1_7" \
        or dialog.mode == "show1_11" or dialog.mode == "show2_1" or dialog.mode == "show2_4" \
        or dialog.mode == "show2_7" or dialog.mode == "show2_9" or dialog.mode == "show2_10" \
        or dialog.mode == "show2_12" or dialog.mode == "show2_13" or dialog.mode == "show2_14":
        await show_dialog(update,context)
    if dialog.mode == "game" or dialog.mode == "game1_3" or dialog.mode == "game1_5" or dialog.mode == "game1_7" \
        or dialog.mode == "game1_11" or dialog.mode == "game2_1" or dialog.mode == "game2_4" \
        or dialog.mode == "game2_7" or dialog.mode == "game2_9" or dialog.mode == "game2_10" \
        or dialog.mode == "game2_12" or dialog.mode == "game2_13" or dialog.mode == "game2_14":
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
    await send_html(update, context, text)
    await show_main_menu(update, context, {
        "start "  : "Главное меню бота",
#        "show "   : "Термины всех разделов",
        "game ": "Игра в угадай термин",
#        "game_lite ": "Облегченная игра в угадай термин",
        "show1_3 ": "Термины раздела 1.3",
        "show1_5 ": "Термины раздела 1.5",
        "show1_7 ": "Термины раздела 1.7",
        "show1_11 ": "Термины раздела 1.11",
        "show2_1 ": "Термины раздела 2.1",
        "show2_4 ": "Термины раздела 2.4",
        "show2_7 ": "Термины раздела 2.7",
        "show2_9": "Термины раздела 2.9",
        "show2_10": "Термины раздела 2.10",
        "show2_12": "Термины раздела 2.12",
        "show2_13": "Термины раздела 2.13",
        "show2_14": "Термины раздела 2.14",
        "show3_1": "Термины раздела 3.1"
    })

# пролистываем изучаемые термины через дефис
async def show(update, context):
    dialog.mode = "show"
    dialog.ind_choice = []
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
        subterm = terms[dialog.len - 1].split(";")
        await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show1_3(update, context):
    dialog.mode = "show1_3"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 1.3""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('1.3;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show1_5(update, context):
    dialog.mode = "show1_5"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 1.5""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('1.5;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show1_7(update, context):
    dialog.mode = "show1_7"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 1.7""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('1.7;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_html(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show1_11(update, context):
    dialog.mode = "show1_11"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 1.11""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('1.11;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_1(update, context):
    dialog.mode = "show2_1"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.1""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.1;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_4(update, context):
    dialog.mode = "show2_4"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.4""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.4;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_7(update, context):
    dialog.mode = "show2_7"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.7""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.7;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_9(update, context):
    dialog.mode = "show2_9"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.9""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.9;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_10(update, context):
    dialog.mode = "show2_10"
    dialog.ind_choice = []
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.10""".format(a = str(load_message("show")), \
                                                    b = str(dialog.mode.replace('show', '')), \
                                                    c = str(len(terms)) \
                                                        )
    await send_html(update, context, text)

    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.10;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ str(dialog.len) + " - " +
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_12(update, context):
    dialog.mode = "show2_12"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.12""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.12;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ str(dialog.len) + " - " +
            await send_text(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_13(update, context):
    dialog.mode = "show2_13"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.13""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.13;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ str(dialog.len) + " - " +
            await send_html(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

# пролистываем изучаемые термины выбранного раздела через дефис
async def show2_14(update, context):
    dialog.mode = "show2_14"
    dialog.ind_choice = []
    # Пригласительный текст из messages
    text = """Выбрали повторение 2.14""".format(a = str(load_message("show")), b = str(dialog.mode.replace('show', '')))
    await send_text(update, context, text)
    # загрузка терминов и описаний в список(массив данных)
    terms = load_terms("terms")
    descr = load_descr("descr")
    dialog.len = len(terms)
    iterms1_3 = []
    # пролистывание терминов
    while dialog.len >= 1:
       # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
        if terms[dialog.len-1].startswith('2.14;') == True:
            iterms1_3.append(dialog.len-1)
            subterm = terms[dialog.len-1].split(";")
            # Отправка текста в ТГ str(dialog.len) + " - " +
            await send_html(update, context, subterm[2] + " - " + descr[dialog.len-1])
        dialog.len -= 1

async def show_dialog(update, context):
    text = update.message.text
    await send_text(update, context, text)

    # надо придумать как оптимизировать показ данных из массива, чтобы он повторялись по алгоритму "Интервальные повторения"
    # конкретная формула: Y=2X+1, где Y означает день, когда информация начнет забываться, а X — день последнего повторения.
    # Таким образом, если вы выучили информацию, например, неделю назад, то повторить ее вам нужно будет через 8 дней.
async def game(update, context):
    # text = """текущий режим - {0}""".format(dialog.mode)
    # await send_html(update, context, text)
    # text = load_message("game")
    # await send_text(update, context, text)

    terms_all = load_terms("terms")
    descr_all = load_descr("descr")
    dialog.len = len(terms_all)
    terms = []
    descr = []
    img = []

    if dialog.mode == "show" or dialog.mode == "game":
        dialog.mode = "game"
        text = load_message("game")
        await send_text(update, context, text)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            subterm = terms_all[dialog.len - 1].split(";")
            # Заполнение массива значениями из нужного раздела ТГ
            terms.append(subterm[2])
            descr.append(descr_all[dialog.len - 1])
            img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show1_3" or dialog.mode == "game1_3":
        dialog.mode = "game1_3"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('1.3;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show1_5" or dialog.mode == "game1_5":
        dialog.mode = "game1_5"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('1.5;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show1_7" or dialog.mode == "game1_7":
        dialog.mode = "game1_7"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('1.7;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show1_11" or dialog.mode == "game1_11":
        dialog.mode = "game1_11"
        text = load_message("game")
        await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('1.11;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_1" or dialog.mode == "game2_1":
        dialog.mode = "game2_1"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.1;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_4" or dialog.mode == "game2_4":
        dialog.mode = "game2_4"
        text = load_message("game")
        await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.4;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_7" or dialog.mode == "game2_7":
        dialog.mode = "game2_7"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.7;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_9" or dialog.mode == "game2_9":
        dialog.mode = "game2_9"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.9;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_10" or dialog.mode == "game2_10":
        dialog.mode = "game2_10"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.10;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_12" or dialog.mode == "game2_12":
        dialog.mode = "game2_12"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.12;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_13" or dialog.mode == "game2_13":
        dialog.mode = "game2_13"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.13;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

    elif dialog.mode == "show2_14" or dialog.mode == "game2_14":
        dialog.mode = "game2_14"
        #text = load_message("game")
        #await send_text(update, context, text)
        dialog.len = len(terms_all)
        # запоминание терминов нужного раздела
        while dialog.len >= 0:
            # await send_text(update, context, terms[dialog.len - 1] + " - " + descr[dialog.len - 1] + str(terms[dialog.len-1].startswith('1.3')))
            if terms_all[dialog.len - 1].startswith('2.14;') == True:
                subterm = terms_all[dialog.len - 1].split(";")
                # Заполнение массива значениями из нужного раздела ТГ
                terms.append(subterm[2])
                descr.append(descr_all[dialog.len - 1])
                img.append(subterm[1])
            dialog.len -= 1
        dialog.len = len(terms)

# индекс термина, который выбирается с учетом того что слово не было ранее правильно набрано
    if len(dialog.ind_choice) == 0:
        dialog.term_choice = random.choice(range(dialog.len))
    else:
        dialog.term_choice = random.choice([e for e in range(dialog.len) if e not in dialog.ind_choice])
#    dialog.ind_choice.append(dialog.term_choice)
#    dialog.term_choice = random.randrange(1, dialog.len)
# повторяемый термин
    dialog.secret_term = terms[dialog.term_choice]
    dialog.secret_img = img[dialog.term_choice]
    dialog.secret_len = len(dialog.secret_term)
    # await send_text(update, context, "Длина термина: " + str(dialog.secret_len))
    secret_index = 0
    dialog.string = []
    while secret_index < dialog.secret_len:
        dialog.string.append('?')
        secret_index += 1

    await send_html(update, context, "Функция/метод выполняют: " + descr[dialog.term_choice])
    # await send_text(update, context, "термин зашифрован: " + str("".join(dialog.string)))
    await send_text(update, context, str("".join(dialog.string)))
    dialog.err = False

async def game_dialog(update, context):
    if dialog.mode == "game" or dialog.mode == "game1_3" or dialog.mode == "game1_5" or dialog.mode == "game1_7" \
        or dialog.mode == "game1_11" or dialog.mode == "game2_1" or dialog.mode == "game2_4" \
        or dialog.mode == "game2_7" or dialog.mode == "game2_9" or dialog.mode == "game2_10" \
        or dialog.mode == "game2_12" or dialog.mode == "game2_13" or dialog.mode == "game2_14":
        text = update.message.text
    #    await send_text(update, context, str("".join(dialog.string)))
        dialog.string1 = update_string(text, dialog.secret_term, dialog.string)
    # Задел для облегченного варианта
    #    await send_html(update, context, """{0} из {1}""".format(str(dialog.string1), str(dialog.secret_term)))
    #    await send_html(update, context, """{0}""".format(str(dialog.string1), str(dialog.secret_term)))
        if dialog.string1 != dialog.secret_term:
            await send_html(update, context, dialog.string1)
            dialog.string = dialog.string1
            dialog.err = True
        else:
            if dialog.err == False:
                dialog.ind_choice.append(dialog.term_choice)
                await send_text(update, context, """Чётко, на изи. Молодца: {0} из {1}""".format(str(len(dialog.ind_choice)), str(dialog.len)))
            else:
                await send_text(update, context, """Рофлишь? Засчитать не могу: {0} из {1}""".format(str(len(dialog.ind_choice)), str(dialog.len)))
                #await send_photo(update, context, dialog.string1)
            await send_photo(update, context, str(dialog.secret_img))
            if len(dialog.ind_choice) < dialog.len:
            # if len(dialog.ind_choice) <= 3:
                await send_text_buttons(update, context, "Еще раз?", {
                    "game_start": "да",
                    "game_stop": "нет"
                })
            else:
                if len(dialog.ind_choice) >= 11 and len(dialog.ind_choice) <= 20:
                    text = "Коллега, вы повторили {n1} терминов из {n}, раздела {n2}.".format(n1 = len(dialog.ind_choice), n = dialog.len, n2 = str(dialog.mode.replace('game', '')))
                elif len(dialog.ind_choice)%10 == 2 or len(dialog.ind_choice)%10 == 3 or len(dialog.ind_choice)%10 == 4:
                    text = "Коллега, вы повторили {n1} термина из {n}, раздела {n2}.".format(n1=len(dialog.ind_choice), n=dialog.len, n2 = str(dialog.mode.replace('game', '')))
                elif len(dialog.ind_choice)%10 == 1:
                    text = "Коллега, вы повторили {n1} термин из {n}, раздела {n2}.".format(n1 = len(dialog.ind_choice), n = dialog.len, n2 = str(dialog.mode.replace('game', '')))
                else:
                    text = "Коллега, вы повторили {n1} терминов из {n}, раздела {n2}.".format(n1=len(dialog.ind_choice), n=dialog.len, n2 = str(dialog.mode.replace('game', '')))
                await send_html(update, context, text)
                dialog.ind_choice = []
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
dialog.mode = None # режим работы диалога
dialog.len = 0 # длина массива содержащего повторяемые термины
dialog.term_choice = 0 # индекс термина для повторения
dialog.secret_term = None # повторяемый термин
dialog.secret_img = None # иллюстрация к повторяемому термину
dialog.secret_len = 0 # количество символов в повторяемом термине
dialog.index = 0
dialog.string = [] # Зашифрованный символами ? повторяемый термин
dialog.string1 = [] # Зашифрованный повторяемый термин, но с уже частично раскрытыми символами
dialog.ind_choice = [] # Список повторенных индексов
dialog.err = False # Термин угадан с первого раза и без ошибок

# Подключаемся к чату
app = ApplicationBuilder().token("7655264179:AAE1LTOG7pDmaphBpFCmRE32rCF-uavuyxY").build()
# Обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show", show))
app.add_handler(CommandHandler("show1_3", show1_3))
app.add_handler(CommandHandler("show1_5", show1_5))
app.add_handler(CommandHandler("show1_7", show1_7))
app.add_handler(CommandHandler("show1_11", show1_11))
app.add_handler(CommandHandler("show2_1", show2_1))
app.add_handler(CommandHandler("show2_4", show2_4))
app.add_handler(CommandHandler("show2_7", show2_7))
app.add_handler(CommandHandler("show2_9", show2_9))
app.add_handler(CommandHandler("show2_10", show2_10))
app.add_handler(CommandHandler("show2_12", show2_12))
app.add_handler(CommandHandler("show2_13", show2_13))
app.add_handler(CommandHandler("show2_14", show2_14))
#app.add_handler(CommandHandler("show2_9", show2_9))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("game1_3", game))
app.add_handler(CommandHandler("game1_5", game))
app.add_handler(CommandHandler("game1_7", game))
app.add_handler(CommandHandler("game1_11", game))
app.add_handler(CommandHandler("game2_1", game))
app.add_handler(CommandHandler("game2_4", game))
app.add_handler(CommandHandler("game2_7", game))
app.add_handler(CommandHandler("game2_9", game))
app.add_handler(CommandHandler("game2_10", game))
app.add_handler(CommandHandler("game2_12", game))
app.add_handler(CommandHandler("game2_13", game))
app.add_handler(CommandHandler("game2_14", game))

# Обработчик текстов, которые пишутся в чат
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

# Обработчик нажатий на кнопки с шаблоном передаваемых значений в виде регулярки
app.add_handler(CallbackQueryHandler(game_button, pattern="^game_.*"))

# Обработчик нажатий на остальные кнопки
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()

