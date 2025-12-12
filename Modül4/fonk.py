
#Parametresiz None(void) döndüren fonksiyonlar
# def selamla():
#     print("Selam")
# print("Fonksiyonun RAM Adresi",selamla)
# print("Fonksiyonun Tipi",type(selamla))
# selamla()

#Parametreli None(void) döndüren fonksiyonlar

# def selamla(isim):
#     return f"Selam {isim}"

# sonuc = selamla("Berkay")
# print(sonuc)
# print(selamla("Berkay"))



# isim = "Damla"
# soyisim = "Toprak"

# tam_isim = isim + " " + soyisim + " hocam f string konusu anladı"
# print(tam_isim)

#tam_isim = f"isim : {isim} soyisim {soyisim}"
# print(tam_isim)

# mesaj = f"{isim} {soyisim} hocam f string konusu anladı"
# print(mesaj)

#Parametreli None(void) Dödüren Fonksiyonlar

# def selamla(isim):
#     print(f"Selam {isim}")

# selamla("Berkay")


#Parametreli Değer Dödüren Fonksiyonlar

# def selamla(isim):
#     return f"Selam {isim}"
# print(selamla("Berkay"))

"""
return keywordünün Görevleri:
1-) Fonnksiyonun değer dödürmesini sağlar
2-) Fonksiyonun çalışmasını sonlandırır.
"""

# def fonk():
#     if False:
#         return True
#     return False

# print(fonk())

# def poiztif_veya_negatif_veya_sıfır(sayi):
#     if sayi == 0:
#         print("Sayı sıfıra eşittir")
#     elif sayi < 0:
#         print("sayi negatiftir")
#     elif sayi > 0:
#         print("sayi pozitifitir")
    
# poiztif_veya_negatif_veya_sıfır(-1)


# def poiztif_veya_negatif_veya_sıfır(sayi):
#     if sayi == 0:
#         return "Sayı sıfıra eşittir."
#     if sayi < 0:
#         return "sayi negatiftir"
#     if sayi > 0:
#         return "sayi pozitifitir"
    
# print(poiztif_veya_negatif_veya_sıfır("a"))


# def mutlak_deger(sayi):
#     print("Fonsiyon çalışmaya başladı...")
#     if sayi>= 0:
#         print("İf Bloğu çalıştı ve fonksiyon sonlandı...")
#         return sayi
    
#     print("Fonsiyon sonlandı...")
#     return -sayi

# print(mutlak_deger(-5))


# def bol(a,b):
#     if b == 0:
#         return "Sıfıra Bölme Hatası"
    
#     return a / b

# def bol(a,b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Sıfıra Bölme Hatası")
        

# print(bol(4,1))





# def yas(yas):
#     if yas < 0:
#         raise ValueError("Yaş sıfırdan küçük olmaza")
    
# def yas(yas):
#     if yas < 0:
#         print("Yaş 0dan küçük olmaz")


# yas(-5)


# def user_input():
#     num1 = int(input("Sayı1 : "))
#     num2 = int(input("Sayı2 : "))
#     return num1,num2


# def add(num1,num2):
#     return num1 + num2

# def sub(num1,num2):
#     return num1 - num2

# def multiply(num1,num2):
#     return num1 * num2

# def divison(num1,num2):
#     if num2 == 0:
#         print("0'a bölme hatası")
#         return
#     return num1 / num2

# def claculator():
#     user_enter_numbers = user_input()
#     print(type(user_enter_numbers))
#     option = input("Lütfen yapmak istediğiniz işlemi(+,-,*,/) seçiniz")

#     if option == "+":
#         result = add(user_enter_numbers[0],user_enter_numbers[1])
#         print(result)
#     elif option == "-":
#         result = sub(user_enter_numbers[0],user_enter_numbers[1])
#         print(result)
#     elif option == "*":
#         result = multiply(user_enter_numbers[0],user_enter_numbers[1])
#         print(result)
#     elif option == "/":
#         result = divison(user_enter_numbers[0],user_enter_numbers[1])
#         print(result)
#     else:
#         print("Lütfen Geçerli Bir İşlem Seçiniz...")

# claculator()


#Recursive Fonksiyonlar

# def fakt(sayi):
#     if sayi == 1 or sayi == 0:
#         return 1
#     return sayi * fakt(sayi - 1)

# print(fakt(5))

# def selamla(isim = "Bilinmiyor"):
#     print(f"Merhaba {isim}")

# selamla()


"""
*args parameter => fonksiyonun değişken sayıda partametre almasını sağlıyor
"""

# def add(liste):
#     result = 0
#     for i in liste:
#         result += i
#     print(result)
# ints = [1,2,3,4,5,6,7,8,9]

# add(ints)

# def add(*args):
#     result = 0
#     # print(type(args))
#     for i in args:
#         result += i 
#     print(result)

# add(1,2,3,4,5,6,7,8,9)



# def add(*nums):
#     result = 0
#     # print(type(args))
#     for i in nums:
#         result += i 
#     print(result)

# add(1,2,3,4,5,6,7,8,9)


"""
**kwargs => berkay_isim = "Berkay",gönül_isim = "Gönül",merve_isim ="Merve"
*args => "berkay","Gönül","Merve"...
"""


# def isimler(**kwargs):
#     print("Type : ",type(kwargs))
#     print("Kwargs items : ")
#     for i in kwargs.items():
#         print(i)
#     print(10*"-")
#     print("Kwargs values : ")
#     for i in kwargs.values():
#         print(i)
#     print(10*"-")
#     print("Kwargs Keys : ")
#     for i in kwargs.keys():
#         print(i)


