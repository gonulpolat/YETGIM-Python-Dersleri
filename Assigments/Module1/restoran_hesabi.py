"""
    **Restoran Hesabı**: Yemek fiyatı, bahşiş oranı ve kişi sayısını alıp kişi başı tutarı hesaplayan program
"""

def kisi_basi_tutar_hesapla(fiyat: int, bahsis: int, kisi: int):
    print(f"Kişi başı ödenmesi gereken tutar: {(fiyat + fiyat * (bahsis/100)) / kisi} TL")


if __name__ == "__main__":
    print("Restoren Hesabı".center(30, "-"))
    yemek_fiyati = int(input("Lütfen yemek fiyatını giriniz: "))
    bahsis_orani = int(input("Lütfen verdiğiniz bahşişi giriniz: %"))
    kisi_sayisi = int(input("Lütfen kaç kişi olduğunuuz giriniz: "))

    kisi_basi_tutar_hesapla(yemek_fiyati, bahsis_orani, kisi_sayisi)
