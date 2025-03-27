from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *


# тут будем писать наш код :)
async def start(update, context):
    dialog.mode = "main"
    # Пригласительный текст из messages
    text = load_message("main")
    # Отправка фото из images
    await send_photo(update, context, "main")
    # Отправка текста в ТГ
    await send_text(update, context, text)
    await show_main_menu(update, context, {
        "start ": "главное меню бота",
        "profile ": "генерация Tinder - профля 😎",
        "opener ": "сообщение для знакомства 🥰",
        "message": "переписка от вашего имени 😈",
        "date": "переписка со звездами 🔥",
        "gpt": "задать вопрос чату GPT 🧠"
    })


async def date(update, context):
    dialog.mode = "date"
    # Пригласительный текст из messages
    text_date = load_message("date")
    # Отправка фото из images
    await send_photo(update, context, "date")
    #    await send_text(update, context, text_date)
    # Отправка кнопок в ТГ
    await send_text_buttons(update, context, text_date, {
        "date_grande": "Ариана Гранде",
        "date_robbie": "Марго Робби",
        "date_zendaya": "Зендея",
        "date_gosling": "Райан Гослинг",
        "date_hardy": "Том Харди"
    })


async def date_dialog(update, context):
    # текст введенный пользователем в ТГ
    text = update.message.text
    # Отправка текста/заглушки в ТГ
    my_message = await send_text(update, context, "Набирает текст...")
    answer = await chatgpt.add_message(text)
    # Изменение текста/заглушки в ТГ
    await my_message.edit_text(answer)
#    await send_text(update, context, answer)

async def date_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()
    # Отправка фото из images для выбранного героя
    await send_photo(update, context, query)
    if query == "date_grande":
        query_date = "Ариана Гранде"
    elif query == "date_robbie":
        query_date = "Марго Робби"
    elif query == "date_zendaya":
        query_date = "Зендея"
    elif query == "date_gosling":
        query_date = "Райан Гослинг"
    elif query == "date_hardy":
        query_date = "Том Харди"
    await send_html(update, context, "Ого, " + query_date + ". Теперь попробуй пригласить на свидание за 5 сообщений")
    prompt = load_prompt(query)
    chatgpt.set_prompt(prompt)


async def message (update, context):
    dialog.mode = "message"
    # Пригласительный текст из messages
    text_message = load_message("message")
    # Отправка фото из images
    await send_photo(update, context, "message")
#    await send_text(update, context, text_message)
    # Отправка кнопок в ТГ
    await send_text_buttons(update, context, text_message, {
        "message_next": "Следующее сообщение",
        "message_date": "Пригласить на свидание"
    })
    dialog.list.clear()

async def message_dialog (update, context):
    # текст введенный пользователем в ТГ
    text = update.message.text
    dialog.list.append(text)

async def profile (update, context):
    dialog.mode = "profile"
    # Пригласительный текст из messages
    text = load_message("profile")
    # Отправка фото из images
    await send_photo(update, context, "profile")
    # Отправка текста в ТГ
    await send_text(update, context, text)
    dialog.user.clear()
    dialog.count = 0
    # Отправка текста в ТГ
    await send_text(update, context, "Сколько вам лет")

async def profile_dialog (update, context):
    dialog.count +=1
    # текст введенный пользователем в ТГ
    text = update.message.text
    if dialog.count == 1:
        # Сохранение текста пользователя в структуру
        dialog.user["age"] = text
        await send_text(update, context, "Кем вы работаете?")
    if dialog.count == 2:
        dialog.user["occupation"] = text
        await send_text(update, context, "У вас есть хобби?")
    if dialog.count == 3:
        dialog.user["hobby"] = text
        await send_text(update, context, "Что вам НЕ нравится в людях?")
    if dialog.count == 4:
        dialog.user["annoys"] = text
        await send_text(update, context, "Цель знакомства?")
    if dialog.count == 5:
        dialog.user["goals"] = text

        prompt = load_prompt("profile")
        # Склеиваем введенные сообщения в один текст
        user_info = dialog_user_info_to_str(dialog.user)
        # Отправка текста/заглушки в ТГ
        my_message = await send_text(update, context, "Обрабатывается полученная информация...")
        answer = await chatgpt.send_question(prompt, user_info)
        # Изменение текста/заглушки в ТГ
        await my_message.edit_text(answer)

async def opener (update, context):
    dialog.mode = "opener"
    # Пригласительный текст из messages
    text = load_message("opener")
    # Отправка фото из images
    await send_photo(update, context, "opener")
    # Отправка текста в ТГ
    await send_text(update, context, text)

    dialog.user.clear()
    dialog.count = 0
    # Отправка текста в ТГ
    await send_text(update, context, "Имя контакта ")

