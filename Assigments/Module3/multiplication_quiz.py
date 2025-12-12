"""
    **Multiplication Quiz**: Rastgele çarpma soruları soran quiz programı
"""

import random

def quiz():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    while True:
        try:
            result = int(input(f"{num1} x {num2} = "))
            if result == num1 * num2:
                print("Doğru bildiniz!")
                break
            else:
                print("Tekrar deneyiniz!")
        except:
            print("Yanlış cevap.")


if __name__ == "__main__":
    quiz()
