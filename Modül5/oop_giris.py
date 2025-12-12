


class Ogrenci:
    isim = ""
    soyisim = ""
    yas = 0

    
    def set_isim(self,isim):
        self.isim = isim
    
    def get_isim(self):
        return self.isim
        
    def set_soyisim(self,soyisim):
        self.soyisim = soyisim
    
    def get_soyisim(self):
        return self.soyisim
    
    def set_yas(self,yas):
        self.yas = yas
    
    def get_yas(self):
        return self.yas
    

ogr = Ogrenci()
# ogr.isim = "Berkay"
# ogr.soyisim = "Kaplan"
# ogr.yas = 0

#Set metotları
ogr.set_isim("Berkay")
ogr.set_soyisim("Kaplan")
ogr.set_yas(20)


#Get Metotları
print(ogr.get_isim())
print(ogr.get_soyisim())
print(ogr.get_yas())

"""
Araba Sınıfı
Özellikleri
Encaptulation
marka 
model
beygir

    def set_marka(self,parametre_marka):
        self.marka = parametre_marka

"""


class Araba:
    model = ""
    marka = ""
    beygir = 0

    # def set_marka(self,parametre_marka):
    #     marka = parametre_marka

    # def set_marka(self,marka):
    #     self.marka = marka
    
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


arb = Araba()

arb.set_marka("Volvo")
arb.set_model("S60")
arb.set_beygir(100)

print(arb.get_marka())
print(arb.get_model())
print(arb.get_beygir())
