import threading
import time
from decorator import thread_safe

@thread_safe
def critical_section(name):
    print(f"{name} почав роботу...")
    time.sleep(1)
    print(f"{name} завершив роботу ✅")

def main():
    # Створюємо кілька потоків, що одночасно викликають функцію
    threads = [
        threading.Thread(target=critical_section, args=(f"Потік {i+1}",))
        for i in range(3)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("🔥 Усі потоки завершили роботу")

if __name__ == "__main__":
    main()
