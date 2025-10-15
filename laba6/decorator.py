import threading
from functools import wraps

# === Потокобезпечний декоратор ===
def thread_safe(func):
    lock = threading.Lock()

    @wraps(func)
    def wrapper(*args, **kwargs):
        with lock:
            print(f"🔒 Функція {func.__name__} виконується без конфліктів потоків")
            result = func(*args, **kwargs)
            print(f"🔓 Функція {func.__name__} завершена")
            return result
    return wrapper
