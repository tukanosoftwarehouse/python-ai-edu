# Kalkulator napiwków - prosty program pokazujący moc Pythona!
# Autor: Tukano Software House
# Data: 2024


def oblicz_napiwek(kwota, procent):
    """Oblicza wysokość napiwku na podstawie kwoty i procentu."""
    return kwota * (procent / 100)


def main():
    # Wyświetl przyjazny banner powitalny
    print("=" * 50)
    print("🎯 Witaj w Kalkulatorze Napiwków!")
    print("Pomożemy Ci szybko obliczyć odpowiedni napiwek")
    print("=" * 50)

    try:
        # Pobierz dane od użytkownika
        kwota = float(input("\n💰 Podaj kwotę rachunku: "))
        procent = float(input("📊 Podaj procent napiwku (np. 10): "))

        # Oblicz napiwek i całkowitą kwotę
        napiwek = oblicz_napiwek(kwota, procent)
        suma = kwota + napiwek

        # Wyświetl wyniki w czytelny sposób
        print("\n" + "-" * 30)
        print(f"🧾 Kwota rachunku:  {kwota:>10.2f} zł")
        print(f"💝 Napiwek ({procent}%): {napiwek:>10.2f} zł")
        print(f"💵 Suma:           {suma:>10.2f} zł")
        print("-" * 30)

    except ValueError:
        print("\n❌ Ups! Wprowadź poprawne liczby.")

    print("\n👋 Dziękujemy za skorzystanie z kalkulatora!")


if __name__ == "__main__":
    main()
