
"""
Karar Yapıları
Döngüler 
fonksiyonlar
"""

# print("Program ana akıştan başladı...")

# if  False:
#     print("İf Kod Bloğu Çalıştı")
# else:
#     print("Else Kod Bloğu Çalıştı")

# print("Program ana akıştan sonlandı...")



# sayi1 = 80
# sayi2 = 80
# sayi3 = 100

# if sayi1 >= sayi2 and sayi1 >= sayi3:
#     en_buyuk = sayi1
# elif sayi2 >= sayi1 and sayi2 >= sayi3:
#     en_buyuk = sayi2
# elif sayi3 >= sayi1 and sayi3 >= sayi2:
#     en_buyuk = sayi3

# print(en_buyuk)


# print("Program başladı")
# sayi = 0

# if sayi > 0:
#     print("İf Bloğu çalıştı")
#     print("sayi pozitiftir")
# elif sayi < 0:
#     print("Elif Bloğu çalıştı")
#     print("sayi negatiftir")
# else:
#     print("Else Bloğu çalıştı")
#     print("sayi sıfıra eşittir")

# print("Program sonlandı")

"""
Kullanıcıdan alınan iki sayının toplamını, farkını, çarpımını ve bölümünü ekrana yazdıran bir program yazınız.

Girilen bir sayının tek mi çift mi olduğunu bulan programı yazınız

Kullanıcıdan vize ve final notlarını alan ve vizenin %40'ı ile finalin %60'ını alarak yıl sonu ortalamasını hesaplayan bir program yazınız. Eğer ortalama 50'den büyük veya eşitse "Geçti", küçükse "Kaldı" yazdırınız.

Bir kargo şirketinin ücretlendirme sistemini yazın. Paketin ağırlığına göre fiyat belirleyin: 0-2 kg arası 15 TL, 2-5 kg arası 25 TL, 5-10 kg arası 40 TL, 10 kg üzeri için "Ağır kargo, özel taşıma gerekir" mesajı verin.
"""
# Kullanıcıdan alınan iki sayının toplamını, farkını, çarpımını ve bölümünü ekrana yazdıran bir program yazınız.

# sayi1 = int(input("Syai1 : "))
# sayi2 = int(input("Syai2 : "))
# print(sayi1 + sayi2)
# print(sayi1 - sayi2)
# print(sayi1 * sayi2)
# print(sayi1 / sayi2)


#Girilen bir sayının tek mi çift mi olduğunu bulan programı yazınız

# sayi = int(input("Sayi : "))

# if sayi % 2 == 0:
#     print("Çift sayı")
# else:
#     print("Tek sayı")


# Kullanıcıdan vize ve final notlarını alan ve vizenin %40'ı ile finalin %60'ını alarak yıl sonu ortalamasını hesaplayan bir program yazınız. Eğer ortalama 50'den büyük veya eşitse "Geçti", küçükse "Kaldı" yazdırınız.


# vize = int(input("Vize : "))
# final = int(input("Final : "))
# ortalama = vize * 0.4 + final * 0.6

# if ortalama >= 50:
#     print("Geçtiniz")
# else:
#     print("Kaldınız")


# Bir kargo şirketinin ücretlendirme sistemini yazın. Paketin ağırlığına göre fiyat belirleyin: 0-2 kg arası 15 TL, 2-5 kg arası 25 TL, 5-10 kg arası 40 TL, 10 kg üzeri için "Ağır kargo, özel taşıma gerekir" mesajı verin.


# kargo = int(input("Lütfen kargo ağırlığını girin : "))

# if kargo > 0:
#     if kargo >= 0 and kargo < 2:
#         fiyat = 15
#         print(fiyat)
#     elif kargo >= 2 and kargo < 5:
#         fiyat = 25
#         print(fiyat)
#     elif kargo >= 5 and kargo < 10:
#         fiyat = 40 
#         print(fiyat)
#     else:
#         print("Ağır kargo, özel taşıma gerekir")
# else:
#     print("Kargo ağirlığı negatif olamaz")


# if kargo > 0:
#     if kargo > 10:
#         print("Ağır kargo, özel taşıma gerekir")
#     elif kargo >= 5:
#         fiyat = 40
#         print(fiyat)
#     elif kargo >= 2:
#         fiyat = 25 
#         print(fiyat)
#     elif kargo >= 0:
#         fiyat = 15 
#         print(fiyat) 
# else:
#     print("Kargo ağirlığı negatif olamaz")

