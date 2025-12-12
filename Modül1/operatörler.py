
#Aritmetik Operatörler
a = 12
b = 5

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)
print("a % b = ", a % b)

print(10*"--")

#Karşılaştırma Operatörleri
print("a == b = ", a == b)
print("a != b = ", a != b)
print("a > b = ", a > b)
print("a < b = ", a < b)
print("a >= b = ", a >= b)
print("a <= b = ", a <= b)

print(10*"--")
condition_one = True
condition_two = False

#Mantıksal Operatörler
print("a and b = ", condition_one and condition_two)
print("a or b = ", condition_one or condition_two)
print("not a = ", not condition_one)

print("=====Logical Operators Tables=======")

print("And Table")
print("False and False :  ",False and False)
print("False and True  : ", False and True)
print("True and False  : ",True and False)
print("True and True   : ",True and True)


print("Or Table")
print("False or False  : ",False or False)
print("False or True   : ",False or True)
print("True or False   : ",True or False)
print("True or True    : ",True or True)



print(10*"--")
#Atama Operatörleri
#
"""
 sol = sağındaki değeri solundaki değişkene atar  
 val = 10

 += operatörü
 val+=5 => val = val + 5

-= operatörü
val-=5 => val = val - 5 

*= operatörü
val *= 5 => val = val * 5 

/= operatörü 
val /= 5 => val = val / 5

//= operatörü
val //= 5 => val = val // 5

%= operatörü 
val %=5 => val = val % 5

**= operatörü
val **=5 => val = val ** 5
"""

a += b # a = a + b
print("a += b = ", a)
a -= b # a = a - b
print("a -= b = ", a)
a *= b
print("a *= b = ", a)
a /= b
print("a /= b = ", a)
a %= b
print("a %= b = ", a)
a **= b
print("a **= b = ", a)
a //= b
print("a //= b = ", a)


print(10*"--")
#Üyelik Operatörleri
#in => iterable obje elemanlarının üyesi olup olmadığını kontrol eder
str_val = "Python"
list = [1,2,3,4,5]
a = 5
print("a in list = ", a in list)
print("a in str_val = ",'a' in str_val)
print("p in str_val = ",'p' not in str_val)

#is operatörü : iki objenin aynı olup olmadığını kontrol eder
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list3 = list1
print("list1 is list2 = ",list1 is list2)
print("list1 is list3 = ",list1 is list3)

print("==========UYGULAMALAR============")
age = 20
result = age >= 18
print(result)

del age
del result
#Kredi alabilir mi?
age = 18
debt = 1000
result = age >= 18 and debt <=1000
print(result)
del result

#Kullanıcı adı ve Parola Kontrolü 
username = "admin"
password = "123456Admin"

user_input_username = input("Kullanıcı Adı : ")
user_input_password = input("Parola : ")
result = username == user_input_username and password == user_input_password
print(result)

#Kullanıcın girdiği sayının tek mi çift mi olduğunu kontrol et