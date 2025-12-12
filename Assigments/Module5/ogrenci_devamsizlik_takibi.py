"""
    **Öğrenci Devamsızlık Takibi**: Tarih bazlı devamsızlık kaydetme ve sorgulama
"""

from datetime import date

devamsizlik_hakki = 3             # Öğrencinin bir dönemdeki devamsızlık hakkı
start = date(2025, 9, 15)         # Dönem başlangıç tarihi
end = date(2026, 1, 17)           # Dönem bitiş tarihi

days = (end - start).days + 1     # Toplam gün sayısı (bitiş Cumartesi günü dahil değil)
total_week = int(days / 7) + 1    # Bir dönemdeki hafta sayısı = 18 hafta

devamsizlik_listesi = []
devamsizlik_sayisi = 0

def imza_listesi_gir():
    global devamsizlik_sayisi     # Aksi halde UnboundLocalError hatası

    print("İmza Gir".center(30, "-"))
    print("İmza atmak için + tuşuna basınız.\nDerse girmediyseniz herhangi bir tuşa basın\nKalınan haftada q tuşuna basınız")
    
    for i in range(1, total_week+1):
        imza = input(f"{i}. Hafta: ")
        if imza == "+":
            devamsizlik_listesi.append(1)
        elif imza.lower() == "q":
            break
        else:
            devamsizlik_listesi.append(0)
            devamsizlik_sayisi += 1
    return devamsizlik_listesi

def imza_listesini_goruntule():
    print("İmza Listesi".center(30, "-"))
    for hafta, devamsizlik in enumerate(devamsizlik_listesi):
        if devamsizlik == 1:
            print(f"{hafta+1}. Hafta : ✍️")
        else:
            print(f"{hafta+1}. Hafta : ❌")

def devamsizlik_hakki_sorgula():
    if devamsizlik_sayisi > devamsizlik_hakki:
        print("Tebrikler yaz okuluna gitmeye hak kazandınız 🫠")
    elif devamsizlik_sayisi == devamsizlik_hakki:
        print("Devamsızlık hakkının tamamını kullandınız. Bundan sonra pıtı pıtı derse 🚶‍♂️")
    else:
        print(f"{devamsizlik_hakki - devamsizlik_sayisi} gün daha devemsızlık hakkınız bulunmakta.")


devamsizlik_hakki_sorgula()
imza_listesi_gir()
imza_listesini_goruntule()
devamsizlik_hakki_sorgula()
