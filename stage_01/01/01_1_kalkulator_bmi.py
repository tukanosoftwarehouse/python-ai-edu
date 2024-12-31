# Kalkulator BMI - prosty program pokazujący moc Pythona!
# Autor: Tukano Software House
# Data: 2024


def oblicz_bmi(waga, wzrost):
    """Oblicza wskaźnik BMI na podstawie wagi i wzrostu."""
    return waga / (wzrost * wzrost)


def interpretuj_bmi(bmi):
    """Zwraca interpretację wyniku BMI."""
    if bmi < 18.5:
        return "📉 Niedowaga"
    elif bmi < 25:
        return "✅ Prawidłowa waga"
    elif bmi < 30:
        return "⚠️ Nadwaga"
    else:
        return "❗ Otyłość"


def main():
    # Wyświetl przyjazny banner powitalny
    print("=" * 50)
    print("⚖️ Witaj w Kalkulatorze BMI!")
    print("Sprawdź czy Twoja waga jest prawidłowa")
    print("=" * 50)

    try:
        # Pobierz dane od użytkownika
        waga = float(input("\n⚖️ Podaj swoją wagę (kg): "))
        wzrost = float(input("📏 Podaj swój wzrost (m): "))

        # Oblicz BMI
        bmi = oblicz_bmi(waga, wzrost)
        interpretacja = interpretuj_bmi(bmi)

        # Wyświetl wyniki w czytelny sposób
        print("\n" + "-" * 40)
        print(f"🔢 Twoje BMI wynosi: {bmi:.1f}")
        print(f"📊 Interpretacja: {interpretacja}")
        print("-" * 40)

    except ValueError:
        print("\n❌ Ups! Wprowadź poprawne liczby.")
    except ZeroDivisionError:
        print("\n❌ Wzrost nie może wynosić 0!")

    print("\n👋 Dziękujemy za skorzystanie z kalkulatora BMI!")


if __name__ == "__main__":
    main()