# isimler( berkay_isim = "Berkay",gönül_isim = "Gönül",merve_isim ="Merve")


# def fonk(isim:str,sayi:int) -> None:
#     print(isim)
#     print(sayi)


# fonk(sayi=10,isim="Berkay")



# def fonk(isim,*args,**kwargs):
#     print(isim)
#     print(args)
#     print(kwargs)

# fonk("berkay",1,2,3,4,5,kwargs_isim="berkay")



"""
lambda fonk.

etiket(tag) = lambda parametreler : fonk_process
"""

# kare_al = lambda sayi : sayi ** 2
# print(kare_al)
# print(type(kare_al))
# print(kare_al(5))

# topla = lambda num1,num2 : num1 + num2
# cikar = lambda num1,num2 : num1 - num2
# carp = lambda num1,num2 : num1 * num2
# bol = lambda num1,num2 : num1 / num2
# print(topla(4,5))
# print(cikar(4,5))
# print(carp(4,5))
# print(bol(4,5))


# selam = lambda : "Merhaba"
# print(selam())


"""
Map Fonksiyounu:
Genel Yapısı => map(fonk,iterasyon yapılacak veri tipi(string,list,tıple))

"""

# liste = [1,2,3,4,5,6]

# def iki_ile_carp(sayi):
#     return sayi * 2

# iki_kati = map(lambda sayi : sayi * 2,liste)
# print(list(map(iki_ile_carp,liste)))
# print(list(iki_kati))



# liste = [1,2,-9,45,0,84,-85]

# def pozitif(sayi):
#     return sayi > 0
# pozitif_sayilar = filter(pozitif,liste)
# print(list(pozitif_sayilar))

# print(list(filter(lambda x : x > 0 , liste)))


"""
Pass_By_Value vs Pass_By_Reference
"""


# def degistir(sayi):
#     sayi = 100
#     print("Parametre olarak gönderilen değişkenin adresi : ",id(sayi))
#     print(sayi)

# sayi = 10
# degistir(sayi)
# print(sayi)
# print("Orjinal Değişkenin Adresi : ",id(sayi))


# def degistir(liste):
#     liste[0] = 1000
#     print("Parametre olarak gönderilen değişkenin adresi : ",id(liste[0]))
#     print(liste[0])

# liste = [1,2,3,4,5]
# degistir(liste)
# print(liste[0])
# print("Orjinal Değişkenin Adresi : ",id(liste[0]))

# print(liste)



"""
decorator fonk.
"""
# def fonk_calistir(fonk,parametre):
#     fonk(parametre)

# def selamla(isim):
#     print(f"Selam {isim}")


# fonk_calistir(selamla,"Berkay")

# def wrapper_fonk(fonk):
#     def inline_fonk(parametre):
#         return fonk(parametre)
#     return inline_fonk

# def selamla(isim):
#     print(f"Selam {isim}")

# fonk = wrapper_fonk(selamla)
# result = fonk("Berkay")
# print(result)


# def wrapper(fonk):
#     def inline_fonk(parametre):
#         print("Fonksiyon Çalıştı...")
#         result = fonk(parametre)
#         print("Fonksiyon Bitti...")
#         return result
#     return inline_fonk

# @wrapper
# def selamla(isim):
#     return f"Selam {isim}"

# print(selamla("berkay"))

# import time
# def sure_olc(fonk):
#     def wrapper(*args,**kwargs):
#         baslangıc = time.time()
#         result = fonk(*args,**kwargs)
#         bitis = time.time()
#         print(bitis - baslangıc)
#         return result
#     return wrapper

# @sure_olc
# def yavas_fonk():
#     time.sleep(1)

# yavas_fonk()

"""
1-Kullanıcın Girdiği sayının asal olup olmadığını kontrol eden alg. yazın
2-Kullanıcın girdiği kelimenin palinndrom olup olmadığını kontrol eden alg. yazın
3-Kullanıcın girdiği kelimedeki tekrar eden karekterleri bulun 
4-Kullanıcın giridiği sayıya kadar Fibonacci serisini bastırın
"""
#1-Kullanıcın Girdiği sayının asal olup olmadığını kontrol eden alg. yazın

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(8))

#2-Kullanıcın girdiği kelimenin palinndrom olup olmadığını kontrol eden alg. yazın





# def is_palindrom(string):
#     return string[::] == string[::-1]


# def is_palindrom(string):
#     left = 0
#     right = len(string) - 1 

#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1 
#         right -= 1 
#     return True
    

# print(is_palindrom("ada"))


#3-Kullanıcın girdiği kelimedeki tekrar eden karekterleri bulun 

# def duplicate_char(string):
#     duplicate_frek = {}
#     duplicate_char_list = []
#     for i in string:
#         if i in duplicate_frek:
#             duplicate_frek[i] += 1
            
#         else:
#             duplicate_frek[i] = 1
    
#     for i in duplicate_frek:
#         if duplicate_frek[i] > 1:
#             duplicate_char_list.append(i)

#     return duplicate_char_list

# print(duplicate_char("berrrkkay"))


#4-Kullanıcın giridiği sayıya kadar Fibonacci serisini bastırın

# def fibonacci(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
    
#     series = [0,1]

#     for i in range(n-2):
#         new_item = series[-1] + series[-2]
#         series.append(new_item)
#     return series

# print(fibonacci(10))