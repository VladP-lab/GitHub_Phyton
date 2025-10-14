import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# === Завантаження токена з config/.env ===
load_dotenv(r"C:\Users\user\PycharmProjects\PythonProject6\.env")
TOKEN = os.getenv("BOT_TOKEN")

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Ти заходиш у старе приміщення... Повітря густе від пилу й тиші.\n"
        "Перед тобою — три об’єкти:\n"
        "🪞 Вікно, 🗿 Статуя, 🖼 Картина.\n\n"
        "Що оглянеш?"
    )
    buttons = [
        [InlineKeyboardButton("🪞 Вікно", callback_data="window")],
        [InlineKeyboardButton("🗿 Статуя", callback_data="statue")],
        [InlineKeyboardButton("🖼 Картина", callback_data="painting")]
    ]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

# === Обробка вибору ===
async def choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "window":
        text = (
            "Ти підходиш до вікна. Скло каламутне, але крізь нього видно місячне сяйво.\n"
            "На мить здається, що у відбитті блиснули чиїсь очі..."
        )
    elif query.data == "statue":
        text = (
            "Статуя стоїть посеред залу. Вона дивно реалістична.\n"
            "Коли ти нахиляєшся ближче — здається, що її губи ледь рухаються..."
        )
    elif query.data == "painting":
        text = (
            "Картина стара й потріскана. На ній — сім’я, яка позує біля цього ж приміщення.\n"
            "І серед них — хтось, схожий на тебе."
        )
    else:
        text = "Невідомий вибір."

    await query.edit_message_text(text)

# === Головна функція ===
def main():
    if not TOKEN:
        raise ValueError("❌ Токен не знайдено. Переконайся, що в config/.env є BOT_TOKEN.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(choice))

    app.run_polling()

if __name__ == "__main__":
    main()
