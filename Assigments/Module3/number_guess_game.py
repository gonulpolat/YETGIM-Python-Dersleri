"""
    **Number Guess Game**: İleri seviye (min-max ipucu, puan sistemi ile)
"""


import random

def number_guess_game():
    computer_num = random.randint(1, 100)
    # print(computer_num)
    hak = 5
    total = 100
    print("Tuttuğum sayıyı bul!")
    while hak > 0:
        try:
            input_num = int(input("----> "))
        except ValueError:
            print("Lütfan sayı tut!")
        
        if input_num != computer_num:
            if input_num > computer_num:
                print("Aşağı")
            elif input_num < computer_num:
                print("Yukarı")
            hak -= 1
            total -= 20
        else:
            print("Tebrikler!")
            print(f"Puan: {total}")
            break

if __name__ == "__main__":
    number_guess_game()
