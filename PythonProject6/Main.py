import telebot
from config import TELEGRAM_BOT_TOKEN
from handlers import register_handlers

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("❌ Помилка: TELEGRAM_BOT_TOKEN не знайдено у .env")
        return

    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
    register_handlers(bot)

    print("✅ Бот запущений. Очікую повідомлень...")
    try:
        # просто без аргументів
        bot.infinity_polling()
    except Exception as e:
        print(f"🔥 Критична помилка: {e}")

if __name__ == '__main__':
    main()
