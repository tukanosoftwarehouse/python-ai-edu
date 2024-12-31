# Zegar cyfrowy - prosty program pokazujący moc Pythona!
# Autor: Tukano Software House
# Data: 2024

import time
from datetime import datetime


def wyswietl_czas():
    """Wyświetla aktualny czas w formacie cyfrowym."""
    while True:
        # Pobierz aktualny czas
        teraz = datetime.now()

        # Wyczyść ekran (działa na większości systemów)
        print("\033[H\033[J", end="")

        # Wyświetl ozdobny banner
        print("=" * 50)
        print("⌚ Super Zegar Cyfrowy w Pythonie!")
        print("=" * 50)

        # Wyświetl czas w atrakcyjnym formacie
        print(f"\n{teraz.hour:02d}:{teraz.minute:02d}:{teraz.second:02d}")
        print(f"📅 {teraz.day:02d}.{teraz.month:02d}.{teraz.year}")

        # Dodaj ozdobny separator
        print("\n" + "=" * 50)
        print("🚀 Zegar stworzony w kilku linijkach kodu!")
        print("=" * 50)

        # Odczekaj sekundę przed następnym odświeżeniem
        time.sleep(1)


def main():
    try:
        wyswietl_czas()
    except KeyboardInterrupt:
        print("\n\n👋 Dziękujemy za skorzystanie z zegara!")


if __name__ == "__main__":
    main()
