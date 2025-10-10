# bot.py
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Завантажуємо токен із .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не знайдено у файлі .env")

# Обробник повідомлень — просто повторює текст користувача
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(update.message.text)

async def main():
    # Створюємо застосунок (бот)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Додаємо обробник усіх повідомлень
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Бот запущений. Натисни Ctrl+C щоб зупинити.")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
