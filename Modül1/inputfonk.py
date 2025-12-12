"""
val = input("Bir değer giriniz")
print(val)
"""
"""
val_int1 = int(input("Bir sayı girin : "))
val_int2 = int(input("Bir sayı girin : ")) 
result = val_int1 + val_int2
print(result)
print(type(val_int1))
print(type(val_int2))
"""

#Modül 1 Örnekler 

# çevre = 2 * pi * r  alan =  pi * r^2
import math

r = float(input("Yarıçap giriniz : "))
pi = math.pi

cevre = 2 * pi * r
alan = pi * r**2

print(f"Çevre : {cevre}")
print("Alan : {}".format(alan))

#Kullanıcıdan alınan 2 sayıya toplama,çıkarma,çarpmai,bölme işlemlerini yapınız.

# int_val1 = int(input("Bir sayı giriniz : "))
# int_val2 = int(input("Bir sayı giriniz : "))

# print(f"Toplam : {int_val1 + int_val2}")
# print(f"Çıkarma : {int_val1 - int_val2}")
# print(f"Çarpma : {int_val1 * int_val2}")
# print(f"Bölme : {int_val1 / int_val2}")

#kilo / boy * boy