async def opener_dialog (update, context):
    dialog.count += 1
    # текст введенный пользователем в ТГ
    text = update.message.text
    if dialog.count == 1:
        # Сохранение текста пользователя в структуру
        dialog.user["name"] = text
        await send_text(update, context, "Сколько лет контакту?")
    elif dialog.count == 2:
        # Сохранение текста пользователя в структуру
        dialog.user["age"] = text
        await send_text(update, context, "Оцените внешность 1-10?")
    elif dialog.count == 3:
        # Сохранение текста пользователя в структуру
        dialog.user["handsome"] = text
        await send_text(update, context, "Кем работает?")
    elif dialog.count == 4:
        # Сохранение текста пользователя в структуру
        dialog.user["occupation"] = text
        await send_text(update, context, "Цель знакомства?")
    elif dialog.count == 5:
        # Сохранение текста пользователя в структуру
        dialog.user["goals"] = text

        prompt = load_prompt("opener")
        # Склеиваем введенные сообщения в один текст
        user_info = dialog_user_info_to_str(dialog.user)
        # Отправка текста/заглушки в ТГ
        my_message = await send_text(update, context, "Обрабатывается полученная информация...")
        answer = await chatgpt.send_question(prompt, user_info)
        # Изменение текста/заглушки в ТГ
        await my_message.edit_text(answer)


async def message_button (update, context):
    query = update.callback_query.data
    await update.callback_query.answer()
    # Пригласительный текст из prompt
    prompt = load_prompt(query)
    # Склеиваем введенные сообщения в один текст
    user_chat_history = "\n\n".join(dialog.list)
    # Отправка текста/заглушки в ТГ
    my_message = await send_text(update, context, "Набирает текст...")
    answer = await chatgpt.send_question(prompt, user_chat_history)
    # Изменение текста/заглушки в ТГ
    await my_message.edit_text(answer)


async def gpt(update, context):
    dialog.mode = "gpt"
    # Пригласительный текст из messages
    text = load_message("gpt")
    # Отправка фото из images
    await send_photo(update, context, "gpt")
    # Отправка текста в ТГ
    await send_text(update, context, text)


# В данной функции заложен алгоритм общения пользователя в контексте чата GPT
async def gpt_dialog(update, context):
    # текст введенный пользователем в ТГ
    text = update.message.text
    prompt = load_prompt("gpt")
    answer = await chatgpt.send_question(prompt, text)
    # Отправка текста в ТГ
    await send_text(update, context, answer)


# научим бота обрабатывать ответ
async def hello(update, context):
    # ответ должен быть в рамках заданного пользователем контекста
    if dialog.mode == "gpt":
        await gpt_dialog(update, context)
    elif dialog.mode == "date":
        await date_dialog(update, context)
    elif dialog.mode == "message":
        await message_dialog(update, context)
    elif dialog.mode == "profile":
        await profile_dialog(update, context)
    elif dialog.mode == "opener":
        await opener_dialog(update, context)
    else:
        # Отправка текста в ТГ
        await send_text(update, context, "*Привет*")
        await send_text(update, context, "_Как дела?_")
        await send_text(update, context, "Вы написали: " + update.message.text)
        # Отправка фото из images
        await send_photo(update, context, "avatar_main")
        # Отправка кнопок в ТГ
        await send_text_buttons(update, context, "Запустить процесс?", {
            "btn_start": "Запустить",
            "btn_stop": "Остановить"
        })


async def hello_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()

    if query == "btn_start":
        # Отправка текста в ТГ
        await send_text(update, context, "Процесс запущен")
    else:
        # Отправка текста в ТГ
        await send_text(update, context, "Процесс остановлен")


dialog = Dialog()
dialog.mode = None
dialog.list = []
dialog.user = { }
dialog.count = 0


chatgpt = ChatGptService(
    token="gpt:AgyOcazJ_9quXv71Cmo5u2qL1h_yytAiMaLywhYDr4xfoPUGP5gydVoBSJn5uc3GqTuBPJbtubJFkblB3TDn6T_un4buKEeUskeZ643kOrIteowKr2YUyjnyrDJyERTkMvgCT-Qm0H05svs_TEjdX546CNgN")

# Подключаемся к чату
app = ApplicationBuilder().token("7655264179:AAE1LTOG7pDmaphBpFCmRE32rCF-uavuyxY").build()
# Обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("date", date))
app.add_handler(CommandHandler("message", message))
app.add_handler(CommandHandler("gpt", gpt))
app.add_handler(CommandHandler("profile", profile))
app.add_handler(CommandHandler("opener", opener))

# Обработчик текстов, которые пишутся в чат
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

# Обработчик нажатий на кнопки с шаблоном передаваемых значений в виде регулярки
app.add_handler(CallbackQueryHandler(date_button, pattern="^date_.*"))
app.add_handler(CallbackQueryHandler(message_button, pattern="^message_.*"))

# Обработчик нажатий на остальные кнопки
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()

