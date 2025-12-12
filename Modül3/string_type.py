
isim = "Berkay"
soyisim = 'Kaplan'
cok_satirli_str = """
    Çok satırlı
    bir 
    string 
"""

# print(isim)
# print(soyisim)
# print(cok_satirli_str)

# tam_isim = isim + " "  + soyisim 

tam_isim = f"{isim} {soyisim}"

# print(tam_isim)

# print("Pozitif İndexleme ile Elemana Erişme: ",tam_isim[3])
# print("Negatif İndexleme ile Elemana Erişme: ",tam_isim[-10])


"""
Slicing(Dilimleme) İşlemleri

string[başlıngıç_indexi:bitiş_indexi(dahil değil):artış_miktarı]

"""
# print(tam_isim[3:10:1])
# print(tam_isim[3:10:2])
# print(tam_isim[-1:-8:-2])

#print(tam_isim[::-1])
# print(tam_isim[::1])
#print(tam_isim[:8:])
# print(tam_isim[::])



#string metotları

print(tam_isim.upper())
#upper_string = tam_isim.upper()
# print(upper_string)

# print(tam_isim.lower())

string = "merhaba,python"

# print(string.title())

# print("   merhaba   ".strip())

print(string.split(","))