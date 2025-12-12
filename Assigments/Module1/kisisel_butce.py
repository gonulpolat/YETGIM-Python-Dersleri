"""
    **Kişisel Bütçe**: Gelir ve giderleri alıp kalan parayı hesaplayan program
"""


def get_info():
    print("Gelir Gider Programı".center(40, "-"))
    while True:
        try:
            income = float(input("Aylık gelirinizi giriniz: "))
            kitchen = float(input("Aylık mutfak masrafınız: "))
            bill = float(input("Aylık toplam faturalarınız: "))
            entertainment = float(input("Aylık eğlence harcamalarınız: "))
            other = float(input("Diğer masraflar: "))
            break
        except:
            print("Lütfen sadece sayısal değer giriniz.")
    return income, (kitchen + bill + entertainment + other)


def calculate_remaining_money(income, expense):
    if income - expense > 0:
        print(f"Bu ayki tasarrufunuz: {income - expense} TL")
    elif income == expense:
        print(f"Ayağınızı yorganınıza göre uzatıyorsunuz. Tüm paranız harcandı.")
    else:
        print(f"Bu ay {expense - income} TL içerdesiniz.")


if __name__ == "__main__":
    gelir, gider = get_info()
    calculate_remaining_money(gelir, gider)
