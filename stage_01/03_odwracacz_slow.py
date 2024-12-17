# Odwracacz słów - prosty program pokazujący moc Pythona!
# Autor: Tukano Software House
# Data: 2024


def odwroc_slowo(tekst):
    """Odwraca kolejność liter w tekście."""
    return tekst[::-1]


def main():
    # Wyświetl przyjazny banner powitalny
    print("=" * 50)
    print("🔄 Witaj w Magicznym Odwracaczu Słów!")
    print("Zamień dowolny tekst w jego lustrzane odbicie")
    print("=" * 50)

    try:
        # Pobierz tekst od użytkownika
        tekst = input("\n✍️  Wpisz dowolny tekst: ")

        # Odwróć tekst i wyświetl wynik
        odwrocony = odwroc_slowo(tekst)

        # Wyświetl wyniki w atrakcyjny sposób
        print("\n" + "🪄 " * 10)
        print(f"📝 Oryginalny tekst: {tekst}")
        print(f"✨ Odwrócony tekst: {odwrocony}")
        print("🪄 " * 10)

    except KeyboardInterrupt:
        print("\n\n❌ Przerwano działanie programu.")

    print("\n👋 Dziękujemy za skorzystanie z Odwracacza!")


if __name__ == "__main__":
    main()
