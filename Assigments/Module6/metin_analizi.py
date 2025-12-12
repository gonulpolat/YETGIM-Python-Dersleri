"""
    **Metin Analizi**: Kelime sayısı, karakter analizi, istatistik fonksiyonları
"""

import string
from collections import Counter

def kelime_sayisini_getir(txt: str) -> int:
    if not txt or not txt.strip():
        return 0
    return len(txt.split())

def karakter_analizi_yap(txt: str) -> dict:
    if not txt:
        return {
            "toplam_karakter": 0,
            "harf": 0,
            "rakam": 0,
            "bosluk": 0,
            "ozel_karakter": 0
        }
    
    toplam_karakter = len(txt)
    harf = sum(1 for c in txt if c.isalpha())
    rakam = sum(1 for c in txt if c.isdigit())
    bosluk = sum(1 for c in txt if c.isspace())
    ozel = toplam_karakter - harf - rakam - bosluk

    return {
        "toplam_karakter": toplam_karakter,
        "harf": harf,
        "rakam": rakam,
        "bosluk": bosluk,
        "ozel_karakter": ozel
    }

def en_cok_gecenleri_bul(txt: str, n: int = 1) -> dict:
    """
    En çok geçen kelimeleri ve harfleri döndürür.
    """
    if not txt or not txt.strip():
        return {"en_cok_gecen_kelime": None, "en_cok_gecen_harf": None}
    
    temiz_txt = txt.translate(str.maketrans("", "", string.punctuation))
    kelimeler = temiz_txt.lower().split()
    harfler = [c.lower() for c in txt if c.isalpha()]

    kelime_sayim = Counter(kelimeler)
    harf_sayim = Counter(harfler)

    en_cok_kelime = kelime_sayim.most_common(1)[0] if kelime_sayim else None # (kelime, freakans)
    en_cok_harf = harf_sayim.most_common(1)[0] if harf_sayim else None       # (harf, frekans)

    return {
        "en_cok_gecen_kelime": en_cok_kelime,
        "en_cok_gecen_harf": en_cok_harf
    }

if __name__ == "__main__":
    metin = "Python; web uygulamaları, yazılım geliştirme, veri bilimi ve makine öğreniminde (ML) yaygın olarak kullanılan bir programlama dilidir. Geliştiriciler, etkili ve öğrenmesi kolay olduğu ve birçok farklı platformda çalıştırılabildiği için Python'ı kullanır. Python yazılımı ücretsiz olarak indirilebilir, her türlü sistemle iyi bir entegrasyon sağlar ve geliştirme hızını artırır."

    kelime_sayisi    = kelime_sayisini_getir(metin)
    karakter_analizi = karakter_analizi_yap(metin)
    en_cok_gecenler  = en_cok_gecenleri_bul(metin)

    print(f"Kelime sayısı      : {kelime_sayisi}")
    print(f"Karakter Analizi   : {karakter_analizi}")
    print(f"En çok geçen kelime: {en_cok_gecenler['en_cok_gecen_kelime']}")
    print(f"En çok geçen harf  : {en_cok_gecenler['en_cok_gecen_harf']}")
