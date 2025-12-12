
"""
def get_marka(self):
        return self.marka
    
    def set_model(self,model):
        self.model = model

    def get_model(self):
        return self.model
    
    def set_beygir(self,beygir):
        self.beygir = beygir
    
    def get_beygir(self):
        return self.beygir
"""



# class Araba:
#     def __init__(self,model = "",marka = "",beygir = 0):
#         print("Obje Oluşturuldu")
#         self.model = model
#         self.marka = marka 
#         self.beygir = beygir

#     #Prop.(Özellikler)
#     @property
#     def modelprop(self):
#         return self.model

#     @modelprop.setter
#     def modelprop(self,model):
#         self.model = model

#     @property
#     def markaprop(self):
#         return self.marka
    
#     @markaprop.setter
#     def markaprop(self,marka):
#         self.marka = marka
    
#     @property
#     def beygirprop(self):
#         return self.beygir
    
#     @beygirprop.setter
#     def beygirprop(self,beygir):
#         self.beygir = beygir


#     #Metotolar(Davranışlar)

#     def bilgileri_gir(self):
#         self.markaprop = input("Lütfen Arabanızın Markasını Girin : ")
#         self.modelprop = input("Lütfen Arabanızın Modelini Girin : ")
#         self.beygirprop = int(input("Lütfen Arabanızın Beygir Gücünü Girin : "))
#         print(50*"-")

#     def bilgileri_goster(self):
#         print(self.markaprop)
#         print(self.modelprop)
#         print(self.beygirprop)
#         print(50*"-")

    


# db = []
# araba_sayisi = int(input("Lütfen Sisteme Kayıt Etmek İstediğiniz Araba Sayısını Girin : "))

# for i in range(araba_sayisi):
#     arb = Araba()
#     arb.bilgileri_gir()
#     db.append(arb)

# print(len(db))

# for i in db:
#     i.bilgileri_goster()

"""
Oğrenci Sınıfı Tanımlayın 
isim 
soyisim
numara
vize_notu
final_notu

notlari_gir()
ortalam_hesapla()
bilgileri_goster()
"""

class Ogrenci:
    def __init__(self,isim="",soyisim = "", numara = "", vize_notu = 0,final_notu = 0):
        self.isim = isim
        self.soyisim = soyisim 
        self.numara = numara
        self.vize_notu = vize_notu
        self.final_notu = final_notu
    

    @property
    def Isim(self):
        return self.isim
    
    @Isim.setter
    def Isim(self,isim):
        self.isim = isim





    @property
    def Soyisim(self):
        return self.soyisim
    
    @Soyisim.setter
    def Soyisim(self,soyisim):
        self.soyisim = soyisim

    
    @property
    def Numara(self):
        return self.numara
    
    @Numara.setter
    def Numara(self,numara):
        self.numara = numara

    
    @property
    def VizeNotu(self):
        return self.vizen_notu
    
    @VizeNotu.setter
    def VizeNotu(self,vize_notu):
        self.vize_notu = vize_notu


    @property
    def FinalNotu(self):
        return self.final_notu
    
    @FinalNotu.setter
    def FinalNotu(self,final_notu):
        self.final_notu = final_notu


    def notlari_gir(self):
        self.VizeNotu = int(input("Vize : "))
        self.FinalNotu = int(input("Final : "))


    def ortalam_hesapla(self):
        return self.VizeNotu * 0.4 + self.FinalNotu * 0.6
    
    def bilgileri_goster(self):
        print(f"""

        ==Öğrenci Bilgileri==
            Öğrenci isim : {self.Isim}
            Öğrenci soyisim : {self.Soyisim}
            Öğrenci numara : {self.Numara}
            Öğrenci Ortalaması : {self.ortalam_hesapla()}
""")



ogr = Ogrenci("Berkay","Kaplan","123")
ogr.notlari_gir()
ogr.bilgileri_goster()



        





    


