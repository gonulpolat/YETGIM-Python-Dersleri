"""
    **Basit Dönüştürücü**: Metre-Feet, Kilogram-Pound dönüştürücüsü yapın

    1 meter    = 3.28 feet
    1 feet     = 0.3048 meter
    1 kilogram = 2.22 pound (lb)
    1 pound    = 0.45 kilogram
"""

def convert(option: str, value: float) -> float:
    if option == "1":
        return value * 3.28, "metre", "feet"
    elif option == "2":
        return value * 0.3048, "feet", "metre"
    elif option == "3":
        return value * 2.22, "kilogram", "pound"
    return value * 0.45, "pound", "kilogram"

def get_input():
    print("Basit Dönüştürücü".center(40, "*"))
    print("1: Metre    - Feet\n2: Feet     - Metre\n3: Kilogram - Pound\n4: Pound    - Kilogram\n5: Çıkış")

    while True:
        user_option = input("Seçiniz: ")
        if user_option == "5":
            break
        elif user_option in ["1", "2", "3", "4"]:
            value = float(input("Değer: "))
            result, first, second = convert(user_option, value)
            print(f"{value} {first} = {result:.2f} {second}")
        else:
            print("Dönüşüm yapmak istediğiniz seçeneğe tıklayınız. (Çıkmak için 5'e basınız)")


if __name__ == "__main__":
    get_input()


##########################################################################################################


meter_to_feet = lambda m: m * 3.28
feet_to_meter = lambda ft: ft * 0.3048
kilogram_to_pound = lambda kg: kg * 2.22
pound_to_kilogram = lambda lb: lb * 0.45
