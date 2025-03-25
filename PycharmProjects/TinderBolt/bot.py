from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

# тут будем писать наш код :)
async def start(update, context):
    dialog.mode = "main"
    text = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, text)
    await show_main_menu(update, context, {
        "start ": "главное меню бота",
        "profile ": "генерация Tinder - профля 😎",
        "opener ": "сообщение для знакомства 🥰",
        "message": "переписка от вашего имени 😈",
        "date": "переписка со звездами 🔥",
        "gpt": "задать вопрос чату GPT 🧠"
    })

async def gpt(update, context):
    dialog.mode = "gpt"
    text = load_message("gpt")
    await send_photo(update, context, "gpt")
    await send_text(update, context, text)

# В данной функции заложен алгоритм общения пользователя в контексте чата GPT
async def gpt_dialog(update, context):
    text = update.message.text
    prompt = load_prompt("gpt")
    answer = await chatgpt.send_question(prompt, text)
    await send_text(update, context, answer)


# научим бота обрабатывать ответ
async def hello(update, context):
# ответ должен быть в рамках заданного пользователем контекста
    if dialog.mode == "gpt":
        await gpt_dialog(update, context)
    else:
        await send_text(update, context, "*Привет*")
        await send_text(update, context, "_Как дела?_")
        await send_text(update, context, "Вы написали: "+ update.message.text)
        await send_photo(update, context, "avatar_main")
        await send_text_buttons(update, context, "Запустить процесс?", {
            "btn_start": "Запустить",
            "btn_stop": "Остановить"
        })

async def hello_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()

    if query == "btn_start":
        await send_text(update, context, "Процесс запущен")
    else:
        await send_text(update, context, "Процесс остановлен")

dialog = Dialog()
dialog.mode = None

chatgpt = ChatGptService(token="gpt:AgyOcazJ_9quXv71Cmo5u2qL1h_yytAiMaLywhYDr4xfoPUGP5gydVoBSJn5uc3GqTuBPJbtubJFkblB3TDn6T_un4buKEeUskeZ643kOrIteowKr2YUyjnyrDJyERTkMvgCT-Qm0H05svs_TEjdX546CNgN")

app = ApplicationBuilder().token("7655264179:AAE1LTOG7pDmaphBpFCmRE32rCF-uavuyxY").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gpt", gpt))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()
