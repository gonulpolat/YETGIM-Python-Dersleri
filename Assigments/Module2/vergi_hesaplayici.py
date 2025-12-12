"""
    **Vergi Hesaplayıcı**: Gelir düzeyine göre farklı oranlarda vergi hesaplayan program
"""

gelir = float(input("Yıllık gelirinizi girin: "))
gider = float(input("Yıllık giderlerinizi girin: "))

net_gelir = gelir - gider

if net_gelir <= 0:
    print("Vergiden muafsınız.")
elif net_gelir <= 10000:
    print(f"Ödemeniz gereken vergi: {net_gelir * 0.5} TL")
elif net_gelir <= 50000:
    print(f"Ödemeniz gereken vergi: {net_gelir * 1.5} TL")
else:
    print(f"Ödemeniz gereken vergi: {net_gelir * 3} TL")

