import os
from dotenv import load_dotenv

# Завантаження змінних середовища
load_dotenv()

# Telegram токен
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Genius токен
GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

# URL для запитів
GENIUS_SEARCH_URL = "https://api.genius.com/search"

# Заголовки для авторизації
GENIUS_HEADERS = {
    "Authorization": f"Bearer {GENIUS_ACCESS_TOKEN}"
}
