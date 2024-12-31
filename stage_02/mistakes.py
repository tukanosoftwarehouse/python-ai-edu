# Przykład 1: Brak dwukropka po instrukcji if/for
if True    # Brak dwukropka!
    print("Ten kod się nie skompiluje")

# ====================

# Przykład 2: Nieprawidłowe wcięcia
if True:
print("Ten kod się nie skompiluje")  # Brak wcięcia!

# ====================

# Przykład 3: Dzielenie przez zero
print("\nPrzykład 3: Dzielenie przez zero")
try:
    x = 10
    y = 0
    wynik = x / y  # Próba dzielenia przez zero!
except ZeroDivisionError as e:
    print(f"Błąd dzielenia: {e}")

# ====================

# Przykład 4: Użycie == zamiast = w przypisaniu
print("\nPrzykład 4: == zamiast = w przypisaniu")
try:
    x == 5  # Użyto operatora porównania zamiast przypisania!
    print(x)
except NameError as e:
    print(f"Błąd nazwy: {e}")
print("Poprawnie powinno być: x = 5")

# ====================

# Przykład 5: Nieprawidłowe indeksy list
print("\nPrzykład 5: Nieprawidłowe indeksy list")
try:
    lista = [1, 2, 3]
    print(lista[3])  # Próba dostępu do nieistniejącego indeksu!
except IndexError as e:
    print(f"Błąd indeksu: {e}")
print(f"Lista ma tylko indeksy od 0 do {len(lista)-1}")