"""
alg1 => a + b 
alg2 => a - b
Koşul sağlınrsa(a+b < 10 and a-b > 0):
    alg3 => a * b 
Değil ise:
    alg4 => a / b

ana = alg1 + alg2 
"""

# print("Program Başladı...")

# if False:
#     print("İf Bloğu çalıştı...")
# else:
#     print("Else Bloğu çalıştı...")

# print("Program ana akıştan devam etti...",end="\n")
# print("Program Bitti...")

#if - else
# print("Program Başladı...")
# yas = 15

# if yas >= 18:
#     print("Reşitsiniz")
# else:
#     print("Reşit değilsiniz")


#print("Program Bitti...")


# if - elif - else

# print("Program Başladı...")

# puan = 200


# if(puan >=0 and puan <= 100):
#     if puan >= 90:
#         print("AA")
#     elif puan >= 80:
#         print("BA")
#     elif puan >= 70:
#         print("BB")
#     elif puan >= 60:
#         print("CB")
#     elif puan >= 50:
#         print("CC")
#     else:
#         print("FF")
# else:
#     print("Hatalı puan girişi yaptınız...")
    

# print("Program Bitti...")



# print("Program Başladı...")

# val = input("Bir sayi giriniz :")


# if isinstance(val,int):
#     if val > 0:
#         print("Girdiğiniz sayi pozitiftir")
#     elif val < 0:
#         print("Girdiğiniz sayi negatiftir")
#     else:
#         print("Girdiğiniz sayi sıfırdır")
# else:
#     print("Lütfen bir tam sayi giriniz")


# print("Program Bitti...")



# boy = float(input("Boyunuzu Girin : "))
# kilo = float(input("Kilonuzu Girin : "))

# vki = kilo / boy**2

# if vki < 18.5:
#     print("zayıf")
# elif vki < 25:
#     print("normal")
# elif vki < 30:
#     print("fazla kilolu")
# elif vki < 35:
#     print("obez")
# else:
#     print("aşırı obez")


#Kullanıcıda 2 tane sayı alınız ve bu sayılardan hangisi büyükse ekrana yazdırınız.

# num1 = int(input("Birinci sayıyı giriniz : "))
# num2 = int(input("İkinci sayıyı giriniz : "))

# if num1 > num2:
#     print(f"Büyük sayı : {num1}")
# elif num2 > num1:
#     print(f"Büyük sayı : {num2}")
# else:
#     print("Sayılar birbirine eşittir")


#Kullanıcın girdiği sayının tek mi çift mi olduğunu kontrol ediniz.

# val = int(input("Bir sayi girin: "))

# if val % 2 == 0:
#     print("Girdiğiniz sayı çifttir")
# else:
#     print("Girdiğiniz sayı tektir")

"""
Otobüs Bileti Fiyatı Uygulaması

Kullanıcda yaş ve mesafa bilgilerini alınız.
Temel ücret =  km * 2.5
Koşullar:
1-12 yaş arasındaki yolculara %50 indirim
12-24 yaş arası %25 indirim
65 yaş üzeri %30 indirim
100 km üsütü yolculukta ek %20 indirim

"""

# yas = int(input("Yaşınızı Girin : "))
# km = float(input("Mesafeyi Girin : "))
# temel_ucret = km * 2.5
# print("Temel Ücret",temel_ucret)
# if yas >= 0:
#     if yas <= 12:
#         ucret = temel_ucret - (temel_ucret * 0.5)
#         print("indirimli ücret",ucret)
#     elif yas <= 24:
#         ucret = temel_ucret - (temel_ucret * 0.25)
#         print("indirimli ücret",ucret)
#     elif yas >= 65:
#         ucret = temel_ucret - (temel_ucret * 0.3)
#         print("indirimli ücret",ucret)
#     else:
#         ucret = temel_ucret
#         print("indirimsiz ücret",ucret)

# if km > 100:
#     ucret = ucret - (ucret * 0.2)
#     print("indirimli ücret",ucret)


# print(f"Ödemeniz gereken ücret : {ucret}")


# yas = int(input("Yaşınızı Girin : "))
# km = float(input("Mesafeyi Girin : "))
# temel_ucret = km * 2.5
# print("Temel Ücret",temel_ucret)
# if yas >= 0:
#     if yas <= 12:
#         ucret = temel_ucret * 0.5
#         print("indirimli ücret",ucret)
#     elif yas <= 24:
#         ucret = temel_ucret * 0.75
#         print("indirimli ücret",ucret)
#     elif yas >= 65:
#         ucret = temel_ucret * 0.7
#         print("indirimli ücret",ucret)
#     else:
#         ucret = temel_ucret
#         print("indirimsiz ücret",ucret)

# if km > 100:
#     ucret = ucret * 0.8
#     print("indirimli ücret",ucret)


# print(f"Ödemeniz gereken ücret : {ucret}")

#Kullanıcıdan iki tane sayı alın ve kullanıcın girdiği işleme göre hesaplama yapım
"""
s1 = kullanıcdan al 
s2 = kulklanıcdan al 
islem = kullanıcdan alınacak
islem:
    + toplama
    - çıkarma
    * çarpma
    / bölme
    ** üs alma
    % mod alma
"""

# num1 = int(input("Birinci sayıyı giriniz : "))
# num2 = int(input("İkinci sayıyı giriniz : "))
# islem = input("İşlemi giriniz : ")

# if islem == "+":
#     print(f"{num1} + {num2} = {num1 + num2}")
# elif islem == "-":
#     print(f"{num1} - {num2} = {num1 - num2}")
# elif islem == "*":
#     print(f"{num1} * {num2} = {num1 * num2}")
# elif islem == "/":
#     print(f"{num1} / {num2} = {num1 / num2}")
# elif islem == "**":
#     print(f"{num1} ** {num2} = {num1 ** num2}")
# elif islem == "%":
#     print(f"{num1} % {num2} = {num1 % num2}")
# else:
#     print("Geçersiz işlem")


# gun = 5 

# match gun:
#     case 1:
#         print("Pazartesi")
#     case 2:
#         print("Salı")
#     case 3:
#         print("Çarşamba")
#     case 4:
#         print("Perşembe")
#     case 5:
#         print("Cuma")
#     case 6:
#         print("Cumartesi")
#     case 7:
#         print("Pazar")
#     case _:
#         print("Geçersiz gün")

    
#Kural : 4 bölünebilir ve 100'e bölünemez veya 400'e bölünebilir

# yil = 2021

# if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
#     print(f"{yil} artık yıldır.")
# else:
#     print(f"{yil} artık yıl değildir.") 




