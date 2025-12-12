
# class Insan:
#     isim = ""
#     soyisim = ""

# insan = Insan()

# insan.isim = "Berkay"
# insan.soyisim = "Kaplan"

# print(type(insan))
# print(insan.isim)
# print(insan.soyisim)



class Insan:
    def __init__(self,isim="",soyisim=""):
        self.isim = isim
        self.soyisim = soyisim
    
    def bilgileri_goster(self):
        print(f"isim : {self.isim}")
        print(f"soyiisim : {self.soyisim}")
    
    def bilgi_gir(self):
        self.isim = input("İsim : ")
        self.soyisim = input("Soyisim : ")

class Ogrenci(Insan):
    def __init__(self, isim="", soyisim="",vize=0,final=0):
        super().__init__(isim, soyisim)
        self.vize = vize
        self.final = final

    
    def ortalama_hesapla(self) -> float:
        return self.vize * 0.4 +  self.final * 0.6
    
    def gecti_mi(self,ortalama:int) -> str:
        if ortalama > 50:
            return "Sınfı geçtiniz..."
        else:
            return "Sınıfta kaldınız..."

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Vize : {self.vize}")
        print(f"Vize : {self.final}")
        print(f"Ders Durum :  {self.gecti_mi(self.ortalama_hesapla())}") 

    def bilgi_gir(self):
        super().bilgi_gir()
        self.vize = int(input("Vize : "))
        self.final = int(input("Final : "))




# insan = Insan()

ogr = Ogrenci()
 
ogr.bilgi_gir()
ogr.bilgileri_goster()



