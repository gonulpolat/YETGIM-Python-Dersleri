"""
    **Hesap Makinesi**: Dört işlem ve gelişmiş işlemler yapan modüler hesap makinesi
"""


import math


# 4 İşlem
topla = lambda a, b : a + b
cikar = lambda a, b : a - b
carp  = lambda a, b : a * b
bol   = lambda a, b : a / b if b != 0 else print(f"{a} 0'a bölünemez!")


# Gelişmiş İşlemler
us_alma = lambda taban, us : taban ** us
karekok = lambda sayi: math.sqrt(sayi) if sayi > 0 else print("Negatif sayıların karakökü yok!")
sinus   = lambda radyan: math.sin(radyan)
kosinus = lambda radyan: math.cos(radyan)
tanjant = lambda radyan: math.tan(radyan)


# Yardımcı Fonksiyonlar
def sayi_al(mesaj):
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

def secim_al(mesaj, secenekler):
    while True:
        secim = input(mesaj).strip().lower()
        if secim in secenekler:
            return secim
        print(f"Geçersiz seçim! Şu seçeneklerden birini girin: {', '.join(secenekler)}")


def main():
    print("🧮 Gelişmiş Hesap Makinesine Hoşgeldiniz!")
    while True:
        print("\n--- Menü ---")
        print("1. Temel İşlemler")
        print("2. Gelişmiş İşlemler")
        print("3. Çıkış")
        secim = secim_al("Seçiminizi yapın (1/2/3): ", ['1', '2', '3'])

        if secim == '1':
            temel_islemler_menu()
        elif secim == '2':
            gelismis_islemler_menu()
        elif secim == '3':
            print("Hesap makinesi kapatılıyor. İyi günler! 🌟")
            break

def temel_islemler_menu():
    print("\n 📝 Temel İşlemler ")
    islem = secim_al("İşlem seçin (+, -, *, /): ", ['+', '-', '*', '/'])
    a = sayi_al("İlk sayıyı girin: ")
    b = sayi_al("İkinci sayıyı girin: ")
    
    try:
        if islem == '+':
            sonuc = topla(a, b)
        elif islem == '-':
            sonuc = cikar(a, b)
        elif islem == '*':
            sonuc = carp(a, b)
        elif islem == '/':
            sonuc = bol(a, b)
        print(f"Sonuç: {sonuc}")
    except ValueError as e:
        print(f"Hata: {e}")

def gelismis_islemler_menu():
    print("\n 📐 Gelişmiş İşlemler")
    print("1. Üs Alma (taban^üs)")
    print("2. Karekök")
    print("3. Sinüs")
    print("4. Kosinüs")
    print("5. Tanjant")
    secim = secim_al("Seçiminizi yapın (1/2/3/4/5): ", ['1', '2', '3', '4', '5'])
    
    try:
        if secim == '1':
            taban = sayi_al("Tabanı girin: ")
            us = sayi_al("Üssü girin: ")
            sonuc = us_alma(taban, us)
        elif secim == '2':
            sayi = sayi_al("Karekökünü almak istediğiniz sayıyı girin: ")
            sonuc = karekok(sayi)
        elif secim == '3':
            radyan = sayi_al("Açıyı radyan cinsinden girin: ")
            sonuc = sinus(radyan)
        elif secim == '4':
            radyan = sayi_al("Açıyı radyan cinsinden girin: ")
            sonuc = kosinus(radyan)
        elif secim == '5':
            radyan = sayi_al("Açıyı radyan cinsinden girin: ")
            sonuc = tanjant(radyan)
        
        print(f"Sonuç: {sonuc}")
    except ValueError as e:
        print(f"Hata: {e}")


if __name__ == "__main__":
    main()
