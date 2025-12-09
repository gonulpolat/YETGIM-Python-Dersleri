# 42 SAATLİK PYTHON EĞİTİMİ - KAPSAMLI DOKÜMAN

## İçindekiler
- [MODÜL 1: Python'a Giriş ve Temel Kavramlar](#modül-1-pythona-giriş-ve-temel-kavramlar)
- [MODÜL 2: Operatörler ve Kontrol Yapıları](#modül-2-operatörler-ve-kontrol-yapıları)
- [MODÜL 3: Döngüler ve İterasyon](#modül-3-döngüler-ve-iterasyon)
- [MODÜL 4: Veri Yapıları - Listeler ve Tuple'lar](#modül-4-veri-yapıları---listeler-ve-tuplelar)
- [MODÜL 5: Veri Yapıları - Dictionary ve Set](#modül-5-veri-yapıları---dictionary-ve-set)
- [MODÜL 6: Fonksiyonlar](#modül-6-fonksiyonlar)
- [MODÜL 7: String İşlemleri ve Dosya Yönetimi](#modül-7-string-i̇şlemleri-ve-dosya-yönetimi)
- [MODÜL 8: Hata Yönetimi ve Exception Handling](#modül-8-hata-yönetimi-ve-exception-handling)
- [MODÜL 9: Nesne Yönelimli Programlama - OOP Temelleri](#modül-9-nesne-yönelimli-programlama---oop-temelleri)
- [MODÜL 10: İleri OOP ve Modüler Programlama](#modül-10-i̇leri-oop-ve-modüler-programlama)
- [MODÜL 11: Popüler Kütüphaneler ve Araçlar](#modül-11-popüler-kütüphaneler-ve-araçlar)

---

# MODÜL 1: Python'a Giriş ve Temel Kavramlar

**Süre:** 2 Oturum (Hafta 1)

## 1.1 Python'ın Tarihçesi ve Kullanım Alanları

### Python Nedir?

Python, Guido van Rossum tarafından 1991 yılında geliştirilen, yüksek seviyeli, yorumlanan (interpreted), nesne yönelimli bir programlama dilidir.

### Neden Python?

1. **Kolay Öğrenilir**: Sade ve anlaşılır söz dizimi
2. **Çok Yönlü**: Web, veri bilimi, yapay zeka, otomasyon, oyun geliştirme
3. **Geniş Kütüphane Desteği**: NumPy, Pandas, Django, Flask, TensorFlow
4. **Platform Bağımsız**: Windows, Mac, Linux
5. **Büyük Topluluk**: Geniş dokümantasyon ve kaynak

### Kullanım Alanları

- **Web Geliştirme**: Django, Flask
- **Veri Bilimi ve Analizi**: Pandas, NumPy, Matplotlib
- **Yapay Zeka ve Makine Öğrenmesi**: TensorFlow, PyTorch, Scikit-learn
- **Otomasyon**: Selenium, BeautifulSoup
- **Oyun Geliştirme**: Pygame
- **Desktop Uygulamaları**: Tkinter, PyQt
- **DevOps ve Sistem Yönetimi**: Ansible, SaltStack

## 1.2 Geliştirme Ortamı Kurulumu

### Kurulum Seçenekleri

1. **Python İndirme**: [python.org](https://python.org)
2. **IDE Seçenekleri**:
   - **VS Code**: Hafif, eklenti desteği güçlü
   - **PyCharm**: Profesyonel, tam özellikli IDE
   - **Jupyter Notebook**: İnteraktif, veri bilimi için ideal
   - **Spyder**: Veri bilimi odaklı
   - **IDLE**: Python ile birlikte gelen basit IDE

### İlk Program: Hello World

```python
# En basit Python programı
print("Merhaba Dünya!")
print("Python öğrenmeye başladım!")

# Çıktı:
# Merhaba Dünya!
# Python öğrenmeye başladım!
```

## 1.3 Python Syntax ve Temel Kurallar

### Girintileme (Indentation)

Python'da kod blokları girintileme (indentation) ile belirlenir. Diğer dillerdeki süslü parantez `{}` yerine girintileme kullanılır.

```python
# Doğru kullanım
if True:
    print("Bu satır içeridedir")
    print("Bu da içeridedir")

# Yanlış kullanım (IndentationError verir)
# if True:
# print("Hata!")  # Girinti yok
```

### Yorumlar (Comments)

```python
# Bu tek satırlık yorumdur

"""
Bu çok satırlı
bir yorumdur.
Docstring olarak da kullanılır.
"""

x = 5  # Satır sonunda yorum
```

### Değişken İsimlendirme Kuralları

```python
# Doğru kullanımlar
ad = "Ahmet"
_yas = 25
ogrenci_no = 12345
sayi1 = 10

# Yanlış kullanımlar
# 1sayi = 10  # Rakamla başlayamaz
# ad-soyad = "Ahmet"  # Tire kullanılamaz
# class = "A"  # Rezerve kelime kullanılamaz
```

### Naming Conventions (Adlandırma Kuralları)

```python
# Snake case (Python'da tercih edilir)
ogrenci_adi = "Mehmet"
toplam_fiyat = 150.5

# Camel case (Class isimleri için)
class OgrenciKayitSistemi:
    pass

# Constants (Sabitler) - BÜYÜK HARF
PI = 3.14159
MAX_OGRENCI_SAYISI = 100
```

## 1.4 Değişkenler ve Veri Tipleri

### Değişken Tanımlama

Python'da değişken tanımlarken tip belirtmeye gerek yoktur (dinamik tiplemeli).

```python
# Temel değişken tanımlama
isim = "Ayşe"
yas = 20
boy = 1.65
ogrenci_mi = True

# Çoklu atama
x, y, z = 10, 20, 30
a = b = c = 5  # Hepsi aynı değer

# Değer değiştirme
x = 100
print(x)  # 100
```

### 1. Integer (int) - Tam Sayılar

```python
# Pozitif ve negatif tam sayılar
sayi1 = 42
sayi2 = -15
buyuk_sayi = 1000000

# Matematiksel işlemler
toplam = 10 + 5        # 15
fark = 20 - 8          # 12
carpim = 6 * 7         # 42
bolum = 15 // 3        # 5 (tam bölme)
kalan = 17 % 5         # 2 (mod)
us = 2 ** 3            # 8 (üs alma)

# Örnekler
print(10 + 3)          # 13
print(10 - 3)          # 7
print(10 * 3)          # 30
print(10 / 3)          # 3.333... (float döner)
print(10 // 3)         # 3 (tam bölme)
print(10 % 3)          # 1 (kalan)
print(2 ** 10)         # 1024
```

### 2. Float - Ondalıklı Sayılar

```python
# Float tanımlama
pi = 3.14159
sicaklik = -5.7
agirlik = 68.5

# İşlemler
sonuc = 10.5 + 3.2     # 13.7
carpim = 2.5 * 4       # 10.0

# Bilimsel gösterim
bilimsel = 1.5e3       # 1500.0
kucuk = 3.2e-2         # 0.032

print(type(3.14))      # <class 'float'>
```

### 3. String (str) - Metinler

```python
# String tanımlama
isim = "Ahmet"
soyisim = 'Yılmaz'
mesaj = """Merhaba,
Bu çok satırlı
bir mesajdır."""

# String birleştirme
tam_isim = isim + " " + soyisim  # "Ahmet Yılmaz"

# String çarpma
tekrar = "Ha" * 3                # "HaHaHa"

# String indexing
ilk_harf = isim[0]              # "A"
son_harf = isim[-1]             # "t"

# String slicing
parcala = "Python"[0:3]         # "Pyt"

# String uzunluğu
uzunluk = len("Merhaba")        # 7

# Örnek kullanımlar
print("Merhaba " + "Dünya")     # Merhaba Dünya
print("=" * 20)                 # ====================
print("Python"[0])              # P
print("Python"[-1])             # n
print(len("Merhaba"))           # 7
```

### 4. Boolean (bool) - Mantıksal Değerler

```python
# Boolean değerler
dogru = True
yanlis = False

# Karşılaştırma sonuçları boolean döner
sonuc1 = 5 > 3         # True
sonuc2 = 10 == 5       # False
sonuc3 = "a" < "b"     # True

# Boolean işlemler
ve_islemi = True and False      # False
veya_islemi = True or False     # True
degil = not True                # False

# Örnekler
print(5 > 3)           # True
print(10 == 10)        # True
print(5 != 3)          # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

### Veri Tipi Kontrolü

```python
# type() fonksiyonu
x = 100
print(type(x))         # <class 'int'>

y = 3.14
print(type(y))         # <class 'float'>

z = "Merhaba"
print(type(z))         # <class 'str'>

t = True
print(type(t))         # <class 'bool'>

# isinstance() ile tip kontrolü
print(isinstance(100, int))        # True
print(isinstance(3.14, float))     # True
print(isinstance("Hi", str))       # True
```

## 1.5 Type Casting (Tip Dönüşümü)

### int() - Tam Sayıya Dönüştürme

```python
# String'den int'e
sayi = int("42")              # 42
print(type(sayi))             # <class 'int'>

# Float'tan int'e (ondalık kısmı atar)
sayi2 = int(3.9)              # 3
sayi3 = int(-2.8)             # -2

# Boolean'dan int'e
sayi4 = int(True)             # 1
sayi5 = int(False)            # 0

# Hata verir
# sayi6 = int("12.5")         # ValueError
# sayi7 = int("abc")          # ValueError
```

### float() - Ondalıklı Sayıya Dönüştürme

```python
# String'den float'a
sayi = float("3.14")          # 3.14
sayi2 = float("42")           # 42.0

# Int'ten float'a
sayi3 = float(10)             # 10.0

# Boolean'dan float'a
sayi4 = float(True)           # 1.0
sayi5 = float(False)          # 0.0
```

### str() - String'e Dönüştürme

```python
# Int'ten string'e
metin = str(100)              # "100"
metin2 = str(3.14)            # "3.14"
metin3 = str(True)            # "True"

# Birleştirme için kullanım
yas = 25
mesaj = "Yaşım: " + str(yas)  # "Yaşım: 25"

# Doğrudan format kullanımı (daha iyi)
mesaj2 = f"Yaşım: {yas}"      # "Yaşım: 25"
```

### bool() - Boolean'a Dönüştürme

```python
# Sayılardan boolean'a
print(bool(1))                # True
print(bool(0))                # False
print(bool(-5))               # True
print(bool(100))              # True

# String'den boolean'a
print(bool("Merhaba"))        # True
print(bool(""))               # False (boş string)

# Diğer değerlerden
print(bool(None))             # False
print(bool([]))               # False (boş liste)
print(bool([1, 2]))           # True
```

### Pratik Örnekler

```python
# Örnek 1: Kullanıcıdan sayı alma
sayi_str = input("Bir sayı girin: ")
sayi = int(sayi_str)
print(f"Girilen sayının karesi: {sayi ** 2}")

# Örnek 2: Hesaplama
a = "10"
b = "20"
toplam = int(a) + int(b)      # 30

# Örnek 3: Format ve tip dönüşümü
fiyat = 149.99
kdv_orani = 0.18
kdv = fiyat * kdv_orani
toplam_fiyat = fiyat + kdv

print(f"Fiyat: {fiyat} TL")
print(f"KDV: {kdv:.2f} TL")
print(f"Toplam: {toplam_fiyat:.2f} TL")
```

## 1.6 Input/Output İşlemleri

### print() Fonksiyonu

```python
# Basit yazdırma
print("Merhaba Dünya!")

# Çoklu değer yazdırma
print("Adı:", "Mehmet", "Yaş:", 25)
# Çıktı: Adı: Mehmet Yaş: 25

# sep parametresi (ayırıcı)
print("Python", "Java", "C++", sep=" | ")
# Çıktı: Python | Java | C++

# end parametresi (sonlandırıcı)
print("Birinci satır", end=" -> ")
print("İkinci satır")
# Çıktı: Birinci satır -> İkinci satır

# Değişken yazdırma
isim = "Ali"
yas = 30
print("İsim:", isim, "Yaş:", yas)
```

### String Formatting Yöntemleri

```python
ad = "Ayşe"
yas = 22
not_ortalamasi = 85.75

# 1. f-string (Python 3.6+) - En modern ve önerilen
print(f"Adı: {ad}, Yaşı: {yas}")
print(f"Not ortalaması: {not_ortalamasi:.2f}")  # 2 ondalık

# 2. format() metodu
print("Adı: {}, Yaşı: {}".format(ad, yas))
print("Adı: {0}, Yaşı: {1}".format(ad, yas))
print("Adı: {isim}, Yaşı: {y}".format(isim=ad, y=yas))

# 3. % operatörü (eski yöntem)
print("Adı: %s, Yaşı: %d" % (ad, yas))

# Formatlama örnekleri
sayi = 123.456789
print(f"{sayi:.2f}")          # 123.46 (2 ondalık)
print(f"{sayi:10.2f}")        # "    123.46" (10 karakter, sağa yasla)
print(f"{sayi:010.2f}")       # "0000123.46" (sıfırla doldur)

# Hizalama
print(f"{'Sol':<10}|")        # "Sol       |"
print(f"{'Orta':^10}|")       # "   Orta   |"
print(f"{'Sağ':>10}|")        # "       Sağ|"
```

### input() Fonksiyonu

```python
# Basit input
isim = input("Adınız nedir? ")
print(f"Merhaba {isim}!")

# Sayı girişi (tip dönüşümü ile)
yas = int(input("Yaşınız: "))
print(f"Doğum yılınız: {2024 - yas}")

# Float girişi
boy = float(input("Boyunuz (m): "))
print(f"Boyunuz cm cinsinden: {boy * 100}")

# Çoklu input
a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
print(f"Toplam: {a + b}")

# Tek satırda çoklu input (split ile)
# Kullanıcı: "10 20 30" şeklinde girer
sayilar = input("Üç sayı girin (boşlukla ayırın): ").split()
x, y, z = int(sayilar[0]), int(sayilar[1]), int(sayilar[2])
print(f"Toplam: {x + y + z}")

# Daha kısa hali
x, y, z = map(int, input("Üç sayı girin: ").split())
```

### Pratik Input/Output Örnekleri

```python
# Örnek 1: Kişisel bilgi formu
print("=" * 40)
print("KİŞİSEL BİLGİ FORMU")
print("=" * 40)

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
sehir = input("Şehir: ")

print("\n--- GİRİLEN BİLGİLER ---")
print(f"Ad Soyad: {ad} {soyad}")
print(f"Yaş: {yas}")
print(f"Şehir: {sehir}")

# Örnek 2: Alan hesaplama
print("\nDAİRE ALAN HESAPLAMA")
yaricap = float(input("Dairenin yarıçapını girin (cm): "))
pi = 3.14159
alan = pi * (yaricap ** 2)
print(f"Dairenin alanı: {alan:.2f} cm²")

# Örnek 3: Sıcaklık dönüştürme
print("\nSICAKLIK DÖNÜŞTÜRÜCÜ")
celsius = float(input("Celsius cinsinden sıcaklık: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")
```

## 1.7 Basit Hesap Makinesi Projesi

```python
"""
HESAP MAKİNESİ PROJESİ
Kullanıcıdan iki sayı ve işlem alır, sonucu gösterir
"""

print("=" * 50)
print("         HESAP MAKİNESİ         ")
print("=" * 50)

# Kullanıcıdan veri alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print("\nİşlemler:")
print("1. Toplama (+)")
print("2. Çıkarma (-)")
print("3. Çarpma (*)")
print("4. Bölme (/)")
print("5. Mod alma (%)")
print("6. Üs alma (**)")

islem = input("\nYapmak istediğiniz işlemi seçin (1-6): ")

# İşlemleri gerçekleştirme
if islem == "1":
    sonuc = sayi1 + sayi2
    print(f"\nSonuç: {sayi1} + {sayi2} = {sonuc}")
elif islem == "2":
    sonuc = sayi1 - sayi2
    print(f"\nSonuç: {sayi1} - {sayi2} = {sonuc}")
elif islem == "3":
    sonuc = sayi1 * sayi2
    print(f"\nSonuç: {sayi1} * {sayi2} = {sonuc}")
elif islem == "4":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print(f"\nSonuç: {sayi1} / {sayi2} = {sonuc:.2f}")
    else:
        print("\nHata: Sıfıra bölme yapılamaz!")
elif islem == "5":
    sonuc = sayi1 % sayi2
    print(f"\nSonuç: {sayi1} % {sayi2} = {sonuc}")
elif islem == "6":
    sonuc = sayi1 ** sayi2
    print(f"\nSonuç: {sayi1} ** {sayi2} = {sonuc}")
else:
    print("\nGeçersiz işlem seçimi!")

print("=" * 50)
```

## 1.8 Algoritma Problemleri - Modül 1

### Problem 1: Basit İşlemler

**Soru:** Kullanıcıdan iki tam sayı alın ve bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırın.

```python
# Çözüm
a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

print(f"Toplam: {a + b}")
print(f"Fark: {a - b}")
print(f"Çarpım: {a * b}")
print(f"Bölüm: {a / b:.2f}")
```

### Problem 2: Alan ve Çevre Hesaplama

**Soru:** Kullanıcıdan dikdörtgenin kısa ve uzun kenarını alın. Alan ve çevreyi hesaplayıp yazdırın.

```python
# Çözüm
kisa_kenar = float(input("Kısa kenar (cm): "))
uzun_kenar = float(input("Uzun kenar (cm): "))

alan = kisa_kenar * uzun_kenar
cevre = 2 * (kisa_kenar + uzun_kenar)

print(f"Alan: {alan} cm²")
print(f"Çevre: {cevre} cm")
```

### Problem 3: Ortalama Hesaplama

**Soru:** Kullanıcıdan üç sınav notu alın ve bu notların ortalamasını hesaplayın.

```python
# Çözüm
vize = float(input("Vize notu: "))
final = float(input("Final notu: "))
odev = float(input("Ödev notu: "))

ortalama = (vize + final + odev) / 3

print(f"Not ortalamanız: {ortalama:.2f}")
```

### Problem 4: KDV Hesaplama

**Soru:** Kullanıcıdan bir ürünün fiyatını alın. %18 KDV ekleyerek toplam fiyatı hesaplayın.

```python
# Çözüm
fiyat = float(input("Ürün fiyatı (TL): "))
kdv_orani = 18  # %18

kdv_tutari = fiyat * kdv_orani / 100
toplam_fiyat = fiyat + kdv_tutari

print(f"KDV Tutarı: {kdv_tutari:.2f} TL")
print(f"Toplam Fiyat: {toplam_fiyat:.2f} TL")
```

### Problem 5: Saniye Çevirme

**Soru:** Kullanıcıdan toplam saniye değeri alın. Bu değeri saat, dakika, saniye formatına çevirin.

```python
# Çözüm
toplam_saniye = int(input("Toplam saniye: "))

saat = toplam_saniye // 3600
kalan = toplam_saniye % 3600
dakika = kalan // 60
saniye = kalan % 60

print(f"{toplam_saniye} saniye = {saat} saat, {dakika} dakika, {saniye} saniye")

# Örnek: 7325 saniye girişi
# Çıktı: 7325 saniye = 2 saat, 2 dakika, 5 saniye
```

### Problem 6: Yaş Hesaplama

**Soru:** Kullanıcının doğum yılını alın ve kaç yaşında olduğunu hesaplayın.

```python
# Çözüm
dogum_yili = int(input("Doğum yılınız: "))
su_anki_yil = 2024

yas = su_anki_yil - dogum_yili

print(f"Yaşınız: {yas}")
```

### Problem 7: İki Sayının Değerini Değiştirme (Swap)

**Soru:** İki değişkenin değerini birbirleriyle değiştirin (swap işlemi).

```python
# Çözüm 1: Geçici değişken kullanarak
a = int(input("a: "))
b = int(input("b: "))

print(f"Önce -> a: {a}, b: {b}")

temp = a
a = b
b = temp

print(f"Sonra -> a: {a}, b: {b}")

# Çözüm 2: Python'a özgü yöntem (daha şık)
a, b = b, a
```

### Problem 8: Daire Bilgileri

**Soru:** Kullanıcıdan dairenin yarıçapını alın. Çevre, alan ve hacim (küre) hesaplayın.

```python
# Çözüm
yaricap = float(input("Yarıçap (cm): "))
pi = 3.14159

cevre = 2 * pi * yaricap
alan = pi * (yaricap ** 2)
hacim = (4/3) * pi * (yaricap ** 3)

print(f"Çevre: {cevre:.2f} cm")
print(f"Alan: {alan:.2f} cm²")
print(f"Hacim (küre): {hacim:.2f} cm³")
```

### Problem 9: Vücut Kitle İndeksi (BMI)

**Soru:** Kullanıcının kilosunu ve boyunu alarak BMI değerini hesaplayın.
BMI = Kilo / (Boy * Boy)

```python
# Çözüm
kilo = float(input("Kilonuz (kg): "))
boy = float(input("Boyunuz (m): "))

bmi = kilo / (boy ** 2)

print(f"Vücut Kitle İndeksiniz: {bmi:.2f}")
```

### Problem 10: Maaş Hesaplama

**Soru:** Bir çalışanın aylık maaşı, çalışma saati ve saat ücreti ile hesaplanıyor. Kullanıcıdan haftalık çalışma saati ve saat ücretini alın. Aylık brüt maaşı hesaplayın (1 ay = 4 hafta).

```python
# Çözüm
haftalik_saat = float(input("Haftalık çalışma saati: "))
saat_ucreti = float(input("Saat ücreti (TL): "))

aylik_saat = haftalik_saat * 4
brut_maas = aylik_saat * saat_ucreti

print(f"Aylık brüt maaş: {brut_maas:.2f} TL")
```

## 1.9 Ödev Önerileri - Modül 1

1. **Basit Dönüştürücü**: Metre-Feet, Kilogram-Pound dönüştürücüsü yapın
2. **Kişisel Bütçe**: Gelir ve giderleri alıp kalan parayı hesaplayan program
3. **Yaş Gün Hesaplayıcı**: Doğum tarihinden bugüne kaç gün yaşandığını hesaplayan program
4. **İndirim Hesaplayıcı**: Ürün fiyatı ve indirim oranını alıp yeni fiyatı hesaplayan program
5. **Restoran Hesabı**: Yemek fiyatı, bahşiş oranı ve kişi sayısını alıp kişi başı tutarı hesaplayan program

---

# MODÜL 2: Operatörler ve Kontrol Yapıları

**Süre:** 2 Oturum (Hafta 2)

## 2.1 Aritmetik Operatörler

Matematiksel işlemler yapmak için kullanılır.

```python
a = 10
b = 3

# Toplama
toplam = a + b              # 13
print(f"{a} + {b} = {toplam}")

# Çıkarma
fark = a - b                # 7
print(f"{a} - {b} = {fark}")

# Çarpma
carpim = a * b              # 30
print(f"{a} * {b} = {carpim}")

# Bölme (float döner)
bolum = a / b               # 3.333...
print(f"{a} / {b} = {bolum:.2f}")

# Tam bölme (floor division)
tam_bolum = a // b          # 3
print(f"{a} // {b} = {tam_bolum}")

# Mod (kalan)
kalan = a % b               # 1
print(f"{a} % {b} = {kalan}")

# Üs alma
us = a ** b                 # 1000
print(f"{a} ** {b} = {us}")
```

### Aritmetik Operatörler Öncelik Sırası

```python
# Öncelik: ** > *, /, //, % > +, -
# Parantez her zaman önceliklidir

sonuc1 = 2 + 3 * 4          # 14 (önce çarpma)
sonuc2 = (2 + 3) * 4        # 20 (önce toplama)
sonuc3 = 10 - 5 / 2         # 7.5
sonuc4 = (10 - 5) / 2       # 2.5

# Karmaşık örnek
sonuc = 2 ** 3 + 4 * 5 - 6 / 2
# 2**3 = 8
# 4*5 = 20
# 6/2 = 3.0
# 8 + 20 - 3.0 = 25.0

print(sonuc)                # 25.0
```

### Artırma ve Azaltma

```python
# Python'da ++ ve -- operatörleri yoktur!
# Bunun yerine += ve -= kullanılır

sayac = 0
sayac += 1                  # sayac = sayac + 1
print(sayac)                # 1

sayac += 5                  # sayac = sayac + 5
print(sayac)                # 6

sayac -= 2                  # sayac = sayac - 2
print(sayac)                # 4

# Diğer operatörlerle de kullanılır
x = 10
x *= 2                      # x = x * 2
print(x)                    # 20

x /= 4                      # x = x / 4
print(x)                    # 5.0

x //= 2                     # x = x // 2
print(x)                    # 2.0

x %= 2                      # x = x % 2
print(x)                    # 0.0
```

## 2.2 Karşılaştırma Operatörleri

İki değeri karşılaştırır ve True/False döner.

```python
a = 10
b = 5

# Eşit mi?
print(a == b)               # False
print(10 == 10)             # True

# Eşit değil mi?
print(a != b)               # True
print(10 != 10)             # False

# Büyük mü?
print(a > b)                # True
print(5 > 10)               # False

# Küçük mü?
print(a < b)                # False
print(5 < 10)               # True

# Büyük veya eşit mi?
print(a >= b)               # True
print(10 >= 10)             # True

# Küçük veya eşit mi?
print(a <= b)               # False
print(10 <= 10)             # True

# String karşılaştırma (alfabetik sıra)
print("ahmet" < "mehmet")   # True (a < m)
print("Ali" == "ali")       # False (büyük-küçük harf duyarlı)
```

### Dikkat Edilmesi Gerekenler

```python
# Float karşılaştırmada dikkatli olun
print(0.1 + 0.2 == 0.3)     # False (floating point hatası)

# Çözüm: round() kullanın veya yaklaşık kontrol edin
print(round(0.1 + 0.2, 1) == 0.3)  # True

# String'de == ve is farkı
a = "python"
b = "python"
print(a == b)               # True (değer karşılaştırma)
print(a is b)               # True (aynı nesne)

# Ama dikkatli!
x = "python programlama"
y = "python programlama"
print(x == y)               # True (değer aynı)
print(x is y)               # False (farklı nesneler)
```

## 2.3 Mantıksal Operatörler

Boolean değerlerle çalışır.

```python
# and operatörü - Her ikisi de True olmalı
print(True and True)        # True
print(True and False)       # False
print(False and False)      # False

# or operatörü - En az biri True olmalı
print(True or False)        # True
print(False or False)       # False
print(True or True)         # True

# not operatörü - Tersi alır
print(not True)             # False
print(not False)            # True

# Pratik örnekler
yas = 25
gelir = 5000

# Hem yaş hem gelir uygun mu?
uygun_mu = (yas >= 18) and (gelir >= 3000)
print(uygun_mu)             # True

# En az birisi doğru mu?
yas = 16
ogrenci_mi = True
indirim = (yas < 18) or ogrenci_mi
print(indirim)              # True

# Karmaşık koşullar
yas = 30
maas = 8000
kredi_skoru = 750

kredi_onay = (yas >= 25 and maas >= 5000) and (kredi_skoru >= 700)
print(f"Kredi onayı: {kredi_onay}")  # True
```

### Kısa Devre (Short-Circuit) Değerlendirmesi

```python
# and operatöründe ilk False görüldüğünde durur
sonuc = False and print("Bu çalışmaz")  # print çalışmaz

# or operatöründe ilk True görüldüğünde durur
sonuc = True or print("Bu çalışmaz")    # print çalışmaz

# Pratik kullanım
x = 0
# Sıfıra bölme hatasını önleme
sonuc = x != 0 and (10 / x > 2)  # x != 0 False olduğu için bölme işlemi yapılmaz
print(sonuc)                      # False
```

## 2.4 Üyelik Operatörleri

```python
# in operatörü - Eleman içinde mi?
metin = "Python programlama"
print("Python" in metin)          # True
print("Java" in metin)            # False

liste = [1, 2, 3, 4, 5]
print(3 in liste)                 # True
print(10 in liste)                # False

# not in operatörü - Eleman içinde değil mi?
print("Java" not in metin)        # True
print(10 not in liste)            # True

# Pratik kullanım
izinli_kullanicilar = ["admin", "moderator", "user123"]
kullanici = "user456"

if kullanici in izinli_kullanicilar:
    print("Erişim izni verildi")
else:
    print("Erişim reddedildi")
```

## 2.5 Kimlik Operatörleri

```python
# is operatörü - Aynı nesne mi?
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)                # True (değerler aynı)
print(a is b)                # False (farklı nesneler)
print(a is c)                # True (aynı nesne)

# is not operatörü
print(a is not b)            # True

# None kontrolü
x = None
print(x is None)             # True
print(x == None)             # True (ama "is" kullanmak daha iyi)

# Dikkat: Küçük sayılarda farklı davranış
x = 256
y = 256
print(x is y)                # True (Python küçük sayıları önbelleğe alır)

x = 257
y = 257
print(x is y)                # False (büyük sayılar için farklı nesneler)
```

## 2.6 If-Elif-Else Yapısı

### Basit If Yapısı

```python
# Tek koşul
yas = 18

if yas >= 18:
    print("Reşitsiniz")
    print("Ehliyet alabilirsiniz")

# If olmadan devam eder
print("Program bitti")
```

### If-Else Yapısı

```python
# İki seçenek
not_ortalamasi = 65

if not_ortalamasi >= 50:
    print("Geçtiniz!")
else:
    print("Kaldınız!")

# Tek satırda if-else (ternary operator)
durum = "Geçti" if not_ortalamasi >= 50 else "Kaldı"
print(durum)
```

### If-Elif-Else Yapısı

```python
# Çoklu koşul
puan = 85

if puan >= 90:
    harf_notu = "AA"
elif puan >= 80:
    harf_notu = "BA"
elif puan >= 70:
    harf_notu = "BB"
elif puan >= 60:
    harf_notu = "CB"
elif puan >= 50:
    harf_notu = "CC"
else:
    harf_notu = "FF"

print(f"Notunuz: {harf_notu}")

# Daha detaylı örnek
yas = int(input("Yaşınızı girin: "))

if yas < 0:
    print("Geçersiz yaş!")
elif yas < 13:
    print("Çocuk kategorisi")
elif yas < 18:
    print("Genç kategorisi")
elif yas < 65:
    print("Yetişkin kategorisi")
else:
    print("Emekli kategorisi")
```

### İç İçe If Yapıları (Nested If)

```python
# Nested if kullanımı
kullanici_adi = "admin"
sifre = "12345"

if kullanici_adi == "admin":
    if sifre == "12345":
        print("Giriş başarılı!")
    else:
        print("Şifre yanlış!")
else:
    print("Kullanıcı adı yanlış!")

# Daha karmaşık örnek
yas = 20
gelir = 6000
kredi_skoru = 800

if yas >= 18:
    if gelir >= 5000:
        if kredi_skoru >= 700:
            print("Kredi başvurunuz onaylandı!")
        else:
            print("Kredi skorunuz yetersiz")
    else:
        print("Geliriniz yetersiz")
else:
    print("Yaş şartını sağlamıyorsunuz")

# Yukarıdakinin daha kısa hali (and kullanarak)
if yas >= 18 and gelir >= 5000 and kredi_skoru >= 700:
    print("Kredi başvurunuz onaylandı!")
else:
    print("Kredi başvurunuz reddedildi")
```

### Pratik If-Elif-Else Örnekleri

```python
# Örnek 1: Mevsim belirleme
ay = int(input("Ay numarası (1-12): "))

if ay in [12, 1, 2]:
    print("Kış")
elif ay in [3, 4, 5]:
    print("İlkbahar")
elif ay in [6, 7, 8]:
    print("Yaz")
elif ay in [9, 10, 11]:
    print("Sonbahar")
else:
    print("Geçersiz ay!")

# Örnek 2: Vücut kitle indeksi değerlendirme
kilo = float(input("Kilonuz (kg): "))
boy = float(input("Boyunuz (m): "))

bmi = kilo / (boy ** 2)

if bmi < 18.5:
    kategori = "Zayıf"
elif bmi < 25:
    kategori = "Normal"
elif bmi < 30:
    kategori = "Fazla Kilolu"
else:
    kategori = "Obez"

print(f"BMI: {bmi:.2f} - Kategori: {kategori}")

# Örnek 3: Çoklu koşullar
isim = input("Adınız: ")
yas = int(input("Yaşınız: "))
uyelik = input("Üyelik tipiniz (standart/premium/vip): ").lower()

# İndirim hesaplama
indirim_orani = 0

if yas < 18:
    indirim_orani = 20  # Gençlere %20
elif yas >= 65:
    indirim_orani = 30  # Yaşlılara %30

if uyelik == "premium":
    indirim_orani += 10
elif uyelik == "vip":
    indirim_orani += 20

print(f"{isim}, toplam indiriminiz: %{indirim_orani}")
```

## 2.7 Match-Case Yapısı (Python 3.10+)

Match-case, switch-case yapısının Python karşılığıdır.

```python
# Basit match-case
ay = 3

match ay:
    case 1:
        print("Ocak")
    case 2:
        print("Şubat")
    case 3:
        print("Mart")
    case 4:
        print("Nisan")
    case 5:
        print("Mayıs")
    case 6:
        print("Haziran")
    case 7:
        print("Temmuz")
    case 8:
        print("Ağustos")
    case 9:
        print("Eylül")
    case 10:
        print("Ekim")
    case 11:
        print("Kasım")
    case 12:
        print("Aralık")
    case _:  # default (diğer durumlar)
        print("Geçersiz ay!")

# Çoklu değer kontrolü
gun = "Cumartesi"

match gun:
    case "Pazartesi" | "Salı" | "Çarşamba" | "Perşembe" | "Cuma":
        print("Hafta içi - Çalışma günü")
    case "Cumartesi" | "Pazar":
        print("Hafta sonu - Tatil günü")
    case _:
        print("Geçersiz gün!")

# Match-case ile pattern matching
komut = input("Komut girin (açık/kapat/yeniden başlat): ").lower()

match komut:
    case "açık" | "aç" | "open":
        print("Sistem açılıyor...")
    case "kapat" | "kapa" | "close":
        print("Sistem kapatılıyor...")
    case "yeniden başlat" | "restart":
        print("Sistem yeniden başlatılıyor...")
    case _:
        print("Geçersiz komut!")

# Koşullu match-case (guard)
sayi = 15

match sayi:
    case n if n < 0:
        print("Negatif sayı")
    case n if n == 0:
        print("Sıfır")
    case n if 0 < n < 10:
        print("Tek haneli pozitif sayı")
    case n if n >= 10:
        print("İki veya daha fazla haneli sayı")
```

## 2.8 Pratik Projeler

### Proje 1: ATM Simülasyonu

```python
"""
ATM SİMÜLASYONU
Kullanıcı bakiye sorgulama, para çekme, para yatırma işlemleri yapabilir
"""

print("=" * 40)
print("     ATM SİSTEMİNE HOŞGELDİNİZ")
print("=" * 40)

bakiye = 1000  # Başlangıç bakiyesi

print("\nİşlemler:")
print("1. Bakiye Sorgula")
print("2. Para Çek")
print("3. Para Yatır")
print("4. Çıkış")

secim = input("\nYapmak istediğiniz işlemi seçin (1-4): ")

if secim == "1":
    print(f"\nGüncel bakiyeniz: {bakiye} TL")

elif secim == "2":
    cekilecek_miktar = float(input("Çekmek istediğiniz tutarı girin: "))
    
    if cekilecek_miktar <= 0:
        print("Hata: Geçersiz tutar!")
    elif cekilecek_miktar > bakiye:
        print("Hata: Yetersiz bakiye!")
    else:
        bakiye -= cekilecek_miktar
        print(f"\n{cekilecek_miktar} TL çekildi.")
        print(f"Kalan bakiye: {bakiye} TL")

elif secim == "3":
    yatirilacak_miktar = float(input("Yatırmak istediğiniz tutarı girin: "))
    
    if yatirilacak_miktar <= 0:
        print("Hata: Geçersiz tutar!")
    else:
        bakiye += yatirilacak_miktar
        print(f"\n{yatirilacak_miktar} TL yatırıldı.")
        print(f"Güncel bakiye: {bakiye} TL")

elif secim == "4":
    print("\nİyi günler dileriz!")

else:
    print("\nHata: Geçersiz işlem seçimi!")

print("=" * 40)
```

### Proje 2: Not Hesaplama Sistemi

```python
"""
NOT HESAPLAMA SİSTEMİ
Öğrencinin vize, final ve ödev notlarını alır
Ortalamayı hesaplar ve harf notu verir
"""

print("=" * 50)
print("        NOT HESAPLAMA SİSTEMİ")
print("=" * 50)

# Notları al
isim = input("\nÖğrenci adı: ")
vize = float(input("Vize notu (0-100): "))
final = float(input("Final notu (0-100): "))
odev = float(input("Ödev notu (0-100): "))

# Not kontrolü
if vize < 0 or vize > 100 or final < 0 or final > 100 or odev < 0 or odev > 100:
    print("\nHata: Notlar 0-100 arasında olmalıdır!")
else:
    # Ortalama hesaplama (%30 vize, %50 final, %20 ödev)
    ortalama = (vize * 0.30) + (final * 0.50) + (odev * 0.20)
    
    # Harf notu belirleme
    if ortalama >= 90:
        harf = "AA"
        durum = "Geçti"
    elif ortalama >= 85:
        harf = "BA"
        durum = "Geçti"
    elif ortalama >= 80:
        harf = "BB"
        durum = "Geçti"
    elif ortalama >= 75:
        harf = "CB"
        durum = "Geçti"
    elif ortalama >= 70:
        harf = "CC"
        durum = "Geçti"
    elif ortalama >= 65:
        harf = "DC"
        durum = "Geçti"
    elif ortalama >= 60:
        harf = "DD"
        durum = "Geçti"
    elif ortalama >= 50:
        harf = "FD"
        durum = "Koşullu Geçti"
    else:
        harf = "FF"
        durum = "Kaldı"
    
    # Sonuçları yazdır
    print("\n" + "=" * 50)
    print("SONUÇLAR")
    print("=" * 50)
    print(f"Öğrenci: {isim}")
    print(f"Vize: {vize}")
    print(f"Final: {final}")
    print(f"Ödev: {odev}")
    print(f"Ortalama: {ortalama:.2f}")
    print(f"Harf Notu: {harf}")
    print(f"Durum: {durum}")
    print("=" * 50)
```

## 2.9 Algoritma Problemleri - Modül 2

### Problem 1: Tek mi Çift mi?

**Soru:** Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu bulun.

```python
# Çözüm
sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print(f"{sayi} çift sayıdır")
else:
    print(f"{sayi} tek sayıdır")
```

### Problem 2: Pozitif, Negatif, Sıfır

**Soru:** Kullanıcıdan bir sayı alın ve pozitif, negatif veya sıfır olduğunu belirleyin.

```python
# Çözüm
sayi = float(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif sayı")
elif sayi < 0:
    print("Negatif sayı")
else:
    print("Sıfır")
```

### Problem 3: En Büyük Sayı

**Soru:** Kullanıcıdan üç sayı alın ve en büyüğünü bulun.

```python
# Çözüm
a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
c = int(input("Üçüncü sayı: "))

if a >= b and a >= c:
    print(f"En büyük sayı: {a}")
elif b >= a and b >= c:
    print(f"En büyük sayı: {b}")
else:
    print(f"En büyük sayı: {c}")

# Alternatif (max fonksiyonu)
en_buyuk = max(a, b, c)
print(f"En büyük sayı: {en_buyuk}")
```

### Problem 4: Artık Yıl

**Soru:** Kullanıcıdan bir yıl alın ve artık yıl olup olmadığını kontrol edin.
Kural: 4'e bölünebilir VE (100'e bölünemez VEYA 400'e bölünebilir)

```python
# Çözüm
yil = int(input("Yıl girin: "))

if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print(f"{yil} artık yıldır (366 gün)")
else:
    print(f"{yil} artık yıl değildir (365 gün)")
```

### Problem 5: Üçgen Kontrolü

**Soru:** Kullanıcıdan üç kenar uzunluğu alın. Bu kenarlarla üçgen oluşturulup oluşturulamayacağını kontrol edin.
Kural: Her bir kenar, diğer iki kenarın toplamından küçük olmalıdır.

```python
# Çözüm
a = float(input("Birinci kenar: "))
b = float(input("İkinci kenar: "))
c = float(input("Üçüncü kenar: "))

if a + b > c and a + c > b and b + c > a:
    print("Bu kenarlarla üçgen oluşturulabilir")
    
    # Üçgen tipi belirleme (bonus)
    if a == b == c:
        print("Eşkenar üçgen")
    elif a == b or b == c or a == c:
        print("İkizkenar üçgen")
    else:
        print("Çeşitkenar üçgen")
else:
    print("Bu kenarlarla üçgen oluşturulamaz")
```

### Problem 6: Kargo Ücreti Hesaplama

**Soru:** Paket ağırlığına göre kargo ücreti hesaplayın:
- 0-1 kg: 15 TL
- 1-5 kg: 25 TL
- 5-10 kg: 40 TL
- 10+ kg: 60 TL

```python
# Çözüm
agirlik = float(input("Paket ağırlığı (kg): "))

if agirlik <= 0:
    print("Geçersiz ağırlık!")
elif agirlik <= 1:
    ucret = 15
elif agirlik <= 5:
    ucret = 25
elif agirlik <= 10:
    ucret = 40
else:
    ucret = 60

if agirlik > 0:
    print(f"{agirlik} kg için kargo ücreti: {ucret} TL")
```

### Problem 7: Kullanıcı Giriş Sistemi

**Soru:** Basit bir kullanıcı giriş sistemi yapın. Kullanıcı adı ve şifre doğruysa "Hoş geldiniz", 3 deneme hakkı tanıyın.

```python
# Çözüm
dogru_kullanici = "admin"
dogru_sifre = "1234"
deneme_hakki = 3

while deneme_hakki > 0:
    kullanici = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    
    if kullanici == dogru_kullanici and sifre == dogru_sifre:
        print("Hoş geldiniz!")
        break
    else:
        deneme_hakki -= 1
        if deneme_hakki > 0:
            print(f"Hatalı giriş! Kalan deneme hakkı: {deneme_hakki}")
        else:
            print("Deneme hakkınız kalmadı. Sistem kilitlendi!")
```

### Problem 8: Elektrik Faturası Hesaplama

**Soru:** Kullanılan elektrik miktarına göre fatura hesaplayın:
- 0-100 kWh: 1.5 TL/kWh
- 101-200 kWh: 2.0 TL/kWh
- 200+ kWh: 2.5 TL/kWh

```python
# Çözüm
tuketim = float(input("Tüketim (kWh): "))

if tuketim <= 0:
    print("Geçersiz tüketim değeri!")
elif tuketim <= 100:
    fatura = tuketim * 1.5
elif tuketim <= 200:
    fatura = (100 * 1.5) + ((tuketim - 100) * 2.0)
else:
    fatura = (100 * 1.5) + (100 * 2.0) + ((tuketim - 200) * 2.5)

if tuketim > 0:
    print(f"Toplam fatura: {fatura:.2f} TL")
```

### Problem 9: Hesap Makinesi (Match-Case ile)

**Soru:** Match-case kullanarak hesap makinesi yapın.

```python
# Çözüm (Python 3.10+)
sayi1 = float(input("Birinci sayı: "))
sayi2 = float(input("İkinci sayı: "))
islem = input("İşlem (+, -, *, /): ")

match islem:
    case "+":
        sonuc = sayi1 + sayi2
        print(f"{sayi1} + {sayi2} = {sonuc}")
    case "-":
        sonuc = sayi1 - sayi2
        print(f"{sayi1} - {sayi2} = {sonuc}")
    case "*":
        sonuc = sayi1 * sayi2
        print(f"{sayi1} * {sayi2} = {sonuc}")
    case "/":
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
            print(f"{sayi1} / {sayi2} = {sonuc:.2f}")
        else:
            print("Hata: Sıfıra bölme!")
    case _:
        print("Geçersiz işlem!")
```

### Problem 10: Geometrik Şekil Alan Hesaplama

**Soru:** Kullanıcının seçimine göre daire, kare veya dikdörtgenin alanını hesaplayın.

```python
# Çözüm
print("Şekil Seçin:")
print("1. Daire")
print("2. Kare")
print("3. Dikdörtgen")

secim = input("Seçiminiz (1-3): ")

if secim == "1":
    yaricap = float(input("Yarıçap: "))
    alan = 3.14159 * (yaricap ** 2)
    print(f"Daire alanı: {alan:.2f}")

elif secim == "2":
    kenar = float(input("Kenar uzunluğu: "))
    alan = kenar ** 2
    print(f"Kare alanı: {alan:.2f}")

elif secim == "3":
    uzun_kenar = float(input("Uzun kenar: "))
    kisa_kenar = float(input("Kısa kenar: "))
    alan = uzun_kenar * kisa_kenar
    print(f"Dikdörtgen alanı: {alan:.2f}")

else:
    print("Geçersiz seçim!")
```

## 2.10 Ödev Önerileri - Modül 2

1. **Sınıf Geçme Sistemi**: Kullanıcıdan notları alıp sınıf geçip geçmediğini, harf notunu gösteren program
2. **Vergi Hesaplayıcı**: Gelir düzeyine göre farklı oranlarda vergi hesaplayan program
3. **Restoran Sipariş Sistemi**: Menüden seçim yapıp toplam tutarı hesaplayan program
4. **Basit Oyun**: Kullanıcı ile bilgisayarın taş-kağıt-makas oynadığı program
5. **Kredi Kartı Doğrulama**: Kredi kartı numarasının geçerli olup olmadığını kontrol eden program (Luhn algoritması)

---

# MODÜL 3: Döngüler ve İterasyon

**Süre:** 2 Oturum (Hafta 3)

## 3.1 While Döngüsü

While döngüsü, koşul True olduğu sürece çalışmaya devam eder.

### Basit While Döngüsü

```python
# Basit sayaç
sayac = 1

while sayac <= 5:
    print(f"Sayaç: {sayac}")
    sayac += 1

# Çıktı:
# Sayaç: 1
# Sayaç: 2
# Sayaç: 3
# Sayaç: 4
# Sayaç: 5

# 10'dan geriye sayma
sayi = 10

while sayi >= 1:
    print(sayi, end=" ")
    sayi -= 1

print("\nFırlatma!")
# Çıktı: 10 9 8 7 6 5 4 3 2 1 Fırlatma!
```

### While ile Toplam Hesaplama

```python
# 1'den 10'a kadar olan sayıların toplamı
toplam = 0
sayi = 1

while sayi <= 10:
    toplam += sayi
    sayi += 1

print(f"Toplam: {toplam}")  # 55

# 1'den N'e kadar olan sayıların toplamı
n = int(input("N değeri: "))
toplam = 0
sayi = 1

while sayi <= n:
    toplam += sayi
    sayi += 1

print(f"1'den {n}'e kadar olan sayıların toplamı: {toplam}")
```

### Kullanıcı Girişi ile While

```python
# Doğru şifre girilene kadar devam et
dogru_sifre = "python123"
sifre = ""

while sifre != dogru_sifre:
    sifre = input("Şifre girin: ")
    if sifre != dogru_sifre:
        print("Yanlış şifre, tekrar deneyin!")

print("Giriş başarılı!")

# Pozitif sayı alana kadar devam et
sayi = -1

while sayi <= 0:
    sayi = int(input("Pozitif bir sayı girin: "))
    if sayi <= 0:
        print("Lütfen pozitif bir sayı girin!")

print(f"Teşekkürler! Girdiğiniz sayı: {sayi}")
```

### Sonsuz Döngü ve Kontrol

```python
# Dikkatli olun! Sonsuz döngü oluşturabilir
# while True:  # Sonsuz döngü!
#     print("Bu sonsuza kadar devam eder")

# Kontrollü sonsuz döngü (break ile çıkış)
while True:
    komut = input("Komut girin (çıkış için 'q'): ")
    
    if komut == 'q':
        print("Programdan çıkılıyor...")
        break
    
    print(f"Girilen komut: {komut}")

# Menü sistemi örneği
while True:
    print("\n=== MENÜ ===")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "3":
        print("Hoşçakalın!")
        break
    elif secim == "1":
        a = int(input("Birinci sayı: "))
        b = int(input("İkinci sayı: "))
        print(f"Sonuç: {a + b}")
    elif secim == "2":
        a = int(input("Birinci sayı: "))
        b = int(input("İkinci sayı: "))
        print(f"Sonuç: {a - b}")
    else:
        print("Geçersiz seçim!")
```

## 3.2 For Döngüsü

For döngüsü, bir dizi veya aralık üzerinde iterasyon yapar.

### range() Fonksiyonu

```python
# range(stop) - 0'dan stop'a kadar
for i in range(5):
    print(i, end=" ")
# Çıktı: 0 1 2 3 4

print()

# range(start, stop) - start'tan stop'a kadar
for i in range(1, 6):
    print(i, end=" ")
# Çıktı: 1 2 3 4 5

print()

# range(start, stop, step) - artış miktarı
for i in range(0, 10, 2):
    print(i, end=" ")
# Çıktı: 0 2 4 6 8

print()

# Geriye doğru sayma
for i in range(10, 0, -1):
    print(i, end=" ")
# Çıktı: 10 9 8 7 6 5 4 3 2 1

print()

# Negatif sayılarla
for i in range(-5, 5):
    print(i, end=" ")
# Çıktı: -5 -4 -3 -2 -1 0 1 2 3 4
```

### For ile Temel Örnekler

```python
# 1'den 10'a kadar olan sayıların toplamı
toplam = 0
for i in range(1, 11):
    toplam += i
print(f"Toplam: {toplam}")  # 55

# Çarpım tablosu
sayi = 5
for i in range(1, 11):
    print(f"{sayi} x {i} = {sayi * i}")

# Faktöriyel hesaplama (5!)
n = 5
faktoriyel = 1

for i in range(1, n + 1):
    faktoriyel *= i

print(f"{n}! = {faktoriyel}")  # 120
```

### String Üzerinde Döngü

```python
# Her karakteri yazdırma
kelime = "Python"

for harf in kelime:
    print(harf)

# İndeks ile birlikte
for i in range(len(kelime)):
    print(f"İndeks {i}: {kelime[i]}")

# enumerate() ile daha şık
for indeks, harf in enumerate(kelime):
    print(f"İndeks {indeks}: {harf}")

# Çıktı:
# İndeks 0: P
# İndeks 1: y
# İndeks 2: t
# İndeks 3: h
# İndeks 4: o
# İndeks 5: n
```

### Liste Üzerinde Döngü

```python
# Liste elemanlarını yazdırma
meyveler = ["elma", "armut", "muz", "kiraz"]

for meyve in meyveler:
    print(meyve)

# İndeks ile birlikte
for i in range(len(meyveler)):
    print(f"{i+1}. {meyveler[i]}")

# enumerate ile (daha Pythonic)
for indeks, meyve in enumerate(meyveler, start=1):
    print(f"{indeks}. {meyve}")

# Çıktı:
# 1. elma
# 2. armut
# 3. muz
# 4. kiraz
```

## 3.3 Break, Continue ve Pass Komutları

### break - Döngüden Çıkış

```python
# Belirli bir değer bulunca dur
for i in range(1, 11):
    if i == 5:
        print("5 bulundu, döngü durduruluyor!")
        break
    print(i)

# Çıktı: 1 2 3 4 5 bulundu, döngü durduruluyor!

# Kullanıcı 'q' girene kadar devam et
while True:
    kelime = input("Bir kelime girin ('q' çıkış): ")
    if kelime == 'q':
        break
    print(f"Girilen kelime: {kelime}")

# Sayı tahmini oyunu
gizli_sayi = 42
tahmin_hakki = 5

for deneme in range(1, tahmin_hakki + 1):
    tahmin = int(input(f"Tahmin {deneme}: "))
    
    if tahmin == gizli_sayi:
        print("Tebrikler! Doğru tahmin!")
        break
    elif tahmin < gizli_sayi:
        print("Daha büyük bir sayı deneyin")
    else:
        print("Daha küçük bir sayı deneyin")
else:
    print(f"Hakkınız bitti. Gizli sayı: {gizli_sayi}")
```

### continue - Döngünün Geri Kalanını Atla

```python
# Çift sayıları atla
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Çift sayıyı atla
    print(i)  # Sadece tek sayıları yazdır

# Çıktı: 1 3 5 7 9

# Negatif sayıları atla
sayilar = [10, -5, 8, -2, 15, -7, 20]

toplam = 0
for sayi in sayilar:
    if sayi < 0:
        continue  # Negatif sayıyı toplamaya ekleme
    toplam += sayi

print(f"Pozitif sayıların toplamı: {toplam}")  # 53

# Boşlukları göz ardı et
metin = "P y t h o n"

sonuc = ""
for karakter in metin:
    if karakter == " ":
        continue
    sonuc += karakter

print(sonuc)  # "Python"
```

### pass - Hiçbir Şey Yapma

```python
# Placeholder (yer tutucu) olarak kullanılır
for i in range(5):
    if i == 3:
        pass  # Şimdilik boş, sonra eklenecek
    else:
        print(i)

# Fonksiyon tasarımında
def gelecekte_yazilacak_fonksiyon():
    pass  # TODO: Bu fonksiyon ileride yazılacak

# Class tasarımında
class GelistirilecekSinif:
    pass  # Şimdilik boş sınıf

# pass vs continue farkı
print("pass ile:")
for i in range(5):
    if i == 2:
        pass  # Hiçbir şey yapma, devam et
    print(i)

print("\ncontinue ile:")
for i in range(5):
    if i == 2:
        continue  # Bu iterasyonu atla
    print(i)
```

## 3.4 İç İçe Döngüler (Nested Loops)

### Basit İç İçe Döngü

```python
# Çarpım tablosu
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j:2}", end="  ")
    print()  # Satır sonu

# Çıktı:
# 1 x 1 =  1  1 x 2 =  2  1 x 3 =  3  1 x 4 =  4  1 x 5 =  5  
# 2 x 1 =  2  2 x 2 =  4  2 x 3 =  6  2 x 4 =  8  2 x 5 = 10  
# 3 x 1 =  3  3 x 2 =  6  3 x 3 =  9  3 x 4 = 12  3 x 5 = 15  
# 4 x 1 =  4  4 x 2 =  8  4 x 3 = 12  4 x 4 = 16  4 x 5 = 20  
# 5 x 1 =  5  5 x 2 = 10  5 x 3 = 15  5 x 4 = 20  5 x 5 = 25
```

### Yıldız Desenleri

```python
# Desen 1: Sağ üçgen
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Çıktı:
# *
# **
# ***
# ****
# *****

# Desen 2: Ters üçgen
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Çıktı:
# *****
# ****
# ***
# **
# *

# Desen 3: Piramit
n = 5
for i in range(1, n + 1):
    # Boşluklar
    for j in range(n - i):
        print(" ", end="")
    # Yıldızlar
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Çıktı:
#     *
#    ***
#   *****
#  *******
# *********

# Desen 4: Kare
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Çıktı:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
```

### Sayı Piramitleri

```python
# Sayı piramidi 1
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Çıktı:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# Sayı piramidi 2
n = 5
sayi = 1
for i in range(1, n + 1):
    for j in range(i):
        print(sayi, end=" ")
        sayi += 1
    print()

# Çıktı:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

# Floyd üçgeni
n = 5
sayi = 1
for i in range(1, n + 1):
    for j in range(i):
        print(f"{sayi:3}", end=" ")
        sayi += 1
    print()

# Çıktı:
#   1 
#   2   3 
#   4   5   6 
#   7   8   9  10 
#  11  12  13  14  15
```

### İç İçe While Döngüleri

```python
# İç içe while
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}", end="  ")
        j += 1
    print()
    i += 1

# Çıktı:
# i=1, j=1  i=1, j=2  i=1, j=3  
# i=2, j=1  i=2, j=2  i=2, j=3  
# i=3, j=1  i=3, j=2  i=3, j=3

# Asal sayı kontrolü (nested while)
sayi = int(input("Bir sayı girin: "))
i = 2
asal = True

while i < sayi:
    if sayi % i == 0:
        asal = False
        break
    i += 1

if sayi < 2:
    print(f"{sayi} asal değil")
elif asal:
    print(f"{sayi} asal sayıdır")
else:
    print(f"{sayi} asal değildir")
```

## 3.5 Döngü Alıştırmaları

### Alıştırma 1: Faktöriyel

```python
# Faktöriyel hesaplama (n!)
n = int(input("Sayı girin: "))
faktoriyel = 1

for i in range(1, n + 1):
    faktoriyel *= i

print(f"{n}! = {faktoriyel}")

# Örnek: 5! = 1 * 2 * 3 * 4 * 5 = 120
```

### Alıştırma 2: Asal Sayı Kontrolü

```python
# Asal sayı kontrolü
sayi = int(input("Bir sayı girin: "))

if sayi < 2:
    print(f"{sayi} asal değil")
else:
    asal = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break
    
    if asal:
        print(f"{sayi} asal sayıdır")
    else:
        print(f"{sayi} asal değildir")
```

### Alıştırma 3: Fibonacci Serisi

```python
# Fibonacci serisi (ilk n terim)
n = int(input("Kaç terim? "))

a, b = 0, 1

print("Fibonacci serisi:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Örnek: n=10
# Çıktı: 0 1 1 2 3 5 8 13 21 34
```

### Alıştırma 4: Sayının Basamaklarını Toplama

```python
# Sayının basamakları toplamı
sayi = int(input("Bir sayı girin: "))
toplam = 0
temp = sayi

while temp > 0:
    basamak = temp % 10
    toplam += basamak
    temp //= 10

print(f"{sayi} sayısının basamakları toplamı: {toplam}")

# Örnek: 12345 -> 1+2+3+4+5 = 15
```

### Alıştırma 5: Mükemmel Sayı

```python
# Mükemmel sayı kontrolü
# Mükemmel sayı: Kendisi hariç pozitif bölenlerinin toplamı kendisine eşit olan sayı
# Örnek: 6 = 1 + 2 + 3

sayi = int(input("Bir sayı girin: "))
toplam = 0

for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i

if toplam == sayi:
    print(f"{sayi} mükemmel sayıdır")
else:
    print(f"{sayi} mükemmel sayı değildir")
```

## 3.6 Algoritma Problemleri - Modül 3

### Problem 1: 1'den N'e Kadar Çift Sayılar

**Soru:** Kullanıcıdan bir sayı alın ve 1'den bu sayıya kadar olan çift sayıları yazdırın.

```python
# Çözüm
n = int(input("N değeri: "))

print(f"1'den {n}'e kadar çift sayılar:")
for i in range(2, n + 1, 2):
    print(i, end=" ")
```

### Problem 2: Rakamları Toplama

**Soru:** Kullanıcıdan bir sayı alın ve bu sayının rakamlarının toplamını bulun.

```python
# Çözüm
sayi = int(input("Bir sayı girin: "))
toplam = 0

while sayi > 0:
    rakam = sayi % 10
    toplam += rakam
    sayi //= 10

print(f"Rakamlar toplamı: {toplam}")

# Alternatif (string kullanarak)
sayi_str = input("Bir sayı girin: ")
toplam = sum(int(rakam) for rakam in sayi_str)
print(f"Rakamlar toplamı: {toplam}")
```

### Problem 3: Tersine Çevirme

**Soru:** Kullanıcıdan bir sayı alın ve bu sayıyı tersine çevirin.

```python
# Çözüm
sayi = int(input("Bir sayı girin: "))
ters = 0

while sayi > 0:
    rakam = sayi % 10
    ters = ters * 10 + rakam
    sayi //= 10

print(f"Ters: {ters}")

# Alternatif (string kullanarak)
sayi_str = input("Bir sayı girin: ")
ters = sayi_str[::-1]
print(f"Ters: {ters}")
```

### Problem 4: Armstrong Sayısı

**Soru:** Bir sayının Armstrong sayısı olup olmadığını kontrol edin.
Armstrong sayısı: Rakamlarının küplerinin toplamı kendisine eşit olan sayı.
Örnek: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

```python
# Çözüm
sayi = int(input("Bir sayı girin: "))
temp = sayi
toplam = 0
basamak_sayisi = len(str(sayi))

while temp > 0:
    rakam = temp % 10
    toplam += rakam ** basamak_sayisi
    temp //= 10

if toplam == sayi:
    print(f"{sayi} bir Armstrong sayısıdır")
else:
    print(f"{sayi} bir Armstrong sayısı değildir")
```

### Problem 5: EBOB (En Büyük Ortak Bölen)

**Soru:** İki sayının EBOB'unu Öklid algoritması ile bulun.

```python
# Çözüm - Öklid Algoritması
a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

# Orijinal değerleri sakla
orijinal_a = a
orijinal_b = b

while b != 0:
    temp = b
    b = a % b
    a = temp

print(f"{orijinal_a} ve {orijinal_b}'nin EBOB'u: {a}")

# Alternatif (recursive kullanmadan)
import math
ebob = math.gcd(orijinal_a, orijinal_b)
print(f"EBOB (math.gcd ile): {ebob}")
```

### Problem 6: Asal Sayı Listesi

**Soru:** 1'den N'e kadar olan asal sayıları listeleyin.

```python
# Çözüm
n = int(input("N değeri: "))

print(f"1'den {n}'e kadar asal sayılar:")

for sayi in range(2, n + 1):
    asal = True
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            asal = False
            break
    
    if asal:
        print(sayi, end=" ")
```

### Problem 7: Baklava Dilimi

**Soru:** Aşağıdaki gibi baklava dilimi çizin:
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

```python
# Çözüm
n = 5

# Üst kısım
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Alt kısım
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

### Problem 8: Sayı Tahmin Oyunu

**Soru:** 1-100 arası rastgele sayı tut. Kullanıcı 7 denemede tahmin etsin. İpucu ver.

```python
# Çözüm
import random

gizli_sayi = random.randint(1, 100)
tahmin_hakki = 7
deneme = 0

print("1-100 arası bir sayı tuttum!")
print(f"Toplam {tahmin_hakki} deneme hakkınız var.")

while deneme < tahmin_hakki:
    deneme += 1
    tahmin = int(input(f"\nTahmin {deneme}: "))
    
    if tahmin == gizli_sayi:
        print(f"Tebrikler! {deneme} denemede bildiniz!")
        break
    elif tahmin < gizli_sayi:
        print("Daha büyük bir sayı deneyin!")
    else:
        print("Daha küçük bir sayı deneyin!")
    
    if deneme == tahmin_hakki:
        print(f"\nHakkınız bitti! Gizli sayı: {gizli_sayi}")
```

### Problem 9: Çarpım Tablosu Matrisi

**Soru:** NxN boyutunda çarpım tablosu matrisi oluşturun.

```python
# Çözüm
n = int(input("Tablo boyutu (N): "))

print(f"\n{n}x{n} Çarpım Tablosu:")

# Başlık satırı
print("   ", end="")
for i in range(1, n + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * (4 * n + 4))

# Tablo
for i in range(1, n + 1):
    print(f"{i:2} |", end="")
    for j in range(1, n + 1):
        print(f"{i*j:4}", end="")
    print()
```

### Problem 10: Palindrom Sayı

**Soru:** Bir sayının palindrom olup olmadığını kontrol edin.
(Palindrom: Tersten okunuşu aynı olan sayı. Örnek: 121, 12321)

```python
# Çözüm
sayi = input("Bir sayı girin: ")

# Tersi oluştur
ters = sayi[::-1]

if sayi == ters:
    print(f"{sayi} bir palindrom sayıdır")
else:
    print(f"{sayi} palindrom sayı değildir")

# Alternatif (sayısal olarak)
sayi_int = int(sayi)
orijinal = sayi_int
ters_sayi = 0

while sayi_int > 0:
    rakam = sayi_int % 10
    ters_sayi = ters_sayi * 10 + rakam
    sayi_int //= 10

if orijinal == ters_sayi:
    print(f"{orijinal} bir palindrom sayıdır")
else:
    print(f"{orijinal} palindrom sayı değildir")
```

## 3.7 İleri Seviye Döngü Teknikleri

### enumerate() Kullanımı

```python
# Liste elemanlarını indeks ile birlikte alma
meyveler = ["elma", "armut", "muz", "kiraz"]

for indeks, meyve in enumerate(meyveler):
    print(f"{indeks}: {meyve}")

# Başlangıç indeksi belirtme
for indeks, meyve in enumerate(meyveler, start=1):
    print(f"{indeks}. {meyve}")
```

### zip() Kullanımı

```python
# İki listeyi eşzamanlı gezme
isimler = ["Ali", "Ayşe", "Mehmet"]
yaslar = [25, 30, 28]

for isim, yas in zip(isimler, yaslar):
    print(f"{isim}: {yas} yaşında")

# Üç liste birden
notlar = [85, 90, 78]

for isim, yas, not_ort in zip(isimler, yaslar, notlar):
    print(f"{isim} ({yas}): {not_ort}")
```

### List Comprehension ile Döngü

```python
# Klasik yöntem
kareler = []
for i in range(1, 11):
    kareler.append(i ** 2)
print(kareler)

# List comprehension ile (tek satır)
kareler = [i ** 2 for i in range(1, 11)]
print(kareler)

# Koşullu list comprehension
# Sadece çift sayıların kareleri
cift_kareler = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(cift_kareler)  # [4, 16, 36, 64, 100]
```

## 3.8 Ödev Önerileri - Modül 3

1. **Prime Number Range**: İki sayı arasındaki tüm asal sayıları bulan program
2. **Pattern Generator**: Kullanıcının seçtiği deseni çizen program
3. **Number Guess Game**: İleri seviye (min-max ipucu, puan sistemi ile)
4. **Multiplication Quiz**: Rastgele çarpma soruları soran quiz programı
5. **Interest Calculator**: Bileşik faiz hesaplayan program (yıl yıl göster)

---

# MODÜL 4: Veri Yapıları - Listeler ve Tuple'lar

**Süre:** 1 Oturum - 5 Saat (Hafta 4)

## 4.1 Liste (List) Nedir?

Liste, Python'da birden fazla öğeyi tek bir değişkende saklamak için kullanılan bir veri yapısıdır. Listeler:
- **Değiştirilebilir (Mutable)**: Elemanlar eklenebilir, silinebilir, değiştirilebilir
- **Sıralı (Ordered)**: Elemanların belirli bir sırası vardır
- **İndekslenebilir**: Her elemanın bir indeksi vardır
- **Farklı Tipleri Barındırabilir**: Aynı listede farklı veri tipleri olabilir

```python
# Boş liste oluşturma
bos_liste = []
bos_liste2 = list()

# Elemanlarla liste oluşturma
sayilar = [1, 2, 3, 4, 5]
meyveler = ["elma", "armut", "muz"]
karisik = [1, "iki", 3.0, True, [5, 6]]  # Farklı tipler

# Liste uzunluğu
print(len(sayilar))  # 5
print(len(meyveler))  # 3

# Liste yazdırma
print(sayilar)       # [1, 2, 3, 4, 5]
print(meyveler)      # ['elma', 'armut', 'muz']
```

## 4.2 Liste İndeksleme ve Slicing

### İndeksleme (Indexing)

```python
meyveler = ["elma", "armut", "muz", "kiraz", "üzüm"]

# Pozitif indeksleme (0'dan başlar)
print(meyveler[0])   # elma
print(meyveler[1])   # armut
print(meyveler[4])   # üzüm

# Negatif indeksleme (sondan başlar)
print(meyveler[-1])  # üzüm
print(meyveler[-2])  # kiraz
print(meyveler[-5])  # elma

# Hata: İndeks aralık dışı
# print(meyveler[10])  # IndexError
```

### Dilimleme (Slicing)

```python
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# liste[başlangıç:bitiş] - bitiş dahil değil
print(sayilar[2:5])    # [2, 3, 4]
print(sayilar[0:3])    # [0, 1, 2]

# Başlangıç veya bitiş belirtmeme
print(sayilar[:4])     # [0, 1, 2, 3]
print(sayilar[6:])     # [6, 7, 8, 9]
print(sayilar[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (tüm liste)

# liste[başlangıç:bitiş:adım]
print(sayilar[::2])    # [0, 2, 4, 6, 8] (2'şer atlayarak)
print(sayilar[1::2])   # [1, 3, 5, 7, 9] (tek indeksliler)

# Negatif adım (tersten)
print(sayilar[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sayilar[8:2:-1]) # [8, 7, 6, 5, 4, 3]

# Pratik örnekler
kelime = list("Python")
print(kelime)          # ['P', 'y', 't', 'h', 'o', 'n']
print(kelime[1:4])     # ['y', 't', 'h']
print(kelime[::-1])    # ['n', 'o', 'h', 't', 'y', 'P']
```

## 4.3 Liste Methodları

### append() - Sona Eleman Ekleme

```python
meyveler = ["elma", "armut"]
print(meyveler)        # ['elma', 'armut']

meyveler.append("muz")
print(meyveler)        # ['elma', 'armut', 'muz']

# Birden fazla eleman eklemek için döngü
for meyve in ["kiraz", "üzüm"]:
    meyveler.append(meyve)

print(meyveler)        # ['elma', 'armut', 'muz', 'kiraz', 'üzüm']

# Sayı listesi
sayilar = []
for i in range(1, 6):
    sayilar.append(i)

print(sayilar)         # [1, 2, 3, 4, 5]
```

### extend() - Liste Birleştirme

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste1.extend(liste2)
print(liste1)          # [1, 2, 3, 4, 5, 6]

# append vs extend farkı
liste_a = [1, 2, 3]
liste_b = [4, 5]

liste_a.append(liste_b)
print(liste_a)         # [1, 2, 3, [4, 5]] (liste içinde liste)

liste_c = [1, 2, 3]
liste_c.extend(liste_b)
print(liste_c)         # [1, 2, 3, 4, 5] (elemanlar eklenir)

# String ile extend
harfler = ['a', 'b']
harfler.extend("cd")
print(harfler)         # ['a', 'b', 'c', 'd']
```

### insert() - Belirli Konuma Ekleme

```python
meyveler = ["elma", "muz", "üzüm"]

# insert(indeks, eleman)
meyveler.insert(1, "armut")  # 1. indekse ekle
print(meyveler)              # ['elma', 'armut', 'muz', 'üzüm']

meyveler.insert(0, "kiraz")  # Başa ekle
print(meyveler)              # ['kiraz', 'elma', 'armut', 'muz', 'üzüm']

meyveler.insert(100, "çilek")  # Büyük indeks -> sona ekler
print(meyveler)                # ['kiraz', 'elma', 'armut', 'muz', 'üzüm', 'çilek']
```

### remove() - Değere Göre Silme

```python
meyveler = ["elma", "armut", "muz", "elma"]

meyveler.remove("armut")
print(meyveler)        # ['elma', 'muz', 'elma']

# İlk bulunan elemanı siler
meyveler.remove("elma")
print(meyveler)        # ['muz', 'elma']

# Olmayan eleman hatası verir
# meyveler.remove("kiraz")  # ValueError

# Güvenli silme
meyve_sil = "kiraz"
if meyve_sil in meyveler:
    meyveler.remove(meyve_sil)
else:
    print(f"{meyve_sil} listede yok")
```

### pop() - İndekse Göre Silme ve Döndürme

```python
sayilar = [10, 20, 30, 40, 50]

# Son elemanı sil ve döndür
son = sayilar.pop()
print(son)             # 50
print(sayilar)         # [10, 20, 30, 40]

# Belirli indeksi sil
ikinci = sayilar.pop(1)
print(ikinci)          # 20
print(sayilar)         # [10, 30, 40]

# İlk elemanı sil
ilk = sayilar.pop(0)
print(ilk)             # 10
print(sayilar)         # [30, 40]

# Stack (yığın) yapısı örneği
stack = []
stack.append(1)        # Push
stack.append(2)
stack.append(3)
print(stack)           # [1, 2, 3]

print(stack.pop())     # 3 (Pop)
print(stack.pop())     # 2
print(stack)           # [1]
```

### clear() - Tüm Elemanları Silme

```python
liste = [1, 2, 3, 4, 5]
print(liste)           # [1, 2, 3, 4, 5]

liste.clear()
print(liste)           # []
print(len(liste))      # 0
```

### index() - Eleman İndeksini Bulma

```python
meyveler = ["elma", "armut", "muz", "elma", "kiraz"]

# İlk bulunan indeksi döner
print(meyveler.index("muz"))     # 2
print(meyveler.index("elma"))    # 0 (ilk elma)

# Olmayan eleman hatası verir
# print(meyveler.index("üzüm"))  # ValueError

# Belirli aralıkta arama
# index(değer, başlangıç, bitiş)
print(meyveler.index("elma", 1))  # 3 (1. indeksten sonra ara)

# Güvenli arama
aranan = "üzüm"
if aranan in meyveler:
    print(f"{aranan} bulundu: {meyveler.index(aranan)}")
else:
    print(f"{aranan} listede yok")
```

### count() - Eleman Sayısı

```python
sayilar = [1, 2, 3, 2, 4, 2, 5, 2]

print(sayilar.count(2))    # 4 (2 sayısı 4 kez var)
print(sayilar.count(5))    # 1
print(sayilar.count(10))   # 0 (yok)

# Pratik kullanım
metin = "merhaba dünya"
harfler = list(metin)
print(harfler.count('a'))  # 3
```

### sort() - Sıralama

```python
# Artan sıralama
sayilar = [3, 1, 4, 1, 5, 9, 2, 6]
sayilar.sort()
print(sayilar)         # [1, 1, 2, 3, 4, 5, 6, 9]

# Azalan sıralama
sayilar.sort(reverse=True)
print(sayilar)         # [9, 6, 5, 4, 3, 2, 1, 1]

# String sıralama (alfabetik)
isimler = ["Zeynep", "Ali", "Mehmet", "Ayşe"]
isimler.sort()
print(isimler)         # ['Ali', 'Ayşe', 'Mehmet', 'Zeynep']

# Büyük-küçük harf duyarsız sıralama
isimler = ["zeynep", "Ali", "mehmet"]
isimler.sort(key=str.lower)
print(isimler)         # ['Ali', 'mehmet', 'zeynep']

# sorted() - Orijinali değiştirmez, yeni liste döner
orijinal = [3, 1, 4, 1, 5]
sirali = sorted(orijinal)
print(orijinal)        # [3, 1, 4, 1, 5] (değişmedi)
print(sirali)          # [1, 1, 3, 4, 5] (yeni liste)
```

### reverse() - Listeyi Ters Çevirme

```python
sayilar = [1, 2, 3, 4, 5]
sayilar.reverse()
print(sayilar)         # [5, 4, 3, 2, 1]

# Slicing ile alternatif
sayilar2 = [1, 2, 3, 4, 5]
ters = sayilar2[::-1]
print(ters)            # [5, 4, 3, 2, 1]
print(sayilar2)        # [1, 2, 3, 4, 5] (orijinal değişmedi)
```

### copy() - Liste Kopyalama

```python
# Shallow copy (sığ kopya)
orijinal = [1, 2, 3]
kopya = orijinal.copy()

kopya.append(4)
print(orijinal)        # [1, 2, 3] (değişmedi)
print(kopya)           # [1, 2, 3, 4]

# Atama ile kopya OLMAZ!
liste1 = [1, 2, 3]
liste2 = liste1        # Referans kopyası (aynı liste)

liste2.append(4)
print(liste1)          # [1, 2, 3, 4] (değişti!)
print(liste2)          # [1, 2, 3, 4]

# Diğer kopyalama yöntemleri
liste_a = [1, 2, 3]
liste_b = liste_a[:]   # Slicing ile
liste_c = list(liste_a)  # list() ile

# İç içe listelerle dikkat!
ic_ice = [[1, 2], [3, 4]]
kopya_sıg = ic_ice.copy()

kopya_sıg[0][0] = 999
print(ic_ice)          # [[999, 2], [3, 4]] (değişti!)

# Deep copy (derin kopya) gerekir
import copy
derin_kopya = copy.deepcopy(ic_ice)
```

## 4.4 Liste Operatörleri

```python
# + (Birleştirme)
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
birlesik = liste1 + liste2
print(birlesik)        # [1, 2, 3, 4, 5, 6]

# * (Çoğaltma)
tekrar = [1, 2] * 3
print(tekrar)          # [1, 2, 1, 2, 1, 2]

# in (Üyelik kontrolü)
meyveler = ["elma", "armut", "muz"]
print("elma" in meyveler)      # True
print("kiraz" in meyveler)     # False

# not in
print("kiraz" not in meyveler) # True

# Karşılaştırma
print([1, 2] == [1, 2])        # True
print([1, 2] != [2, 1])        # True
print([1, 2] < [1, 3])         # True (leksikografik)
```

## 4.5 List Comprehension

List comprehension, liste oluşturmanın kısa ve okunabilir bir yoludur.

```python
# Klasik yöntem
kareler = []
for i in range(1, 6):
    kareler.append(i ** 2)
print(kareler)         # [1, 4, 9, 16, 25]

# List comprehension ile
kareler = [i ** 2 for i in range(1, 6)]
print(kareler)         # [1, 4, 9, 16, 25]

# Koşullu list comprehension
# Sadece çift sayılar
ciftler = [i for i in range(1, 11) if i % 2 == 0]
print(ciftler)         # [2, 4, 6, 8, 10]

# Çift sayıların kareleri
cift_kareler = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(cift_kareler)    # [4, 16, 36, 64, 100]

# If-else ile
# Çift ise karesi, tek ise kendisi
sonuc = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
print(sonuc)           # [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]

# String işlemleri
kelime = "Python"
buyuk_harfler = [harf.upper() for harf in kelime]
print(buyuk_harfler)   # ['P', 'Y', 'T', 'H', 'O', 'N']

# İç içe list comprehension
matris = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matris)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Dosyadan satırları okuma (örnek)
# satirlar = [satir.strip() for satir in open('dosya.txt')]

# Birden fazla liste ile
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
carpimlar = [x * y for x in liste1 for y in liste2]
print(carpimlar)       # [4, 5, 6, 8, 10, 12, 12, 15, 18]
```

## 4.6 İç İçe Listeler (Nested Lists)

```python
# 2 boyutlu liste (matris)
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Elemanlara erişim
print(matris[0])       # [1, 2, 3]
print(matris[0][0])    # 1
print(matris[1][2])    # 6
print(matris[2][1])    # 8

# Döngü ile gezme
for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
    print()

# Matris toplamı
toplam = 0
for satir in matris:
    for eleman in satir:
        toplam += eleman
print(f"Toplam: {toplam}")  # 45

# List comprehension ile matris oluşturma
# 3x3 sıfır matrisi
sifir_matris = [[0 for j in range(3)] for i in range(3)]
print(sifir_matris)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Öğrenci notları tablosu
ogrenciler = [
    ["Ali", 85, 90, 78],
    ["Ayşe", 92, 88, 95],
    ["Mehmet", 78, 85, 82]
]

# Her öğrencinin ortalamasını hesaplama
for ogrenci in ogrenciler:
    isim = ogrenci[0]
    notlar = ogrenci[1:]
    ortalama = sum(notlar) / len(notlar)
    print(f"{isim}: {ortalama:.2f}")
```

## 4.7 Tuple (Demet) Nedir?

Tuple, liste gibi bir veri yapısıdır ancak **değiştirilemez (immutable)**'dir.

### Tuple Özellikleri

```python
# Tuple oluşturma
bos_tuple = ()
tek_elemanli = (1,)    # Virgül önemli!
sayilar = (1, 2, 3, 4, 5)
karisik = (1, "iki", 3.0, True)

# Parantez olmadan da olur
koordinat = 10, 20, 30
print(type(koordinat))  # <class 'tuple'>

# Liste vs Tuple farkı
liste = [1, 2, 3]
liste[0] = 999         # Değiştirilebilir
print(liste)           # [999, 2, 3]

tuple_ornek = (1, 2, 3)
# tuple_ornek[0] = 999  # TypeError! Değiştirilemez

# Tuple unpacking
koordinat = (10, 20)
x, y = koordinat
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# Çoklu değer dönüşü için tuple kullanımı
def min_max(liste):
    return min(liste), max(liste)

kucuk, buyuk = min_max([3, 1, 4, 1, 5])
print(f"Min: {kucuk}, Max: {buyuk}")  # Min: 1, Max: 5
```

### Tuple İndeksleme ve Slicing

```python
renkler = ("kırmızı", "yeşil", "mavi", "sarı", "turuncu")

# İndeksleme (liste gibi)
print(renkler[0])      # kırmızı
print(renkler[-1])     # turuncu

# Slicing
print(renkler[1:4])    # ('yeşil', 'mavi', 'sarı')
print(renkler[::2])    # ('kırmızı', 'mavi', 'turuncu')
print(renkler[::-1])   # Ters sıra
```

### Tuple Methodları

```python
sayilar = (1, 2, 3, 2, 4, 2, 5)

# count() - Eleman sayısı
print(sayilar.count(2))    # 3

# index() - İlk bulunan indeks
print(sayilar.index(4))    # 4

# Tuple methodları çok azdır (immutable olduğu için)

# Diğer işlemler
print(len(sayilar))        # 7
print(max(sayilar))        # 5
print(min(sayilar))        # 1
print(sum(sayilar))        # 19
```

### Tuple vs List - Ne Zaman Hangisi?

```python
# TUPLE kullan:
# - Değişmeyecek verilerde (koordinat, RGB değerleri)
# - Fonksiyondan çoklu değer döndürmede
# - Sözlük anahtarı olarak (liste kullanılamaz)
# - Daha hızlı ve az bellek kullanır

koordinatlar = (40.7128, -74.0060)  # NY koordinatları
rgb_renk = (255, 0, 0)  # Kırmızı

# Sözlük anahtarı olarak tuple
lokasyonlar = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

# LIST kullan:
# - Değişken boyutlu koleksiyon gerektiğinde
# - Eleman ekleme/çıkarma yapılacaksa
# - Sıralama yapılacaksa

alisveris_listesi = ["süt", "ekmek", "yumurta"]
alisveris_listesi.append("peynir")  # Değiştirilebilir

# Liste'den Tuple'a ve tersi
liste = [1, 2, 3]
tuple_yap = tuple(liste)
print(tuple_yap)       # (1, 2, 3)

tuple_ornek = (4, 5, 6)
liste_yap = list(tuple_ornek)
print(liste_yap)       # [4, 5, 6]
```

## 4.8 Pratik Projeler

### Proje 1: Öğrenci Not Sistemi

```python
"""
ÖĞRENCİ NOT YÖNETİM SİSTEMİ
Öğrenci ekleme, not girme, ortalama hesaplama, listeleme
"""

ogrenciler = []

def ogrenci_ekle():
    isim = input("Öğrenci adı: ")
    yas = int(input("Yaş: "))
    sinif = input("Sınıf: ")
    
    ogrenci = {
        "isim": isim,
        "yas": yas,
        "sinif": sinif,
        "notlar": []
    }
    
    ogrenciler.append(ogrenci)
    print(f"{isim} eklendi!")

def not_ekle():
    isim = input("Öğrenci adı: ")
    
    for ogrenci in ogrenciler:
        if ogrenci["isim"] == isim:
            ders = input("Ders adı: ")
            not_degeri = float(input("Not: "))
            ogrenci["notlar"].append({"ders": ders, "not": not_degeri})
            print("Not eklendi!")
            return
    
    print("Öğrenci bulunamadı!")

def ortalama_hesapla():
    isim = input("Öğrenci adı: ")
    
    for ogrenci in ogrenciler:
        if ogrenci["isim"] == isim:
            if not ogrenci["notlar"]:
                print("Henüz not girilmemiş!")
                return
            
            toplam = sum(not_bilgisi["not"] for not_bilgisi in ogrenci["notlar"])
            ortalama = toplam / len(ogrenci["notlar"])
            
            print(f"\n{isim} - Not Ortalaması: {ortalama:.2f}")
            return
    
    print("Öğrenci bulunamadı!")

def ogrenci_listele():
    if not ogrenciler:
        print("Henüz öğrenci eklenmemiş!")
        return
    
    print("\n=== ÖĞRENCİ LİSTESİ ===")
    for i, ogrenci in enumerate(ogrenciler, 1):
        print(f"{i}. {ogrenci['isim']} - Sınıf: {ogrenci['sinif']}")
        if ogrenci["notlar"]:
            for not_bilgisi in ogrenci["notlar"]:
                print(f"   {not_bilgisi['ders']}: {not_bilgisi['not']}")
        else:
            print("   (Not girilmemiş)")

# Ana program
while True:
    print("\n=== ÖĞRENCİ NOT SİSTEMİ ===")
    print("1. Öğrenci Ekle")
    print("2. Not Ekle")
    print("3. Ortalama Hesapla")
    print("4. Öğrenci Listele")
    print("5. Çıkış")
    
    secim = input("\nSeçim: ")
    
    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        not_ekle()
    elif secim == "3":
        ortalama_hesapla()
    elif secim == "4":
        ogrenci_listele()
    elif secim == "5":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")
```

## 4.9 Algoritma Problemleri - Modül 4

### Problem 1: İki Listenin Kesişimi

**Soru:** İki liste verildiğinde, her iki listede de bulunan elemanları bulun.

```python
# Çözüm
liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]

kesisim = []
for eleman in liste1:
    if eleman in liste2 and eleman not in kesisim:
        kesisim.append(eleman)

print(f"Kesişim: {kesisim}")  # [4, 5]

# Alternatif (set kullanarak - daha hızlı)
kesisim = list(set(liste1) & set(liste2))
print(f"Kesişim: {kesisim}")
```

### Problem 2: Listeyi Tekrarsız Yapma

**Soru:** Bir listeden tekrar eden elemanları kaldırın.

```python
# Çözüm
sayilar = [1, 2, 2, 3, 4, 4, 4, 5]

# Yöntem 1: Manuel
tekrarsiz = []
for sayi in sayilar:
    if sayi not in tekrarsiz:
        tekrarsiz.append(sayi)

print(tekrarsiz)  # [1, 2, 3, 4, 5]

# Yöntem 2: set kullanarak (sıra korunmaz)
tekrarsiz = list(set(sayilar))
print(tekrarsiz)

# Yöntem 3: dict.fromkeys() (sıra korunur, Python 3.7+)
tekrarsiz = list(dict.fromkeys(sayilar))
print(tekrarsiz)  # [1, 2, 3, 4, 5]
```

### Problem 3: Liste Ortalaması ve Varyans

**Soru:** Bir sayı listesinin ortalamasını ve varyansını hesaplayın.

```python
# Çözüm
sayilar = [10, 20, 30, 40, 50]

# Ortalama
ortalama = sum(sayilar) / len(sayilar)
print(f"Ortalama: {ortalama}")

# Varyans: Her elemanın ortalamadan farkının karelerinin ortalaması
farklar_karesi = [(x - ortalama) ** 2 for x in sayilar]
varyans = sum(farklar_karesi) / len(sayilar)

print(f"Varyans: {varyans}")

# Standart sapma
standart_sapma = varyans ** 0.5
print(f"Standart sapma: {standart_sapma}")
```

### Problem 4: Liste Rotasyonu

**Soru:** Listeyi sağa veya sola k pozisyon kaydırın.

```python
# Çözüm
def rotate_right(liste, k):
    """Listeyi sağa k pozisyon kaydır"""
    if not liste:
        return liste
    
    k = k % len(liste)  # Gereksiz tam tur önleme
    return liste[-k:] + liste[:-k]

def rotate_left(liste, k):
    """Listeyi sola k pozisyon kaydır"""
    if not liste:
        return liste
    
    k = k % len(liste)
    return liste[k:] + liste[:k]

sayilar = [1, 2, 3, 4, 5]

print(f"Orijinal: {sayilar}")
print(f"Sağa 2: {rotate_right(sayilar, 2)}")    # [4, 5, 1, 2, 3]
print(f"Sola 2: {rotate_left(sayilar, 2)}")     # [3, 4, 5, 1, 2]
```

### Problem 5: İkinci En Büyük Sayı

**Soru:** Bir listede ikinci en büyük sayıyı bulun.

```python
# Çözüm
def ikinci_en_buyuk(liste):
    if len(liste) < 2:
        return None
    
    # Tekrarsız hale getir ve sırala
    tekrarsiz = list(set(liste))
    tekrarsiz.sort(reverse=True)
    
    if len(tekrarsiz) < 2:
        return None
    
    return tekrarsiz[1]

sayilar = [10, 5, 20, 8, 20, 15]
print(f"İkinci en büyük: {ikinci_en_buyuk(sayilar)}")  # 15

# Alternatif (daha verimli)
def ikinci_en_buyuk_v2(liste):
    if len(liste) < 2:
        return None
    
    en_buyuk = float('-inf')
    ikinci = float('-inf')
    
    for sayi in liste:
        if sayi > en_buyuk:
            ikinci = en_buyuk
            en_buyuk = sayi
        elif sayi > ikinci and sayi != en_buyuk:
            ikinci = sayi
    
    return ikinci if ikinci != float('-inf') else None
```

### Problem 6: Alt Liste Toplamı

**Soru:** Liste içinde ardışık elemanların toplamının en büyük olduğu alt listeyi bulun. (Kadane's Algorithm)

```python
# Çözüm - Kadane's Algorithm
def max_alt_liste_toplami(liste):
    if not liste:
        return 0
    
    max_toplam = liste[0]
    guncel_toplam = liste[0]
    
    for i in range(1, len(liste)):
        # Ya önceki toplamla devam et ya da yeniden başla
        guncel_toplam = max(liste[i], guncel_toplam + liste[i])
        max_toplam = max(max_toplam, guncel_toplam)
    
    return max_toplam

sayilar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"En büyük alt liste toplamı: {max_alt_liste_toplami(sayilar)}")  # 6
# Alt liste: [4, -1, 2, 1]
```

### Problem 7: Liste Düzleştirme (Flatten)

**Soru:** İç içe listeleri tek seviye listeye çevirin.

```python
# Çözüm
def flatten(ic_ice_liste):
    sonuc = []
    
    for eleman in ic_ice_liste:
        if isinstance(eleman, list):
            sonuc.extend(flatten(eleman))  # Recursive
        else:
            sonuc.append(eleman)
    
    return sonuc

ic_ice = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
duz = flatten(ic_ice)
print(duz)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# İteratif çözüm (tek seviye için)
def flatten_bir_seviye(ic_ice_liste):
    sonuc = []
    for eleman in ic_ice_liste:
        if isinstance(eleman, list):
            sonuc.extend(eleman)
        else:
            sonuc.append(eleman)
    return sonuc

tek_seviye = [1, [2, 3], 4, [5, 6]]
print(flatten_bir_seviye(tek_seviye))  # [1, 2, 3, 4, 5, 6]
```

### Problem 8: Çift ve Tek Sayıları Ayırma

**Soru:** Bir listede çift ve tek sayıları ayrı listelere ayırın.

```python
# Çözüm
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ciftler = [sayi for sayi in sayilar if sayi % 2 == 0]
tekler = [sayi for sayi in sayilar if sayi % 2 != 0]

print(f"Çift sayılar: {ciftler}")   # [2, 4, 6, 8, 10]
print(f"Tek sayılar: {tekler}")     # [1, 3, 5, 7, 9]

# Alternatif (tek döngüde)
ciftler, tekler = [], []

for sayi in sayilar:
    if sayi % 2 == 0:
        ciftler.append(sayi)
    else:
        tekler.append(sayi)
```

### Problem 9: Palindrom Liste

**Soru:** Bir listenin palindrom olup olmadığını kontrol edin.

```python
# Çözüm
def palindrom_mu(liste):
    return liste == liste[::-1]

# Test
print(palindrom_mu([1, 2, 3, 2, 1]))     # True
print(palindrom_mu([1, 2, 3, 4, 5]))     # False
print(palindrom_mu(['a', 'b', 'a']))     # True

# Alternatif (iki pointer yaklaşımı)
def palindrom_mu_v2(liste):
    sol = 0
    sag = len(liste) - 1
    
    while sol < sag:
        if liste[sol] != liste[sag]:
            return False
        sol += 1
        sag -= 1
    
    return True
```

### Problem 10: N Boyutlu Matris Oluşturma

**Soru:** Kullanıcıdan satır ve sütun sayısını alın. Bu boyutta bir matris oluşturun ve kullanıcıdan değerleri doldurun.

```python
# Çözüm
def matris_olustur():
    satir = int(input("Satır sayısı: "))
    sutun = int(input("Sütun sayısı: "))
    
    matris = []
    
    for i in range(satir):
        satir_listesi = []
        for j in range(sutun):
            deger = int(input(f"[{i}][{j}] elemanı: "))
            satir_listesi.append(deger)
        matris.append(satir_listesi)
    
    return matris

def matris_yazdir(matris):
    for satir in matris:
        for eleman in satir:
            print(f"{eleman:4}", end="")
        print()

# Kullanım
m = matris_olustur()
print("\nOluşturulan Matris:")
matris_yazdir(m)

# Otomatik matris oluşturma (sıfırlarla)
def sifir_matris_olustur(satir, sutun):
    return [[0 for j in range(sutun)] for i in range(satir)]

# Birim matris
def birim_matris(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("\n3x3 Birim Matris:")
matris_yazdir(birim_matris(3))
```

## 4.10 Ödev Önerileri - Modül 4

1. **To-Do List Uygulaması**: Görev ekleme, silme, tamamlandı işaretleme
2. **İstatistik Hesaplayıcı**: Liste için min, max, ortalama, medyan, mod hesaplama
3. **Matris İşlemleri**: Matris toplama, çıkarma, çarpma programı
4. **Frekans Analizi**: Bir metindeki kelimelerin sıklığını bulan program
5. **Liste Birleştirme**: İki sıralı listeyi birleştiren program (merge sort mantığı)

---

*Bu dokümanın devamı MODÜL 5 ile sürecektir. Sonraki modüller: Dictionary ve Set, Fonksiyonlar, String İşlemleri, Dosya Yönetimi, Exception Handling, OOP ve İleri Konular.*

# MODÜL 5: Veri Yapıları - Dictionary ve Set

**Süre:** 1 Oturum (Hafta 5)

## 5.1 Dictionary (Sözlük) Nedir?

Dictionary, anahtar-değer (key-value) çiftlerini saklayan bir veri yapısıdır.

### Dictionary Özellikleri

- **Anahtar-Değer Çiftleri**: Her eleman bir anahtar ve değer içerir
- **Sıralı** (Python 3.7+): Ekleme sırasını korur
- **Değiştirilebilir**: Değerler eklenebilir, silinebilir, değiştirilebilir
- **Anahtarlar Benzersiz**: Her anahtar sadece bir kez bulunabilir
- **Anahtarlar Değiştirilemez Tipler Olmalı**: string, int, tuple kullanılabilir

```python
# Boş dictionary
bos_sozluk = {}
bos_sozluk2 = dict()

# Dictionary oluşturma
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "bolum": "Bilgisayar Mühendisliği",
    "ortalama": 3.45
}

print(ogrenci)

# Farklı veri tipleri
karisik = {
    "sayi": 42,
    "metin": "Python",
    "liste": [1, 2, 3],
    "tuple": (4, 5),
    "bool": True
}

# dict() constructor
kisi = dict(ad="Ali", soyad="Yılmaz", yas=25)
print(kisi)  # {'ad': 'Ali', 'soyad': 'Yılmaz', 'yas': 25}
```

## 5.2 Dictionary'ye Erişim

```python
ogrenci = {
    "isim": "Ayşe",
    "yas": 22,
    "bolum": "Matematik",
    "notlar": [85, 90, 78]
}

# Köşeli parantez ile erişim
print(ogrenci["isim"])      # Ayşe
print(ogrenci["yas"])       # 22

# Olmayan anahtar hatası verir
# print(ogrenci["soyad"])   # KeyError

# get() metodu (güvenli erişim)
print(ogrenci.get("isim"))           # Ayşe
print(ogrenci.get("soyad"))          # None
print(ogrenci.get("soyad", "Yok"))   # Yok (varsayılan değer)

# Değer değiştirme
ogrenci["yas"] = 23
print(ogrenci["yas"])       # 23

# Yeni anahtar ekleme
ogrenci["sehir"] = "İstanbul"
print(ogrenci)

# İç içe erişim
print(ogrenci["notlar"][0])  # 85
```

## 5.3 Dictionary Methodları

### keys(), values(), items()

```python
urun = {
    "ad": "Laptop",
    "marka": "Dell",
    "fiyat": 15000,
    "stok": 50
}

# Tüm anahtarlar
anahtarlar = urun.keys()
print(anahtarlar)           # dict_keys(['ad', 'marka', 'fiyat', 'stok'])
print(list(anahtarlar))     # ['ad', 'marka', 'fiyat', 'stok']

# Tüm değerler
degerler = urun.values()
print(list(degerler))       # ['Laptop', 'Dell', 15000, 50]

# Anahtar-değer çiftleri
ogeleri = urun.items()
print(list(ogeleri))
# [('ad', 'Laptop'), ('marka', 'Dell'), ('fiyat', 15000), ('stok', 50)]

# Döngü ile kullanım
for anahtar in urun.keys():
    print(anahtar)

for deger in urun.values():
    print(deger)

for anahtar, deger in urun.items():
    print(f"{anahtar}: {deger}")
```

### update() - Dictionary Birleştirme

```python
sozluk1 = {"a": 1, "b": 2}
sozluk2 = {"c": 3, "d": 4}

sozluk1.update(sozluk2)
print(sozluk1)              # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Var olan anahtarları güncelleme
ogrenci = {"isim": "Ali", "yas": 20}
ogrenci.update({"yas": 21, "sehir": "Ankara"})
print(ogrenci)              # {'isim': 'Ali', 'yas': 21, 'sehir': 'Ankara'}

# ** operatörü ile birleştirme (Python 3.5+)
sozluk3 = {**sozluk1, **sozluk2}
print(sozluk3)
```

### pop() - Anahtar ile Silme

```python
ogrenci = {"isim": "Mehmet", "yas": 25, "bolum": "Fizik"}

# Anahtarı sil ve değeri döndür
bolum = ogrenci.pop("bolum")
print(bolum)                # Fizik
print(ogrenci)              # {'isim': 'Mehmet', 'yas': 25}

# Olmayan anahtar için varsayılan değer
soyad = ogrenci.pop("soyad", "Bulunamadı")
print(soyad)                # Bulunamadı

# pop() hata vermeden silme
if "sehir" in ogrenci:
    ogrenci.pop("sehir")
```

### popitem() - Son Eklenen Çifti Silme

```python
sozluk = {"a": 1, "b": 2, "c": 3}

# Son eklenen çifti sil ve döndür
son = sozluk.popitem()
print(son)                  # ('c', 3)
print(sozluk)               # {'a': 1, 'b': 2}
```

### clear() - Tüm Elemanları Silme

```python
ogrenci = {"isim": "Ali", "yas": 20}
ogrenci.clear()
print(ogrenci)              # {}
```

### setdefault() - Varsayılan Değer Atama

```python
sozluk = {"a": 1, "b": 2}

# Var olan anahtar
print(sozluk.setdefault("a", 10))     # 1 (değişmez)

# Yeni anahtar
print(sozluk.setdefault("c", 3))      # 3 (eklenir)
print(sozluk)                          # {'a': 1, 'b': 2, 'c': 3}

# Sayaç uygulaması
metin = "merhaba"
sayac = {}

for harf in metin:
    sayac[harf] = sayac.get(harf, 0) + 1

print(sayac)  # {'m': 1, 'e': 1, 'r': 1, 'h': 1, 'a': 2, 'b': 1}

# setdefault ile
sayac2 = {}
for harf in metin:
    sayac2.setdefault(harf, 0)
    sayac2[harf] += 1
```

### copy() - Dictionary Kopyalama

```python
orijinal = {"a": 1, "b": 2}
kopya = orijinal.copy()

kopya["c"] = 3
print(orijinal)             # {'a': 1, 'b': 2} (değişmedi)
print(kopya)                # {'a': 1, 'b': 2, 'c': 3}

# Referans kopyası (DİKKAT!)
sozluk1 = {"x": 10}
sozluk2 = sozluk1           # Aynı dictionary'ye işaret eder

sozluk2["y"] = 20
print(sozluk1)              # {'x': 10, 'y': 20} (değişti!)
```

## 5.4 İç İçe Dictionary (Nested Dictionaries)

```python
# Öğrenci veritabanı
ogrenciler = {
    "001": {
        "isim": "Ali Yılmaz",
        "yas": 20,
        "notlar": {
            "matematik": 85,
            "fizik": 90,
            "kimya": 78
        }
    },
    "002": {
        "isim": "Ayşe Demir",
        "yas": 22,
        "notlar": {
            "matematik": 92,
            "fizik": 88,
            "kimya": 95
        }
    }
}

# Erişim
print(ogrenciler["001"]["isim"])                    # Ali Yılmaz
print(ogrenciler["002"]["notlar"]["matematik"])     # 92

# Döngü ile gezme
for ogrenci_no, bilgiler in ogrenciler.items():
    print(f"\nÖğrenci No: {ogrenci_no}")
    print(f"İsim: {bilgiler['isim']}")
    print(f"Yaş: {bilgiler['yas']}")
    print("Notlar:")
    for ders, not_degeri in bilgiler['notlar'].items():
        print(f"  {ders}: {not_degeri}")

# Yeni öğrenci ekleme
ogrenciler["003"] = {
    "isim": "Mehmet Kaya",
    "yas": 21,
    "notlar": {
        "matematik": 87,
        "fizik": 91,
        "kimya": 84
    }
}
```

## 5.5 Dictionary Comprehension

```python
# Basit dictionary comprehension
kareler = {x: x**2 for x in range(1, 6)}
print(kareler)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Listeden dictionary oluşturma
isimler = ["Ali", "Ayşe", "Mehmet"]
yaslar = [25, 30, 28]

kisi_sozluk = {isim: yas for isim, yas in zip(isimler, yaslar)}
print(kisi_sozluk)  # {'Ali': 25, 'Ayşe': 30, 'Mehmet': 28}

# Koşullu dictionary comprehension
sayilar = {x: "çift" if x % 2 == 0 else "tek" for x in range(1, 11)}
print(sayilar)

# Kelime uzunlukları
kelimeler = ["elma", "armut", "muz", "kiraz"]
uzunluklar = {kelime: len(kelime) for kelime in kelimeler}
print(uzunluklar)  # {'elma': 4, 'armut': 5, 'muz': 3, 'kiraz': 5}

# Büyük harfe çevirme
isimler = {"ali": 25, "ayşe": 30}
buyuk = {k.upper(): v for k, v in isimler.items()}
print(buyuk)  # {'ALI': 25, 'AYŞE': 30}
```

## 5.6 Set (Küme) Nedir?

Set, matematikteki küme yapısının Python karşılığıdır.

### Set Özellikleri

- **Benzersiz Elemanlar**: Tekrar eden elemanları kabul etmez
- **Sırasız**: Elemanların belirli bir sırası yoktur
- **Değiştirilebilir**: Eleman eklenebilir, silinebilir
- **İndekslenemez**: Köşeli parantez ile erişilemez
- **Değiştirilemez Tipler İçermelidir**: string, int, tuple (liste içeremez)

```python
# Boş set
bos_set = set()             # {} boş dictionary oluşturur!

# Set oluşturma
sayilar = {1, 2, 3, 4, 5}
print(sayilar)              # {1, 2, 3, 4, 5}

# Tekrar edenler kaldırılır
tekrarli = {1, 2, 2, 3, 3, 3, 4}
print(tekrarli)             # {1, 2, 3, 4}

# Listeden set oluşturma
liste = [1, 2, 2, 3, 4, 4, 5]
set_yapmak = set(liste)
print(set_yapmak)           # {1, 2, 3, 4, 5}

# String'den set
harf_seti = set("merhaba")
print(harf_seti)            # {'m', 'e', 'r', 'h', 'a', 'b'}

# Set uzunluğu
print(len(sayilar))         # 5

# Üyelik kontrolü
print(3 in sayilar)         # True
print(10 in sayilar)        # False
```

## 5.7 Set Methodları

### add() - Eleman Ekleme

```python
meyveler = {"elma", "armut"}
meyveler.add("muz")
print(meyveler)             # {'elma', 'armut', 'muz'}

# Var olan elemanı ekleme (değişmez)
meyveler.add("elma")
print(meyveler)             # {'elma', 'armut', 'muz'}
```

### update() - Çoklu Eleman Ekleme

```python
sayilar = {1, 2, 3}
sayilar.update([4, 5, 6])
print(sayilar)              # {1, 2, 3, 4, 5, 6}

# Birden fazla iterable
sayilar.update([7, 8], {9, 10})
print(sayilar)              # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

### remove() ve discard() - Eleman Silme

```python
sayilar = {1, 2, 3, 4, 5}

# remove() - Yoksa hata verir
sayilar.remove(3)
print(sayilar)              # {1, 2, 4, 5}

# sayilar.remove(10)        # KeyError!

# discard() - Yoksa hata vermez
sayilar.discard(4)
print(sayilar)              # {1, 2, 5}

sayilar.discard(10)         # Hata vermez
print(sayilar)              # {1, 2, 5}
```

### pop() - Rastgele Eleman Silme

```python
sayilar = {1, 2, 3, 4, 5}

# Rastgele bir eleman sil ve döndür
eleman = sayilar.pop()
print(f"Silinen: {eleman}")
print(sayilar)
```

### clear() - Tüm Elemanları Silme

```python
sayilar = {1, 2, 3}
sayilar.clear()
print(sayilar)              # set()
```

## 5.8 Set Matematiksel İşlemleri

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Birleşim (Union) - A ∪ B
birlesim = A | B
print(birlesim)             # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))           # Aynı sonuç

# Kesişim (Intersection) - A ∩ B
kesisim = A & B
print(kesisim)              # {4, 5}
print(A.intersection(B))    # Aynı sonuç

# Fark (Difference) - A - B
fark = A - B
print(fark)                 # {1, 2, 3}
print(A.difference(B))      # Aynı sonuç

# Simetrik Fark (Symmetric Difference) - A △ B
simetrik_fark = A ^ B
print(simetrik_fark)        # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))  # Aynı sonuç

# Alt küme kontrolü (Subset)
C = {1, 2, 3}
D = {1, 2, 3, 4, 5}

print(C.issubset(D))        # True (C ⊆ D)
print(C <= D)               # True

# Üst küme kontrolü (Superset)
print(D.issuperset(C))      # True (D ⊇ C)
print(D >= C)               # True

# Ayrık kümeler mi? (Disjoint)
E = {1, 2, 3}
F = {4, 5, 6}
print(E.isdisjoint(F))      # True (kesişimleri yok)
```

## 5.9 Frozenset - Değiştirilemez Set

```python
# Frozenset oluşturma
sabit_set = frozenset([1, 2, 3, 4, 5])
print(sabit_set)

# Frozenset değiştirilemez
# sabit_set.add(6)          # AttributeError!

# Frozenset dictionary anahtarı olarak kullanılabilir
sozluk = {
    frozenset([1, 2]): "Grup A",
    frozenset([3, 4]): "Grup B"
}

print(sozluk[frozenset([1, 2])])  # Grup A

# Set içinde frozenset kullanımı
set_koleksiyonu = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}
```

## 5.10 Pratik Örnekler

### Örnek 1: Kelime Frekans Analizi

```python
def kelime_frekansi(metin):
    """Metindeki kelimelerin frekansını hesaplar"""
    kelimeler = metin.lower().split()
    frekans = {}
    
    for kelime in kelimeler:
        # Noktalama işaretlerini temizle
        kelime = kelime.strip('.,!?;:"')
        frekans[kelime] = frekans.get(kelime, 0) + 1
    
    return frekans

metin = "Python programlama dili Python ile kolay. Python öğrenmek eğlenceli."
sonuc = kelime_frekansi(metin)

print("Kelime Frekansları:")
for kelime, sayi in sorted(sonuc.items(), key=lambda x: x[1], reverse=True):
    print(f"{kelime}: {sayi}")
```

### Örnek 2: Telefon Rehberi

```python
telefon_rehberi = {}

def kisi_ekle():
    isim = input("İsim: ")
    telefon = input("Telefon: ")
    telefon_rehberi[isim] = telefon
    print(f"{isim} rehbere eklendi.")

def kisi_ara():
    isim = input("Aramak istediğiniz kişi: ")
    telefon = telefon_rehberi.get(isim)
    
    if telefon:
        print(f"{isim}: {telefon}")
    else:
        print("Kişi bulunamadı!")

def kisi_sil():
    isim = input("Silmek istediğiniz kişi: ")
    
    if isim in telefon_rehberi:
        telefon_rehberi.pop(isim)
        print(f"{isim} silindi.")
    else:
        print("Kişi bulunamadı!")

def rehber_listele():
    if not telefon_rehberi:
        print("Rehber boş!")
        return
    
    print("\n=== TELEFON REHBERİ ===")
    for isim, telefon in sorted(telefon_rehberi.items()):
        print(f"{isim}: {telefon}")

# Ana program döngüsü
while True:
    print("\n1. Kişi Ekle")
    print("2. Kişi Ara")
    print("3. Kişi Sil")
    print("4. Rehberi Listele")
    print("5. Çıkış")
    
    secim = input("\nSeçim: ")
    
    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisi_ara()
    elif secim == "3":
        kisi_sil()
    elif secim == "4":
        rehber_listele()
    elif secim == "5":
        break
```

### Örnek 3: Set ile Ortak Öğrenci Bulma

```python
# İki dersi alan öğrenciler
matematik = {"Ali", "Ayşe", "Mehmet", "Zeynep", "Can"}
fizik = {"Ayşe", "Can", "Ebru", "Fatih", "Zeynep"}

print("Her iki dersi de alanlar:", matematik & fizik)
print("Sadece matematik alanlar:", matematik - fizik)
print("Sadece fizik alanlar:", fizik - matematik)
print("Sadece bir ders alanlar:", matematik ^ fizik)
print("En az bir ders alanlar:", matematik | fizik)
```

## 5.11 Algoritma Problemleri - Modül 5

### Problem 1: İki Listenin Ortak ve Farklı Elemanları

**Soru:** İki liste verildiğinde, ortak elemanları ve her listede özgün olan elemanları bulun.

```python
# Çözüm
liste1 = [1, 2, 3, 4, 5, 6]
liste2 = [4, 5, 6, 7, 8, 9]

set1 = set(liste1)
set2 = set(liste2)

ortak = set1 & set2
sadece_birinci = set1 - set2
sadece_ikinci = set2 - set1
tum_elemanlar = set1 | set2

print(f"Ortak elemanlar: {ortak}")
print(f"Sadece birinci listede: {sadece_birinci}")
print(f"Sadece ikinci listede: {sadece_ikinci}")
print(f"Tüm elemanlar: {tum_elemanlar}")
```

### Problem 2: Anagram Kontrolü

**Soru:** İki kelimenin anagram olup olmadığını kontrol edin. (Anagram: Harfleri aynı olan kelimeler)

```python
# Çözüm
def anagram_mi(kelime1, kelime2):
    # Boşlukları kaldır ve küçük harfe çevir
    kelime1 = kelime1.replace(" ", "").lower()
    kelime2 = kelime2.replace(" ", "").lower()
    
    # Sıralanmış karakterler karşılaştırılır
    return sorted(kelime1) == sorted(kelime2)

# Alternatif (Counter kullanarak)
from collections import Counter

def anagram_mi_v2(kelime1, kelime2):
    kelime1 = kelime1.replace(" ", "").lower()
    kelime2 = kelime2.replace(" ", "").lower()
    return Counter(kelime1) == Counter(kelime2)

# Test
print(anagram_mi("listen", "silent"))      # True
print(anagram_mi("hello", "world"))        # False
print(anagram_mi("astronomer", "moon starer"))  # True
```

### Problem 3: En Sık Geçen Karakter

**Soru:** Bir string'de en sık geçen karakteri bulun.

```python
# Çözüm
def en_sik_karakter(metin):
    # Boşlukları yok say
    metin = metin.replace(" ", "").lower()
    
    if not metin:
        return None
    
    # Frekans hesaplama
    frekans = {}
    for karakter in metin:
        frekans[karakter] = frekans.get(karakter, 0) + 1
    
    # En yüksek frekanslı karakteri bul
    en_sik = max(frekans.items(), key=lambda x: x[1])
    
    return en_sik

metin = "merhaba dünya"
karakter, sayi = en_sik_karakter(metin)
print(f"En sık geçen: '{karakter}' ({sayi} kez)")

# Alternatif (Counter kullanarak)
from collections import Counter

def en_sik_karakter_v2(metin):
    metin = metin.replace(" ", "").lower()
    sayac = Counter(metin)
    return sayac.most_common(1)[0]
```

### Problem 4: Öğrenci Not Sistemi

**Soru:** Dictionary kullanarak öğrenci not sistemi oluşturun. Ortalama hesaplama ve en başarılı öğrenciyi bulma.

```python
# Çözüm
ogrenciler = {
    "Ali": [85, 90, 78, 92],
    "Ayşe": [92, 88, 95, 91],
    "Mehmet": [78, 85, 82, 79],
    "Zeynep": [95, 93, 97, 94]
}

def ortalama_hesapla(notlar):
    return sum(notlar) / len(notlar)

# Her öğrencinin ortalaması
ortalamalar = {}
for isim, notlar in ogrenciler.items():
    ortalama = ortalama_hesapla(notlar)
    ortalamalar[isim] = ortalama
    print(f"{isim}: {ortalama:.2f}")

# En başarılı öğrenci
en_basarili = max(ortalamalar.items(), key=lambda x: x[1])
print(f"\nEn başarılı: {en_basarili[0]} ({en_basarili[1]:.2f})")

# Sınıf ortalaması
sinif_ortalamasi = sum(ortalamalar.values()) / len(ortalamalar)
print(f"Sınıf ortalaması: {sinif_ortalamasi:.2f}")

# Ortalamanın üstünde olanlar
print("\nOrtalamanın üstünde olanlar:")
for isim, ortalama in ortalamalar.items():
    if ortalama > sinif_ortalamasi:
        print(f"  {isim}: {ortalama:.2f}")
```

### Problem 5: Grup Oluşturma

**Soru:** Öğrencileri ilgi alanlarına göre gruplara ayırın.

```python
# Çözüm
ogrenciler_ilgi = [
    {"isim": "Ali", "ilgi": ["spor", "müzik"]},
    {"isim": "Ayşe", "ilgi": ["resim", "müzik"]},
    {"isim": "Mehmet", "ilgi": ["spor", "teknoloji"]},
    {"isim": "Zeynep", "ilgi": ["müzik", "resim"]},
    {"isim": "Can", "ilgi": ["spor", "resim"]}
]

# İlgi alanlarına göre grupla
gruplar = {}

for ogrenci in ogrenciler_ilgi:
    for ilgi in ogrenci["ilgi"]:
        if ilgi not in gruplar:
            gruplar[ilgi] = []
        gruplar[ilgi].append(ogrenci["isim"])

# Sonuçları yazdır
print("İlgi Alanı Grupları:")
for ilgi, ogrenciler in gruplar.items():
    print(f"\n{ilgi.capitalize()}:")
    for ogrenci in ogrenciler:
        print(f"  - {ogrenci}")

# En popüler ilgi alanı
en_populer = max(gruplar.items(), key=lambda x: len(x[1]))
print(f"\nEn popüler ilgi alanı: {en_populer[0]} ({len(en_populer[1])} öğrenci)")
```

## 5.12 Ödev Önerileri - Modül 5

1. **Ürün Envanter Sistemi**: Dictionary ile ürün ekleme, stok güncelleme, arama
2. **Sözlük Uygulaması**: Türkçe-İngilizce kelime çevirme programı
3. **E-Ticaret Sepeti**: Ürün ekleme, çıkarma, toplam fiyat hesaplama
4. **Öğrenci Devamsızlık Takibi**: Tarih bazlı devamsızlık kaydetme ve sorgulama
5. **Set ile Veri Temizleme**: Tekrar eden kayıtları temizleme programı

---

# MODÜL 6: Fonksiyonlar

**Süre:** 1 Oturum - 5 Saat (Hafta 6)

## 6.1 Fonksiyon Nedir?

Fonksiyon, belirli bir görevi yerine getiren, yeniden kullanılabilir kod bloklarıdır.

### Fonksiyon Tanımlama

```python
# Basit fonksiyon
def selamla():
    print("Merhaba!")

# Fonksiyonu çağırma
selamla()  # Merhaba!

# Parametreli fonksiyon
def selamla_isim(isim):
    print(f"Merhaba, {isim}!")

selamla_isim("Ahmet")  # Merhaba, Ahmet!
selamla_isim("Ayşe")   # Merhaba, Ayşe!

# Çoklu parametre
def toplama(a, b):
    sonuc = a + b
    print(f"{a} + {b} = {sonuc}")

toplama(5, 3)  # 5 + 3 = 8
```

## 6.2 return - Değer Döndürme

```python
# Değer döndüren fonksiyon
def topla(a, b):
    return a + b

sonuc = topla(10, 20)
print(sonuc)  # 30

# Return olmadan (None döner)
def yazdir(metin):
    print(metin)

sonuc = yazdir("Merhaba")
print(sonuc)  # None

# Çoklu return
def hesapla(a, b):
    toplam = a + b
    fark = a - b
    carpim = a * b
    bolum = a / b
    return toplam, fark, carpim, bolum

t, f, c, b = hesapla(10, 2)
print(t, f, c, b)  # 12 8 20 5.0

# Koşullu return
def mutlak_deger(sayi):
    if sayi >= 0:
        return sayi
    else:
        return -sayi

print(mutlak_deger(5))   # 5
print(mutlak_deger(-5))  # 5

# Erken return (guard clause)
def bol(a, b):
    if b == 0:
        return "Sıfıra bölme hatası!"
    return a / b

print(bol(10, 2))  # 5.0
print(bol(10, 0))  # Sıfıra bölme hatası!
```

## 6.3 Parametre Türleri

### Positional Arguments (Konumsal Parametreler)

```python
def tanitim(isim, yas, sehir):
    print(f"Adım {isim}, {yas} yaşındayım ve {sehir}'de yaşıyorum.")

# Sıra önemli!
tanitim("Ali", 25, "İstanbul")
# Adım Ali, 25 yaşındayım ve İstanbul'de yaşıyorum.

# Yanlış sıra
tanitim(25, "Ali", "İstanbul")  # Hatalı çıktı!
```

### Keyword Arguments (İsimlendirilmiş Parametreler)

```python
def tanitim(isim, yas, sehir):
    print(f"Adım {isim}, {yas} yaşındayım ve {sehir}'de yaşıyorum.")

# Sıra önemsiz
tanitim(yas=25, sehir="Ankara", isim="Ayşe")
# Adım Ayşe, 25 yaşındayım ve Ankara'de yaşıyorum.

# Karışık kullanım (önce positional, sonra keyword)
tanitim("Mehmet", sehir="İzmir", yas=30)
# Adım Mehmet, 30 yaşındayım ve İzmir'de yaşıyorum.
```

### Default Parameters (Varsayılan Parametreler)

```python
def selamla(isim, selam="Merhaba"):
    print(f"{selam}, {isim}!")

selamla("Ali")              # Merhaba, Ali!
selamla("Ayşe", "Günaydın") # Günaydın, Ayşe!

# Dikkat: Değiştirilebilir varsayılan değerler
def liste_ekle(eleman, liste=None):  # DOĞRU
    if liste is None:
        liste = []
    liste.append(eleman)
    return liste

# Yanlış kullanım
def liste_ekle_yanlis(eleman, liste=[]):  # YANLIŞ!
    liste.append(eleman)
    return liste

# Bu hatalı davranışa yol açar
print(liste_ekle_yanlis(1))  # [1]
print(liste_ekle_yanlis(2))  # [1, 2] (Beklenmeyen!)
```

### *args - Değişken Sayıda Argüman

```python
# Sınırsız sayıda argüman
def topla_hepsi(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(topla_hepsi(1, 2, 3))           # 6
print(topla_hepsi(10, 20, 30, 40))    # 100
print(topla_hepsi(5))                  # 5

# *args tuple olarak gelir
def goster(*args):
    print(type(args))  # <class 'tuple'>
    print(args)

goster(1, 2, 3, "a", True)
# (1, 2, 3, 'a', True)

# Normal parametre + *args
def bilgi_ver(isim, *hobiler):
    print(f"{isim}'in hobileri:")
    for hobi in hobiler:
        print(f"  - {hobi}")

bilgi_ver("Ali", "futbol", "müzik", "okuma")
```

### **kwargs - Değişken Sayıda Keyword Argüman

```python
# Sınırsız keyword argüman
def ogrenci_bilgi(**bilgiler):
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

ogrenci_bilgi(isim="Ali", yas=20, bolum="Bilgisayar")
# isim: Ali
# yas: 20
# bolum: Bilgisayar

# **kwargs dictionary olarak gelir
def goster(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

goster(a=1, b=2, c=3)
# {'a': 1, 'b': 2, 'c': 3}

# Tüm parametre türlerini birlikte kullanma
def tam_ornek(zorunlu, varsayilan="default", *args, **kwargs):
    print(f"Zorunlu: {zorunlu}")
    print(f"Varsayılan: {varsayilan}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

tam_ornek(1, 2, 3, 4, 5, x=10, y=20)
# Zorunlu: 1
# Varsayılan: 2
# args: (3, 4, 5)
# kwargs: {'x': 10, 'y': 20}
```

## 6.4 Lambda Fonksiyonları

Lambda, tek satırlık anonim fonksiyonlardır.

```python
# Normal fonksiyon
def kare(x):
    return x ** 2

print(kare(5))  # 25

# Lambda ile
kare_lambda = lambda x: x ** 2
print(kare_lambda(5))  # 25

# Çoklu parametre
toplam = lambda a, b: a + b
print(toplam(3, 5))  # 8

# Lambda'yı doğrudan kullanma
print((lambda x, y: x * y)(4, 6))  # 24

# map() ile kullanım
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x ** 2, sayilar))
print(kareler)  # [1, 4, 9, 16, 25]

# filter() ile kullanım
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(ciftler)  # [2, 4]

# sorted() ile kullanım
ogrenciler = [
    {"isim": "Ali", "not": 85},
    {"isim": "Ayşe", "not": 92},
    {"isim": "Mehmet", "not": 78}
]

sirali = sorted(ogrenciler, key=lambda x: x["not"], reverse=True)
for ogrenci in sirali:
    print(f"{ogrenci['isim']}: {ogrenci['not']}")
```

## 6.5 Scope (Kapsam) Kavramı

### Local ve Global Scope

```python
# Global değişken
x = "global"

def fonksiyon():
    # Local değişken
    x = "local"
    print(f"Fonksiyon içi: {x}")

fonksiyon()              # Fonksiyon içi: local
print(f"Dışarıda: {x}")  # Dışarıda: global

# Global değişkeni değiştirme
sayi = 10

def artir():
    global sayi  # Global kullanacağımızı belirt
    sayi += 1

print(sayi)  # 10
artir()
print(sayi)  # 11

# Nonlocal (iç içe fonksiyonlarda)
def dis_fonksiyon():
    x = "dış"
    
    def ic_fonksiyon():
        nonlocal x  # Dış fonksiyonun değişkenini kullan
        x = "iç"
        print(f"İç fonksiyon: {x}")
    
    ic_fonksiyon()
    print(f"Dış fonksiyon: {x}")

dis_fonksiyon()
# İç fonksiyon: iç
# Dış fonksiyon: iç
```

### LEGB Kuralı

Python değişken aramada LEGB sırasını takip eder:
- **L**ocal: Fonksiyon içi
- **E**nclosing: Kapsayan fonksiyon
- **G**lobal: Modül seviyesi
- **B**uilt-in: Python'ın yerleşik isimleri

```python
# Built-in
print(len([1, 2, 3]))  # 3

# Global
x = "global x"

def dis():
    # Enclosing
    x = "enclosing x"
    
    def ic():
        # Local
        x = "local x"
        print(x)  # local x
    
    ic()
    print(x)  # enclosing x

dis()
print(x)  # global x
```

## 6.6 Yüksek Seviye Fonksiyon Özellikleri

### Fonksiyonları Parametre Olarak Kullanma

```python
def uygula(fonksiyon, deger):
    return fonksiyon(deger)

def kare(x):
    return x ** 2

def kup(x):
    return x ** 3

print(uygula(kare, 5))  # 25
print(uygula(kup, 3))   # 27

# Lambda ile
print(uygula(lambda x: x * 2, 10))  # 20
```

### Fonksiyonları Return Etme

```python
def us_fonksiyonu_olustur(n):
    def us_al(x):
        return x ** n
    return us_al

kare = us_fonksiyonu_olustur(2)
kup = us_fonksiyonu_olustur(3)

print(kare(5))  # 25
print(kup(3))   # 27
```

### Decorator (Dekoratör) Temelleri

```python
# Basit decorator
def suresini_olc(fonksiyon):
    import time
    
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} {bitis - baslangic:.4f} saniye sürdü")
        return sonuc
    
    return wrapper

@suresini_olc
def yavas_fonksiyon():
    import time
    time.sleep(1)
    return "Bitti"

yavas_fonksiyon()
# yavas_fonksiyon 1.0012 saniye sürdü

# Decorator zincirleme
def buyuk_harf(fonksiyon):
    def wrapper(*args, **kwargs):
        sonuc = fonksiyon(*args, **kwargs)
        return sonuc.upper()
    return wrapper

def unlem_ekle(fonksiyon):
    def wrapper(*args, **kwargs):
        sonuc = fonksiyon(*args, **kwargs)
        return sonuc + "!"
    return wrapper

@buyuk_harf
@unlem_ekle
def selamla(isim):
    return f"merhaba {isim}"

print(selamla("ali"))  # MERHABA ALI!
```

## 6.7 Recursive (Özyinelemeli) Fonksiyonlar

```python
# Faktöriyel
def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)

print(faktoriyel(5))  # 120

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# EBOB (Öklid Algoritması)
def ebob(a, b):
    if b == 0:
        return a
    else:
        return ebob(b, a % b)

print(ebob(48, 18))  # 6

# Liste toplamı
def liste_toplami(liste):
    if not liste:
        return 0
    else:
        return liste[0] + liste_toplami(liste[1:])

print(liste_toplami([1, 2, 3, 4, 5]))  # 15
```

## 6.8 Pratik Fonksiyon Örnekleri

### Örnek 1: Sayı Kontrol Fonksiyonları

```python
def asal_mi(sayi):
    """Sayının asal olup olmadığını kontrol eder"""
    if sayi < 2:
        return False
    
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    
    return True

def mukemmel_mi(sayi):
    """Mükemmel sayı kontrolü"""
    if sayi < 1:
        return False
    
    toplam = sum(i for i in range(1, sayi) if sayi % i == 0)
    return toplam == sayi

def armstrong_mi(sayi):
    """Armstrong sayısı kontrolü"""
    basamak_sayisi = len(str(sayi))
    toplam = sum(int(rakam) ** basamak_sayisi for rakam in str(sayi))
    return toplam == sayi

# Test
print(f"7 asal mı? {asal_mi(7)}")              # True
print(f"6 mükemmel mi? {mukemmel_mi(6)}")      # True
print(f"153 armstrong mı? {armstrong_mi(153)}")# True
```

### Örnek 2: Liste İşlem Fonksiyonları

```python
def liste_istatistikleri(liste):
    """Liste istatistiklerini döndürür"""
    return {
        "toplam": sum(liste),
        "ortalama": sum(liste) / len(liste),
        "min": min(liste),
        "max": max(liste),
        "uzunluk": len(liste)
    }

def tekrarsiz_yap(liste):
    """Listeden tekrarları kaldırır (sıra korur)"""
    return list(dict.fromkeys(liste))

def liste_sirala(liste, azalan=False):
    """Listeyi sıralar"""
    return sorted(liste, reverse=azalan)

# Test
sayilar = [5, 2, 8, 2, 9, 1, 5, 8]
print(liste_istatistikleri(sayilar))
print(tekrarsiz_yap(sayilar))
print(liste_sirala(sayilar))
```

### Örnek 3: String İşlem Fonksiyonları

```python
def kelime_say(metin):
    """Metindeki kelime sayısını döndürür"""
    return len(metin.split())

def sesli_harf_say(metin):
    """Sesli harf sayısını döndürür"""
    sesliler = "aeiouAEIOU"
    return sum(1 for harf in metin if harf in sesliler)

def palindrom_mu(metin):
    """Palindrom kontrolü"""
    temiz = metin.replace(" ", "").lower()
    return temiz == temiz[::-1]

def kelime_frekansi(metin):
    """Kelime frekanslarını döndürür"""
    kelimeler = metin.lower().split()
    frekans = {}
    for kelime in kelimeler:
        frekans[kelime] = frekans.get(kelime, 0) + 1
    return frekans

# Test
metin = "Python programlama Python ile kolay"
print(f"Kelime sayısı: {kelime_say(metin)}")
print(f"Sesli harf sayısı: {sesli_harf_say(metin)}")
print(f"Frekanslar: {kelime_frekansi(metin)}")
```

## 6.9 Algoritma Problemleri - Modül 6

### Problem 1: Fibonacci Serisi (N. Terim)

**Soru:** Fibonacci serisinin n. terimini bulan fonksiyon yazın.

```python
# Recursive çözüm
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# İteratif çözüm (daha verimli)
def fibonacci_iterative(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Memoization ile (en verimli)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Test
print(fibonacci_iterative(10))  # 55
```

### Problem 2: Asal Sayı Kontrolü ve Liste

**Soru:** Bir sayının asal olup olmadığını kontrol eden ve verilen aralıktaki asal sayıları listeleyen fonksiyonlar yazın.

```python
def asal_mi(sayi):
    if sayi < 2:
        return False
    
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    
    return True

def asal_listesi(baslangic, bitis):
    return [sayi for sayi in range(baslangic, bitis + 1) if asal_mi(sayi)]

# Test
print(asal_listesi(1, 50))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Problem 3: Liste Düzleştirme (Recursive)

**Soru:** İç içe listeleri düzleştiren recursive fonksiyon yazın.

```python
def flatten(liste):
    """İç içe listeleri düzleştirir"""
    sonuc = []
    
    for eleman in liste:
        if isinstance(eleman, list):
            sonuc.extend(flatten(eleman))
        else:
            sonuc.append(eleman)
    
    return sonuc

# Test
ic_ice_liste = [1, [2, 3, [4, 5]], 6, [7, [8, [9]]]]
print(flatten(ic_ice_liste))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Problem 4: Permütasyon ve Kombinasyon

**Soru:** n elemandan r tanesini seçmenin kaç yolla yapılabileceğini hesaplayan fonksiyonlar.

```python
def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    return n * faktoriyel(n - 1)

def permutasyon(n, r):
    """nPr = n! / (n-r)!"""
    return faktoriyel(n) // faktoriyel(n - r)

def kombinasyon(n, r):
    """nCr = n! / (r! * (n-r)!)"""
    return faktoriyel(n) // (faktoriyel(r) * faktoriyel(n - r))

# Test
print(f"10P3 = {permutasyon(10, 3)}")  # 720
print(f"10C3 = {kombinasyon(10, 3)}")  # 120
```

### Problem 5: Sayı Sistemleri Dönüştürme

**Soru:** Onluk sayıyı ikili, sekizli, onaltılı sisteme çeviren fonksiyonlar.

```python
def onluktan_ikiliye(sayi):
    if sayi == 0:
        return "0"
    
    binary = ""
    while sayi > 0:
        binary = str(sayi % 2) + binary
        sayi //= 2
    
    return binary

def onluktan_sekizliye(sayi):
    if sayi == 0:
        return "0"
    
    octal = ""
    while sayi > 0:
        octal = str(sayi % 8) + octal
        sayi //= 8
    
    return octal

def onluktan_onaltiliya(sayi):
    if sayi == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    
    while sayi > 0:
        hexadecimal = hex_digits[sayi % 16] + hexadecimal
        sayi //= 16
    
    return hexadecimal

# Test
sayi = 255
print(f"{sayi} (10) = {onluktan_ikiliye(sayi)} (2)")    # 11111111
print(f"{sayi} (10) = {onluktan_sekizliye(sayi)} (8)")  # 377
print(f"{sayi} (10) = {onluktan_onaltiliya(sayi)} (16)")# FF

# Python built-in fonksiyonlar
print(bin(255))   # 0b11111111
print(oct(255))   # 0o377
print(hex(255))   # 0xff
```

## 6.10 Ödev Önerileri - Modül 6

1. **Hesap Makinesi**: Dört işlem ve gelişmiş işlemler yapan modüler hesap makinesi
2. **Şifre Oluşturucu**: Güvenli rastgele şifre üreten fonksiyonlar
3. **Metin Analizi**: Kelime sayısı, karakter analizi, istatistik fonksiyonları
4. **Dönüştürücü Paketi**: Birim dönüştürme fonksiyonları (sıcaklık, uzunluk, ağırlık)
5. **Matematiksel Fonksiyonlar**: Trigonometri, logaritma, istatistik fonksiyonları

---
