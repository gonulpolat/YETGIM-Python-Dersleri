"""
    Interest Calculator**: Bileşik faiz hesaplayan program (yıl yıl göster)

    Birleşik faiz (compound interest), faizlerin sadece ana paraya değil, önceki dönemlerde kazanılmış faizlere de eklenerek hesaplandığı faiz türüdür. Yani “faizin faizi” de hesaba katılır.

    Formül => A = P * (1 + r/n)^(n*t)

    A → Toplam tutar (ana para + faiz)
    P → Başlangıçtaki ana para (principal)
    r → Yıllık faiz oranı (decimal olarak, örn. %10 → 0.10)
    n → Yılda kaç kez faiz uygulanıyor (ör. aylık → 12, yıllık → 1)
    t → Yıl sayısı
"""

def faiz_hesapla(principal, yillik_faiz_orani, faiz_sayisi, yil_sayisi):
    return principal * ((1 + yillik_faiz_orani / faiz_sayisi)** (faiz_sayisi * yil_sayisi))

p = int(input("Başlangıçtaki ana para: "))
r = float(input("Yıllık faiz oranı: "))
n = int(input("Yılda kaç kez faiz uygulanıyor: "))
t = int(input("Yıl sayısı: "))

toplam_tutar = faiz_hesapla(p, r, n, t)
print(f"Toplam tutar: {toplam_tutar} TL")
print(f"Faiz Kazancı: {toplam_tutar - p} TL")
