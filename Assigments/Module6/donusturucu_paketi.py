"""
    **Dönüştürücü Paketi**: Birim dönüştürme fonksiyonları (sıcaklık, uzunluk, ağırlık)
"""

def celsius_to_fahrenheit(c): return c * 1.8 + 32
def fahrenheit_to_celsius(f): return (f - 32) / 1.8
def celsius_to_kelvin(c): return c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def fahrenheit_to_kelvin(f): return celsius_to_kelvin(fahrenheit_to_celsius(f))
def kelvin_to_fahrenheit(k): return celsius_to_fahrenheit(kelvin_to_celsius(k))

def metre_to_cm(m): return m * 100
def cm_to_metre(cm): return cm / 100
def km_to_mile(km): return km / 1.60934
def mile_to_km(mile): return mile * 1.60934
def inch_to_cm(inch): return inch * 2.54
def cm_to_inch(cm): return cm / 2.54
def feet_to_metre(feet): return feet * 0.3048
def metre_to_feet(m): return m / 0.3048

def kg_to_g(kg): return kg * 1000
def g_to_kg(g): return g / 1000
def kg_to_pound(kg): return kg * 2.20462
def pound_to_kg(pound): return pound / 2.20462
def gram_to_ounce(g): return g / 28.3495
def ounce_to_gram(oz): return oz * 28.3495


def sicaklik_menu():
    print("\nSıcaklık Dönüşümleri")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")
    
    secim = input("Seçiminiz (1-6): ").strip()
    deger = float(input("Değeri girin: "))

    if secim == "1":
        print(f"{deger} °C = {celsius_to_fahrenheit(deger):.2f} °F")
    elif secim == "2":
        print(f"{deger} °F = {fahrenheit_to_celsius(deger):.2f} °C")
    elif secim == "3":
        print(f"{deger} °C = {celsius_to_kelvin(deger):.2f} K")
    elif secim == "4":
        print(f"{deger} K = {kelvin_to_celsius(deger):.2f} °C")
    elif secim == "5":
        print(f"{deger} °F = {fahrenheit_to_kelvin(deger):.2f} K")
    elif secim == "6":
        print(f"{deger} K = {kelvin_to_fahrenheit(deger):.2f} °F")
    else:
        print("❌ Geçersiz seçim!")

def uzunluk_menu():
    print("\nUzunluk Dönüşümleri")
    print("1. Metre → Santimetre")
    print("2. Santimetre → Metre")
    print("3. Kilometre → Mil")
    print("4. Mil → Kilometre")
    print("5. İnç → Santimetre")
    print("6. Santimetre → İnç")
    print("7. Feet → Metre")
    print("8. Metre → Feet")
    
    secim = input("Seçiminiz (1-8): ").strip()
    deger = float(input("Değeri girin: "))

    if secim == "1":
        print(f"{deger} m = {metre_to_cm(deger):.4f} cm")
    elif secim == "2":
        print(f"{deger} cm = {cm_to_metre(deger):.4f} m")
    elif secim == "3":
        print(f"{deger} km = {km_to_mile(deger):.4f} mil")
    elif secim == "4":
        print(f"{deger} mil = {mile_to_km(deger):.4f} km")
    elif secim == "5":
        print(f"{deger} in = {inch_to_cm(deger):.4f} cm")
    elif secim == "6":
        print(f"{deger} cm = {cm_to_inch(deger):.4f} in")
    elif secim == "7":
        print(f"{deger} ft = {feet_to_metre(deger):.4f} m")
    elif secim == "8":
        print(f"{deger} m = {metre_to_feet(deger):.4f} ft")
    else:
        print("❌ Geçersiz seçim!")

def agirlik_menu():
    print("\nAğırlık Dönüşümleri")
    print("1. Kilogram → Gram")
    print("2. Gram → Kilogram")
    print("3. Kilogram → Pound")
    print("4. Pound → Kilogram")
    print("5. Gram → Ounce")
    print("6. Ounce → Gram")
    
    secim = input("Seçiminiz (1-6): ").strip()
    deger = float(input("Değeri girin: "))


    if secim == "1":
        print(f"{deger} kg = {kg_to_g(deger):.4f} g")
    elif secim == "2":
        print(f"{deger} g = {g_to_kg(deger):.4f} kg")
    elif secim == "3":
        print(f"{deger} kg = {kg_to_pound(deger):.4f} lb")
    elif secim == "4":
        print(f"{deger} lb = {pound_to_kg(deger):.4f} kg")
    elif secim == "5":
        print(f"{deger} g = {gram_to_ounce(deger):.4f} oz")
    elif secim == "6":
        print(f"{deger} oz = {ounce_to_gram(deger):.4f} g")
    else:
        print("❌ Geçersiz seçim!")

def main():
    print("Birim Dönüştürücü")
    while True:
        print("\n" + "="*40)
        print("Dönüşüm kategorisini seçin:")
        print("1. Sıcaklık")
        print("2. Uzunluk")
        print("3. Ağırlık")
        print("4. Çıkış")
        print("="*40)
        
        secim = input("Seçiminiz (1-4): ").strip()

        if secim == "1":
            sicaklik_menu()
        elif secim == "2":
            uzunluk_menu()
        elif secim == "3":
            agirlik_menu()
        elif secim == "4":
            print("✅ Programdan çıkılıyor. İyi günler!")
            break
        else:
            print("❌ Geçersiz seçim! Lütfen 1-4 arasında bir değer girin.")


if __name__ == "__main__":
    main()
