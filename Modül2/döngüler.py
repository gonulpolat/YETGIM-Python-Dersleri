# print("Merhaba")
# print("Merhaba")
# print("Merhaba")
# print("Merhaba")
# print("Merhaba")


# val = range(5,100,2)
# print(type(val))
# print(val)

# for i in range(5):
#     print(type(i))
#     print("Merhaba")


# string = "Python"

# for i in string:
#     print(type(i))
#     print(i)


# count = 0
# while count < 5:
#     print("Merhaba")
#     count += 1

# for i in range(5):
#     print(i)
#     if i == 3:
#         break


# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# toplam = 0
# while True:
#     kullanıcı_girdisi = input("Bir sayi giriniz (Çıkmak için 'q')")
#     if kullanıcı_girdisi == "q":
#         break
#     sayi = int(kullanıcı_girdisi)
#     toplam += sayi

# print("Toplam : ",toplam)

# sayi = 6
# fakt = 1
# for i in range(1,sayi+1):
#     fakt *= i
# print(fakt)

# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)


# sayi = 1234
# basamak = 0
# while sayi > 0:
#     sayi //= 10
#     basamak += 1
# print(basamak)



# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("---------------")


# i = 1
# j = 1

# while i < 11:
#     while j < 11:
#         print(f"{i} * {j} = {i*j}")
#         j += 1
#     print("---------------")
#     i += 1
#     j = 1

"""
1-100 arasındaki sayılar için 
3'e tam bölünenleri için => Fizz
5'e tam bölünenleri için => Buzz
15'e tam bölünenleri için => FizzBuzz
Diğer durumlar için => Sayı
"""

# for i in range(1,101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)


# for i in range(1,101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Buzz")
#     elif i % 5 == 0:
#         print("Fizz")
#     else:
#         print(i)

# sesli_harf = "aeiıoöuü"
# kullanıcı_gidisi = "Merhaba Python"

# for i in kullanıcı_gidisi:
#     if i in sesli_harf:
#         print(i)

#Mükemmel sayı : Pozitif tam bölenlerinin toplamı kendisine eşit olan sayı
# 6 => 1,2,3,6 => 1+2+3 = 6

# sayi = 12 
# toplam = 0
# for i in range(1,sayi):
#     if sayi % i == 0:
#         toplam += i
# if toplam == sayi:
#     print("Mükemmel sayi girdiniz")
# else:
#     print("Mükemmel sayi girmediniz")


"""
Data Structure(Veri Yapısı)
Hashmap
dict
list
array

10 Yöntem
two pointers
sliding window
"""


"""
Kullanıcın girdiği sayının basakamakları toplamını bulunuz
Kullanıcının girdiği sayının Armstrong sayısı olup olmadığını bulunuz
    Armstrong sayısı : 153 => 1^3 + 5^3 + 3^3 = 153

Asal 1-100 arasındaki sayıların asal olanları ekrana bastıran bir program yazınız



ATM simülasyonu : 
    Kullanıcıya şu seçenekleri sununuz
    1- Bakiye Sorgulama
    2- Para Çekme
    3- Para Yatırma
    4- Çıkış
    Kullanıcı 4'e basmadığı sürece işlem yapmaya devam ediniz

Sayı Tahmin oyunu 
    Kopya:
        import random
        sayi = random.randint(1,100)
    Kullanıcıdan 1-100 arasında bir sayı tahmini alın
    Eğer kullanıcı 5 hakkı bitmeden sayıyı bulursa "Tebrikler" yazdırın
    Eğer kullanıcı 5 hakkı bitmeden sayıyı bulamazsa "Kaybettiniz" yazdırın      

"""


# Kullanıcın girdiği sayının basakamakları toplamını bulunuz
# Kullanıcının girdiği sayının Armstrong sayısı olup olmadığını bulunuz
#     Armstrong sayısı : 153 => 1^3 + 5^3 + 3^3 = 153

# sayi = 153
# basamak_sayisi = len(str(sayi))
# gecici_sayi = sayi
# armstrong_toplam = 0

# while sayi > 0:
#     basamak = sayi % 10
#     armstrong_toplam += basamak ** basamak_sayisi
#     sayi //= 10

# if gecici_sayi == armstrong_toplam:
#     print("Armstrong sayısı girdiniz")
# else:
#     print("Armstrong sayi girmediniz")

 
# Asal 1-100 arasındaki sayıların asal olanları ekrana bastıran bir program yazınız

# for i in range(2,101):
#     asal = True
#     for j in range(2,i):
#         if i % j == 0:
#             asal = False
#             break
#     if asal:
#         print(i,end=" ")

# for i in range(2,101):  
#     for j in range(2,i+1):
#         if i%j == 0:
#             break
#     if i == j:
#         print(i,end=",")

"""
i = 11
j = 2 3 4 5 6 7 8 9 10 11

if i == j 
    print("Asal")
"""


# ATM simülasyonu : 
#     Kullanıcıya şu seçenekleri sununuz
#     1- Bakiye Sorgulama
#     2- Para Çekme
#     3- Para Yatırma
#     4- Çıkış
#     Kullanıcı 4'e basmadığı sürece işlem yapmaya devam ediniz

# bakiye = 1000

# while True:
#     print("""
#     1- Bakiye Sorgulama
#     2- Para Çekme
#     3- Para Yatırma
#     4- Çıkış
#     """)
#     secim = input("Lütfen bir seçim yapınız:")
#     if secim == "1":
#         print(f"Bakiyeniz: {bakiye}")
#     elif secim == "2":
#         para = int(input("Çekmek istediğiniz miktarı giriniz:"))
#         if para > bakiye:
#             print("Yetersiz bakiye")
#         else:
#             bakiye -= para
#             print(f"Yeni bakiyeniz: {bakiye}")
#     elif secim == "3":
#         para = int(input("Yatırmak istediğiniz miktarı giriniz:"))
#         bakiye += para
#         print(f"Yeni bakiyeniz: {bakiye}")
#     elif secim == "4":
#         print("Çıkış yapılıyor...")
#         break
#     else:
#         print("Hatalı seçim")


# Sayı Tahmin oyunu 
#     Kopya:
#         import random
#         sayi = random.randint(1,100)
#     Kullanıcıdan 1-100 arasında bir sayı tahmini alın
#     Eğer kullanıcı 5 hakkı bitmeden sayıyı bulursa "Tebrikler" yazdırın
#     Eğer kullanıcı 5 hakkı bitmeden sayıyı bulamazsa "Kaybettiniz" yazdırın

# import random 
# hak = 0

# rastgele_sayi = random.randint(1,100)
# print(rastgele_sayi)

# while hak < 5:
#     sayi = int(input("sayi : "))
#     if sayi == rastgele_sayi:
#         print("Oyunuı kazandınız...")
#         break
#     elif sayi > rastgele_sayi:
#         print("Tahmininizi küçültün")
#     elif sayi < rastgele_sayi:
#         print("Tahmininizi büyültün")
    
#     hak += 1 
    