"""
    **Set ile Veri Temizleme**: Tekrar eden kayıtları temizleme programı
"""

veri = [8, 'a', 9, 8, 8, 'a', "elma", 1, 9, 1, "elma"]


def veri_temizleme_set(veri: list) -> list:
    return list(set(veri))


def veri_temizleme_dongu(veri: list) -> list:
    temp = []
    for i in veri:
        if i not in temp:
            temp.append(i)
    return temp


print(veri_temizleme_set(veri))
print(veri_temizleme_dongu(veri))
