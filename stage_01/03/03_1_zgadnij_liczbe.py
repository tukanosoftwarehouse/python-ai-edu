# Zgadnij liczbę - prosty program pokazujący moc Pythona!
# Autor: Tukano Software House
# Data: 2024

import random


def sprawdz_odpowiedz(liczba, proba):
    """Sprawdza odpowiedź użytkownika i zwraca wskazówkę."""
    if proba < liczba:
        return "📈 Za mało! Spróbuj większej liczby."
    elif proba > liczba:
        return "📉 Za dużo! Spróbuj mniejszej liczby."
    else:
        return "🎯 Brawo! Zgadłeś liczbę!"


def main():
    # Wyświetl przyjazny banner powitalny
    print("=" * 50)
    print("🎲 Witaj w grze Zgadnij Liczbę!")
    print("Spróbuj odgadnąć liczbę od 1 do 100")
    print("=" * 50)

    # Wylosuj liczbę do zgadnięcia
    liczba = random.randint(1, 100)
    proby = 0

    try:
        while True:
            # Pobierz próbę od użytkownika
            proba = int(input("\n🤔 Podaj swoją propozycję: "))
            proby += 1

            # Sprawdź odpowiedź i wyświetl wskazówkę
            wynik = sprawdz_odpowiedz(liczba, proba)
            print(wynik)

            # Jeśli użytkownik zgadł, zakończ grę
            if proba == liczba:
                print(f"\n🌟 Gratulacje! Odgadłeś liczbę w {proby} próbach!")
                break

    except ValueError:
        print("\n❌ Ups! Wprowadź poprawną liczbę.")
    except KeyboardInterrupt:
        print("\n\n❌ Przerwano grę.")

    print("\n👋 Dziękujemy za wspólną zabawę!")


if __name__ == "__main__":
    main()
