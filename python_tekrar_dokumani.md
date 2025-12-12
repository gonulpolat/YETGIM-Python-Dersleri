# Python Genel Tekrar Dokümanı

Bu doküman, Python programlama dilindeki temel ve orta seviye konuları kapsayan 5 saatlik bir genel tekrar materyali olarak hazırlanmıştır. Her konu başlığı altında teorik anlatımlar, pratik syntax örnekleri ve algoritma soruları bulunmaktadır.

## 1. Temel Python

### 1.1. Değişkenler, Veri Tipleri, Operatörler ve Tip Dönüşümleri

**Teorik İçerik (10-15 dakika)**

Programlamanın temel taşı olan **değişkenler**, verileri hafızada geçici olarak saklamak için kullanılan isimlendirilmiş alanlardır. Python, dinamik tipli bir dildir, yani bir değişkenin tipini önceden belirtmenize gerek yoktur; değişkenin tipi, atanan değere göre otomatik olarak belirlenir.

**Temel Veri Tipleri:**

*   **Integer (`int`):** Tam sayıları ifade eder (örn: 5, -10, 1000).
*   **Float (`float`):** Ondalıklı sayıları ifade eder (örn: 3.14, -0.5, 2.718).
*   **String (`str`):** Metinsel verileri ifade eder. Tek tırnak (`'...'`), çift tırnak (`"..."`) veya üç tırnak (`'''...'''` veya `"""..."""`) içinde tanımlanır.
*   **Boolean (`bool`):** Mantıksal `True` (Doğru) ve `False` (Yanlış) değerlerini temsil eder.

**Operatörler:**

Operatörler, değişkenler ve değerler üzerinde işlem yapmak için kullanılan özel sembollerdir.

*   **Aritmetik Operatörler:** Toplama (`+`), çıkarma (`-`), çarpma (`*`), bölme (`/`), tam bölme (`//`), mod alma (`%`) ve üs alma (`**`).
*   **Atama Operatörleri:** Değişkenlere değer atamak için kullanılır (`=`, `+=`, `-=`, `*=`, `/=` vb.).
*   **Karşılaştırma Operatörleri:** İki değeri karşılaştırır ve sonuç olarak `True` veya `False` döndürür (`==`, `!=`, `>`, `<`, `>=`, `<=`).
*   **Mantıksal Operatörler:** Mantıksal ifadeleri birleştirmek için kullanılır (`and`, `or`, `not`).

**Tip Dönüşümleri:**

Bazen bir veri tipini başka bir veri tipine dönüştürmek gerekebilir. Python'da bu işlem, `int()`, `float()`, `str()` gibi yerleşik fonksiyonlar kullanılarak yapılır. Örneğin, kullanıcıdan `input()` ile alınan bir değer her zaman string'dir. Matematiksel bir işlem yapmak için bu değeri `int()` veya `float()` ile sayısal bir tipe dönüştürmek gerekir.

---

**Syntax Örnekleri**

1.  **Değişken Tanımlama ve Veri Tipleri**

    ```python
    # Bir mağazadaki ürün bilgilerini saklayalım
    urun_adi = "Laptop"
    stok_miktari = 15
    fiyat = 25000.75
    garantisi_var_mi = True

    print(f"Ürün Adı: {urun_adi}, Tipi: {type(urun_adi)}")
    print(f"Stok Miktarı: {stok_miktari}, Tipi: {type(stok_miktari)}")
    print(f"Fiyat: {fiyat}, Tipi: {type(fiyat)}")
    print(f"Garanti Durumu: {garantisi_var_mi}, Tipi: {type(garantisi_var_mi)}")
    ```

2.  **Aritmetik Operatörler ile Basit Hesaplama**

    ```python
    # Dikdörtgenin alanını ve çevresini hesaplama
    kisa_kenar = 10
    uzun_kenar = 25

    alan = kisa_kenar * uzun_kenar
    cevre = 2 * (kisa_kenar + uzun_kenar)

    print(f"Dikdörtgenin Alanı: {alan}")
    print(f"Dikdörtgenin Çevresi: {cevre}")
    ```

3.  **Atama Operatörleri ile Değer Güncelleme**

    ```python
    # Bir online oyunda oyuncunun puanını güncelleme
    puan = 100
    print(f"Başlangıç Puanı: {puan}")

    puan += 50  # Oyuncu 50 puan kazandı
    print(f"Kazanılan Puan Sonrası: {puan}")

    puan -= 20  # Oyuncu 20 puan kaybetti
    print(f"Kaybedilen Puan Sonrası: {puan}")
    ```

4.  **Karşılaştırma ve Mantıksal Operatörler**

    ```python
    # Bir öğrencinin dersten geçip geçmediğini kontrol etme
    vize_notu = 60
    final_notu = 75
    devam_durumu = True

    # Geçme notu 50 ve üzeri olmalı, devamsızlık yapmamış olmalı
    gecme_kosulu = (final_notu >= 50) and (devam_durumu == True)

    print(f"Öğrenci dersten geçti mi? {gecme_kosulu}")
    ```

