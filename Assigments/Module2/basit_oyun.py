"""
    **Basit Oyun**: Kullanıcı ile bilgisayarın taş-kağıt-makas oynadığı program

    taş   - kağıt -> 2
    taş   - makas -> 1
    kağıt - makas -> 2
    kağıt - taş   -> 1
    makas - taş   -> 2
    makas - kağıt -> 1
"""

import random

score_oyuncu     = 0
score_bilgisayar = 0

def play():
    global score_oyuncu, score_bilgisayar

    while score_oyuncu < 3 and score_bilgisayar < 3:
        bilgisayar_secim = random.choice(["Taş", "Kağıt", "Makas"])
        kullanici_secim = input("Taş-Kağıt-Makas: ")

        if bilgisayar_secim=="Taş" and kullanici_secim=="Makas" or \
        bilgisayar_secim=="Kağıt" and kullanici_secim=="Taş" or \
        bilgisayar_secim=="Makas" and kullanici_secim=="Kağıt":
            score_bilgisayar += 1
        elif bilgisayar_secim=="Taş" and kullanici_secim=="Kağıt" or \
            bilgisayar_secim=="Kağıt" and kullanici_secim=="Makas" or \
            bilgisayar_secim=="Makas" and kullanici_secim=="Taş":
            score_oyuncu += 1
    
    return score_oyuncu, score_bilgisayar


if __name__ == "__main__":
    
    score_oyuncu, score_bilgisayar = play()

    if score_bilgisayar == 3:
        print(f"Kaybettiniz")
    else:
        print("Tebrikler🎉🎉🎉🎉")
