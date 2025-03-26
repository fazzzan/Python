import random
import string

from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

# тут будем писать наш код :)
heart_symbol = u'\u2764'

# меню бота
async def start(update, context):
    dialog.mode = "main"
    dialog.terms = load_terms("terms")
    dialog.descr = load_terms("descr")
    secret_term = random.choice(dialog.terms)
    await send_text(update, context, secret_term)
    await show_main_menu(update, context, {
        "start ": "Начить игру",
    })

# научим бота обрабатывать ответ
async def hello(update, context):
# ответ должен быть в рамках заданного пользователем контекста
    if dialog.mode == "gpt":
        await gpt_dialog(update, context)
    else:
        await send_text(update, context, "*Привет*")
        await send_text(update, context, "_Как дела?_")
        await send_text(update, context, "Вы написали: " + update.message.text)
        await send_photo(update, context, "avatar_main")
        await send_text_buttons(update, context, "Запустить процесс?", {
            "btn_start": "Запустить",
            "btn_stop": "Остановить"
        })

dialog = Dialog()
dialog.mode = None
dialog.terms = []
dialog.descr = []

# Подключаемся к чату
app = ApplicationBuilder().token("7655264179:AAE1LTOG7pDmaphBpFCmRE32rCF-uavuyxY").build()

# Обработчики команд
app.add_handler(CommandHandler("start", start))
# Обработчик текстов, которые пишутся в чат
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

# Обработчик нажатий на остальные кнопки
app.run_polling()