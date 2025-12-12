"""
    **Kredi Kartı Doğrulama**: Kredi kartı numarasının geçerli olup olmadığını kontrol eden program (Luhn algoritması)
    
    1. Son rakam (check digit) doğrulama için kullanılır.
    2. Sağdan sola doğru her ikinci rakam ikiyle çarpılır.
    3. Çarpım 9’dan büyükse, rakamlar toplanır.
    4. Tüm rakamlar toplanır.
    5. Toplamın 10’a bölümünden kalan 0 ise numara geçerlidir.
"""

card = input("Kredi kartı numaranızı girin: ")
card = card.replace(" ", "")

if not card.isdigit():
    print("Geçersiz kart numarası. Sadece rakamlar ve boşluklar kullanılabilir.")
elif len(card) != 16:
    print("Geçersiz kart numarası. Kart numarası 16 haneli olmalıdır.")
else:
    toplam = 0
    tersi = card[::-1]
    for iter, sayi in enumerate(tersi):
        n = int(sayi)
        if iter % 2 == 1:
            n = n * 2
            if n > 9:
                n -= 9
        toplam += n
    if toplam % 10 == 0:
        print("Lütfen telefonunuza gelen kodu giriniz.")
    else:
        print("Geçersiz kart numarası.")
