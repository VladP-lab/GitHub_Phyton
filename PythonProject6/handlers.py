from config import GENIUS_ACCESS_TOKEN
from genius_api import search_genius, extract_best_song_info

def register_handlers(bot):
    """Реєструє всі обробники команд і повідомлень."""

    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(
            message.chat.id,
            "Привіт! 🎵 Я бот для пошуку пісень через Genius.\n"
            "Просто надішли мені назву пісні або виконавця!"
        )

    @bot.message_handler(content_types=['text'])
    def search_message_handler(message):
        user_query = message.text
        chat_id = message.chat.id

        if user_query.startswith('/'):
            return

        if not GENIUS_ACCESS_TOKEN:
            bot.send_message(chat_id, "❌ Токен Genius API не налаштовано. Пошук неможливий.")
            return

        bot.send_message(chat_id, f"🔎 Шукаю '{user_query}' на Genius...")

        genius_data = search_genius(user_query)
        if genius_data:
            song_info = extract_best_song_info(genius_data)
            if song_info:
                response_text = (
                    f"🎶 <b>Знайдено:</b>\n"
                    f"<b>Назва:</b> {song_info['title']}\n"
                    f"<b>Виконавець:</b> {song_info['artist']}\n"
                    f"<a href='{song_info['url']}'>Перейти на Genius</a>"
                )
                bot.send_message(chat_id, response_text, parse_mode='HTML', disable_web_page_preview=True)
            else:
                bot.send_message(chat_id, "🤷 Нічого не знайдено за цим запитом.")
        else:
            bot.send_message(chat_id, "⚠️ Виникла помилка при з'єднанні з Genius API.")
