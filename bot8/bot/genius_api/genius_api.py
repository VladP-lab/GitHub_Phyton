import requests
from config import GENIUS_SEARCH_URL, GENIUS_HEADERS, GENIUS_ACCESS_TOKEN

def search_genius(query: str):
    """Виконує пошук пісень через Genius API."""
    if not GENIUS_ACCESS_TOKEN:
        return None

    params = {"q": query}
    try:
        response = requests.get(GENIUS_SEARCH_URL, headers=GENIUS_HEADERS, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка при запиті до Genius API: {e}")
        return None


def extract_best_song_info(genius_response):
    """Витягує інформацію про найкращий результат пошуку."""
    if genius_response and 'response' in genius_response and 'hits' in genius_response['response']:
        hits = genius_response['response']['hits']
        if hits:
            song_info = hits[0]['result']
            return {
                "title": song_info.get("title"),
                "artist": song_info.get("artist_names"),
                "url": song_info.get("url")
            }
    return None
