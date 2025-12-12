


# class UstSınıf:
#     def __init__(self,ozellik):
#         self.ozellik = ozellik
    
#     def metot(self):
#         print("Üst sınıfın metotdu")
    
# class AltSınıf(UstSınıf):
#     pass

# alt_sinif_nesne = AltSınıf()
# alt_sinif_nesne.


# class Hayvan:
#     def __init__(self,isim="",yas = ""):
#         print("Hayvan objesi oluşturuldu")
#         self.isim = isim
#         self.yas = yas

#     def ses_cikar(self):
#         print("Hayvan ses çıkarıyor...")
    
# class Kedi(Hayvan):
#     def __init__(self,isim="",yas = "",cins=""):
#         print("Kedi objesi oluşturuldu")
#         super().__init__(isim,yas)
#         self.cins = cins
    
#     def ses_cikar(self):
        
#         print("Miyav Miyav!")
    
# kedi = Kedi()
# kedi.isim = "Şans"
# kedi.cins = "Siyam"
# kedi.yas = 2

# print(kedi.isim,kedi.cins,kedi.yas)
# kedi.ses_cikar()


# Hayvan.ses_cikar()





# class Banka:
#     def __init__(self,cüzdan):
#         self.cüzdan = cüzdan

#     def faiz_hesapla(self,bakiye):
#         return bakiye * 0.05
    
# class VadesizHesap(Banka):
#     def faiz_hesapla(self, bakiye):
#         return bakiye * 0.03

# class VadeliHesap(Banka):
#     def faiz_hesapla(self, bakiye):
#         return bakiye * 0.10


# bakiye = 1000
# banka = Banka()
# print(banka.faiz_hesapla(bakiye))

# vadeli_hesap = VadeliHesap()
# print(vadeli_hesap.faiz_hesapla(bakiye))


# vadesiz_hesap = VadesizHesap()
# print(vadesiz_hesap.faiz_hesapla(bakiye))



"""

==Kolay==





==Orta==







==Zor==
Soru:
Kapsamlı bir e-ticaret sipariş sistemi oluşturun. Farklı ürün tipleri, sepet yönetimi ve indirim hesaplamaları yapın.
İstenenler:

Urun base sınıfı ve alt sınıfları (Elektronik, Giyim)
Her ürün tipinin kendine özel özellikleri olsun
Sepet sınıfı ile ürünleri yönetin
Musteri sınıfı ile müşteri bilgileri ve indirim oranını saklayın
Property kullanarak indirim oranını kontrol edin (0-50 arası)
Polymorphism ile farklı ürün tiplerinin farklı KDV oranları olsun
Sipariş özeti çıkarın (toplam tutar, KDV, indirim sonrası)

"""
"""
Soru:
Bir kütüphane için kitap yönetim sistemi oluşturun. Kitap sınıfı oluşturup, kitap bilgilerini saklayın ve görüntüleyin.İstenenler:

Kitap sınıfı oluşturun
__init__ metodunda: ad, yazar, sayfa_sayisi, yayın_yılı alınsın
bilgi_goster() metodu ile kitap bilgilerini ekrana yazdırın
eski_mi() metodu ile kitabın 10 yıldan eski olup olmadığını kontrol edin (2025 baz alınarak)
"""

# class Kitap: 
#     def __init__(self,ad,yazar,sayfa_sayisi,yayin_yili):
#         self.ad = ad
#         self.yazar = yazar
#         self.sayfa_sayisi = sayfa_sayisi
#         self.yayin_yili = yayin_yili

#     def biligileri_goster(self):
#         print(f"""
#         Kitap :  {self.ad}
#         Yazar : {self.yazar}
#         Sayfa Sayısı : {self.sayfa_sayisi}
#         Yayın yılı : {self.yayin_yili}
# """)
        
#     def eski_mi(self):
#         return 2025 - self.yayin_yili > 10
    

# kitap1 = Kitap("Suç ve Ceza","Dostoyevski",671,1866)

# kitap1.biligileri_goster()
# print(kitap1.eski_mi())
        

"""
Soru:
Bir teknoloji mağazasının telefon envanteri için sistem yapın. Telefonları listeye ekleyin ve batarya durumunu güncelleyebilme özelliği ekleyin.İstenenler:

Telefon sınıfı oluşturun (marka, model, fiyat, batarya_yuzdesi)
get_batarya() ve set_batarya() metotları ekleyin
sarj_gerekli_mi() metodu ile batarya %20'nin altında mı kontrol edin
Birden fazla telefon oluşturup liste içinde saklayın
Tüm telefonları ve batarya durumlarını listeleyin
"""

# class Telefon:
#     def __init__(self,marka,model,fiyat,batarya_yuzde):
#         self.marka = marka
#         self.model = model
#         self.fiyat = fiyat 
#         self.batarya_yuzde = batarya_yuzde

#     def set_marka(self,marka):
#         self.marka = marka

#     def get_marka(self):
#         return self.marka
    
    
#     def set_model(self,model):
#         self.model = model

#     def get_model(self):
#         return self.model
    
 
#     def set_fiyat(self,fiyat):
#         self.fiyat = fiyat

#     def get_fiyat(self):
#         return self.fiyat
    
#     def get_batarya_yuzdesi(self):
#         return self.batarya_yuzde
    
#     def set_batarya_yuzdesi(self,batarya_yuzdesi):
#         if batarya_yuzdesi>=0 and batarya_yuzdesi <= 100:
#             self.batarya_yuzde = batarya_yuzdesi
#             print("Batarya şarj oldu")
#         else:
#             print("Batarya 0-100 arasında bir değer olmalıdır")
        

