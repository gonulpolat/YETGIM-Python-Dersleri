"""
    **İstatistik Hesaplayıcı**: Liste için min, max, ortalama, medyan, mod hesaplama
"""

liste = [7, 8, 9, 45, 12, 100, 1, 63, 23, 85, 2, 4, 9, 56]

def minimum(data: list) -> int:
    en_kucuk = data[0]
    for i in data[1:]:
        if en_kucuk > i:
            en_kucuk = i
    return en_kucuk

def maximum(data: list) -> int:
    en_buyuk = data[0]
    for i in data[1:]:
        if en_buyuk < i:
            en_buyuk = i
    return en_buyuk

def ortalama(data: list) -> float:
    total = 0
    for i in data:
        total += i
    return total / len(data)

def _insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        val = data[i]
        j = i - 1
        while j >= 0 and data[j] > val:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = val
    return data

def medyan(data: list) -> float:
    sirali_liste = _insertion_sort(data.copy())
    if len(sirali_liste) % 2 == 1:
        return float(sirali_liste[len(sirali_liste) // 2])
    else:
        return (sirali_liste[len(sirali_liste) // 2 - 1] + sirali_liste[len(sirali_liste) // 2]) / 2
        
def _frekans(data: list) -> dict:
    sozluk = {}
    for i in data:
        if i not in sozluk:
            sozluk[i] = 1
        else:
            sozluk[i] += 1
    return sozluk

def mod(data: list) -> int:
    """
    En fazla bulunan elemanlardan ilkini döner.
    """
    frekanslar = _frekans(data)  # dictionary
    en_yuksek = 0
    for key, value in frekanslar.items():
        if en_yuksek < value:
            en_yuksek = value
    key = next(k for k, v in frekanslar.items() if v == en_yuksek)
    return key

result1 = minimum(liste)
result2 = maximum(liste)
result3 = ortalama(liste)
result4 = medyan(liste)
result5 = mod(liste)

print(f"Minimum değer: {result1}")
print(f"Maximum değer: {result2}")
print(f"Ortalama     : {result3}")
print(f"Medyan       : {result4}")
print(f"Mod          : {result5}")
