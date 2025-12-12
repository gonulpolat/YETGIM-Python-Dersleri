"""
    **Restoran Sipariş Sistemi**: Menüden seçim yapıp toplam tutarı hesaplayan program
"""

print("Meclis Lokantası".center(30, "="))
print("1. Keloğlan Çorbası - 15 TL")
print("2. Ayran Aşı - 12 TL")
print("3. Kayseri Yağlaması - 20 TL")
print("4. Fırın Sütlaç - 10 TL")
print("5. Hoşaf - 5 TL")

total_price = 0
while True:
    girdi = input("Sipariş numarasını girin (Çıkmak için q tuşlayınız): ")
    if girdi.lower() == 'q':
        if total_price == 0:
            print("Sipariş verilmedi!")
        else:
            print("Sipariş verildi!")
            print(f"Toplam tutar: {total_price} TL")
        break
    elif girdi == '1':
        total_price += 15
    elif girdi == '2':
        total_price += 12
    elif girdi == '3':
        total_price += 20
    elif girdi == '4':
        total_price += 10
    elif girdi == '5':
        total_price += 5
    else:
        print("Geçersiz sipariş numarası. Tekrar deneyin.")