5.  **Tip Dönüşümü ile Kullanıcı Girdisi İşleme**

    ```python
    # Kullanıcının doğum yılına göre yaşını hesaplama
    dogum_yili_str = input("Lütfen doğum yılınızı giriniz: ")

    # input() ile alınan string değeri integer'a çevirme
    dogum_yili = int(dogum_yili_str)
    guncel_yil = 2025

    yas = guncel_yil - dogum_yili
    print(f"Siz {yas} yaşındasınız.")
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** Kullanıcıdan alınan iki sayının toplamını, farkını, çarpımını ve bölümünü ekrana yazdıran bir program yazınız.
2.  **Kolay:** Yarıçapı verilen bir dairenin alanını ve çevresini hesaplayan programı yazınız. (Pi = 3.14 alınabilir).
3.  **Kolay:** Kullanıcıdan ismini ve yaşını alıp "Merhaba [isim], sen [yaş] yaşındasın." formatında bir çıktı veren program yazınız.
4.  **Kolay:** Bir ürünün KDV'siz fiyatı veriliyor. Bu ürünün %18 KDV'li fiyatını hesaplayan programı yazınız.
5.  **Kolay:** Girilen bir sayının tek mi çift mi olduğunu bulan programı yazınız. (Mod operatörü `%` kullanınız).
6.  **Orta:** Kullanıcıdan vize ve final notlarını alan ve vizenin %40'ı ile finalin %60'ını alarak yıl sonu ortalamasını hesaplayan bir program yazınız. Eğer ortalama 50'den büyük veya eşitse "Geçti", küçükse "Kaldı" yazdırınız.
7.  **Orta:** Girilen üç sayıdan en büyüğünü bulan programı yazınız.
8.  **Orta:** Bir çalışanın saatlik ücreti ve aylık çalışma saati bilgisi alınıyor. Aylık maaşını hesaplayan, ancak eğer aylık çalışma saati 160'tan fazlaysa, fazla olan her saat için %50 daha fazla ücret ödeyen bir program yazınız.
9.  **Orta:** Kullanıcının girdiği bir sayının pozitif, negatif veya sıfır olduğunu kontrol eden programı yazınız.
10. **Orta:** Vücut Kitle İndeksi (VKİ) hesaplayan bir program yazınız. Kullanıcıdan boy (metre cinsinden) ve kilo (kg cinsinden) bilgilerini alınız. VKİ = Kilo / (Boy * Boy) formülünü kullanarak sonucu hesaplayıp ekrana yazdırınız.


### 1.2. Giriş/Çıkış: input(), print(), formatlama

**Teorik İçerik (10-15 dakika)**

Python'da programlar ile dış dünya arasındaki iletişimi sağlayan temel mekanizmalar giriş ve çıkış fonksiyonlarıdır. Kullanıcıdan veri almak (giriş) ve kullanıcıya bilgi sunmak (çıkış) programların interaktif olmasını sağlar.

**Çıkış Fonksiyonu: `print()`**

`print()` fonksiyonu, belirtilen verileri standart çıktıya (genellikle terminal veya konsol ekranı) yazdırmak için kullanılır. Bu fonksiyon, içine yazılan string, sayı, değişken veya hatta karmaşık veri yapılarını ekranda gösterebilir.

*   **Birden Fazla Değeri Yazdırma:** `print()` fonksiyonuna virgülle ayrılmış birden fazla argüman verilebilir. Varsayılan olarak, bu argümanlar aralarında birer boşluk bırakılarak yazdırılır.
*   **`sep` ve `end` Parametreleri:**
    *   `sep` (separator): Birden fazla değer yazdırılırken aralarına konulacak ayırıcıyı belirler. Varsayılan değeri boşluktur (`' '`).
    *   `end`: `print()` fonksiyonu çalıştıktan sonra satırın sonuna eklenecek karakteri belirler. Varsayılan değeri yeni satır karakteridir (`'\n'`), bu yüzden her `print()` çağrısı çıktıyı yeni bir satıra yazar.

**Giriş Fonksiyonu: `input()`**

`input()` fonksiyonu, programın çalışmasını durdurarak kullanıcıdan klavye aracılığıyla bir veri girmesini bekler. Kullanıcı veriyi girip Enter tuşuna bastığında, girilen bu veri **her zaman string (`str`) tipinde** bir değer olarak programa döndürülür. Eğer bu veriyle matematiksel bir işlem yapılacaksa, mutlaka `int()` veya `float()` gibi fonksiyonlarla sayısal tipe dönüştürülmelidir.

**String Formatlama**

Çıktıları daha okunaklı ve düzenli hale getirmek için string formatlama yöntemleri kullanılır. Değişkenlerin değerlerini bir metin içinde dinamik olarak göstermemizi sağlarlar.

*   **f-string (Formatted String Literals):** Python 3.6 ve sonrasında gelen en modern ve kullanışlı yöntemdir. String'in başına `f` veya `F` harfi konularak kullanılır. Süslü parantezler `{}` içine doğrudan değişken isimleri yazılarak değerleri string'e eklenir.
*   **`str.format()` Metodu:** String'in içindeki süslü parantezlere, `.format()` metoduna verilen argümanlar sırasıyla veya isimlendirilerek yerleştirilir.
*   **`%` Operatörü:** Eski bir yöntem olmasına rağmen hala karşılaşılabilir. C dilindeki `printf` fonksiyonuna benzer bir kullanımı vardır.

---

**Syntax Örnekleri**

1.  **Temel `print()` ve `input()` Kullanımı**

    ```python
    # Kullanıcıya bir karşılama mesajı gösterme ve ismini sorma
    print("Merhaba, size nasıl hitap edebilirim?")
    isim = input("Lütfen isminizi giriniz: ")
    print(f"Hoş geldin, {isim}!")
    ```

2.  **`sep` ve `end` Parametrelerinin Kullanımı**

    ```python
    # Bir alışveriş listesini farklı formatlarda yazdırma
    urun1 = "Elma"
    urun2 = "Süt"
    urun3 = "Ekmek"

    # Virgülle ayrılmış liste
    print(urun1, urun2, urun3, sep=", ")

    # Aynı satırda tire ile ayrılmış liste
    print(urun1, urun2, urun3, sep=" - ", end="\nAlışveriş tamamlandı.")
    ```

3.  **f-string ile Dinamik Metin Oluşturma**

    ```python
    # Bir öğrencinin sınav sonuçlarını raporlama
    ogrenci_adi = "Ayşe"
    ders = "Matematik"
    puan = 85

    rapor = f"{ogrenci_adi} adlı öğrenci, {ders} dersinden {puan} almıştır."
    print(rapor)
    ```

4.  **`str.format()` Metodu ile Formatlama**

    ```python
    # Bir siparişin özetini oluşturma
    siparis_no = "12345XYZ"
    tutar = 150.99
    tarih = "07-12-2025"

    ozet = "Sipariş No: {}, Tarih: {}, Toplam Tutar: {:.2f} TL".format(siparis_no, tarih, tutar)
    print(ozet)
    ```

5.  **`input()` ile Sayısal Veri Alıp İşlem Yapma**

    ```python
    # Kullanıcıdan iki sayı alıp ortalamasını hesaplama
    sayi1_str = input("Birinci sayıyı giriniz: 
")
    sayi2_str = input("İkinci sayıyı giriniz: 
")

    # Girdileri float tipe dönüştürme
    ortalama = (float(sayi1_str) + float(sayi2_str)) / 2

    print(f"Girdiğiniz sayıların ortalaması: {ortalama}")
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** Kullanıcıdan adını, soyadını ve yaşını ayrı ayrı `input()` ile alan ve "Adı: [ad], Soyadı: [soyad], Yaşı: [yaş]" formatında tek bir `print()` fonksiyonu ile ekrana yazdıran programı yazınız.
2.  **Kolay:** Kullanıcıdan bir selamlama mesajı ve bir isim alan, bu iki metni birleştirip ekrana yazdıran programı yazınız.
3.  **Kolay:** Ekrana `print()` fonksiyonunu kullanarak üç farklı satırda en sevdiğiniz üç filmin adını yazdırınız.
4.  **Kolay:** Kullanıcıdan bir sayı girmesini isteyen ve girilen sayının karesini "Girdiğiniz sayının karesi: [sonuç]" formatında yazdıran programı yazınız.
5.  **Kolay:** `print()` fonksiyonunun `sep` parametresini kullanarak "Python", "öğrenmek", "çok", "eğlenceli" kelimelerini aralarında `*` olacak şekilde tek satırda yazdırınız.
6.  **Orta:** Bir marketin manav reyonu için basit bir hesap programı yazınız. Kullanıcıdan elma, muz ve çileğin kilogram fiyatlarını ve kaçar kilo aldığını ayrı ayrı girmesini isteyiniz. Toplam tutarı hesaplayıp f-string kullanarak "Toplam Borcunuz: XX.XX TL" formatında ekrana yazdırınız.
7.  **Orta:** Kullanıcıdan bir cümle girmesini isteyin. Cümlenin kaç karakterden oluştuğunu (`len()` fonksiyonu) ve cümlenin ilk ve son harfini ekrana formatlı bir şekilde yazdırın.
8.  **Orta:** `print()` fonksiyonunun `end` parametresini kullanarak, 1'den 5'e kadar olan sayıları aynı satırda, aralarında virgül olacak şekilde (`1,2,3,4,5`) yazdıran bir program yazınız.
9.  **Orta:** Kullanıcıdan bir Fahrenheit derecesi girmesini isteyen ve bunu Celsius derecesine çeviren bir program yazınız. Formül: C = (F - 32) * 5/9. Sonucu "XX Fahrenhayt, YY Santigrat derecedir." formatında yazdırınız.
10. **Orta:** Kullanıcıdan üç basamaklı bir sayı girmesini isteyin. Bu sayının basamaklarındaki rakamların toplamını bulan ve ekrana yazdıran bir program yazınız. (İpucu: String olarak alınan sayının her bir karakterine erişebilirsiniz.)

### 1.3. Kontrol Yapıları: if-else, elif, match-case

**Teorik İçerik (10-15 dakika)**

Kontrol yapıları, bir programın akışını belirli koşullara göre yönlendiren temel programlama unsurlarıdır. Kodun her zaman yukarıdan aşağıya doğru düz bir şekilde çalışması yerine, belirli durumlarda farklı kod bloklarının çalışmasını veya hiç çalışmamasını sağlarlar. Bu, programlara karar verme yeteneği kazandırır.

**`if` Yapısı**

`if` (eğer) ifadesi, en temel kontrol yapısıdır. Belirtilen bir koşulun `True` (doğru) olup olmadığını kontrol eder. Eğer koşul doğruysa, `if` bloğunun içindeki girintili kod çalıştırılır. Koşul `False` (yanlış) ise, bu blok atlanır.

```python
if koşul:
    # Koşul True ise bu blok çalışır
```

**`if-else` Yapısı**

`else` (değilse) ifadesi, bir `if` koşulu `False` olduğunda çalıştırılacak bir alternatif kod bloğu sunar. Bu yapı, bir koşulun doğru ve yanlış olma durumları için iki ayrı yol tanımlar.

```python
if koşul:
    # Koşul True ise bu blok çalışır
else:
    # Koşul False ise bu blok çalışır
```

**`if-elif-else` Yapısı**

`elif` (else if - değilse eğer) ifadesi, ikiden fazla olası durumu kontrol etmek için kullanılır. Program, ilk `if` koşulunu kontrol eder. Eğer `False` ise, sıradaki `elif` koşulunu kontrol eder ve bu şekilde devam eder. Herhangi bir `elif` koşulu `True` olduğunda, o blok çalıştırılır ve yapıdan çıkılır. Hiçbir `if` veya `elif` koşulu `True` olmazsa, en sondaki `else` bloğu çalıştırılır.

```python
if koşul_1:
    # Koşul 1 True ise çalışır
elif koşul_2:
    # Koşul 1 False ve Koşul 2 True ise çalışır
else:
    # Yukarıdaki hiçbir koşul True değilse çalışır
```

**`match-case` Yapısı (Python 3.10+)**

`match-case` yapısı, yapısal desen eşleştirme (structural pattern matching) sağlar. Özellikle bir değişkenin birden çok farklı olası değere veya yapıya sahip olabileceği durumlarda, karmaşık `if-elif-else` zincirlerine modern ve daha okunaklı bir alternatif sunar. Bir `switch-case` ifadesine benzer, ancak çok daha esnektir.

*   `match` ile kontrol edilecek değişken belirtilir.
*   `case` ile bu değişkenin eşleşebileceği desenler tanımlanır.
*   `case _:` (alt çizgi), hiçbir desenin eşleşmediği durumlar için varsayılan (default) durumu ifade eder.

---

**Syntax Örnekleri**

1.  **`if-else` ile Ehliyet Kontrolü**

    ```python
    # Kullanıcının yaşını alıp ehliyet alıp alamayacağını kontrol etme
    yas = int(input("Yaşınızı giriniz: "))

    if yas >= 18:
        print("Ehliyet alabilirsiniz.")
    else:
        kalan_yil = 18 - yas
        print(f"Ehliyet alamazsınız. {kalan_yil} yıl daha beklemeniz gerekiyor.")
    ```

2.  **`if-elif-else` ile Not Harf Karşılığı**

    ```python
    # Bir öğrencinin notuna göre harf notunu belirleme
    puan = int(input("Notunuzu giriniz (0-100): "))

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

    print(f"Harf notunuz: {harf_notu}")
    ```

3.  **İç İçe `if` ile Kullanıcı Girişi Kontrolü**

    ```python
    # Basit bir kullanıcı adı ve şifre kontrolü
    dogru_kullanici_adi = "admin"
    dogru_sifre = "12345"

    kullanici_adi = input("Kullanıcı adınız: ")
    sifre = input("Şifreniz: ")

    if kullanici_adi == dogru_kullanici_adi:
        if sifre == dogru_sifre:
            print("Giriş başarılı!")
        else:
            print("Şifre hatalı!")
    else:
        print("Kullanıcı adı bulunamadı!")
    ```

4.  **`match-case` ile Komut İşleme**

    ```python
    # Bir robotu yönlendirmek için verilen komutu işleme
    komut = input("Robota bir komut verin (ileri, geri, sağ, sol): ")

    match komut.lower():
        case "ileri":
            print("Robot ileri gidiyor.")
        case "geri":
            print("Robot geri gidiyor.")
        case "sağ":
            print("Robot sağa dönüyor.")
        case "sol":
            print("Robot sola dönüyor.")
        case _:
            print("Geçersiz komut!")
    ```

5.  **Mantıksal Operatörlerle `if` Kullanımı**

    ```python
    # Bir online mağazada indirim kuponu uygulama koşulu
    sepet_tutari = float(input("Sepet tutarınızı giriniz: "))
    kupon_kodu_var_mi = input("İndirim kuponunuz var mı? (evet/hayır): ").lower()

    # İndirim için sepet tutarı 100 TL üzerinde ve kuponu olmalı
    if sepet_tutari > 100 and kupon_kodu_var_mi == "evet":
        print("İndirim uygulandı! Yeni tutar: ", sepet_tutari * 0.9)
    else:
        print("İndirim koşulları sağlanamadı.")
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** Kullanıcıdan bir sayı alınız. Sayı 0'dan büyükse "Pozitif", küçükse "Negatif", eşitse "Sıfır" yazdırınız.
2.  **Kolay:** Kullanıcıdan bir gün numarası (1-7) alınız ve bu numaraya karşılık gelen günün adını (1: Pazartesi, 2: Salı, vb.) yazdırınız.
3.  **Kolay:** İki sayı alıp bu sayıların eşit olup olmadığını kontrol eden bir program yazınız.
4.  **Kolay:** Bir sinema için bilet fiyatı belirleyen bir program yazınız. 12 yaşından küçükler için 10 TL, diğer herkes için 20 TL bilet fiyatı uygulayınız.
5.  **Kolay:** Kullanıcıdan bir harf girmesini isteyin. Eğer harf sesli bir harf (a, e, i, o, u) ise "Sesli harf", değilse "Sessiz harf" yazdırın.
6.  **Orta:** Bir yılın artık yıl olup olmadığını kontrol eden bir program yazınız. Bir yıl, 4'e tam bölünüyorsa artık yıldır. Ancak, 100'e tam bölünen yıllardan sadece 400'e de tam bölünenler artık yıldır.
7.  **Orta:** Kullanıcıdan bir üçgenin üç kenar uzunluğunu alın. Bu kenarların bir üçgen oluşturup oluşturmadığını kontrol edin (Herhangi iki kenarın toplamı üçüncü kenardan büyük olmalıdır). Eğer üçgen oluşturuyorsa, üçgenin eşkenar, ikizkenar veya çeşitkenar olduğunu belirtin.
8.  **Orta:** Bir restoranda hesap ödeme sistemi için bir program yazın. Kullanıcıdan hesap tutarını ve bahşiş yüzdesini (%10, %15, %20 gibi) alın. Toplam ödenecek tutarı hesaplayıp yazdırın. Eğer geçersiz bir bahşiş yüzdesi girilirse, varsayılan olarak %15 uygulayın.
9.  **Orta:** `match-case` yapısını kullanarak basit bir hesap makinesi yapın. Kullanıcıdan iki sayı ve bir işlem (`+`, `-`, `*`, `/`) alın. Seçilen işleme göre sonucu hesaplayıp ekrana yazdırın. Geçersiz işlem girilirse hata mesajı verin.
10. **Orta:** Bir kargo şirketinin ücretlendirme sistemini yazın. Paketin ağırlığına göre fiyat belirleyin: 0-2 kg arası 15 TL, 2-5 kg arası 25 TL, 5-10 kg arası 40 TL, 10 kg üzeri için "Ağır kargo, özel taşıma gerekir" mesajı verin.

### 1.4. Döngüler: for, while, break, continue

**Teorik İçerik (10-15 dakika)**

Döngüler, bir kod bloğunu belirli bir koşul sağlandığı sürece veya bir veri koleksiyonundaki her bir eleman için tekrar tekrar çalıştırmamızı sağlayan yapılardır. Programlamada tekrar eden görevleri otomatikleştirmek için vazgeçilmezdirler.

**`for` Döngüsü**

`for` döngüsü, "yinelemeli" (iterable) nesneler üzerinde gezinmek için kullanılır. Yinelemeli nesneler, elemanları tek tek dolaşılabilen veri yapılarıdır. Bunlara örnek olarak listeler, demetler (tuple), stringler ve `range()` fonksiyonu ile oluşturulan sayı dizileri verilebilir.

`for` döngüsü, koleksiyondaki her bir elemanı sırayla geçici bir değişkene atar ve döngü bloğundaki kodları o eleman için çalıştırır. Koleksiyondaki tüm elemanlar bittiğinde döngü sona erer.

```python
for eleman in koleksiyon:
    # Her bir 'eleman' için bu blok çalışır
```

**`while` Döngüsü**

`while` (olduğu sürece) döngüsü, başlangıçta belirtilen bir koşul `True` olduğu müddetçe çalışmaya devam eder. Koşul `False` değerini aldığında döngü durur.

`while` döngüsü kullanırken dikkat edilmesi gereken en önemli nokta, döngü içinde koşulu değiştirecek bir mekanizma kurmaktır. Aksi takdirde, koşul her zaman `True` kalır ve **sonsuz döngü** (infinite loop) oluşur. Bu genellikle bir sayaç değişkeninin değerini döngü içinde artırmak veya azaltmakla sağlanır.

```python
while koşul:
    # Koşul True olduğu sürece bu blok çalışır
    # Koşulu değiştirecek bir ifade (örn: sayaç artırımı)
```

**Döngü Kontrol İfadeleri**

Bazen bir döngünün normal akışını değiştirmek isteyebiliriz. Bunun için `break` ve `continue` ifadeleri kullanılır.

*   **`break`:** Karşılaşıldığı anda içinde bulunduğu döngüyü tamamen sonlandırır. Programın çalışması döngüden sonraki ilk satırdan devam eder. Genellikle bir arama işleminde istenen eleman bulunduğunda döngüyü gereksiz yere devam ettirmemek için kullanılır.

*   **`continue`:** Karşılaşıldığı anda döngünün o anki turunu (iteration) atlar. Döngü bloğunun geri kalan kodları çalıştırılmaz ve döngü bir sonraki eleman veya bir sonraki koşul kontrolü ile devam eder. Genellikle belirli bir koşulu sağlayan elemanları es geçmek için kullanılır.

---

**Syntax Örnekleri**

1.  **`for` ve `range()` ile Sayı Dizisi Üzerinde Gezinme**

    ```python
    # Bir roketin fırlatılması için 10'dan geriye sayım
    print("Geri sayım başlıyor...")
    for sayi in range(10, 0, -1):
        print(sayi)
    print("Fırlat!")
    ```

2.  **`for` ile Liste Elemanlarını İşleme**

    ```python
    # Bir alışveriş listesindeki ürünleri ekrana yazdırma
    alisveris_listesi = ["Elma", "Süt", "Ekmek", "Peynir"]

    print("Alınacaklar:")
    for urun in alisveris_listesi:
        print(f"- {urun}")
    ```

3.  **`while` ile Koşullu Tekrar (Sayı Tahmin Oyunu)**

    ```python
    # Bilgisayarın tuttuğu sayıyı kullanıcının tahmin etmesi
    import random
    tutulan_sayi = random.randint(1, 20)
    tahmin = 0

    while tahmin != tutulan_sayi:
        tahmin = int(input("1-20 arası bir sayı tahmin edin: "))
        if tahmin < tutulan_sayi:
            print("Daha yüksek bir sayı söyleyin.")
        elif tahmin > tutulan_sayi:
            print("Daha düşük bir sayı söyleyin.")

    print(f"Tebrikler! Doğru sayıyı ({tutulan_sayi}) buldunuz.")
    ```

4.  **`break` ile Döngüyü Kırma**

    ```python
    # Bir listede belirli bir meyveyi arama
    meyveler = ["elma", "muz", "kiraz", "portakal", "çilek"]

    for meyve in meyveler:
        print(f"{meyve} kontrol ediliyor...")
        if meyve == "portakal":
            print("Portakal bulundu!")
            break  # Döngüyü sonlandır
    ```

5.  **`continue` ile Turu Atlama**

    ```python
    # Bir listedeki negatif sayıları atlayarak sadece pozitifleri toplama
    sayilar = [10, 20, -5, 30, -15, 40]
    toplam = 0

    for sayi in sayilar:
        if sayi < 0:
            continue  # Negatifse bu turu atla, toplama ekleme
        toplam += sayi

    print(f"Pozitif sayıların toplamı: {toplam}")
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** 1'den 100'e kadar olan tüm sayıları ekrana yazdıran bir `for` döngüsü yazınız.
2.  **Kolay:** 1'den 100'e kadar olan çift sayıları ekrana yazdıran bir `for` döngüsü ve `if` koşulu kullanarak bir program yazınız.
3.  **Kolay:** Kullanıcıdan bir kelime alın ve `for` döngüsü kullanarak o kelimenin her harfini alt alta yazdırın.
4.  **Kolay:** `while` döngüsü kullanarak 1'den 10'a kadar olan sayıların toplamını bulan bir program yazınız.
5.  **Kolay:** Bir listenin (örneğin `[1, 2, 3, 4, 5]`) elemanlarının karesini alıp yeni bir listeye ekleyen ve bu yeni listeyi ekrana yazdıran bir program yazınız.
6.  **Orta:** Kullanıcıdan bir sayı alın ve bu sayının faktöriyelini hesaplayan bir program yazınız. (Örneğin, 5! = 5 * 4 * 3 * 2 * 1 = 120).
7.  **Orta:** 1'den 100'e kadar olan sayılardan hem 3'e hem de 5'e tam bölünenleri (yani 15'in katlarını) bulan ve ekrana yazdıran bir program yazınız.
8.  **Orta:** Kullanıcıdan sürekli sayı girmesini isteyen, kullanıcı 'q' harfine bastığında ise girişi durduran ve o ana kadar girilen sayıların ortalamasını hesaplayan bir program yazınız. (`break` kullanınız).
9.  **Orta:** Çarpım tablosunu (1'den 10'a kadar) ekrana güzel bir formatta yazdıran iç içe `for` döngüleri içeren bir program yazınız.
10. **Orta:** Asal sayı bulma programı yazınız. Kullanıcıdan bir sayı alın ve bu sayının asal olup olmadığını `for` döngüsü ve `break` kullanarak kontrol edin. (Bir sayı sadece 1'e ve kendisine tam bölünüyorsa asaldır).

### 1.5. Veri Yapıları: String, List, Tuple, Dictionary

**Teorik İçerik (15-20 dakika)**

Veri yapıları, birden çok veri parçasını organize bir şekilde bir arada tutmak ve yönetmek için kullanılan programlama araçlarıdır. Python, güçlü ve esnek yerleşik veri yapıları sunar.

**String (`str`)**

Stringler, karakter dizileridir ve metinsel verileri temsil eder. Tırnak işaretleri (`'`, `"`, `'''`, `"""`) içinde oluşturulurlar. Stringler **değiştirilemez (immutable)** veri tipleridir, yani bir string oluşturulduktan sonra içeriğindeki tek bir karakter doğrudan değiştirilemez. Ancak, string metodları kullanılarak yeni stringler türetilebilir.

*   **İndeksleme ve Dilimleme (Slicing):** Karakterlere `[]` operatörü ile erişilir. `[0]` ilk karakteri, `[-1]` son karakteri verir. `[start:stop:step]` ile belirli bir aralık alınabilir.
*   **Temel Metodlar:** `len()`, `lower()`, `upper()`, `strip()`, `split()`, `replace()`, `find()`.

**Liste (`list`)**

Listeler, farklı veri tiplerinden elemanları bir arada tutabilen, sıralı ve **değiştirilebilir (mutable)** koleksiyonlardır. Köşeli parantezler `[]` içinde, elemanlar virgülle ayrılarak tanımlanırlar.

*   **Eleman Ekleme/Çıkarma:** `append()` (sona ekler), `insert()` (belirtilen indekse ekler), `remove()` (değere göre siler), `pop()` (indekse göre siler ve değeri döndürür).
*   **Sıralama ve Ters Çevirme:** `sort()` (yerinde sıralar), `reverse()` (yerinde ters çevirir).
*   **İndeksleme ve Dilimleme:** Stringlerde olduğu gibi çalışır.

**Demet (`tuple`)**

Demetler, listelere çok benzerler; sıralı koleksiyonlardır. Ancak en önemli farkları, **değiştirilemez (immutable)** olmalarıdır. Bir demet oluşturulduktan sonra elemanları eklenemez, silinemez veya değiştirilemez. Normal parantezler `()` içinde tanımlanırlar. Performans açısından listelerden biraz daha hızlıdırlar ve içeriğinin değişmemesi gereken verileri (örneğin, koordinat bilgileri, ay isimleri) saklamak için idealdirler.

**Sözlük (`dict`)**

Sözlükler, **anahtar-değer (key-value)** çiftlerinden oluşan, sırasız (Python 3.7+ itibarıyla sıralı) ve **değiştirilebilir (mutable)** koleksiyonlardır. Her bir değere, o değere özel olan benzersiz bir anahtar üzerinden erişilir. Süslü parantezler `{}` içinde `{anahtar: değer}` şeklinde tanımlanırlar.

*   **Erişim, Ekleme, Güncelleme:** `sozluk[anahtar]` ile değere erişilir. Eğer anahtar yoksa ve bu şekilde bir atama yapılırsa yeni bir anahtar-değer çifti eklenir. Var olan bir anahtara atama yapılırsa değer güncellenir.
*   **Eleman Silme:** `del sozluk[anahtar]` veya `pop()` metodu ile eleman silinir.
*   **Temel Metodlar:** `keys()` (anahtarları döner), `values()` (değerleri döner), `items()` (anahtar-değer çiftlerini döner).

---

**Syntax Örnekleri**

1.  **String Dilimleme ve Metodları**

    ```python
    # Bir e-posta adresini analiz etme
    email = "  kullanici.adi@example.com  "

    # Başındaki ve sonundaki boşlukları temizle
    temiz_email = email.strip()
    print(f"Temizlenmiş E-posta: {temiz_email}")

    # Kullanıcı adını ve domaini ayır
    kullanici_adi = temiz_email.split('@')[0]
    domain = temiz_email.split('@')[1]
    print(f"Kullanıcı Adı: {kullanici_adi}, Domain: {domain}")
    ```

2.  **Liste Manipülasyonu (Yapılacaklar Listesi)**

    ```python
    # Basit bir yapılacaklar listesi uygulaması
    yapilacaklar = ["Markete git", "Ödevleri yap"]
    print(f"Liste: {yapilacaklar}")

    yapilacaklar.append("Spor yap") # Yeni görev ekle
    print(f"Yeni görev eklendi: {yapilacaklar}")

    yapilacaklar.remove("Ödevleri yap") # Bir görevi tamamla
    print(f"Görev tamamlandı: {yapilacaklar}")

    yapilacaklar.sort() # Listeyi alfabetik sırala
    print(f"Sıralanmış liste: {yapilacaklar}")
    ```

3.  **Tuple Kullanımı (Sabit Veri Saklama)**

    ```python
    # Bir noktanın 2D koordinatlarını saklama
    nokta = (150, 250) # x ve y koordinatları

    # Tuple unpacking
    x, y = nokta

    print(f"Noktanın X koordinatı: {x}")
    print(f"Noktanın Y koordinatı: {y}")

    # Değiştirmeye çalışınca hata verir: nokta[0] = 100 -> TypeError
    ```

4.  **Sözlük ile Veri Modelleme (Kişi Bilgileri)**

    ```python
    # Bir kişi hakkındaki bilgileri sözlükte tutma
    kisi = {
        "ad": "Ali",
        "soyad": "Veli",
        "yas": 30,
        "meslek": "Mühendis"
    }

    print(f"{kisi['ad']} {kisi['soyad']}, {kisi['yas']} yaşında bir {kisi['meslek']}.")

    # Yeni bir bilgi ekleme
    kisi["sehir"] = "İstanbul"
    print(f"Kişinin yaşadığı şehir: {kisi['sehir']}")

    # Bir bilgiyi güncelleme
    kisi["yas"] += 1
    print(f"Kişinin yeni yaşı: {kisi['yas']}")
    ```

5.  **Sözlük Üzerinde `for` Döngüsü**

    ```python
    # Bir ürün envanterindeki ürünleri ve stok miktarlarını listeleme
    envanter = {"elma": 50, "muz": 30, "portakal": 45}

    print("--- Ürün Stok Durumu ---")
    for urun, stok in envanter.items():
        print(f"{urun.capitalize()}: {stok} adet")
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** Kullanıcıdan bir cümle alın ve cümlenin kaç kelimeden oluştuğunu `split()` metodu ile bulun.
2.  **Kolay:** Bir liste oluşturun (`[1, 2, 3, 4, 5]`). `for` döngüsü kullanarak bu listenin elemanlarının toplamını bulun.
3.  **Kolay:** Bir sözlük oluşturun (`{"ad": "Zeynep", "yas": 25}`). Bu sözlüğün anahtarlarını ve değerlerini ayrı ayrı ekrana yazdırın.
4.  **Kolay:** Bir string'i (`"Python"`) `for` döngüsü ile tersten yazdıran bir program yazın. (İpucu: Dilimleme `[::-1]`)
5.  **Kolay:** Beş favori meyvenizi içeren bir tuple oluşturun ve bu tuple'ın ikinci elemanını ekrana yazdırın.
6.  **Orta:** Bir listedeki tekrar eden elemanları kaldıran ve yeni bir liste olarak döndüren bir program yazınız. (Örn: `[1, 2, 2, 3, 4, 4, 5]` -> `[1, 2, 3, 4, 5]`)
7.  **Orta:** Bir metin içindeki sesli harflerin sayısını bulan bir program yazınız. (Metni `for` ile gezip her harfi kontrol edebilirsiniz).
8.  **Orta:** Öğrenci notlarını saklayan bir sözlük yapısı oluşturun. `{ "Ahmet": 85, "Ayşe": 92, "Mehmet": 78 }`. Bu sözlükteki en yüksek notu alan öğrenciyi ve notunu bulun.
9.  **Orta:** İki listeyi birleştirip tek bir sıralı liste haline getiren bir program yazınız. (Örn: `[1, 3, 5]` ve `[2, 4, 6]` -> `[1, 2, 3, 4, 5, 6]`)
10. **Orta:** Basit bir telefon rehberi uygulaması yapın. Kullanıcıya 3 seçenek sunun: 1-Kişi Ekle, 2-Kişi Ara, 3-Çıkış. Kişileri bir sözlükte `{isim: telefon_no}` şeklinde saklayın. Kullanıcı seçimlerine göre ilgili işlemleri yapın.

### 1.6. Fonksiyonlar: Tanımlama, Parametreler, lambda, decorator, recursive

**Teorik İçerik (15-20 dakika)**

Fonksiyonlar, belirli bir görevi yerine getirmek için tasarlanmış, yeniden kullanılabilir kod bloklarıdır. Kod tekrarını önler, programları daha modüler, organize ve okunabilir hale getirirler. Bir kez yazılan bir fonksiyon, programın farklı yerlerinde defalarca çağrılabilir.

**Fonksiyon Tanımlama ve Çağırma**

Python'da bir fonksiyon, `def` anahtar kelimesi ile tanımlanır. Fonksiyon adını, parantez içinde alacağı parametreleri ve iki nokta üst üsteyi takip eden girintili bir kod bloğunu içerir.

```python
def fonksiyon_adi(parametre1, parametre2):
    # Fonksiyonun yapacağı işlemler
    return sonuc # İsteğe bağlı
```

Bir fonksiyonu çalıştırmak için adı ve gerekli argümanlar ile çağrılır: `fonksiyon_adi(deger1, deger2)`.

**Parametreler ve Argümanlar**

*   **Parametre:** Fonksiyon tanımında belirtilen değişken adıdır.
*   **Argüman:** Fonksiyon çağrılırken parametrelere atanan gerçek değerdir.
*   **Varsayılan Değerli Parametreler:** Fonksiyon tanımlanırken bir parametreye varsayılan bir değer atanabilir. Eğer fonksiyon çağrılırken bu parametre için bir argüman verilmezse, varsayılan değer kullanılır.
*   **`*args` ve `**kwargs`:**
    *   `*args`: Fonksiyona belirsiz sayıda pozisyonel argüman gönderilmesini sağlar. Bu argümanlar fonksiyon içinde bir **tuple** olarak tutulur.
    *   `**kwargs`: Fonksiyona belirsiz sayıda anahtar kelimeli argüman gönderilmesini sağlar. Bu argümanlar fonksiyon içinde bir **sözlük** olarak tutulur.

**`return` İfadesi**

`return` ifadesi, bir fonksiyonun çalışmasını sonlandırır ve bir değer döndürür. Bu değer, fonksiyonun çağrıldığı yerde kullanılabilir. Bir fonksiyon `return` ifadesi içermiyorsa, varsayılan olarak `None` değerini döndürür.

**Lambda Fonksiyonları**

Lambda fonksiyonları, `lambda` anahtar kelimesi ile oluşturulan küçük, isimsiz (anonim) fonksiyonlardır. Genellikle tek bir ifade içeren ve kısa süreliğine ihtiyaç duyulan fonksiyonlar için kullanılırlar. `map()`, `filter()` gibi fonksiyonlarla birlikte sıkça kullanılırlar.

`lambda argümanlar: ifade`

**Decorator (Dekoratör) Fonksiyonlar**

Dekoratörler, mevcut bir fonksiyonun kodunu değiştirmeden ona yeni özellikler eklememizi sağlayan özel fonksiyonlardır. Bir fonksiyonu argüman olarak alıp, genişletilmiş yeni bir fonksiyon döndürürler. Genellikle `@` sembolü ile kullanılırlar. Örneğin, bir fonksiyonun çalışma süresini ölçmek, kullanıcı girişi kontrolü yapmak gibi görevler için idealdirler.

**Recursive (Özyinelemeli) Fonksiyonlar**

Recursive fonksiyon, kendi kendini çağıran bir fonksiyondur. Karmaşık problemleri daha küçük ve benzer alt problemlere bölerek çözer. Her recursive fonksiyonun bir **temel durum (base case)** içermesi gerekir. Bu durum, fonksiyonun kendi kendini çağırmayı durduracağı ve bir sonuç döndüreceği koşuldur. Aksi takdirde sonsuz bir döngüye girer.

---

**Syntax Örnekleri**

1.  **Basit Fonksiyon Tanımlama ve Çağırma**

    ```python
    # İki sayıyı toplayıp sonucu döndüren bir fonksiyon
    def topla(sayi1, sayi2):
        """Bu fonksiyon verilen iki sayıyı toplar."""
        return sayi1 + sayi2

    # Fonksiyonu çağırma
    sonuc = topla(15, 25)
    print(f"Toplam: {sonuc}")
    ```

2.  **Varsayılan Değerli Parametre Kullanımı**

    ```python
    # Bir kişiyi selamlayan, ülke belirtilmezse Türkiye varsayan fonksiyon
    def selamla(isim, ulke="Türkiye"):
        print(f"Merhaba {isim}, {ulke} ülkesinden misiniz?")

    selamla("Ahmet")
    selamla("John", "ABD")
    ```

3.  **`lambda` ile Kısa Fonksiyon**

    ```python
    # Bir sayının karesini alan bir lambda fonksiyonu
    karesini_al = lambda x: x * x

    print(f"5'in karesi: {karesini_al(5)}")

    # filter() ile kullanımı: Sadece çift sayıları filtreleme
    sayilar = [1, 2, 3, 4, 5, 6, 7, 8]
    cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
    print(f"Çift sayılar: {cift_sayilar}")
    ```

4.  **Decorator ile Fonksiyonun Çalışma Süresini Ölçme**

    ```python
    import time

    def zaman_olc(fonk):
        def wrapper(*args, **kwargs):
            baslangic = time.time()
            sonuc = fonk(*args, **kwargs)
            bitis = time.time()
            print(f"{fonk.__name__} fonksiyonu {bitis - baslangic:.4f} saniyede çalıştı.")
            return sonuc
        return wrapper

    @zaman_olc
    def buyuk_bir_islem():
        # Zaman alacak bir işlem simülasyonu
        sum([i**2 for i in range(1000000)])

    buyuk_bir_islem()
    ```

5.  **Recursive Fonksiyon ile Faktöriyel Hesaplama**

    ```python
    # Faktöriyeli özyinelemeli olarak hesaplama
    def faktoriyel(n):
        # Temel durum: n, 0 veya 1 ise 1 döndür
        if n == 0 or n == 1:
            return 1
        # Recursive adım: n * (n-1)!
        else:
            return n * faktoriyel(n - 1)

    sayi = 5
    print(f"{sayi}! = {faktoriyel(sayi)}")
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** Adı `dikdortgen_alan` olan ve iki parametre (kısa_kenar, uzun_kenar) alıp bu dikdörtgenin alanını döndüren bir fonksiyon yazınız.
2.  **Kolay:** Bir liste alan ve listenin en büyük elemanını döndüren `en_buyugu_bul` adında bir fonksiyon yazınız. (Yerleşik `max()` fonksiyonunu kullanmadan `for` döngüsü ile yapınız).
3.  **Kolay:** Bir string parametre alan ve bu string'i tersten döndüren `ters_cevir` adında bir fonksiyon yazınız.
4.  **Kolay:** `lambda` kullanarak, verilen bir sayının 10'dan büyük olup olmadığını kontrol eden (`True`/`False` döndüren) bir fonksiyon oluşturun.
5.  **Kolay:** Bir sayının çift mi tek mi olduğunu kontrol eden `cift_mi` adında bir fonksiyon yazınız. Fonksiyon, sayı çift ise `True`, tek ise `False` döndürmelidir.
6.  **Orta:** Bir liste ve bir eleman alan, elemanın listede kaç kez geçtiğini sayan `frekans_bul` adında bir fonksiyon yazınız. (Yerleşik `.count()` metodunu kullanmadan yapınız).
7.  **Orta:** Fibonacci serisinin n-inci elemanını bulan recursive bir fonksiyon yazınız. (Fibonacci serisi: 0, 1, 1, 2, 3, 5, 8, ... Her sayı kendinden önceki iki sayının toplamıdır).
8.  **Orta:** Bir cümlenin içindeki kelimeleri ters sırada yazdıran bir fonksiyon yazınız. (Örn: "Merhaba dünya bu ben" -> "ben bu dünya Merhaba").
9.  **Orta:** Bir decorator yazarak, bir fonksiyon çağrıldığında "[Fonksiyon Adı] çalıştırıldı." mesajını ve bittiğinde "[Fonksiyon Adı] tamamlandı." mesajını yazdırın.
10. **Orta:** `*args` kullanarak, fonksiyona gönderilen tüm sayıların toplamını hesaplayan `toplam` adında bir fonksiyon yazınız.

## 2. Nesne Yönelimli Programlama (OOP)

### 2.1. Sınıfların ve Nesnelerin Temelleri

**Teorik İçerik (15-20 dakika)**

**Nesne Yönelimli Programlama (OOP)**, programları "nesneler" etrafında organize eden bir programlama paradigmalarıdır. Bu nesneler, hem veri (nitelikler - attributes) hem de bu veriler üzerinde işlem yapan davranışları (metotlar - methods) bir arada tutar. OOP, gerçek dünyadaki nesneleri ve onların etkileşimlerini bilgisayar ortamında modellemeyi amaçlar. Bu yaklaşım, büyük ve karmaşık programları daha yönetilebilir, modüler ve yeniden kullanılabilir hale getirir.

**Neden OOP Kullanırız?**

*   **Modülerlik:** Her nesne kendi içinde bağımsız bir birimdir. Bu, programın parçalara ayrılmasını ve her parçanın ayrı ayrı geliştirilip test edilmesini kolaylaştırır.
*   **Yeniden Kullanılabilirlik:** Bir kez oluşturulan bir sınıf (class), farklı projelerde veya projenin farklı yerlerinde yeni nesneler yaratmak için tekrar tekrar kullanılabilir (örneğin, Kalıtım yoluyla).
*   **Bakım ve Yönetim Kolaylığı:** Kod, nesneler etrafında organize edildiği için hataları bulmak ve düzeltmek (debugging) veya yeni özellikler eklemek daha kolaydır.
*   **Soyutlama:** Karmaşık sistemlerin iç detaylarını gizleyerek sadece gerekli bilgileri sunar.

**Class ve Object Kavramları**

*   **Sınıf (`class`):** Bir nesnenin nasıl olacağını tanımlayan bir şablon veya prototiptir. Hangi niteliklere (attributes) ve metotlara (methods) sahip olacağını belirler. Örneğin, bir `Araba` sınıfı, `renk`, `model`, `hiz` gibi niteliklere ve `hizlan()`, `yavasla()` gibi metotlara sahip olabilir.

*   **Nesne (`object` veya `instance`):** Bir sınıftan oluşturulmuş somut bir örnektir. `Araba` sınıfından oluşturulan "kırmızı bir Ford Focus" bir nesnedir. Her nesne, sınıf tanımında belirtilen niteliklere ve metotlara sahiptir, ancak niteliklerin değerleri (örneğin, rengi, modeli) nesneye özgü olabilir.

**Temel Yapı Taşları**

*   **`class` Anahtar Kelimesi:** Python'da bir sınıf tanımlamak için kullanılır.
*   **`__init__()` Metodu:** Bu özel metot, bir sınıftan yeni bir nesne oluşturulduğunda otomatik olarak çağrılan "yapıcı" (constructor) metottur. Nesnenin başlangıç durumunu ayarlamak ve niteliklerine ilk değerleri atamak için kullanılır.
*   **`self` Parametresi:** Sınıf içindeki metotların ilk parametresi her zaman `self` olmalıdır. `self`, oluşturulan nesnenin kendisini temsil eder. Metotlar içinde nesnenin diğer niteliklerine ve metotlarına erişmek için `self.nitelik_adi` şeklinde kullanılır.
*   **Nitelikler (Attributes):**
    *   **Instance Attributes (Örnek Nitelikleri):** Her bir nesneye özgü olan niteliklerdir. Genellikle `__init__()` içinde `self.nitelik = deger` şeklinde tanımlanırlar.
    *   **Class Attributes (Sınıf Nitelikleri):** O sınıftan oluşturulan tüm nesneler tarafından paylaşılan ortak niteliklerdir. Sınıf tanımının hemen altında tanımlanırlar.

---

**Syntax Örnekleri**

1.  **Basit Bir `Kopek` Sınıfı Oluşturma**

    ```python
    class Kopek:
        # Class Attribute
        tur = "Canis lupus familiaris"

        def __init__(self, isim, yas):
            # Instance Attributes
            self.isim = isim
            self.yas = yas

        # Instance Method
        def havla(self):
            return "Hav hav!"

    # Nesne (instance) oluşturma
    kopek1 = Kopek("Karabaş", 3)
    kopek2 = Kopek("Fındık", 5)

    print(f"{kopek1.isim}, {kopek1.yas} yaşında bir köpek. Türü: {kopek1.tur}")
    print(f"{kopek2.isim} diyor ki: {kopek2.havla()}")
    ```

2.  **Bir `BankaHesabi` Sınıfı**

    ```python
    class BankaHesabi:
        def __init__(self, hesap_sahibi, baslangic_bakiye=0):
            self.hesap_sahibi = hesap_sahibi
            self.bakiye = baslangic_bakiye

        def para_yatir(self, miktar):
            if miktar > 0:
                self.bakiye += miktar
                print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

        def para_cek(self, miktar):
            if 0 < miktar <= self.bakiye:
                self.bakiye -= miktar
                print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")
            else:
                print("Yetersiz bakiye veya geçersiz miktar!")

    hesap = BankaHesabi("Ali Yılmaz", 500)
    hesap.para_yatir(250)
    hesap.para_cek(100)
    hesap.para_cek(800)
    ```

3.  **Bir `Kitap` Sınıfı ve Bilgileri**

    ```python
    class Kitap:
        def __init__(self, ad, yazar, sayfa_sayisi):
            self.ad = ad
            self.yazar = yazar
            self.sayfa_sayisi = sayfa_sayisi

        def bilgi_ver(self):
            return f"'{self.ad}' adlı kitap, {self.yazar} tarafından yazılmıştır ve {self.sayfa_sayisi} sayfadır."

    kitap1 = Kitap("Sefiller", "Victor Hugo", 1500)
    print(kitap1.bilgi_ver())
    ```

4.  **Bir `Ogrenci` Sınıfı ve Not Ortalaması**

    ```python
    class Ogrenci:
        def __init__(self, ad, soyad):
            self.ad = ad
            self.soyad = soyad
            self.notlar = []

        def not_ekle(self, notu):
            self.notlar.append(notu)

        def ortalama_hesapla(self):
            if not self.notlar:
                return 0
            return sum(self.notlar) / len(self.notlar)

    ogr1 = Ogrenci("Ayşe", "Kaya")
    ogr1.not_ekle(80)
    ogr1.not_ekle(90)
    ogr1.not_ekle(85)
    print(f"{ogr1.ad} adlı öğrencinin not ortalaması: {ogr1.ortalama_hesapla():.2f}")
    ```

5.  **Class ve Instance Attribute Farkı**

    ```python
    class Oyuncu:
        # Class attribute: Tüm oyuncular için ortak
        takim = "Galaksi Savaşçıları"

        def __init__(self, kullanici_adi):
            # Instance attribute: Her oyuncuya özel
            self.kullanici_adi = kullanici_adi

    oyuncu1 = Oyuncu("Alfa")
    oyuncu2 = Oyuncu("Beta")

    print(f"{oyuncu1.kullanici_adi} -> Takım: {oyuncu1.takim}")
    print(f"{oyuncu2.kullanici_adi} -> Takım: {oyuncu2.takim}")

    # Class attribute'u değiştirmek tüm nesneleri etkiler
    Oyuncu.takim = "Evren Koruyucuları"
    print(f"\nTakım adı değişti!\n{oyuncu1.kullanici_adi} -> Yeni Takım: {oyuncu1.takim}")
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** `ad`, `model`, `uretim_yili` niteliklerine ve `bilgileri_goster()` metoduna sahip bir `Araba` sınıfı oluşturun. Bu sınıftan bir nesne yaratıp bilgilerini ekrana yazdırın.
2.  **Kolay:** `x` ve `y` koordinatlarını tutan bir `Nokta` sınıfı oluşturun. Bu sınıftan iki farklı nokta nesnesi oluşturun.
3.  **Kolay:** `ad`, `fiyat` niteliklerine sahip bir `Urun` sınıfı oluşturun. `fiyat_guncelle(yeni_fiyat)` adında bir metot ekleyin. Bir ürün nesnesi oluşturup fiyatını güncelleyin ve yeni fiyatı yazdırın.
4.  **Kolay:** `baslik` ve `icerik` niteliklerine sahip bir `NotDefteri` sınıfı oluşturun. Bir not nesnesi oluşturup başlığını ve içeriğini ekrana yazdırın.
5.  **Kolay:** Bir `Kedi` sınıfı oluşturun. `__init__` metodunda kedinin `ad`'ını alsın ve `miyavla()` adında bir metodu olsun. Bu metot "[Kedi Adı] miyavlıyor..." şeklinde bir çıktı versin.
6.  **Orta:** Bir `Daire` sınıfı oluşturun. `__init__` metodu yarıçap (`radius`) bilgisini alsın. `alan_hesapla()` ve `cevre_hesapla()` adında iki metot ekleyin. (Pi = 3.14)
7.  **Orta:** Bir `Calisan` sınıfı oluşturun. `ad`, `soyad`, `maas` nitelikleri olsun. `maas_arttir(yuzde)` adında bir metot ekleyin. Bu metot, maaşı belirtilen yüzde oranında artırsın.
8.  **Orta:** Bir `Film` sınıfı oluşturun. `ad`, `yonetmen`, `sure_dk` nitelikleri olsun. `__init__` içinde bu değerleri alsın. Ayrıca, filmin kaç saat kaç dakika sürdüğünü hesaplayıp "X saat Y dakika" formatında döndüren `sureyi_formatla()` adında bir metot yazın.
9.  **Orta:** Bir `Sepet` sınıfı oluşturun. Bu sınıfın `urunler` adında boş bir listesi olsun. `urun_ekle(urun_adi, fiyat)` ve `toplam_tutari_goster()` metotları ekleyin. `urun_ekle` metodu, ürünleri bir sözlük (`{"ad": urun_adi, "fiyat": fiyat}`) olarak listeye eklesin. `toplam_tutari_goster` ise sepetteki tüm ürünlerin fiyatlarını toplayıp döndürsün.
10. **Orta:** Bir `Zamanlayici` sınıfı oluşturun. `saniye` niteliği olsun. `baslat()` metodu, belirtilen saniye kadar geriye saysın ve her saniyede ekrana kalan süreyi yazdırsın. Süre bitince "Süre doldu!" mesajı versin. (`time.sleep(1)` kullanabilirsiniz.)

### 2.2. Kapsülleme (Encapsulation)

**Teorik İçerik (15-20 dakika)**

**Kapsülleme (Encapsulation)**, nesne yönelimli programlamanın temel prensiplerinden biridir. Bir nesnenin verilerini (nitelikler) ve bu veriler üzerinde işlem yapan metotları tek bir birim (sınıf) içinde bir araya getirme ve verilerin dışarıdan doğrudan erişime karşı korunması fikrine dayanır. Amaç, nesnenin iç yapısını ve uygulama detaylarını gizleyerek, verilere sadece sınıfın kendi metotları aracılığıyla kontrollü bir şekilde erişilmesini sağlamaktır.

Bu prensip, bir ilacın kapsülüne benzetilebilir. Kapsül, içindeki etken maddeleri dış etkenlerden korur ve ilacın doğru şekilde çalışmasını sağlar. Benzer şekilde, kapsülleme de bir nesnenin verilerini istenmeyen veya hatalı değişikliklerden korur.

**Erişim Belirleyiciler (Access Modifiers)**

Python'da diğer dillerdeki gibi katı `public`, `protected`, `private` anahtar kelimeleri yoktur. Bunun yerine, isimlendirme kuralları ile erişim seviyeleri ima edilir.

*   **Public (Genel):** Varsayılan olarak, tüm nitelikler ve metotlar public'tir. Yani, sınıfın içinden de dışından da serbestçe erişilebilirler. Herhangi bir özel ön ek almazlar (örn: `self.ad`).

*   **Protected (Korumalı):** Bir nitelik veya metot adının başına tek alt çizgi (`_`) konularak tanımlanır (örn: `self._bakiye`). Bu bir kuraldan çok, bir "centilmenlik anlaşmasıdır". Programcıya "Bu niteliğe sınıf dışından doğrudan erişmemelisin, bu bir iç özelliktir." mesajını verir. Ancak teknik olarak erişim engellenmez.

*   **Private (Özel):** Bir nitelik veya metot adının başına çift alt çizgi (`__`) konularak tanımlanır (örn: `self.__gizli_kod`). Python, bu şekilde tanımlanan isimleri **Name Mangling (İsim Bulandırma)** adı verilen bir işlemle değiştirir. İsmi `_SinifAdi__nitelikAdi` şekline dönüştürür. Bu, sınıf dışından doğrudan erişimi büyük ölçüde engeller ve özellikle kalıtım (inheritance) sırasında alt sınıfların üst sınıftaki aynı isimli nitelikleri yanlışlıkla ezmesini önler.

**Getter ve Setter Metotları**

Kapsüllemenin bir gereği olarak, korumalı veya özel niteliklere kontrollü erişim sağlamak için `getter` ve `setter` metotları kullanılır.

*   **Getter:** Özel bir niteliğin değerini okumak (get) için kullanılan bir metottur. Genellikle `get_nitelik()` şeklinde isimlendirilir.
*   **Setter:** Özel bir niteliğin değerini ayarlamak (set) için kullanılan bir metottur. Bu metot içinde, atanacak yeni değere bir doğrulama veya kısıtlama (validation) uygulanabilir. Örneğin, yaşın negatif olmaması veya bir şifrenin belirli bir uzunlukta olması gibi. Genellikle `set_nitelik(yeni_deger)` şeklinde isimlendirilir.

**`@property` Dekoratörü**

Python, getter ve setter metotlarını daha "Pythonic" ve zarif bir şekilde kullanmak için `@property` dekoratörünü sunar. Bu dekoratör sayesinde, metotları sanki public bir niteliğe erişiyormuş gibi kullanabiliriz.

*   `@property`: Bir metodu getter olarak tanımlar. `nesne.nitelik` şeklinde çağrılır.
*   `@nitelik.setter`: O property için bir setter metodu tanımlar. `nesne.nitelik = deger` şeklinde kullanılır.

---

**Syntax Örnekleri**

1.  **Public, Protected ve Private Nitelikler**

    ```python
    class Calisan:
        def __init__(self, ad, maas, tc_kimlik):
            self.ad = ad              # Public
            self._maas = maas          # Protected
            self.__tc_kimlik = tc_kimlik # Private

        def bilgileri_goster(self):
            print(f"Ad: {self.ad}, Maaş: {self._maas}")
            # Private niteliğe sınıf içinden erişim
            print(f"TC Kimlik No (iç erişim): {self.__tc_kimlik}")

    calisan1 = Calisan("Büşra", 5000, "12345678901")
    print(calisan1.ad)       # Erişilebilir
    print(calisan1._maas)      # Erişilebilir (ama önerilmez)
    # print(calisan1.__tc_kimlik) # Hata verir (AttributeError)

    # Name Mangling ile erişim (kesinlikle önerilmez, sadece gösterim amaçlı)
    print(f"Name Mangling ile erişim: {calisan1._Calisan__tc_kimlik}")
    ```

2.  **Getter ve Setter Metotları**

    ```python
    class Ogrenci:
        def __init__(self, ad, yas):
            self.ad = ad
            self.__yas = yas # Yaşı private yapalım

        # Getter metodu
        def get_yas(self):
            return self.__yas

        # Setter metodu
        def set_yas(self, yeni_yas):
            if yeni_yas > 6:
                self.__yas = yeni_yas
            else:
                print("Yaş 6'dan küçük olamaz!")

    ogr = Ogrenci("Efe", 8)
    print(f"{ogr.ad}, {ogr.get_yas()} yaşında.")

    ogr.set_yas(9)
    print(f"Yeni yaşı: {ogr.get_yas()}")

    ogr.set_yas(5) # Hata mesajı verecek
    ```

3.  **`@property` Dekoratörü Kullanımı**

    ```python
    class Sicaklik:
        def __init__(self, derece_celsius):
            self._derece_celsius = derece_celsius

        @property
        def derece(self):
            print("Getter çağrıldı")
            return self._derece_celsius

        @derece.setter
        def derece(self, deger):
            print("Setter çağrıldı")
            if deger < -273.15: # Mutlak sıfır kontrolü
                raise ValueError("Sıcaklık mutlak sıfırın altında olamaz!")
            self._derece_celsius = deger

    termometre = Sicaklik(25)
    print(f"Sıcaklık: {termometre.derece} C") # Getter çağrılır

    termometre.derece = 30 # Setter çağrılır
    print(f"Yeni sıcaklık: {termometre.derece} C")
    ```

4.  **Sadece Okunabilir (Read-Only) Nitelik**

    ```python
    class Kullanici:
        def __init__(self, kullanici_id):
            # ID'nin değiştirilmemesi gerekir, bu yüzden private yapalım
            self.__kullanici_id = kullanici_id

        @property
        def id(self):
            # Sadece getter tanımlayarak niteliği okunabilir yaparız
            return self.__kullanici_id

    k1 = Kullanici("USR12345")
    print(f"Kullanıcı ID: {k1.id}")

    # k1.id = "NEWID" # Hata verir (AttributeError: can't set attribute)
    ```

5.  **Hesaplamalı Property**

    ```python
    class Dikdortgen:
        def __init__(self, genislik, yukseklik):
            self.genislik = genislik
            self.yukseklik = yukseklik

        @property
        def alan(self):
            # Alan, her seferinde genişlik ve yükseklikten hesaplanır
            # Ayrı bir _alan niteliği tutmaya gerek yoktur
            return self.genislik * self.yukseklik

    d = Dikdortgen(10, 5)
    print(f"Genişlik: {d.genislik}, Yükseklik: {d.yukseklik}, Alan: {d.alan}")

    d.genislik = 12
    print(f"Yeni genişlikten sonra alan: {d.alan}") # Alan otomatik güncellenir
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** `ad` (public) ve `__seri_no` (private) niteliklerine sahip bir `Urun` sınıfı oluşturun. Seri numarasını dışarıdan doğrudan değiştirememeyi, ancak bir metot aracılığıyla okuyabilmeyi sağlayın.
2.  **Kolay:** Bir `Kasa` sınıfı oluşturun. İçinde `__para_miktari` adında private bir nitelik olsun. `para_ekle` ve `para_cikar` metotları yazın, ancak kasanın içindeki para asla negatif olamasın.
3.  **Kolay:** `_hiz` adında protected bir niteliği olan bir `Araba` sınıfı yazın. Hızı doğrudan değiştirmek yerine `hizlan(artis)` ve `yavasla(azalis)` metotları ile kontrollü bir şekilde değiştirin.
4.  **Kolay:** `@property` kullanarak, bir `Kisi` sınıfının `ad` ve `soyad` niteliklerini birleştiren `tam_ad` adında sadece okunabilir bir property oluşturun.
5.  **Kolay:** Bir `Kitap` sınıfı oluşturun. `sayfa_sayisi` niteliği için bir setter yazın ve sayfa sayısının 0'dan küçük bir değere ayarlanmasını engelleyin.
6.  **Orta:** Bir `BankaHesabi` sınıfı tasarlayın. `__bakiye` private olsun. `@property` kullanarak `bakiye` adında bir getter oluşturun. `para_yatir` ve `para_cek` metotları yazın. `para_cek` metodu, çekilmek istenen miktarın bakiyeden büyük olmamasını kontrol etsin.
7.  **Orta:** Bir `KullaniciProfili` sınıfı oluşturun. `email` adında bir niteliği olsun. `@property` ve setter kullanarak, `email` niteliğine atanan değerin her zaman geçerli bir e-posta formatında olup olmadığını (en azından `@` içermesi gerektiğini) kontrol edin. Geçersizse atamayı reddedin.
8.  **Orta:** Bir `OyunKarakteri` sınıfı oluşturun. `_can` adında protected bir niteliği olsun (0-100 arası). `can` için bir `@property` ve setter yazın. Setter, can değerinin 0'ın altına düşmemesini ve 100'ün üstüne çıkmamasını sağlasın.
9.  **Orta:** `dogum_yili` niteliğini private olarak tutan bir `Insan` sınıfı yazın. `@property` kullanarak `yas` adında hesaplamalı bir property oluşturun. Bu property, her çağrıldığında `(guncel_yil - dogum_yili)` formülü ile yaşı hesaplayıp döndürsün. `yas` property'sinin bir setter'ı olmamalıdır (read-only).
10. **Orta:** Bir `Sifre` sınıfı oluşturun. `__parola` adında private bir niteliği olsun. `parola` için bir `@property` (getter) ve setter yazın. Getter, parolayı asla doğrudan döndürmemeli, bunun yerine `"********"` gibi maskeli bir değer döndürmelidir. Setter ise yeni parolanın en az 8 karakter uzunluğunda olmasını zorunlu kılmalıdır.

### 2.3. Kalıtım (Inheritance)

**Teorik İçerik (15-20 dakika)**

**Kalıtım (Inheritance)**, nesne yönelimli programlamanın en güçlü ve temel prensiplerinden biridir. Mevcut bir sınıfın (üst sınıf) tüm niteliklerini ve metotlarını yeni bir sınıfa (alt sınıf) aktarma yeteneğidir. Bu sayede, kod tekrarını önleyerek, var olan kodu genişletip yeniden kullanabiliriz.

Kalıtım, "bir ...dır" (is-a) ilişkisini modeller. Örneğin, bir `Kopek` **bir** `Hayvan`'dır. Bir `Mudur` **bir** `Calisan`'dır. Bu ilişkide, daha genel olan sınıf **üst sınıf (parent/base class)**, daha özel olan sınıf ise **alt sınıf (child/derived class)** olarak adlandırılır.

**Kalıtımın Faydaları:**

*   **Kod Yeniden Kullanımı:** Üst sınıfta tanımlanmış olan tüm ortak metot ve nitelikler, alt sınıflar tarafından otomatik olarak miras alınır. Bu sayede aynı kodu tekrar tekrar yazmaktan kurtuluruz.
*   **Hiyerarşik Yapı:** Gerçek dünyadaki nesneler arasındaki hiyerarşik ilişkileri (örneğin, Canlı -> Hayvan -> Memeli -> Kedi) kodda modellemeyi kolaylaştırır.
*   **Genişletilebilirlik:** Alt sınıflar, üst sınıftan aldıkları özelliklere ek olarak kendi yeni nitelik ve metotlarını tanımlayabilirler.
*   **Metot Ezme (Method Overriding):** Alt sınıflar, üst sınıftan miras aldıkları bir metodun davranışını, kendi ihtiyaçlarına göre yeniden tanımlayabilirler.

**Temel Kavramlar**

*   **Parent (Base) Class (Üst Sınıf):** Özellikleri miras alınan sınıftır.
*   **Child (Derived) Class (Alt Sınıf):** Miras alan sınıftır. Python'da bir sınıfın başka bir sınıftan miras aldığını belirtmek için, sınıf tanımında sınıf adının yanına parantez içinde üst sınıfın adı yazılır: `class AltSinif(UstSinif):`

*   **`super()` Fonksiyonu:** Alt sınıf içinde, üst sınıfın metotlarına (özellikle `__init__()` metoduna) erişmek için kullanılır. Alt sınıfın `__init__` metodu yazıldığında, üst sınıfın `__init__` metodunun da çağrılarak oradaki başlangıç ayarlarının yapılmasını sağlamak için `super().__init__(...)` kullanılır. Bu, kalıtım zincirinin doğru bir şekilde kurulması için kritik öneme sahiptir.

*   **Method Overriding (Metot Ezme):** Alt sınıf, üst sınıfla aynı isme sahip bir metot tanımlarsa, bu yeni metot üst sınıftaki eski metodu "ezer" ve geçersiz kılar. Artık alt sınıfın nesnesi için bu metot çağrıldığında, alt sınıfta tanımlanan versiyon çalışır.

---

**Syntax Örnekleri**

1.  **Temel Kalıtım: `Hayvan` ve `Kedi` Sınıfları**

    ```python
    # Üst Sınıf (Base Class)
    class Hayvan:
        def __init__(self, ad):
            self.ad = ad

        def ses_cikar(self):
            return "Bilinmeyen bir hayvan sesi"

    # Alt Sınıf (Child Class)
    class Kedi(Hayvan):
        def __init__(self, ad, cins):
            # Üst sınıfın __init__ metodunu çağır
            super().__init__(ad)
            self.cins = cins

        # Metot Ezme (Method Overriding)
        def ses_cikar(self):
            return "Miyav!"

    hayvan = Hayvan("Canlı")
    kedi = Kedi("Pamuk", "Van Kedisi")

    print(f"{hayvan.ad} diyor ki: {hayvan.ses_cikar()}")
    print(f"{kedi.ad} ({kedi.cins}) diyor ki: {kedi.ses_cikar()}")
    ```

2.  **`Calisan` ve `Yonetici` Sınıfları**

    ```python
    class Calisan:
        def __init__(self, ad, maas):
            self.ad = ad
            self.maas = maas

        def bilgileri_goster(self):
            return f"Ad: {self.ad}, Maaş: {self.maas} TL"

    class Yonetici(Calisan):
        def __init__(self, ad, maas, departman):
            super().__init__(ad, maas)
            self.departman = departman # Yöneticiye özel nitelik

        # Üst sınıfın metodunu genişletme
        def bilgileri_goster(self):
            temel_bilgi = super().bilgileri_goster()
            return f"{temel_bilgi}, Departman: {self.departman}"

    calisan = Calisan("Ali", 4000)
    yonetici = Yonetici("Zeynep", 8000, "İnsan Kaynakları")

    print(calisan.bilgileri_goster())
    print(yonetici.bilgileri_goster())
    ```

3.  **Geometrik Şekil Hiyerarşisi**

    ```python
    class Sekil:
        def __init__(self, renk):
            self.renk = renk

        def alan(self):
            return "Alan hesaplanamadı"

    class Kare(Sekil):
        def __init__(self, renk, kenar):
            super().__init__(renk)
            self.kenar = kenar

        def alan(self):
            return self.kenar ** 2

    class Daire(Sekil):
        def __init__(self, renk, yaricap):
            super().__init__(renk)
            self.yaricap = yaricap

        def alan(self):
            return 3.14 * (self.yaricap ** 2)

    kare = Kare("Mavi", 5)
    daire = Daire("Kırmızı", 3)

    print(f"{kare.renk} karenin alanı: {kare.alan()}")
    print(f"{daire.renk} dairenin alanı: {daire.alan()}")
    ```

4.  **`isinstance()` ve `issubclass()` Fonksiyonları**

    ```python
    # Önceki örnekteki sınıfları kullanarak
    print(f"kare, bir Kare nesnesi mi? {isinstance(kare, Kare)}")
    print(f"kare, bir Sekil nesnesi mi? {isinstance(kare, Sekil)}")
    print(f"Kare sınıfı, Sekil sınıfının bir alt sınıfı mı? {issubclass(Kare, Sekil)}")
    print(f"Sekil sınıfı, Kare sınıfının bir alt sınıfı mı? {issubclass(Sekil, Kare)}")
    ```

5.  **Çoklu Kalıtım (Multiple Inheritance)**

    ```python
    class Ucabilen:
        def uc(self):
            return "Uçuyorum!"

    class Yuzebilen:
        def yuz(self):
            return "Yüzüyorum!"

    # Hem uçabilen hem yüzebilen bir ördek
    class Ordek(Ucabilen, Yuzebilen):
        pass

    ordek = Ordek()
    print(ordek.uc())
    print(ordek.yuz())
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** `Tasit` adında bir üst sınıf oluşturun (`hiz` niteliği olsun). Bu sınıftan miras alan `Otomobil` adında bir alt sınıf oluşturun. `Otomobil` sınıfına `kapi_sayisi` adında ek bir nitelik ekleyin.
2.  **Kolay:** `Kitap` adında bir üst sınıf (`ad`, `yazar`) ve ondan türeyen `Roman` adında bir alt sınıf oluşturun. `Roman` sınıfının `konu` adında ek bir niteliği olsun.
3.  **Kolay:** `Kisi` (`ad`, `yas`) ve ondan türeyen `Ogrenci` (`okul_no`) sınıflarını oluşturun. `Ogrenci` sınıfının `__init__` metodunda `super()` kullanarak `Kisi`'nin `__init__`'ini çağırın.
4.  **Kolay:** `Hayvan` sınıfının `beslen()` metodu "Yemek yiyor." çıktısı versin. `Kus` adında bir alt sınıf oluşturun ve bu sınıfın `beslen()` metodunu "Solucan yiyor." çıktısı verecek şekilde ezin (override).
5.  **Kolay:** `Sekil` adında bir sınıf ve ondan türeyen `Ucgen` adında bir sınıf oluşturun. Her ikisinin de `ciz()` metodu olsun, ancak farklı mesajlar yazdırsınlar ("Şekil çiziliyor" ve "Üçgen çiziliyor").
6.  **Orta:** Bir `Bina` sınıfı (`adres`, `kat_sayisi`) oluşturun. Bu sınıftan `Apartman` (`daire_sayisi`) ve `IsYeri` (`ofis_sayisi`) adında iki alt sınıf türetin. Her sınıfın kendine özgü bilgilerini gösteren bir metodu olsun.
7.  **Orta:** Bir `ElektronikCihaz` sınıfı (`marka`, `model`) oluşturun. Bu sınıftan `Telefon` (`kamera_mp`) ve `Bilgisayar` (`ram_gb`) alt sınıflarını türetin. `Telefon` sınıfına `fotograf_cek()` metodu, `Bilgisayar` sınıfına ise `program_calistir()` metodu ekleyin.
8.  **Orta:** `MuzikAleti` adında bir üst sınıf oluşturun. `cal()` metodu olsun. Bu sınıftan `Gitar` (`tel_sayisi`) ve `Piyano` (`tussayisi`) alt sınıflarını türetin. Her iki alt sınıf da `cal()` metodunu kendilerine özgü bir ses çıkaracak şekilde (örneğin, "Gitar sesi...", "Piyano sesi...") ezsin.
9.  **Orta:** Bir `Posta` sınıfı (`gonderen`, `alici`) oluşturun. Bu sınıftan `Mektup` (`icerik`) ve `Kargo` (`agirlik_kg`) alt sınıflarını türetin. `Kargo` sınıfına, ağırlığa göre gönderim ücretini hesaplayan `ucret_hesapla()` adında bir metot ekleyin (örneğin, kg başına 5 TL).
10. **Orta:** `Ogretmen` ve `Ogrenci` sınıflarınız olduğunu varsayın. Her ikisi de `OkulInsani` adında bir üst sınıftan türesin. `OkulInsani` sınıfı `ad` ve `soyad` tutsun. `Ogretmen`'in `brans`, `Ogrenci`'nin ise `sinif` niteliği olsun. Tüm bu yapıyı `super()` kullanarak doğru bir şekilde kurun.

### 2.4. Polimorfizm (Polymorphism)

**Teorik İçerik (10-15 dakika)**

**Polimorfizm (Polymorphism)**, kelime anlamı olarak "birçok şekle sahip olma" demektir. Nesne yönelimli programlamada, farklı sınıflara ait nesnelerin aynı arayüzü (metot adını) paylaşmasına rağmen, bu arayüzü kendilerine özgü şekillerde uygulayabilme yeteneğidir. Başka bir deyişle, aynı metot çağrısının, çağrıldığı nesnenin tipine bağlı olarak farklı davranışlar sergilemesidir.

Polimorfizm, genellikle kalıtım (inheritance) ile birlikte kullanılır ve kodun esnekliğini ve genişletilebilirliğini önemli ölçüde artırır. Üst sınıf türünden bir referansın, alt sınıf nesnelerini tutabilmesi ve bu nesneler üzerinden metotlar çağrıldığında, nesnenin gerçek tipine ait metodun çalışması polimorfizmin temelini oluşturur.

**Polimorfizmin İki Temel Uygulaması:**

1.  **Metot Ezme (Method Overriding) ile Polimorfizm:**
    Bu, en yaygın polimorfizm şeklidir. Bir alt sınıf, üst sınıftan miras aldığı bir metodu yeniden tanımladığında (override ettiğinde) ortaya çıkar. Bir grup farklı nesne (farklı alt sınıflardan) üzerinde aynı metot çağrıldığında, her nesne kendi sınıfında tanımlı olan metot versiyonunu çalıştırır.
    Örneğin, bir `Hayvan` sınıfının `ses_cikar()` metodu olsun. `Kedi`, `Kopek` ve `Kus` alt sınıfları bu metodu miras alır ve her biri kendine özgü bir ses çıkaracak şekilde ezer ("Miyav", "Hav hav", "Cik cik"). Bir listede bu hayvanları tutup, döngü içinde her birinin `ses_cikar()` metodunu çağırdığımızda, her hayvan kendi sesini çıkaracaktır. İşte bu polimorfik bir davranıştır.

2.  **Ördek Yazımı (Duck Typing) ile Polimorfizm:**
    Python gibi dinamik tipli dillerde görülen özel bir polimorfizm türüdür. Bu yaklaşımın arkasındaki felsefe şudur: "Eğer bir şey ördek gibi yürüyorsa ve ördek gibi vaklıyorsa, o zaman o bir ördektir." Yani, bir nesnenin tipinin ne olduğuyla değil, hangi metotlara veya davranışlara sahip olduğuyla ilgileniriz. Eğer farklı sınıflardan gelen nesneler, aynı isimde bir metoda sahipse, bu metot onlar üzerinde polimorfik olarak çağrılabilir. Bu nesnelerin aynı üst sınıftan miras alması gerekmez.

**Polimorfizmin Avantajları:**

*   **Esneklik:** Yeni sınıflar eklendiğinde, bu sınıflar mevcut arayüzü uyguladığı sürece, onları kullanan kodda değişiklik yapmaya gerek kalmaz.
*   **Genişletilebilirlik:** Sisteme yeni fonksiyonellikler eklemek kolaylaşır.
*   **Okunabilirlik:** Farklı nesneler için ayrı ayrı `if-elif-else` blokları yazmak yerine, tek bir metot çağrısı ile işlem yapılır, bu da kodu basitleştirir.

---

**Syntax Örnekleri**

1.  **Metot Ezme ile Klasik Polimorfizm**

    ```python
    class Hayvan:
        def ses_cikar(self):
            raise NotImplementedError("Alt sınıf bu metodu implemente etmelidir.")

    class Kedi(Hayvan):
        def ses_cikar(self):
            return "Miyav"

    class Kopek(Hayvan):
        def ses_cikar(self):
            return "Hav hav"

    class Kus(Hayvan):
        def ses_cikar(self):
            return "Cik cik"

    # Farklı sınıflardan nesneler oluşturma
    hayvanlar = [Kedi(), Kopek(), Kus()]

    # Aynı metot çağrısı, farklı davranışlar
    for hayvan in hayvanlar:
        print(f"Bu hayvanın sesi: {hayvan.ses_cikar()}")
    ```

2.  **Ördek Yazımı (Duck Typing)**

    ```python
    class Ordek:
        def uc(self):
            print("Ördek uçuyor.")
        def yuz(self):
            print("Ördek yüzüyor.")

    class OyuncakOrdek:
        def uc(self):
            print("Bu oyuncak uçamaz.")
        def yuz(self):
            print("Oyuncak ördek suda batmıyor.")

    # Bu fonksiyon, nesnenin tipine değil, uc() ve yuz() metotlarına sahip olup olmadığına bakar.
    def ordek_davranislarini_goster(ordek_gibi_nesne):
        ordek_gibi_nesne.uc()
        ordek_gibi_nesne.yuz()

    gercek_ordek = Ordek()
    oyuncak = OyuncakOrdek()

    print("--- Gerçek Ördek ---")
    ordek_davranislarini_goster(gercek_ordek)

    print("\n--- Oyuncak Ördek ---")
    ordek_davranislarini_goster(oyuncak)
    ```

3.  **Farklı Veritabanı Bağlantıları**

    ```python
    class MySQLBaglantisi:
        def baglan(self):
            print("MySQL veritabanına bağlanıldı.")
        def sorgu_calistir(self, sorgu):
            print(f"MySQL sorgusu çalıştırılıyor: {sorgu}")

    class PostgreSQLBaglantisi:
        def baglan(self):
            print("PostgreSQL veritabanına bağlanıldı.")
        def sorgu_calistir(self, sorgu):
            print(f"PostgreSQL sorgusu çalıştırılıyor: {sorgu}")

    def veritabani_islemi_yap(db_baglantisi):
        db_baglantisi.baglan()
        db_baglantisi.sorgu_calistir("SELECT * FROM kullanicilar")

    mysql = MySQLBaglantisi()
    pgsql = PostgreSQLBaglantisi()

    veritabani_islemi_yap(mysql)
    print("---")
    veritabani_islemi_yap(pgsql)
    ```

4.  **Polimorfizm ve Fonksiyon Argümanları**

    ```python
    class Document:
        def show(self):
            print("Bir doküman gösteriliyor.")

    class PdfDocument(Document):
        def show(self):
            print("PDF dokümanı açılıyor.")

    class WordDocument(Document):
        def show(self):
            print("Word dokümanı açılıyor.")

    def print_document(doc):
        # doc argümanı Document, PdfDocument veya WordDocument olabilir.
        doc.show()

    pdf = PdfDocument()
    word = WordDocument()

    print_document(pdf)   # Çıktı: PDF dokümanı açılıyor.
    print_document(word)  # Çıktı: Word dokümanı açılıyor.
    ```

5.  **Operatörlerde Polimorfizm**

    ```python
    # '+' operatörü farklı tipler için farklı çalışır (polimorfik davranış)
    sayi1 = 5
    sayi2 = 10
    print(f"Sayılar için +: {sayi1 + sayi2}") # Toplama işlemi

    str1 = "Merhaba"
    str2 = " Dünya"
    print(f"Stringler için +: {str1 + str2}") # Birleştirme işlemi

    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6]
    print(f"Listeler için +: {liste1 + liste2}") # Birleştirme işlemi
    ```

---

**Algoritma Soruları (Kolay-Orta)**

1.  **Kolay:** `Arac` adında bir üst sınıf ve `ilerle()` metodu oluşturun. `Otomobil` ve `Bisiklet` adında iki alt sınıf oluşturun. Her ikisi de `ilerle()` metodunu kendilerine özgü bir mesajla ("Otomobil yolda gidiyor", "Bisiklet pedal çevirerek ilerliyor") ezsin. Bir listede bu iki nesneyi tutup döngü ile `ilerle()` metotlarını çağırın.
2.  **Kolay:** `Cizici` adında bir sınıf ve `ciz()` metodu olsun. Bu metot, `Sekil` tipinde bir argüman alsın ve o şeklin `ciz()` metodunu çağırsın. `Kare` ve `Daire` sınıfları oluşturup her birinin kendi `ciz()` metodu olsun. `Cizici` sınıfını kullanarak her iki şekli de çizin.
3.  **Kolay:** `DosyaOkuyucu` adında bir sınıf ve `oku()` metodu olsun. `MetinOkuyucu` ve `CsvOkuyucu` sınıfları oluşturun. Her biri `oku()` metodunu farklı bir mesajla ("Metin dosyası okunuyor...", "CSV dosyası satır satır işleniyor...") implemente etsin.
4.  **Kolay:** `Muzisyen` adında bir sınıf ve `enstruman_cal(enstruman)` metodu yazın. Bu metot, kendisine verilen `enstruman` nesnesinin `ses_cikar()` metodunu çağırsın. `Gitar` ve `Piyano` sınıfları oluşturup her birinin `ses_cikar()` metodu olsun. `Muzisyen` nesnesi ile her iki enstrümanı da çalın.
5.  **Kolay:** `len()` fonksiyonunun polimorfik davranışını gösteren bir örnek yazın. Bir string, bir liste ve bir sözlük oluşturup her birinin `len()` ile uzunluğunu ekrana yazdırın.
6.  **Orta:** Bir `OdemeYontemi` üst sınıfı ve `odeme_yap(tutar)` metodu tanımlayın. `KrediKarti` ve `PayPal` adında iki alt sınıf oluşturun. `KrediKarti` sınıfı `kart_no` alırken, `PayPal` sınıfı `email` alsın. Her ikisi de `odeme_yap` metodunu, kendi bilgilerini kullanarak ödemenin nasıl yapıldığını anlatan bir mesajla ezsin.
7.  **Orta:** Bir oyun için `Silah` adında bir üst sınıf ve `saldir()` metodu oluşturun. `Kilic` ve `Ok` adında iki alt sınıf türetin. `Kilic` sınıfı `saldir()` metodunda "Kılıçla keskin bir vuruş yapıldı!" yazarken, `Ok` sınıfı "Uzak mesafeden ok atıldı!" yazsın. Bir `Savasci` sınıfı oluşturun. Bu sınıfın `silah_kullan(silah)` metodu, verilen silahın `saldir()` metodunu çağırsın.
8.  **Orta:** Bir `BildirimGonderici` arayüzü gibi davranacak bir yapı kurun. `EmailGonderici`, `SMSGonderici` ve `PushBildirimGonderici` sınıfları oluşturun. Hepsinin `gonder(mesaj)` adında bir metodu olsun. Bir fonksiyon yazın; bu fonksiyon bir liste `gonderici` nesnesi ve bir `mesaj` alsın, listedeki her bir gönderici aracılığıyla mesajı göndersin.
9.  **Orta:** `__add__` (toplama `+` operatörü için) özel metodunu kullanarak polimorfizmi gösterin. `Vektor` adında bir sınıf oluşturun. İki `Vektor` nesnesi `+` ile toplandığında, karşılıklı elemanlarının toplanmasını sağlayın. Örneğin, `Vektor(1, 2) + Vektor(3, 4)` sonucu `Vektor(4, 6)` olmalıdır.
10. **Orta:** Bir `RaporOlusturucu` sistemi tasarlayın. `Rapor` adında bir üst sınıf ve `export()` metodu olsun. `PdfRapor` ve `ExcelRapor` alt sınıfları oluşturun. Her biri `export()` metodunu "Rapor PDF olarak dışa aktarıldı." ve "Rapor Excel dosyasına yazıldı." şeklinde ezsin. Bir fonksiyon, bir liste `Rapor` nesnesi alıp hepsini export etsin.


---

## Özet ve Tekrar Noktaları

Bu doküman, Python programlama dilinin temel ve orta seviye konularını kapsamlı bir şekilde sunmaktadır. İşlenen konuları aşağıdaki şekilde özetleyebiliriz:

### Temel Python Konuları

**Temel Python** bölümü, programlamanın en temel yapı taşlarını içermektedir. Değişkenler ve veri tipleri, bir programın bilgileri nasıl saklayıp işleyeceğini belirler. Operatörler ve tip dönüşümleri, bu veriler üzerinde işlem yapmamızı sağlar. Giriş/Çıkış fonksiyonları, programları interaktif hale getirerek kullanıcı ile iletişim kurmasını mümkün kılar.

Kontrol yapıları (`if-else`, `elif`, `match-case`), bir programın akışını belirli koşullara göre yönlendirir. Döngüler (`for`, `while`), tekrarlayan görevleri otomatikleştirerek kod tekrarını önler. Veri yapıları (String, List, Tuple, Dictionary), farklı türdeki verileri organize bir şekilde saklamak ve yönetmek için kullanılır. Fonksiyonlar, kodu modüler ve yeniden kullanılabilir hale getirerek programın karmaşıklığını azaltır.

### Nesne Yönelimli Programlama (OOP)

**OOP** bölümü, programları daha organize, ölçeklenebilir ve bakım yapılabilir hale getiren bir paradigmayı sunar. Sınıflar ve nesneler, gerçek dünyadaki varlıkları bilgisayar ortamında modellememizi sağlar. Kapsülleme, verilerin korunmasını ve kontrollü erişimini sağlar. Kalıtım, kod tekrarını önleyerek yeniden kullanılabilirliği artırır. Polimorfizm, farklı nesneleri aynı arayüz üzerinden kullanmamızı sağlayarak kodun esnekliğini ve genişletilebilirliğini artırır.

### Öğrenme Stratejisi

Bu dokümanı etkili bir şekilde kullanmak için aşağıdaki stratejileri önerilir:

1. **Teorik İçeriği Anlaşılana Kadar Okuyun:** Her konu başlığının teorik kısmını dikkatlice okuyun. Konseptleri tam olarak anlamadan örneklere geçmeyin.

2. **Syntax Örneklerini Çalıştırın:** Verilen 5 syntax örneğinin her birini kendi Python ortamınızda yazıp çalıştırın. Kodu değiştirerek farklı sonuçlar elde etmeyi deneyin.

3. **Algoritma Sorularını Çözün:** 10 algoritma sorusunun tümünü çözmek için zaman ayırın. Başta kolay soruları çözerek özgüveninizi artırın, sonra orta seviye sorulara geçin.

4. **Hata Ayıklama Yapın:** Kodunuzda hata oluştuğunda, hata mesajını dikkatle okuyun ve sorunu anlayarak düzeltmeyi öğrenin.

5. **Kendi Projelerinizi Yapın:** Öğrendiklerinizi gerçek projeler üzerinde uygulamaya çalışın. Bu, öğrenmeyi kalıcı hale getirir.

### Zaman Yönetimi

Bu doküman, yaklaşık 5 saatlik bir tekrar materyalidir. Aşağıdaki zaman dağılımı önerilir:

*   **Temel Python (2.5 saat):** Her konu için 15-20 dakika teorik içerik, 10 dakika syntax örnekleri, 20-30 dakika algoritma soruları.
*   **OOP (2.5 saat):** Her konu için 15-20 dakika teorik içerik, 10 dakika syntax örnekleri, 20-30 dakika algoritma soruları.

### Başarı İçin İpuçları

1. **Düzenli Pratik:** Haftada en az 3-4 gün, her gün 1-2 saat pratik yapın.
2. **Sorular Hakkında Düşünün:** Bir soruyu hemen çözmek yerine, önce sorunu analiz etmeye zaman ayırın.
3. **Farklı Çözümler Deneyin:** Aynı problemi farklı yollarla çözmeyi deneyin. Bu, yaratıcılığınızı ve problem çözme becerilerinizi geliştirir.
4. **Kodunuzu Belgelendirin:** Yazdığınız kodun ne yaptığını açıklayan yorumlar ekleyin. Bu, kodu anlamanızı ve hatırlamanızı kolaylaştırır.
5. **Topluluğa Katılın:** Python topluluklarında (forum, Discord, Reddit vb.) aktif olun. Başkalarının sorularını cevaplamak, öğrenmenizi pekiştirir.

---

## Kaynaklar

Bu doküman, aşağıdaki resmi kaynaklar referans alınarak hazırlanmıştır:

*   **Python Resmi Dokümentasyonu:** https://docs.python.org/3/
*   **Python Tutorial:** https://docs.python.org/3/tutorial/
*   **Python Standard Library:** https://docs.python.org/3/library/