#     def sarj_gerekli_mi(self):
#         durum = self.batarya_yuzde < 20
#         if durum:
#             return "Şarj Etmelisiniz..."
#         return "Şarj Etmenize Gerek Yok..."
    
#     def biligi_goster(self):
        
#         print(f"""

#             {self.marka} - {self.model} - {self.fiyat} - {self.batarya_yuzde} 
#             Şarj Edilisin mi? {self.sarj_gerekli_mi()}
# """)
        


# telefon = Telefon("Apple","17",40.000,80)
# telefon.biligi_goster()


"""
Bir banka hesap sistemi oluşturun. Hesap bakiyesi private olacak ve @property dekoratörü ile erişilecek.İstenenler:

BankaHesabi sınıfı oluşturun (hesap_no, sahibi, __bakiye)
@property dekoratörü ile bakiye getter ve setter tanımlayın
Setter'da bakiye negatif olamaz kontrolü yapın
para_yatir() ve para_cek() metotları ekleyin
İşlem geçmişini tutan bir liste ekleyin
"""

# class BankaHesabi:
#     def __init__(self,hesap_no,sahibi,baslangic_bakiye = 0):
#         self.hesap_no = hesap_no
#         self.sahibi = sahibi
#         self.bakiye = baslangic_bakiye
#         self.islem_gecmisi = []
#         self.islem_gecmisi.append(f"Hesap Açıldı... Başlangıç Bakiyeniz : {baslangic_bakiye}")

#     @property
#     def Bakiye(self):
#         return self.bakiye
    
#     @Bakiye.setter
#     def Bakiye(self,yeni_bakiye):
#         if yeni_bakiye < 0:
#             print("HATA : Bakiye Negatif Olamaz.")
#         else:
#             self.bakiye = yeni_bakiye

    
#     def para_yatir(self,miktar):
#         if miktar > 0:
#             self.bakiye += miktar
#             self.islem_gecmisi.append(f"+ {miktar} TL yatırıldı. Yeni Bakiye {self.bakiye}")
#             print(f"{miktar} Hesabınıza yatırıldı")
#         else:
#             print("HATA : Yatırılacak miktar pozitif olmalıdır.")


#     def para_cek(self,miktar):
#         if miktar > 0:
#             if self.bakiye >= miktar:
#                 self.bakiye -= miktar
#                 self.islem_gecmisi.append(f"- {miktar} TL Çekildi. Yeni Bakiye : {self.bakiye}")
#                 print(f"{miktar} Hesabınızdan çekildi...")
#             else:
#                 print("HATA : Yetersiz bakiye!")
#         else:
#             print("HATA : Çekilecek miktar pozitif olmalıdır")
    
#     def hesap_ozeti(self):
#         print(f"""
#         Hesap No : {self.hesap_no}
#         Hesap Sahibi : {self.sahibi}
#         Güncel Bakiye : {self.bakiye}
# """)


#     def islem_gecmisini_goster(self):
#         for islem in self.islem_gecmisi:
#             print(islem)


# hesap = BankaHesabi("TR123456789","Berkay",1000)
# hesap.para_yatir(500)
# hesap.para_cek(300)
# hesap.para_cek(200000000)

# hesap.hesap_ozeti()
        
"""
Soru:
Bir şirketin çalışan sistemi için kalıtım kullanın. Temel Calisan sınıfından farklı çalışan tipleri türetin.
İstenenler:

Calisan base sınıfı (ad, soyad, maas, departman)
Yazilimci ve Muhasebeci alt sınıfları oluşturun
Her alt sınıf kendi özel özelliklerini eklesin (Yazılımcı: programlama_dilleri, Muhasebeci: sertifikalar)
maas_hesapla() metodunu her sınıfta override edin (Yazılımcılar %20, Muhasebeçiler %10 zam alsın)
bilgi_goster() metodunu override edin
"""

# class Calisan:
#     def __init__(self,ad,soyad,maas,departman):
#         self.ad = ad
#         self.soyad = soyad
#         self.maas = maas
#         self.departman = departman

#     def tam_ad(self):
#         return f"{self.ad} {self.soyad}"
    
#     def maas_hesapla(self):
#         return self.maas
    
#     def bilgileri_goster(self):
#         print(f"Çalışan : {self.tam_ad()}")
#         print(f"Departman : {self.departman}")
#         print(f"Maaş : {self.maas_hesapla()}")

# class Yazilimci(Calisan):
#     def __init__(self, ad, soyad, maas,programlama_dili):
#         super().__init__(ad, soyad, maas, "Yazılım")
#         self.programlama_dili = programlama_dili
    
#     def maas_hesapla(self):
#         return self.maas * 1.20
    
#     def bilgileri_goster(self):
#         super().bilgileri_goster()
#         print(" Kullandığı Programlama Dili: ",self.programlama_dili)
#         print("Zamlı Maaş",self.maas_hesapla())

# class Muhasebeci(Calisan):
#     def __init__(self, ad, soyad, maas,sertifikalar):
#         super().__init__(ad, soyad, maas, "Muhasebe")
#         self.sertifikalar = sertifikalar
    
#     def maas_hesapla(self):
#         return self.maas * 1.10

#     def bilgileri_goster(self):
#         super().bilgileri_goster()
#         print("Sertifikalar : ",self.sertifikalar)
#         print("Zamlı Maaş",self.maas_hesapla())
    

# yazilimci = Yazilimci("Berkay","Kaplan",1000000,"C#")
# yazilimci.bilgileri_goster()

# print("")

# muhasebeci = Muhasebeci("Cenk","Çetin",200000000,"Muhasebede Yapay Zeka")
# muhasebeci.bilgileri_goster()