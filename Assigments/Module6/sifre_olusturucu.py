"""
    **Şifre Oluşturucu**: Güvenli rastgele şifre üreten fonksiyonlar
"""

import secrets
import string

OZEL_KARAKTERLER = "!@#$%^&*"

def guvenli_sifre_olustur(
    uzunluk: int = 12,
    buyuk_harf: bool = True,
    kucuk_harf: bool = True,
    rakam: bool = True,
    ozel_karakter: bool = True,
    ozel_karakter_seti: str = string.punctuation
) -> str:
    """
    Güvenli, rastgele bir şifre oluşturur.

    Parametreler:
        uzunluk (int): Şifre uzunluğu (varsayılan: 12)
        buyuk_harf (bool): Büyük harf içerir mi? (varsayılan: True)
        kucuk_harf (bool): Küçük harf içerir mi? (varsayılan: True)
        rakam (bool): Rakam içerir mi? (varsayılan: True)
        ozel_karakter (bool): Özel karakter içerir mi? (varsayılan: True)
        ozel_karakter_seti (str): Kullanılacak özel karakterler (varsayılan: string.punctuation)

    Dönüş:
        str: Oluşturulan şifre

    Hata:
        ValueError: Geçersiz parametre kombinasyonu (örneğin tüm seçenekler False)
    """

    if uzunluk <= 0:
        raise ValueError("Lütfen şifre giriniz.")

    karakterler = ""
    zorunlu_karakterler = []

    if buyuk_harf:
        buyukler = string.ascii_uppercase
        karakterler += buyukler
        zorunlu_karakterler.append(secrets.choice(buyukler))

    if kucuk_harf:
        kucukler = string.ascii_lowercase
        karakterler += kucukler
        zorunlu_karakterler.append(secrets.choice(kucukler))

    if rakam:
        rakamlar = string.digits
        karakterler += rakamlar
        zorunlu_karakterler.append(secrets.choice(rakamlar))

    if ozel_karakter:
        karakterler += ozel_karakter_seti
        zorunlu_karakterler.append(secrets.choice(ozel_karakter_seti))

    if not karakterler:
        raise ValueError("En az bir karakter türü seçilmelidir (büyük/küçük harf, rakam, özel karakter).")

    sifre_listesi = zorunlu_karakterler.copy()

    for _ in range(uzunluk - len(zorunlu_karakterler)):
        sifre_listesi.append(secrets.choice(karakterler))

    secrets.SystemRandom().shuffle(sifre_listesi)

    return ''.join(sifre_listesi)


if __name__ == "__main__":
    password = guvenli_sifre_olustur()
    print(password)

    pin_kodu = guvenli_sifre_olustur(uzunluk=6, buyuk_harf=False, kucuk_harf=False, ozel_karakter=False)
    print(pin_kodu)
