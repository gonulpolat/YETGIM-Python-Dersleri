"""
    **Pattern Generator**: Kullanıcının seçtiği deseni çizen program

    Bu turtle ile yazılabilir
"""

def draw(desen):
    if desen == '1':
        draw_triangle()
    elif desen == '2':
        draw_square()
    elif desen == '3':
        draw_hexagon()
    else:
        print("Çıkış yapıldı!")

def draw_triangle():
    for i in range(1, 30, 2):
        var = "*" * i
        print(var.center(50))

def draw_square():
    for i in range(1, 20):
        var = "* " * 20
        print(var)

def draw_hexagon():
    """
    Burada 2 for çok gereksiz gibi. 
    Farklı bir yaklaşım izlenebilir.
    """
    var = "*"
    for i in range(6, 12):
        print((var * 2*i).center(64))
    for i in range(12, 6, -1):
        print((var * 2*i).center(64))


if __name__ == "__main__":
    print("1. Üçgen\n2. Kare\n3. Altıgen")
    user_input = input("Ne çizmek istersiniz? Tuşlayınız: ")
    print() # new line
    draw(user_input)
